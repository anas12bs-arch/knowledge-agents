---
title: "vercel/next.js v16.5.0-canary.6 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.6"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-09T18:51:18Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.6"
---

# vercel/next.js v16.5.0-canary.6 released

> Source: github-releases | Category: changelog | 2026-10-09T18:51:18Z

## vercel/next.js — v16.5.0-canary.6

### Core Changes

- Add more metadata to agent upgrade telemetry: #99925
- perf: reduce build tree view allocations: #99930
- fix: classify collapsed generated paths from child routes: #99864
- Upgrade React from `d75b0697-20261006` to `b618bbb4-20261007`: #99879

### Misc Changes

- docs(skills): use agent-agnostic branch prefix in create-pr: #99934
- [test] Regression test for XSS-safe `GoogleTagManager#dataLayer`: #99464
- [image-optimization] Expose `next/image-optimizer-transform` as a public subpath: #99312
- fix(next): register the chunk groups that are chunked: #99749
- refactor(turbopack): chunk several chunk groups in one chunk_group call: #99686
- Turbopack: canonicalize chunk group identity: #98733
- Turbopack: add zstd compression flags for NEXT_TURBOPACK_TRACING: #99808
- Turbopack: omit Exit+Enter trace row pairs with (almost) no gap: #99780
- Turbopack: delta-encode trace allocation counters and skip unchanged ones: #99779
- Turbopack: merge allocation counters into trace Enter/Exit rows: #99778
- [cd] Replace versioned release branches with fixed `releases/lts/*` refs: #99807
- test: Really use pnpm on deploy tests: #95360
- test: compare cache-control directives as a set in deploy tests: #99892

### Credits 

Huge thanks to @devjiwonchoi, @aurorascharff, @sokra, @eps1lon, and @mischnic for helping!
