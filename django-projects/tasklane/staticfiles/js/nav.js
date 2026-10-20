/**
 * nav.js — mobile navigation menu toggle.
 */
(function () {
  const toggle = document.querySelector("[data-nav-toggle]");
  const nav = document.getElementById("main-nav");

  if (!toggle || !nav) return;

  toggle.addEventListener("click", function () {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
})();
