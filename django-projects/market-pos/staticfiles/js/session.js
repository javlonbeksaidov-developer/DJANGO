/* session.js: access guard and session helpers.
   Loaded in <head> so redirects happen before the page paints.

   Page access is declared on <html data-access="...">:
     public  login page (signed-in users are sent to the register)
     any     any signed-in user (cashier or admin)
     admin   admin only

   DEMO ONLY: the session is kept in sessionStorage and the role is derived from
   the username. In production, use a server-side session (cookie) and enforce
   roles on the backend; this file then only needs to fill in the user's name. */
(function () {
  'use strict';

  var KEY = 'pos.session';
  var root = document.documentElement;

  function read() {
    try { return JSON.parse(sessionStorage.getItem(KEY)); } catch (e) { return null; }
  }
  function write(value) {
    try { sessionStorage.setItem(KEY, JSON.stringify(value)); } catch (e) { /* storage blocked */ }
  }
  function clear() {
    try { sessionStorage.removeItem(KEY); } catch (e) { /* storage blocked */ }
  }

  var session = read();
  var access = root.dataset.access || 'any';

  if (access === 'public') {
    if (session) location.replace('sale.html');
  } else if (!session) {
    location.replace('login.html');
  } else if (access === 'admin' && session.role !== 'admin') {
    location.replace('sale.html');
  }
  if (session) root.dataset.role = session.role;

  window.POS = window.POS || {};
  window.POS.session = {
    get: read,
    login: function (username) {
      var admin = String(username).trim().toLowerCase() === 'admin';
      write(admin
        ? { role: 'admin', roleLabel: 'Admin', name: 'Jasur Tursunov', short: 'Jasur T.' }
        : { role: 'cashier', roleLabel: 'Cashier', name: 'Aziza Karimova', short: 'Aziza K.' });
      location.href = 'sale.html';
    },
    logout: function () {
      clear();
      location.href = 'login.html';
    }
  };

  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) el.textContent = text;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var s = read();
    if (s) {
      setText('uname', s.name);
      setText('urole', s.roleLabel);
      setText('tbname', s.short);
      setText('rolebadge', s.roleLabel);
    }
    document.querySelectorAll('form.logout').forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault(); // remove this handler when /logout is a real endpoint
        window.POS.session.logout();
      });
    });
  });
})();
