/* clock.js: keeps the status-bar date and time current. */
(function () {
  'use strict';
  function tick() {
    var el = document.getElementById('clock');
    if (!el) return;
    var now = new Date();
    el.textContent =
      now.toLocaleDateString(undefined, { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' }) +
      ' · ' + now.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' });
  }
  document.addEventListener('DOMContentLoaded', function () { tick(); setInterval(tick, 30000); });
})();
