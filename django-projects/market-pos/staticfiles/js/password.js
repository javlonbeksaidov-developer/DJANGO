/* password.js: adds a Show/Hide button to every <input type="password">.
   UI only; the value is never read. Revealed fields return to hidden when
   their form is reset. */
(function () {
  'use strict';

  function hideAll() {
    document.querySelectorAll('input[data-pw]').forEach(function (input) {
      input.type = 'password';
      var btn = input.nextElementSibling;
      btn.textContent = 'Show';
      btn.setAttribute('aria-pressed', 'false');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('input[type=password]').forEach(function (input) {
      var wrap = document.createElement('span');
      wrap.className = 'pw';
      input.before(wrap);
      wrap.append(input);
      input.dataset.pw = '';

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'eye';
      btn.textContent = 'Show';
      btn.setAttribute('aria-pressed', 'false');
      btn.setAttribute('aria-label', 'Show or hide password');
      btn.addEventListener('click', function () {
        var show = input.type === 'password';
        input.type = show ? 'text' : 'password';
        btn.textContent = show ? 'Hide' : 'Show';
        btn.setAttribute('aria-pressed', String(show));
      });
      wrap.append(btn);
    });
  });

  document.addEventListener('reset', hideAll);
})();
