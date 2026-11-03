const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

// Exercise the shipped inline functions, without packages, a browser or a network.
const html = fs.readFileSync(path.join(__dirname, '../public/index.html'), 'utf8');
function section(start, end) {
  const from = html.indexOf(start);
  const to = html.indexOf(end, from);
  assert.ok(from >= 0 && to > from, `Missing demo source section: ${start}`);
  return html.slice(from, to);
}
const timing = section('  function activeNow()', '\n  const SCRIPTS=');
const playback = section('  async function play(idx)', '  function renderFinal(i)');
const stream = section('  async function stream(b,text,me)', '  function addData(b,data)');
const select = section('  function selectPanel(i)', '  tabs.forEach((t,i)=>{\n    t.addEventListener');
const tabControls = section('  tabs.forEach((t,i)=>{\n    t.addEventListener', "  document.querySelectorAll('.d-jump')");
const playbackControl = section("    playback.addEventListener('click'", '    const ioDemo=');

function fixture({ reduced = false } = {}) {
  let now = 0;
  const pending = [], events = [], selections = [], resets = [];
  const listeners = {}, playbackListeners = {};
  const scenes = [
    { total: 10000, ev: [{ t: 100, fx: 'first' }, { t: 500, fx: 'second' }, { t: 900, fx: 'third' }] },
    { total: 10000, ev: [{ t: 100, fx: 'other' }] },
  ];
  const context = vm.createContext({
    run: 0, paused: false, pauseStarted: 0, pausedFor: 0, running: false,
    userPaused: false, focusPaused: false, visible: false, cur: 0,
    REDUCED: reduced, performance: { now: () => now },
    shell: {
      classList: { toggle() {} },
      addEventListener: (name, handler) => { listeners[name] = handler; },
      contains: target => target?.inside === true,
    }, playback: {
      textContent: 'Pause demo',
      addEventListener: (name, handler) => { playbackListeners[name] = handler; },
    },
    sleep: ms => new Promise(resolve => pending.push({ at: now + ms, resolve })),
    SCRIPTS: scenes,
    tabs: scenes.map(() => {
      const handlers = {};
      return {
        offsetWidth: 0, style: { setProperty() {} }, classList: { add() {} },
        addEventListener: (name, handler) => { handlers[name] = handler; },
        click: () => handlers.click(),
      };
    }),
    setTabs: index => selections.push(index), resetPanel: index => resets.push(index), startTick() {},
    FX: Object.fromEntries(['first', 'second', 'third', 'other'].map(name => [name, () => events.push({ name, at: now })])),
    Math: Object.assign(Object.create(Math), { random: () => 0 }),
  });
  vm.runInContext(timing + playback + stream + select + tabControls + (reduced ? '' : playbackControl), context);
  function focus(keyboard = true) {
    listeners.focusin({ target: { matches: selector => {
      assert.equal(selector, ':focus-visible');
      return keyboard;
    } } });
  }
  async function flush() { for (let i = 0; i < 12; i++) await Promise.resolve(); }
  async function advance(target) {
    assert.ok(target >= now);
    await flush();
    while (pending.length) {
      pending.sort((a, b) => a.at - b.at);
      if (pending[0].at > target) break;
      const timer = pending.shift(); now = timer.at; timer.resolve(); await flush();
    }
    now = target; await flush();
  }
  return { context, events, selections, resets, advance, flush, listeners, focus, playbackListeners };
}

test('pause preserves remaining scene time instead of releasing overdue effects together', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.context.setPaused(true);
  await f.advance(2050);
  assert.deepEqual(f.events, []);
  f.context.setPaused(false);
  await f.advance(2100);
  assert.deepEqual(f.events, [{ name: 'first', at: 2100 }]);
  await f.advance(2500);
  assert.deepEqual(f.events.map(e => e.at), [2100, 2500]);
  await f.advance(2900);
  assert.deepEqual(f.events.map(e => e.at), [2100, 2500, 2900]);
});

test('repeated pauses accumulate without losing the remaining scene duration', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(150);
  f.context.setPaused(true);
  await f.advance(650);
  f.context.setPaused(false);
  await f.advance(750);
  f.context.setPaused(true);
  await f.advance(1750);
  f.context.setPaused(false);
  await f.advance(2000);
  assert.deepEqual(f.events, [{ name: 'first', at: 100 }, { name: 'second', at: 2000 }]);
});

test('manual selection resumes a paused demo and cancels the previous scene', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.context.setPaused(true);
  await f.advance(1050);
  f.context.selectPanel(1);
  assert.equal(f.context.paused, false);
  assert.equal(f.context.playback.textContent, 'Pause demo');
  assert.deepEqual(f.selections, [0, 1]);
  await f.advance(2000);
  assert.deepEqual(f.events, [{ name: 'other', at: 1150 }]);
});

test('cancelling an offscreen run prevents its pending effects', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.context.run++;
  await f.advance(5000);
  assert.deepEqual(f.events, []);
});

test('streaming text stays still while paused and resumes without losing a word', async () => {
  const f = fixture();
  f.context.run = 1;
  const paragraph = { textContent: '' };
  let finished = false;
  const bubble = { querySelector: () => paragraph, classList: { remove: () => { finished = true; } } };
  f.context.stream(bubble, 'one two three', 1);
  await f.flush();
  assert.equal(paragraph.textContent, 'one');
  await f.advance(20);
  f.context.setPaused(true);
  await f.advance(1020);
  assert.equal(paragraph.textContent, 'one');
  f.context.setPaused(false);
  await f.advance(1150);
  assert.equal(paragraph.textContent, 'one two three');
  assert.equal(finished, true);
});

test('reduced-motion tab selection uses the existing storyboard without starting playback', async () => {
  const f = fixture({ reduced: true });
  f.context.selectPanel(1);
  await f.advance(5000);
  assert.deepEqual(f.selections, [1]);
  assert.deepEqual(f.resets, []);
  assert.deepEqual(f.events, []);
  assert.equal(f.context.running, false);
});


test('keyboard focus inside the demo freezes the scene past its deadline and preserves remaining time', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.focus();
  await f.advance(20050);
  assert.deepEqual(f.events, []);
  assert.deepEqual(f.selections, [0]);
  assert.equal(f.context.paused, true);
  // Moving from a panel to another demo control must keep the pause.
  f.listeners.focusout({ relatedTarget: { inside: true } });
  f.focus();
  await f.advance(21050);
  assert.deepEqual(f.selections, [0]);
  f.listeners.focusout({ relatedTarget: null });
  await f.advance(21100);
  assert.deepEqual(f.events, [{ name: 'first', at: 21100 }]);
  await f.advance(30950);
  assert.deepEqual(f.selections, [0]);
  await f.advance(31000);
  assert.deepEqual(f.selections, [0, 1]);
});

test('focus changes preserve explicit pause and Resume overrides keyboard focus pause', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.context.setPaused(true);
  f.focus();
  f.listeners.focusout({ relatedTarget: { inside: false } });
  assert.equal(f.context.paused, true);
  assert.equal(f.context.playback.textContent, 'Resume demo');
  f.focus();
  f.playbackListeners.click();
  assert.equal(f.context.paused, false);
  assert.equal(f.context.focusPaused, false);
  assert.equal(f.context.playback.textContent, 'Pause demo');
  await f.advance(100);
  assert.deepEqual(f.events, [{ name: 'first', at: 100 }]);
  assert.deepEqual(f.selections, [0]);
});

test('mouse-click tab selection plays even when the browser focuses the clicked tab', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.focus(false);
  assert.equal(f.context.paused, false);
  f.context.tabs[1].click();
  assert.equal(f.context.paused, false);
  await f.advance(150);
  assert.deepEqual(f.selections, [0, 1]);
  assert.deepEqual(f.events, [{ name: 'other', at: 150 }]);
});

test('explicit tab selection clears a keyboard focus pause and a new keyboard focus pauses again', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.focus();
  assert.equal(f.context.paused, true);
  await f.advance(1050);
  f.context.tabs[1].click();
  assert.equal(f.context.paused, false);
  await f.advance(1150);
  assert.deepEqual(f.events, [{ name: 'other', at: 1150 }]);
  f.focus();
  assert.equal(f.context.paused, true);
  await f.advance(21150);
  assert.deepEqual(f.selections, [0, 1]);
});

test('mouse-click Resume plays while focus remains on the control', async () => {
  const f = fixture();
  f.context.play(0);
  await f.advance(50);
  f.focus(false);
  f.playbackListeners.click();
  assert.equal(f.context.paused, true);
  assert.equal(f.context.playback.textContent, 'Resume demo');
  await f.advance(2050);
  f.playbackListeners.click();
  assert.equal(f.context.paused, false);
  assert.equal(f.context.playback.textContent, 'Pause demo');
  await f.advance(2100);
  assert.deepEqual(f.events, [{ name: 'first', at: 2100 }]);
});


test('leaving focus starts a visible demo that was waiting to autoplay', async () => {
  const f = fixture();
  f.context.visible = true;
  f.focus();
  await f.advance(1000);
  assert.deepEqual(f.selections, []);
  f.listeners.focusout({ relatedTarget: null });
  await f.advance(1100);
  assert.deepEqual(f.selections, [0]);
  assert.deepEqual(f.events, [{ name: 'first', at: 1100 }]);
});
