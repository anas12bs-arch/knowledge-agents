---
title: "vercel/next.js v16.4.0-canary.26 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.4.0-canary.26"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-09-11T00:48:26Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.4.0-canary.26"
---

# vercel/next.js v16.4.0-canary.26 released

> Source: github-releases | Category: changelog | 2026-09-11T00:48:26Z

## vercel/next.js — v16.4.0-canary.26

### Misc Changes

- Add in warning for workers around the fsevents bug: #98447
- skill: add Partial Prefetching optimizer: #96471
- bundle-analyzer: add table view to single-build analyzer: #93523
- bundle-analyzer: add table view to compare mode: #93522
- bundle-analyzer: add compare view with treemap diff: #93521
- [testmode] Stop using deprecated `url.parse`: #98194
- fix(next/image): don't share the requester's socket with the internal image response: #98168
- Fix duplicate background revalidation for `'use cache'`: #98446
- Turbopack: Deduplicate project options documentation: #98465
- Report incompatible parallel route slots: #97430
- Require canonical routes for interception routes: #97428
- Error when app pages do not match any route: #97401
- fix(turbopack): add `get_relative_request_to` for paths used as module requests: #98497
- [ci] Cleanup orphaned `next-stats-action`: #98348
- [scripts] Move scripts (and benchmarks) off of `node-fetch`: #98347
- [test] Move fixtures off `node-fetch`: #98346
- [test] Move the harness off `node-fetch`: #98195
- fix(turbopack): resolve `../` and `/`-rooted `import.meta.glob` patterns: #96557

### Credits 

Huge thanks to @jimmyhmiller, @aurorascharff, @wbinnssmith, @eps1lon, @Amusac, @unstubbable, @bgw, @gnoff, and @sokra for helping!
