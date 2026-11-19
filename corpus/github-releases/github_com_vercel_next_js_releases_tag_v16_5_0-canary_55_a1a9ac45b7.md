---
title: "vercel/next.js v16.5.0-canary.55 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.55"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-19T04:02:30Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.55"
---

# vercel/next.js v16.5.0-canary.55 released

> Source: github-releases | Category: changelog | 2026-11-19T04:02:30Z

## vercel/next.js — v16.5.0-canary.55

### Core Changes

- fix(ts-plugin): accept quoted prefetch segment config values: #101895
- Fix Navigation Inspector dark mode contrast: #102008
- Turbopack: add max_chunk_size to production chunking: #100478
- refactor: Move minimalMode checks earlier in conditionals: #102004
- Upgrade React from `df6aa4ec-20261112` to `a8342585-20261117`: #101942
- Refactor durableUseCacheEntries configuration: #101930
- Remove unused `didStripLocale` request meta: #101999
- Widen Turbopack maxDuration to u64: #101116
- turbo-bincode: remove indexmap/indexset helpers and use OrderedAutoMap/OrderedAutoSet in cells: #101520

### Misc Changes

- [test] Stop using async Client Components: #101948
- Change REVIEW.md instructions to never at-mention owners: #102001
- chore: add ast-grep untracked() rule: #101994
- Add INVALIDATION comments to untracked() calls: #101993
- chore: switch to ident_string() where possible: #101996
- docs: clarify Route Handler caching config with Cache Components: #101990
- Turbopack: detect top-level `this` as CommonJS exports: #101727
- feat(turbopack): Add EmitOption trait for extensible chunking context configuration: #101001
- pr-status: look up PR runs by head SHA and load job logs on gh 2.97+: #101707
- Clarify images.path docs and ungate two routing gate tests: #101582
- pr-status: flag finished runs that didn't pass but have no failed jobs: #101714
- Add e2e coverage for next start's HTTP and process behavior: #101710
- docs: note tsconfig include changes with a custom distDir: #101963

### Credits 

Huge thanks to @DominikKoniarz, @samselikoff, @sokra, @lubieowoce, @eps1lon, @mischnic, @aurorascharff, @jamiboym, and @lukesandberg for helping!
