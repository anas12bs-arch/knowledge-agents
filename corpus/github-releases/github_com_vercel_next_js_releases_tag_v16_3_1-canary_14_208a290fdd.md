---
title: "vercel/next.js v16.3.1-canary.14 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.1-canary.14"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-08-12T13:39:34Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.1-canary.14"
---

# vercel/next.js v16.3.1-canary.14 released

> Source: github-releases | Category: changelog | 2026-08-12T13:39:34Z

## vercel/next.js — v16.3.1-canary.14

### Core Changes

- Fix debug build paths Pages Router support entries: #93529

### Misc Changes

- Restore the live `headers()` view of the incoming request: #97166
- [test] Compile the middleware redirect routes up front in dev: #97190
- Update gh-stack skill guidance: #97163
- [test] Unflake `use-cache-custom-handler-dev` tests: #97187
- Forward a build-container pin to deploy-test deployments: #97191
- Fix unset crossOrigin in Turbopack manifests: #97164
- Allow literal exports in `'use cache'` files: #97181
- Fix shared Turbopack runtime initialization race: #97215
- Fix stale data after navigation despite revalidation: #95439
- [turbopack] Only use the shared runtime by default on canary: #97208

### Credits 

Huge thanks to @unstubbable, @timneutkens, @Stanzilla, @gnoff, @gaearon, and @sampoder for helping!
