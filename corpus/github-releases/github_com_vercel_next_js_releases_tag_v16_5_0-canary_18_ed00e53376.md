---
title: "vercel/next.js v16.5.0-canary.18 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.18"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-20T12:00:55Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.18"
---

# vercel/next.js v16.5.0-canary.18 released

> Source: github-releases | Category: changelog | 2026-10-20T12:00:55Z

## vercel/next.js — v16.5.0-canary.18

### Core Changes

- Revert "Turbopack: loader change invalidation (#95732)": #100414
- Add <Link prefetch="navigation">: #99871
- remove Static render stage: #100388
- Don't load the app-page runtime in proxy.ts: #100384
- Format all READMEs with Prettier: #100310
- Fix Pages Router HMR crash when the ISR manifest arrives before the router: #100095
- Use os.availableParallelism() instead of os.cpus().length: #100258

### Misc Changes

- test: fix flakiness in segment-cache-stale-time: #100404
- docs: Clarify when useSearchParams boundaries render on the server with Cache Components: #100276
- Clarify which pathname usePathname reads under rewrites: #100393
- test: avoid useTempDir cleanup hang on Windows (fs-extra fixWinEPERM): #100088
- test: run custom install commands async with a hard timeout: #100057
- Clarify lazy SST opening in turbo-persistence docs: #100311
- Bump to swc v82: #100270
- test: disable the `reads fallback params after a client navigation` deployment test: #100371
- test: Pin react-virtualized: #100383
- turbo-persistence: read SST metadata blocks once with pread: #100288
- turbopack: intern merge bitmaps in compute_merged_modules: #100236
- Turbopack: don't scope hoist modules using direct eval: #100308

### Credits 

Huge thanks to @mischnic, @acdlite, @lubieowoce, @icyJoseph, @tobiaslins, @sokra, and @lukesandberg for helping!
