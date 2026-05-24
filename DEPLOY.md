# Deploying to Cloudflare Pages

This project is a Vue 3 + Vite SPA configured for deployment on Cloudflare Pages via Git integration.

## Project configuration

| Setting | Value |
|---|---|
| Framework | Vue 3 + Vite 8 |
| Router mode | HTML5 history (`createWebHistory`) |
| Package manager | pnpm (locked via `packageManager` field) |
| Node version | 22 (pinned in `.nvmrc`) |
| Build output | `dist/` |

## Files relevant to deployment

| File | Purpose |
|---|---|
| `public/_redirects` | SPA fallback. Routes every non-asset path to `index.html` so vue-router can resolve client-side routes. Without it, direct hits to `/about`, `/services`, etc. would 404. Vite copies `public/` contents into `dist/` at build time. |
| `.nvmrc` | Pins Node 22. Cloudflare Pages reads this automatically. Vite 8 requires Node `>=20.19` or `>=22.12`. |
| `package.json` → `packageManager` | Locks pnpm@10.32.1 via corepack so Cloudflare uses the same pnpm version as local. |
| `package.json` → `engines.node` | Documents the Node requirement. |
| `pnpm-lock.yaml` | The single source of truth for dependency versions. `package-lock.json` was removed to eliminate package-manager ambiguity. |

## One-time setup in the Cloudflare dashboard

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Authorize Cloudflare to access your Git provider, then select this repository.
4. On the **Set up builds and deployments** screen, enter:

   | Field | Value |
   |---|---|
   | Production branch | `main` |
   | Framework preset | `Vue` (or `None` — the values below are what matter) |
   | Build command | `pnpm run build` |
   | Build output directory | `dist` |
   | Root directory | *(leave blank)* |

5. Expand **Environment variables (advanced)** and add:

   | Variable | Value | Notes |
   |---|---|---|
   | `NODE_VERSION` | `22` | Redundant with `.nvmrc` but explicit. |

6. Click **Save and Deploy**. The first build takes ~1–2 minutes.

## How deploys work

- **Production**: every push to `main` triggers a build and deploys to `<project>.pages.dev` and any custom domain you attach.
- **Previews**: every push to any other branch (and every pull request) produces a unique preview URL like `<commit>.<project>.pages.dev`.
- **Rollbacks**: in the Pages dashboard, open any prior deployment and click **Rollback to this deployment**.

## Custom domain

In the Pages project → **Custom domains** → **Set up a custom domain**. Cloudflare provisions the TLS cert automatically. If the domain's DNS is on Cloudflare, the CNAME is added for you; otherwise, point a CNAME at `<project>.pages.dev`.

## Verification checklist (run after every deploy)

- [ ] `https://<project>.pages.dev/` loads the home view.
- [ ] `https://<project>.pages.dev/about` loaded **directly** (not via in-app nav) returns the About page, **not** a 404. This proves `_redirects` shipped.
- [ ] Hard-refresh (Ctrl/Cmd+Shift+R) on `/services` still loads the page.
- [ ] Browser console is free of 404s for assets, fonts, or images.
- [ ] Build log shows pnpm was used (look for `Installing dependencies with pnpm`) and Node 22.

If `/about`-style URLs 404, the `_redirects` file did not ship — confirm it exists at `public/_redirects` and check the build log shows it copied into `dist/`.

## Local commands

```sh
pnpm install         # install deps
pnpm run dev         # local dev server (http://localhost:5173)
pnpm run build       # production build → dist/
pnpm run preview     # serve dist/ locally to smoke-test the build
```

## Troubleshooting

**Build fails with "Unsupported engine" or Node version errors.**
Set the `NODE_VERSION` environment variable to `22` in the Pages project settings and re-run the deploy.

**Build uses npm instead of pnpm.**
Cloudflare auto-detects the package manager from the lockfile. Make sure `pnpm-lock.yaml` is committed and `package-lock.json` and `yarn.lock` are absent.

**`/about` loads on first visit but 404s on refresh.**
The `_redirects` file is missing from the deployed output. Verify `public/_redirects` exists in the repo and that `dist/_redirects` is produced locally by `pnpm run build`.

**Stale assets after deploy.**
Vite hashes asset filenames, so cache-busting is automatic. If you see stale HTML, it's the browser cache — hard refresh. Cloudflare's edge cache for HTML on Pages is short-lived (a few seconds).

**Need to deploy a one-off from your local machine without pushing to Git.**
Install Wrangler (`pnpm add -g wrangler`), then run `pnpm run build && wrangler pages deploy dist --project-name=<project>`. This bypasses the Git integration entirely.
