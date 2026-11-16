/* shortcuts.js: keyboard shortcuts for the register.
   F1 Sale   F2 Search products   F3 Return   F9 Charge (sale page only) */
document.addEventListener('keydown', function (e) {
  'use strict';
  if (document.querySelector('dialog[open]')) return;

  if (e.key === 'F1') { e.preventDefault(); location.href = 'sale.html'; }
  if (e.key === 'F3') { e.preventDefault(); location.href = 'return.html'; }

  if (e.key === 'F2') {
    e.preventDefault();
    var search = document.getElementById('q');
    if (search) search.focus(); else location.href = 'sale.html';
  }

  if (e.key === 'F9') {
    var pay = document.getElementById('m-pay');
    if (pay) { e.preventDefault(); pay.showModal(); }
  }
});
