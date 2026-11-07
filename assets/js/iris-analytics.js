/* Basic consent mode: no Google requests at all until an explicit opt-in. */
(function () {
  'use strict';
  const script = document.getElementById('iris-analytics');
  const panel = document.getElementById('iris-analytics-consent');
  if (!script || !panel) return;
  const id = script.dataset.measurementId;
  const key = 'iris.analytics.consent.v1';
  const lifetime = 180 * 24 * 60 * 60 * 1000;
  const protectedBrowser = navigator.globalPrivacyControl === true ||
    navigator.doNotTrack === '1' || window.doNotTrack === '1';
  let enabled = false;
  let choice = null;
  try {
    const saved = JSON.parse(localStorage.getItem(key));
    if (saved && Date.now() - saved.at >= 0 && Date.now() - saved.at < lifetime &&
        ['granted', 'denied'].includes(saved.value)) choice = saved.value;
  } catch (_) { /* Storage blocked: consent lasts only for this page. */ }

  const banner = panel.querySelector('[data-consent-banner]');
  const settings = panel.querySelector('[data-consent-settings]');
  const accept = panel.querySelector('[data-consent-accept]');
  const notice = panel.querySelector('[data-consent-signal]');
  const cleanURL = (input) => {
    try {
      const url = new URL(input);
      return /^https?:$/.test(url.protocol) ? url.origin + url.pathname : '';
    } catch (_) { return ''; }
  };

  function start() {
    if (protectedBrowser) return;
    window['ga-disable-' + id] = false;
    if (enabled) {
      window.gtag('consent', 'update', { analytics_storage: 'granted' });
      return;
    }
    enabled = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'denied', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied'
    });
    window.gtag('consent', 'update', { analytics_storage: 'granted' });
    window.gtag('js', new Date());
    // Preserve campaign attribution without sending arbitrary query parameters.
    const campaign = {};
    const params = new URL(window.location.href).searchParams;
    Object.entries({ utm_source: 'campaign_source', utm_medium: 'campaign_medium',
      utm_campaign: 'campaign_name', utm_id: 'campaign_id', utm_content: 'campaign_content'
    }).forEach(([query, field]) => {
      const value = params.get(query);
      if (value && /^[a-zA-Z0-9._~-]{1,100}$/.test(value)) campaign[field] = value;
    });
    window.gtag('config', id, {
      ...campaign,
      // Do not send page query strings/fragments (e.g. internal search text).
      page_location: cleanURL(window.location.href),
      page_referrer: cleanURL(document.referrer),
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      cookie_flags: 'SameSite=Lax;Secure'
    });
    const tag = document.createElement('script');
    tag.async = true;
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(tag);
  }

  function stop() {
    window['ga-disable-' + id] = true;
    if (window.gtag) window.gtag('consent', 'update', { analytics_storage: 'denied' });
    // GA cookies can be host-only or set on an ancestor domain.
    const host = window.location.hostname.split('.');
    const domains = ['', ...host.map((_, i) => host.slice(i).join('.'))];
    document.cookie.split(';').forEach((entry) => {
      const name = entry.trim().split('=')[0];
      if (!/^_ga(?:_|$)/.test(name)) return;
      domains.forEach((domain) => {
        document.cookie = name + '=; Max-Age=0; path=/' +
          (domain ? '; domain=' + domain : '') + '; SameSite=Lax; Secure';
      });
    });
  }

  function save(value) {
    choice = value;
    try { localStorage.setItem(key, JSON.stringify({ value, at: Date.now() })); } catch (_) {}
    if (value === 'granted') start();
    else stop();
    banner.hidden = true;
    settings.hidden = false;
    settings.focus();
  }

  accept.addEventListener('click', () => save('granted'));
  panel.querySelector('[data-consent-reject]').addEventListener('click', () => save('denied'));
  settings.addEventListener('click', () => {
    banner.hidden = false;
    settings.hidden = true;
    (protectedBrowser ? panel.querySelector('[data-consent-reject]') : accept).focus();
  });
  panel.hidden = false;
  accept.hidden = protectedBrowser;
  notice.hidden = !protectedBrowser;
  banner.hidden = protectedBrowser || choice !== null;
  settings.hidden = !banner.hidden;
  if (protectedBrowser || choice === 'denied') stop();
  else if (choice === 'granted') start();
})();
