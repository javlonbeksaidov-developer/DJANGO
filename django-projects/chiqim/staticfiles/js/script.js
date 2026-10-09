/* ==========================================================================
   Chiqim — UI xatti-harakatlari
   Faqat interfeys uchun: mavzu almashtirish, mobil sidebar, dropdown menyu,
   xabarnomani yopish. Serverga hech qanday so'rov (fetch/AJAX) yubormaydi —
   barcha ma'lumot almashinuvi oddiy <form method="post"> orqali amalga oshadi.
   ========================================================================== */

(function () {
  "use strict";

  /* ---- Mavzu (dark / light) ---- */
  var THEME_KEY = "chiqim-theme";

  function applyTheme(theme) {
    if (theme === "dark") {
      document.documentElement.setAttribute("data-theme", "dark");
    } else {
      document.documentElement.removeAttribute("data-theme");
    }
    var icons = document.querySelectorAll("[data-theme-icon]");
    icons.forEach(function (icon) {
      icon.textContent = theme === "dark" ? "☀" : "☾";
    });
  }

  function initTheme() {
    var saved = localStorage.getItem(THEME_KEY);
    if (!saved) {
      saved = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    applyTheme(saved);
  }

  function toggleTheme() {
    var current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
    var next = current === "dark" ? "light" : "dark";
    localStorage.setItem(THEME_KEY, next);
    applyTheme(next);
  }

  /* ---- Mobil sidebar ---- */
  function initSidebar() {
    var sidebar = document.querySelector("[data-sidebar]");
    var scrim = document.querySelector("[data-scrim]");
    var openBtns = document.querySelectorAll("[data-sidebar-open]");
    if (!sidebar || !scrim) return;

    function close() {
      sidebar.classList.remove("open");
      scrim.classList.remove("open");
    }
    function open() {
      sidebar.classList.add("open");
      scrim.classList.add("open");
    }
    openBtns.forEach(function (btn) {
      btn.addEventListener("click", open);
    });
    scrim.addEventListener("click", close);
    window.addEventListener("resize", function () {
      if (window.innerWidth > 980) close();
    });
  }

  /* ---- Profil dropdown ---- */
  function initDropdown() {
    var trigger = document.querySelector("[data-profile-trigger]");
    var menu = document.querySelector("[data-profile-menu]");
    if (!trigger || !menu) return;

    trigger.addEventListener("click", function (e) {
      e.stopPropagation();
      menu.classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      if (!menu.contains(e.target)) menu.classList.remove("open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") menu.classList.remove("open");
    });
  }

  /* ---- Xabarnomani yopish (flash / alert) ---- */
  function initAlerts() {
    document.querySelectorAll("[data-alert-dismiss]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var alertEl = btn.closest(".alert");
        if (alertEl) alertEl.remove();
      });
    });
  }

  /* ---- Theme toggle tugmalari ---- */
  function initThemeButtons() {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", toggleTheme);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initTheme();
    initSidebar();
    initDropdown();
    initAlerts();
    initThemeButtons();
  });
})();
