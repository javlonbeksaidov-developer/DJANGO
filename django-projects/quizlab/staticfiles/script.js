// Saved theme (UI preference only)
const root = document.documentElement;
try { const t = localStorage.getItem('theme'); if (t) root.dataset.theme = t; } catch (e) {}

document.addEventListener('DOMContentLoaded', () => {
  // Theme toggle
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => btn.addEventListener('click', () => {
    const next = root.dataset.theme === 'light' ? 'dark' : 'light';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  }));

  // Mobile nav
  const burger = document.querySelector('.burger'), nav = document.querySelector('.nav');
  if (burger && nav) burger.addEventListener('click', () => {
    burger.setAttribute('aria-expanded', nav.classList.toggle('open'));
  });

  // Close profile dropdown on outside click / Esc
  const menu = document.querySelector('.menu');
  if (menu) {
    document.addEventListener('click', e => { if (!menu.contains(e.target)) menu.open = false; });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') menu.open = false; });
  }

  // Countdown on the quiz page
  const timer = document.querySelector('[data-minutes]');
  if (timer) {
    let left = timer.dataset.minutes * 60;
    const tick = () => {
      const m = String(Math.floor(left / 60)).padStart(2, '0'), s = String(left % 60).padStart(2, '0');
      timer.textContent = m + ':' + s;
      timer.classList.toggle('low', left <= 60);
      if (left-- <= 0) { clearInterval(id); document.querySelector('main form').requestSubmit(); }
    };
    const id = setInterval(tick, 1000); tick();
  }
});
