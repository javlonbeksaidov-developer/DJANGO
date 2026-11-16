/* login.js: demo sign-in for login.html.
   DEMO ONLY: intercepts the form and creates a local session. Delete this file
   (and its <script> tag) once the form posts to a real /login endpoint. */
document.addEventListener('DOMContentLoaded', function () {
  'use strict';
  var form = document.getElementById('login-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    window.POS.session.login(form.elements.user.value);
  });
});
