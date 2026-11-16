/* theme.js: light/dark switch. Loaded in <head> so the saved theme is applied
   before first paint. Any button with class "tsw" acts as the switch. */
(function () {
  'use strict';

  var KEY = 'pos.theme';
  var root = document.documentElement;
  var media = window.matchMedia('(prefers-color-scheme: dark)');

  try {
    var saved = localStorage.getItem(KEY);
    if (saved === 'dark' || saved === 'light') root.dataset.theme = saved;
  } catch (e) { /* storage blocked */ }

  function isDark() {
    return (root.dataset.theme || (media.matches ? 'dark' : 'light')) === 'dark';
  }

  function sync() {
    document.querySelectorAll('.tsw').forEach(function (btn) {
      btn.setAttribute('aria-checked', String(isDark()));
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    sync();
    document.querySelectorAll('.tsw').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var next = isDark() ? 'light' : 'dark';
        root.dataset.theme = next;
        try { localStorage.setItem(KEY, next); } catch (e) { /* storage blocked */ }
        sync();
      });
    });
  });

  media.addEventListener('change', sync);
})();
