const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const html = fs.readFileSync(path.join(__dirname, '../public/index.html'), 'utf8');
const helpers = html.slice(html.indexOf('/* signup requests:'), html.indexOf('/* live count */'));
const forms = html.slice(html.indexOf('/* waitlist submit'), html.indexOf("wire('wlHero','successHero');"));
const classes = () => { const values = new Set(); return {add: x => values.add(x), remove: x => values.delete(x), contains: x => values.has(x)}; };
function fixture(response = async () => ({ok:true,status:201}), source = 'hero') {
  const timers = new Map(); let nextTimer = 0, handler, copyHandler;
  const attributes = {};
  const form = {addEventListener: (_,fn) => {handler=fn;},setAttribute:(k,v)=>attributes[k]=v,removeAttribute:k=>delete attributes[k]};
  const input = {value:'player@example.test',disabled:true,setAttribute:(k,v)=>attributes[k]=v,removeAttribute:k=>delete attributes[k]};
  const button = {disabled:true,textContent:'Claim your spot'};
  const note = {className:'note',textContent:''};
  const message = {textContent:'You are on the list.'};
  const copyStatus = {textContent:''};
  const fallback = {hidden:true,focus(){this.focused=true;},select(){this.selected=true;}};
  const success = {classList:classes(),querySelector:s=>({'p':message,'.share-status':copyStatus,'.share-fallback':fallback})[s],focus(){this.focused=true;}};
  const copyButton = {disabled:false,closest:()=>success,addEventListener:(_,fn)=>copyHandler=fn};
  const box = {classList:classes(),dataset:{source},querySelector:s=>({'form':form,'input':input,'.note':note,'button':button})[s]};
  const requests = [];
  const context = {
    document:{getElementById:id=>id==='box'?box:id==='success'?success:null,querySelectorAll:()=>[copyButton],referrer:''},
    location:{href:'https://site.example/'},navigator:{clipboard:{writeText:async()=>{}}},URL,AbortController,
    SUPABASE_URL:'https://api.example',SUPABASE_ANON_KEY:'test-only',REDUCED:true,loadCount:()=>{},
    fetch:(url,options)=>{requests.push({url,options});return response(url,options);},
    setTimeout:fn=>{const id=++nextTimer;timers.set(id,fn);return id;},clearTimeout:id=>timers.delete(id)
  };
  vm.runInNewContext(helpers+forms+'\nwire("box","success");',context);
  return {context,requests,timers,input,button,note,box,success,message,attributes,copyStatus,fallback,copyButton,submit:()=>handler({preventDefault(){}}),copy:()=>copyHandler(),expire:()=>[...timers.values()].forEach(fn=>fn())};
}
const response = (status,body) => async()=>({ok:status>=200&&status<300,status,json:async()=>body});
for (const source of ['hero','mid','cta']) test(`successful ${source} signup sends expected placement, restores controls and focuses confirmation`, async()=>{
  const f=fixture(response(201),source);
  assert.equal(f.input.disabled,false);assert.equal(f.button.disabled,false);
  await f.submit();
  assert.equal(f.success.classList.contains('show'),true);assert.equal(f.success.focused,true);
  assert.equal(JSON.parse(f.requests[0].options.body).source,source);
  assert.equal(f.input.disabled,false);assert.equal(f.button.disabled,false);assert.equal(f.attributes['aria-busy'],undefined);assert.equal(f.timers.size,0);
  await f.submit();assert.equal(f.requests.length,1);
});
test('invalid input makes no request and remains editable',async()=>{
  const f=fixture();f.input.value='invalid';await f.submit();assert.equal(f.requests.length,0);assert.equal(f.attributes['aria-invalid'],'true');assert.equal(f.button.disabled,false);
});
for(const column of ['email','lower(email)']) test(`recognized ${column} duplicate confirms registration`,async()=>{
  const f=fixture(response(409,{code:'23505',details:`Key (${column})=(player@example.test) already exists.`}));await f.submit();assert.equal(f.success.classList.contains('show'),true);assert.match(f.message.textContent,/already on the list/);
});
for(const body of [{code:'23503'},{code:'23505',details:'Key (other_column)=(sample) already exists.'},{code:'23505'},null]) test(`unrecognized conflict is recoverable (${body?.code||'empty'} / ${body?.details?'details':'no details'})`,async()=>{
  const f=fixture(response(409,body));await f.submit();assert.equal(f.success.classList.contains('show'),false);assert.equal(f.button.disabled,false);assert.match(f.note.textContent,/couldn't confirm/);
});
for(const status of [400,429,500]) test(`HTTP ${status} permits a manual retry`,async()=>{
  const f=fixture(response(status));await f.submit();await f.submit();assert.equal(f.requests.length,2);assert.equal(f.input.value,'player@example.test');assert.equal(f.button.disabled,false);assert.equal(f.success.classList.contains('show'),false);
});
test('network rejection restores controls without automatic resubmission',async()=>{
  const f=fixture(async()=>{throw new TypeError('offline');});await f.submit();assert.equal(f.requests.length,1);assert.equal(f.button.disabled,false);assert.equal(f.attributes['aria-busy'],undefined);
});
test('pending submission rejects reentry; deadline aborts and restores the form',async()=>{
  const f=fixture(()=>new Promise(()=>{}));const pending=f.submit();await f.submit();assert.equal(f.requests.length,1);assert.equal(f.button.disabled,true);assert.equal(f.input.disabled,true);assert.equal(f.attributes['aria-busy'],'true');
  f.expire();await pending;assert.equal(f.requests[0].options.signal.aborted,true);assert.equal(f.button.disabled,false);assert.equal(f.input.disabled,false);assert.match(f.note.textContent,/too long/);assert.equal(f.timers.size,0);
});
test('deadline also covers a stalled conflict response body',async()=>{
  const f=fixture(async()=>({ok:false,status:409,json:()=>new Promise(()=>{})}));const pending=f.submit();await Promise.resolve();f.expire();await pending;assert.match(f.note.textContent,/too long/);assert.equal(f.button.disabled,false);
});
test('late completion after a deadline cannot change the failed form to success',async()=>{
  let resolve;const f=fixture(()=>new Promise(r=>resolve=r));const pending=f.submit();f.expire();await pending;resolve({ok:true,status:201});await Promise.resolve();assert.equal(f.success.classList.contains('show'),false);
});
test('unconfigured signup never reports a fabricated registration',async()=>{
  const f=fixture();f.context.SUPABASE_URL='__UNCONFIGURED__';await f.submit();assert.equal(f.success.classList.contains('show'),false);assert.equal(f.requests.length,0);assert.equal(f.button.disabled,false);
});
test('referrer is reduced to an HTTP origin and browser details are omitted',async()=>{
  const f=fixture();f.context.document.referrer='https://community.example/path?campaign=sample#section';await f.submit();const body=JSON.parse(f.requests[0].options.body);assert.equal(body.referrer,'https://community.example');assert.equal(body.user_agent,'');
});
test('existing duo invite is retained without arbitrary landing URL parameters',async()=>{
  const f=fixture();f.context.location.href='https://site.example/?ref=duo&unknown=sample';await f.submit();assert.equal(JSON.parse(f.requests[0].options.body).referrer,'https://seer.coach/?ref=duo');
});
for(const referrer of ['', 'invalid', 'file:///sample']) test(`unsupported referrer is omitted (${referrer||'empty'})`,async()=>{
  const f=fixture();f.context.document.referrer=referrer;await f.submit();assert.equal(JSON.parse(f.requests[0].options.body).referrer,null);
});
test('clipboard success is announced only after completion',async()=>{
  let resolve;const f=fixture();f.context.navigator.clipboard.writeText=()=>new Promise(r=>resolve=r);const pending=f.copy();assert.equal(f.copyStatus.textContent,'');assert.equal(f.copyButton.disabled,true);resolve();await pending;assert.match(f.copyStatus.textContent,/copied/);assert.equal(f.fallback.hidden,true);assert.equal(f.copyButton.disabled,false);
});
for(const unavailable of [false,true]) test(`clipboard ${unavailable?'unavailable':'denied'} exposes a manual copy fallback`,async()=>{
  const f=fixture();f.context.navigator.clipboard=unavailable?undefined:{writeText:async()=>{throw new Error('denied');}};await f.copy();assert.doesNotMatch(f.copyStatus.textContent,/copied/i);assert.equal(f.fallback.hidden,false);assert.equal(f.fallback.value,'https://seer.coach/?ref=duo');assert.equal(f.fallback.focused,true);assert.equal(f.fallback.selected,true);assert.equal(f.copyButton.disabled,false);
});
