---
title: "vercel/next.js v16.3.2 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-08-21T09:43:58Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.2"
---

# vercel/next.js v16.3.2 released

> Source: github-releases | Category: changelog | 2026-08-21T09:43:58Z

## vercel/next.js — v16.3.2

> [!NOTE]
> This release is backporting bug fixes. It does **not** include all pending features/changes on canary.

### Core Changes

- [backport] Scope app-entry export validation to files inside the app directory (#97357)
- [backport] Fix catch-all index page being served for every other slug (#97416)
- [16.3] Turbopack: don't trace embedded WASM loader helpers (#97353) (#97463)
- [16.3] Turbopack: retain conditions when replacing resolve request keys (#97453)
- [16.3.x] Fix Turbopack worker chunk loading with asset prefix (#97419)
- [16.3.x] Authenticate Turborepo remote caching with OIDC instead of a static PAT (#97603)

### Credits

Huge thanks to @lubieowoce, @unstubbable, @timneutkens, @mischnic, and @eps1lon for helping!
