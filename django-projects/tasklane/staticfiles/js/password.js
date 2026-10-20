/**
 * password.js — show / hide a password field.
 * Pure interactivity: it only switches the input type, it never reads,
 * sends, or stores the value.
 *
 * Usage: <button type="button" data-password-toggle="INPUT_ID">Show</button>
 */
(function () {
  document.querySelectorAll("[data-password-toggle]").forEach(function (button) {
    const input = document.getElementById(button.dataset.passwordToggle);
    if (!input) return;

    button.addEventListener("click", function () {
      const isHidden = input.type === "password";
      input.type = isHidden ? "text" : "password";
      button.textContent = isHidden ? "Hide" : "Show";
    });
  });
})();
