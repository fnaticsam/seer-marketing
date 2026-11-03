const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const html=fs.readFileSync(path.join(__dirname,'../public/index.html'),'utf8');
const hero=html.slice(html.indexOf('/* hero motion:'),html.indexOf('/* headline scramble */'));
const cards=html.slice(html.indexOf('/* card cursor-spotlight and'),html.indexOf('/* final-CTA eye:'));
function fixture(reduced=false){
 let next=0,rectReads=0;const intervals=new Map(),timeouts=new Map(),frames=new Map(),observers=[],listeners={};
 const node=()=>{const values=new Set();return {style:{setProperty(k,v){this[k]=v;}},classList:{add:x=>values.add(x),remove:x=>values.delete(x),contains:x=>values.has(x),toggle:(x,on)=>on?values.add(x):values.delete(x)},getBoundingClientRect(){rectReads++;return {left:0,top:0,width:100,height:100};}};};
 const stage=node(),pupil=node(),hint=node(),section=node(),step=node(),card=node();hint.textContent='META';
 const on=(event,fn)=>(listeners[event]??=[]).push(fn);
 const context={REDUCED:reduced,document:{hidden:false,querySelector:()=>section,getElementById:id=>({eyeStage:stage,heroStar:pupil,hintWord:hint})[id],querySelectorAll:()=>[step],addEventListener:on},addEventListener:on,innerWidth:1000,innerHeight:1000,
  IntersectionObserver:class {constructor(callback){this.callback=callback;observers.push(this);}observe(target){this.target=target;}},
  setInterval:fn=>{const id=++next;intervals.set(id,fn);return id;},clearInterval:id=>intervals.delete(id),setTimeout:fn=>{const id=++next;timeouts.set(id,fn);return id;},clearTimeout:id=>timeouts.delete(id),requestAnimationFrame:fn=>{const id=++next;frames.set(id,fn);return id;},cancelAnimationFrame:id=>frames.delete(id)};
 const send=(name,event={})=>(listeners[name]||[]).forEach(fn=>fn(event));
 const visible=(index,value)=>observers[index].callback([{target:observers[index].target,isIntersecting:value}]);
 const flush=map=>{const callbacks=[...map.values()];map.clear();callbacks.forEach(fn=>fn());};
 return {context,intervals,timeouts,frames,observers,stage,pupil,hint,step,card,send,visible,flush,reads:()=>rectReads};
}
test('hero timers stop offscreen and document-hidden; interrupted fade remains visible',()=>{
 const f=fixture();vm.runInNewContext(hero,f.context);assert.equal(f.intervals.size,0);
 f.visible(0,true);assert.equal(f.intervals.size,1);[...f.intervals.values()][0]();assert.equal(f.hint.style.opacity,0);assert.equal(f.timeouts.size,1);
 f.visible(0,false);assert.equal(f.intervals.size,0);assert.equal(f.timeouts.size,0);assert.equal(f.hint.style.opacity,1);
 f.visible(0,true);f.context.document.hidden=true;f.send('visibilitychange');assert.equal(f.intervals.size,0);
 f.context.document.hidden=false;f.send('visibilitychange');assert.equal(f.intervals.size,1);[...f.intervals.values()][0]();f.flush(f.timeouts);assert.equal(f.hint.textContent,'VISION');
});
test('hero coalesces pointer events and avoids offscreen layout work',()=>{
 const f=fixture();vm.runInNewContext(hero,f.context);
 f.send('mousemove',{clientX:100,clientY:100});assert.equal(f.frames.size,0);
 f.visible(0,true);for(let i=0;i<10;i++)f.send('mousemove',{clientX:i*100,clientY:100});assert.equal(f.frames.size,1);assert.equal(f.reads(),0);
 f.flush(f.frames);assert.equal(f.reads(),1);assert.ok(Math.abs(parseFloat(f.pupil.style.transform.slice('translate('.length))-7.65)<1e-9);
 f.send('mousemove',{clientX:100,clientY:100});f.visible(0,false);assert.equal(f.frames.size,0);assert.equal(f.reads(),1);
});
test('spotlight applies the latest pointer once per frame and clears on exit',()=>{
 const f=fixture();vm.runInNewContext(cards,f.context);
 for(let i=0;i<10;i++)f.send('mousemove',{target:{closest:()=>f.card},clientX:i,clientY:i});assert.equal(f.frames.size,1);assert.equal(f.reads(),0);
 f.flush(f.frames);assert.equal(f.reads(),1);assert.equal(f.card.style['--mx'],'9px');assert.equal(f.card.classList.contains('lit'),true);
 f.send('mousemove',{target:{closest:()=>null}});f.flush(f.frames);assert.equal(f.card.classList.contains('lit'),false);
});
test('hidden documents cancel pending spotlight work',()=>{
 const f=fixture();vm.runInNewContext(cards,f.context);f.send('mousemove',{target:{closest:()=>f.card},clientX:1,clientY:1});f.context.document.hidden=true;f.send('visibilitychange');assert.equal(f.frames.size,0);assert.equal(f.reads(),0);
 f.send('mousemove',{target:{closest:()=>f.card},clientX:1,clientY:1});assert.equal(f.frames.size,0);
});
test('step animation activation follows section and document visibility',()=>{
 const f=fixture();vm.runInNewContext(cards,f.context);f.visible(0,true);assert.equal(f.step.classList.contains('motion-active'),true);
 f.context.document.hidden=true;f.send('visibilitychange');assert.equal(f.step.classList.contains('motion-active'),false);
 f.context.document.hidden=false;f.send('visibilitychange');assert.equal(f.step.classList.contains('motion-active'),true);
 f.visible(0,false);assert.equal(f.step.classList.contains('motion-active'),false);
});
test('reduced motion schedules no decorative work',()=>{
 const f=fixture(true);vm.runInNewContext(hero+cards,f.context);assert.equal(f.observers.length,0);assert.equal(f.intervals.size,0);f.send('mousemove',{});assert.equal(f.frames.size,0);
});
