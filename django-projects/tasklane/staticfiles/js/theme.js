/**
 * theme.js — dark / light mode.
 * Load in <head> (no defer) so the theme is set before the page paints.
 */
(function () {
  const STORAGE_KEY = "todo-theme";
  const root = document.documentElement;

  function getSavedTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function saveTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (error) {
      /* Storage unavailable: the theme still applies for this page view. */
    }
  }

  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";

  root.dataset.theme = getSavedTheme() || systemTheme;

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      button.addEventListener("click", function () {
        const next = root.dataset.theme === "dark" ? "light" : "dark";
        root.dataset.theme = next;
        saveTheme(next);
      });
    });
  });
})();
