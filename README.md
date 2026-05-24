# solviaone-vue

Marketing site for **Solvia One LLC** — *Precision in Digital Architecture*.

Single-page Vue 3 app deployed to Cloudflare Pages at [solviaone.pages.dev](https://solviaone.pages.dev) and (eventually) [www.solvia-one.com](https://www.solvia-one.com).

## Stack

| | |
|---|---|
| Framework | [Vue 3](https://vuejs.org/) (`<script setup>` SFCs) |
| Build tool | [Vite 8](https://vite.dev/) |
| Routing | [vue-router 4](https://router.vuejs.org/) (HTML5 history mode) |
| Styling | [Tailwind CSS 3](https://tailwindcss.com/) with a Material Design 3 color token palette |
| Fonts | Manrope (headlines), Inter (body) — loaded from Google Fonts |
| Package manager | [pnpm](https://pnpm.io/) 10 |
| Node | 22 (pinned in [`.nvmrc`](.nvmrc)) |
| Hosting | [Cloudflare Pages](https://pages.cloudflare.com/) |

## Project layout

```
.
├── public/              # static assets copied as-is into dist/
│   ├── _redirects       # SPA fallback for Cloudflare Pages routing
│   ├── favicon.svg
│   ├── icons.svg
│   └── images/
├── src/
│   ├── App.vue          # root layout: NavBar + <router-view> + Footer
│   ├── main.js          # app bootstrap
│   ├── style.css        # global styles + Tailwind directives
│   ├── assets/          # imported images and SVGs
│   ├── components/
│   │   ├── NavBar.vue
│   │   └── Footer.vue
│   ├── router/
│   │   └── index.js     # route definitions
│   └── views/
│       ├── HomeView.vue
│       ├── AboutView.vue
│       ├── ServicesView.vue
│       ├── AdvantagesView.vue
│       ├── CasesView.vue
│       ├── NewsView.vue
│       └── ContactView.vue
├── index.html
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
└── DEPLOY.md            # Cloudflare Pages deployment guide
```

## Routes

| Path | View |
|---|---|
| `/` | `HomeView` |
| `/about` | `AboutView` |
| `/services` | `ServicesView` |
| `/advantages` | `AdvantagesView` |
| `/cases` | `CasesView` |
| `/news` | `NewsView` |
| `/contact` | `ContactView` |

All routes are SPA-resolved client-side. Cloudflare Pages serves `index.html` for unknown paths via [`public/_redirects`](public/_redirects) so deep links and refreshes work.

## Getting started

Prerequisites: Node 22+, pnpm 10+.

```sh
pnpm install         # install dependencies
pnpm run dev         # start dev server at http://localhost:5173
pnpm run build       # production build → dist/
pnpm run preview     # serve the built dist/ locally
```

## Deployment

This project deploys to Cloudflare Pages via GitHub integration on push to `main`. See [DEPLOY.md](DEPLOY.md) for the full deployment guide — project setup, custom domain configuration for `solvia-one.com`, verification checklist, and troubleshooting.

## Utility scripts

| File | Purpose |
|---|---|
| [`download-images.cjs`](download-images.cjs) | One-off Node script for fetching marketing imagery into `public/images/`. |
| [`download_images.py`](download_images.py) | Python equivalent of the above. |

These are tooling scripts, not part of the runtime build.
