const { test } = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../assets/js/iris-analytics.js'), 'utf8');

function boot({ value, at = Date.now(), blocked = false, gpc = false, dnt = null, malformed = false, query = '?private=value#fragment' } = {}) {
  const nodes = {};
  for (const name of ['banner', 'settings', 'accept', 'reject', 'signal']) {
    nodes[name] = { hidden: true, addEventListener(_, fn) { this.click = fn; }, focus() {} };
  }
  const panel = { hidden: true, querySelector(s) { return nodes[s.match(/data-consent-(\w+)/)[1]]; } };
  const requests = [], writes = [], cookies = [];
  const document = {
    referrer: 'https://example.org/paper/?private=value#fragment',
    getElementById(id) { return id === 'iris-analytics' ? { dataset: { measurementId: 'G-TEST123' } } : panel; },
    createElement() { return {}; }, head: { appendChild(tag) { requests.push(tag.src); } },
    get cookie() { return '_ga=123; _ga_TEST123=456; unrelated=keep'; },
    set cookie(value) { cookies.push(value); }
  };
  const window = { location: { href: 'https://iris-rs-lab.github.io/zh/' + query, hostname: 'iris-rs-lab.github.io' } };
  const storage = {
    getItem() { if (blocked) throw Error('blocked'); return malformed ? '{' : value ? JSON.stringify({ value, at }) : null; },
    setItem(key, value) { if (blocked) throw Error('blocked'); writes.push(JSON.parse(value)); }
  };
  vm.runInNewContext(source, { window, document, navigator: { globalPrivacyControl: gpc, doNotTrack: dnt }, localStorage: storage, URL, Date });
  return { nodes, panel, requests, writes, cookies, window };
}

test('no tracking or Google requests before consent', () => {
  const s = boot();
  assert.equal(s.panel.hidden, false);
  assert.equal(s.nodes.banner.hidden, false);
  assert.equal(s.requests.length, 0);
  assert.equal(s.window.gtag, undefined);
});
test('accept loads once, strips query/fragment and denies advertising', () => {
  const s = boot();
  s.nodes.accept.click(); s.nodes.accept.click();
  assert.equal(s.requests.length, 1);
  assert.equal(s.requests[0], 'https://www.googletagmanager.com/gtag/js?id=G-TEST123');
  const config = s.window.dataLayer.find(args => args[0] === 'config')[2];
  assert.equal(config.page_location, 'https://iris-rs-lab.github.io/zh/');
  assert.equal(config.page_referrer, 'https://example.org/paper/');
  assert.equal(config.allow_google_signals, false);
  assert.equal(s.window.dataLayer[0][2].ad_storage, 'denied');
});
test('decline persists and does not load Google', () => {
  const s = boot(); s.nodes.reject.click();
  assert.equal(s.writes[0].value, 'denied');
  assert.equal(s.requests.length, 0);
  assert.equal(boot({ value: 'denied' }).requests.length, 0);
});
test('withdraw disables GA, clears only GA cookies; reaccept works without reloading', () => {
  const s = boot({ value: 'granted' });
  s.nodes.settings.click();
  assert.equal(s.nodes.banner.hidden, false);
  s.nodes.reject.click();
  assert.equal(s.window['ga-disable-G-TEST123'], true);
  assert.ok(s.cookies.some(c => c.startsWith('_ga=')));
  assert.ok(s.cookies.every(c => !c.startsWith('unrelated=')));
  s.nodes.settings.click(); s.nodes.accept.click();
  assert.equal(s.window['ga-disable-G-TEST123'], false);
  assert.equal(s.requests.length, 1);
});
test('DNT and GPC override previously granted consent', () => {
  for (const opts of [{ gpc: true }, { dnt: '1' }]) {
    const s = boot({ value: 'granted', ...opts });
    assert.equal(s.requests.length, 0);
    assert.equal(s.nodes.accept.hidden, true);
    assert.equal(s.nodes.signal.hidden, false);
  }
});
test('expired, future, invalid and malformed choices require consent again', () => {
  for (const opts of [{ value: 'granted', at: 0 }, { value: 'granted', at: Date.now() + 60000 }, { value: 'unknown' }, { malformed: true }]) {
    const s = boot(opts);
    assert.equal(s.requests.length, 0);
    assert.equal(s.nodes.banner.hidden, false);
  }
});
test('blocked browser storage does not break browsing or explicit consent', () => {
  const s = boot({ blocked: true });
  s.nodes.accept.click();
  assert.equal(s.requests.length, 1);
  s.nodes.reject.click();
  assert.equal(s.window['ga-disable-G-TEST123'], true);
});

test('campaign attribution allows public UTM labels, not arbitrary query values', () => {
  const s = boot({ value: 'granted', query: '?utm_source=newsletter&utm_medium=email&utm_campaign=lab-2026&utm_content=hero&utm_term=private&email=private' });
  const config = s.window.dataLayer.find(args => args[0] === 'config')[2];
  assert.equal(config.campaign_source, 'newsletter');
  assert.equal(config.campaign_medium, 'email');
  assert.equal(config.campaign_name, 'lab-2026');
  assert.equal(config.campaign_content, 'hero');
  assert.equal(config.campaign_term, undefined);
  assert.equal(config.page_location, 'https://iris-rs-lab.github.io/zh/');
});
