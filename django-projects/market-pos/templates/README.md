# MarketPOS: front-end

A desktop-style point-of-sale UI built with plain HTML, CSS and JavaScript. No build step and no dependencies.
Open `login.html` in a browser (Chrome, Edge, Firefox or Safari, window at least 1024px wide).

## Demo sign-in
Any password works. Username `admin` signs in as **Admin** (all pages). Any other username signs in as **Cashier** (Sale, Return, Profile only).

## Structure
```
login.html      Sign in
sale.html       Sale (cashier)         return.html    Return / refund (cashier)
profile.html    Profile (cashier)
reports.html    Cashier reports (admin)    products.html  Products + discounts (admin)
users.html      Users (admin)              store.html     Store settings (admin)

css/
  base.css          design tokens (light + dark), reset
  layout.css        app shell: sidebar, toolbar, page area, status bar
  components.css    cards, grids, tags, tables, totals, avatar
  forms.css         buttons, inputs, labels, password reveal button
  modal.css         <dialog> modals
  theme-switch.css  dark mode toggle
  login.css  sale.css  reports.css    page-specific styles

js/
  session.js    access guard (data-access on <html>), session, logout, user name
  login.js      demo sign-in handler (login page only)
  theme.js      light/dark switch, saved in localStorage
  modal.js      opens/closes dialogs via data-open / data-close
  password.js   Show/Hide button on password fields
  shortcuts.js  F1 Sale, F2 Search, F3 Return, F9 Charge
  clock.js      status-bar date and time
```

## Data handling
All data actions are plain HTML `<form>`s (`method="post"` / `get`) with static sample data and no JavaScript.
Point each form's `action` at your backend. Pages are static, so render the real data server-side.

## Moving from demo to production
- Delete `js/login.js` and its `<script>` tag; let the `/login` form post to the server.
- In `session.js`, remove the demo `login()` and the logout `submit` handler; keep only the part that fills in the user's name.
- Enforce roles on the server. The `data-access` check and the `.admin` CSS class only hide UI.
