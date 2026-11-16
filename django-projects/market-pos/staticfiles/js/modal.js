/* modal.js: opens and closes native <dialog> elements.
   [data-open="id"]  opens the dialog with that id
   [data-close]      closes the dialog it sits in
   Clicking the backdrop or pressing Esc also closes it. */
document.addEventListener('click', function (e) {
  'use strict';

  var opener = e.target.closest('[data-open]');
  if (opener) {
    e.preventDefault();
    var dialog = document.getElementById(opener.dataset.open);
    if (dialog) dialog.showModal();
    return;
  }

  var closer = e.target.closest('[data-close]');
  if (closer) {
    closer.closest('dialog').close();
    return;
  }

  if (e.target.tagName === 'DIALOG') {
    var r = e.target.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) {
      e.target.close();
    }
  }
});
