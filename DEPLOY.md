# Deploying to Cloudflare Pages

This project is a Vue 3 + Vite SPA configured for deployment on Cloudflare Pages via Git integration.

## Deployment summary

| | |
|---|---|
| Cloudflare project name | `solviaone` |
| Production URL (Cloudflare) | `https://solviaone.pages.dev` |
| Custom domain (apex) | `solvia-one.com` |
| Custom domain (www) | `www.solvia-one.com` |
| GitHub repo | `jonathanlyao/solviaone-vue` |
| Deploy owner | Jonathan (admin on the GitHub repo) |
| Preview deployments | **Disabled** — only `main` builds |

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

## Prerequisites

- All deployment-prep changes (this file, `.nvmrc`, `public/_redirects`, `package.json` edits, `pnpm-lock.yaml`, removal of `package-lock.json`) must be committed to `main` and pushed before connecting Cloudflare. Cloudflare builds from the current state of the production branch.
- **Jonathan** (repo admin on `jonathanlyao/solviaone-vue`) must perform the dashboard setup, since the Cloudflare GitHub App needs to be installed on the account that owns the repo.

## One-time setup in the Cloudflare dashboard

1. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/).
2. Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Authorize the Cloudflare GitHub App on the `jonathanlyao` account and grant access to `solviaone-vue`. Then select that repository.
4. On the **Set up builds and deployments** screen, enter:

   | Field | Value |
   |---|---|
   | Project name | `solviaone` |
   | Production branch | `main` |
   | Framework preset | `Vue` (or `None` — the values below are what matter) |
   | Build command | `pnpm run build` |
   | Build output directory | `dist` |
   | Root directory | *(leave blank)* |

5. Expand **Environment variables (advanced)** and add:

   | Variable | Value | Notes |
   |---|---|---|
   | `NODE_VERSION` | `22` | Redundant with `.nvmrc` but explicit. |

6. Click **Save and Deploy**. The first build takes ~1–2 minutes. The site will be live at `https://solviaone.pages.dev`.

## Disable preview deployments

This project is configured for production-only deploys (no preview URLs for branches or PRs).

After the first deploy:

1. Open the **solviaone** Pages project.
2. **Settings** → **Builds & deployments** → **Configure preview deployments**.
3. Set **Preview deployments** to **None**.
4. Save.

Only pushes to `main` will trigger builds from this point on.

## How deploys work

- **Production**: every push to `main` triggers a build and deploys to `https://solviaone.pages.dev` and the custom domains below.
- **Previews**: disabled for this project (see previous section). Branch and PR pushes do not build.
- **Rollbacks**: in the Pages dashboard, open any prior deployment and click **Rollback to this deployment**.

## Custom domain setup — solvia-one.com

DNS for `solvia-one.com` is hosted **outside Cloudflare**. Both apex (`solvia-one.com`) and `www.solvia-one.com` will be attached, with apex redirecting to www (the standard pattern that avoids the apex-CNAME problem).

### Step 1 — add the domains in the Cloudflare Pages dashboard

In the **solviaone** Pages project → **Custom domains** → **Set up a custom domain**:

1. Add `www.solvia-one.com`. Cloudflare will display the CNAME target it expects (it will be `solviaone.pages.dev`).
2. Add `solvia-one.com`. Cloudflare will display the DNS records it expects.

### Step 2 — add DNS records at your external DNS host

| Type | Name | Value | Notes |
|---|---|---|---|
| `CNAME` | `www` | `solviaone.pages.dev` | Standard subdomain CNAME — works at every DNS host. |
| `ALIAS` / `ANAME` | `@` (apex) | `solviaone.pages.dev` | Most DNS hosts (Cloudflare DNS, Route 53, DNSimple, easyDNS, Namecheap "URL Redirect Record") support this. **If your DNS host does not support ALIAS/ANAME**, see "Apex domain options" below. |

After the DNS records propagate (usually minutes, occasionally up to 24h), Cloudflare auto-provisions TLS certificates for both hostnames.

### Step 3 — redirect apex to www (or vice versa)

In the Pages project → **Custom domains** → click the row for `solvia-one.com` → **Edit** → enable the redirect to `https://www.solvia-one.com`. This sets up a 301 at the edge.

### Apex domain options if your DNS host does not support ALIAS/ANAME

A plain `CNAME` is not legal at the zone apex per RFC 1034. If your DNS host only supports `A`/`AAAA`/`CNAME` for the apex, pick one:

- **Move DNS for solvia-one.com to Cloudflare** (recommended). Cloudflare's DNS supports CNAME flattening at the apex automatically. The rest of the setup is unchanged.
- **Use HTTP redirect record** (some hosts call this "URL Redirect" or "Web Forwarding") to permanently redirect `solvia-one.com` → `https://www.solvia-one.com`. The apex never serves the site directly in this case.
- **A records** are not provided by Cloudflare Pages (Pages serves from a CDN with rotating IPs), so this is not a usable fallback.

### Verifying the custom domain

- `https://www.solvia-one.com/` loads the home view.
- `https://solvia-one.com/` redirects to `https://www.solvia-one.com/` (301).
- Browser shows a valid TLS certificate issued for both names.
- `dig www.solvia-one.com CNAME` resolves to `solviaone.pages.dev`.

## Verification checklist (run after every deploy)

- [ ] `https://solviaone.pages.dev/` loads the home view.
- [ ] `https://solviaone.pages.dev/about` loaded **directly** (not via in-app nav) returns the About page, **not** a 404. This proves `_redirects` shipped.
- [ ] Hard-refresh (Ctrl/Cmd+Shift+R) on `/services` still loads the page.
- [ ] Browser console is free of 404s for assets, fonts, or images.
- [ ] Build log shows pnpm was used (look for `Installing dependencies with pnpm`) and Node 22.
- [ ] (After custom domain setup) `https://www.solvia-one.com/` serves the site over HTTPS and `https://solvia-one.com/` 301-redirects to it.

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
Vite hashes asset filenames (`index-<hash>.js`), so cache-busting for JS and CSS is automatic. Cloudflare Pages does not cache `index.html` at the edge by default, so if you see stale content it's almost always the browser cache — hard refresh (Ctrl/Cmd+Shift+R).

**Custom domain not resolving or shows TLS error.**
- Confirm the DNS records at the external host match what the Pages dashboard requested. Use `dig www.solvia-one.com CNAME` to check.
- TLS provisioning can take a few minutes after DNS propagates. The Pages dashboard shows a status indicator for each custom domain.
- If the apex still doesn't resolve and your DNS host doesn't support ALIAS/ANAME, see "Apex domain options" in the custom domain section.

**Need to deploy a one-off from your local machine without pushing to Git.**
Install Wrangler (`pnpm add -g wrangler`), then run `pnpm run build && wrangler pages deploy dist --project-name=solviaone`. This bypasses the Git integration entirely.
