const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const vm=require('node:vm');
const {execFileSync}=require('node:child_process');
const root=path.join(__dirname,'..');
const pages=fs.readdirSync(path.join(root,'public')).filter(name=>name.endsWith('.html'));
for(const page of pages) test(`${page}: scripts parse; capture controls start unavailable with safe native defaults`,()=>{
  const html=fs.readFileSync(path.join(root,'public',page),'utf8');
  for(const script of html.matchAll(/<script>([\s\S]*?)<\/script>/g))new vm.Script(script[1]);
  for(const match of html.matchAll(/<form\b([^>]*)>([\s\S]*?)<\/form>/g)){
    assert.match(match[1],/method="post"/);
    for(const input of match[2].matchAll(/<input\b[^>]*>/g)){assert.match(input[0],/\bdisabled\b/);assert.doesNotMatch(input[0],/\bname=/);}
    for(const button of match[2].matchAll(/<button\b[^>]*>/g))assert.match(button[0],/\bdisabled\b/);
  }
  assert.match(html,/<noscript>/);
});
for(const page of ['index.html','designsystem-final.html']) test(`${page}: unavailable storage leaves the gate usable and does not abort initialization`,()=>{
  const html=fs.readFileSync(path.join(root,'public',page),'utf8');
  const code=page==='index.html'?html.slice(html.indexOf('/* password gate */'),html.indexOf('/* nav solidify */')):html.match(/<script>([\s\S]*?)<\/script>/)[1];
  const button={disabled:true};let submit;
  const input={disabled:true,focus(){this.focused=true;}};
  const form={querySelector:()=>button,addEventListener:(_,fn)=>submit=fn};
  const note={textContent:''};
  const gate={querySelector:s=>({'form':form,'input':input,'.gate-note':note,'.gate-box':{}})[s]};
  const context={document:{getElementById:()=>gate,body:{classList:{add(){}}}},localStorage:{getItem(){throw new Error('Storage unavailable');}},scrollTo(){},completed:false};
  vm.runInNewContext(code+'\ncompleted=true',context);
  assert.equal(context.completed,true);assert.equal(input.disabled,false);assert.equal(button.disabled,false);assert.equal(typeof submit,'function');
});
test('design pages regenerate exactly without modifying repository inputs',()=>{
  const temp=fs.mkdtempSync(path.join(os.tmpdir(),'seer-generated-'));
  try{
    fs.mkdirSync(path.join(temp,'scripts'));fs.mkdirSync(path.join(temp,'public/logos'),{recursive:true});
    fs.copyFileSync(path.join(root,'scripts/gen-designsystem.py'),path.join(temp,'scripts/gen-designsystem.py'));
    fs.copyFileSync(path.join(root,'public/logos/seer-mark.svg'),path.join(temp,'public/logos/seer-mark.svg'));
    execFileSync('python3',[path.join(temp,'scripts/gen-designsystem.py')]);
    for(const page of pages.filter(n=>n.startsWith('designsystem-')))assert.equal(fs.readFileSync(path.join(temp,'public',page),'utf8'),fs.readFileSync(path.join(root,'public',page),'utf8'),page);
  }finally{fs.rmSync(temp,{recursive:true,force:true});}
});
