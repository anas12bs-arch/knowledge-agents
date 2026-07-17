---
title: "vercel/next.js v16.3.0-canary.88 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.88"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-17T00:11:16Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.88"
---

# vercel/next.js v16.3.0-canary.88 released

> Source: github-releases | Category: changelog | 2026-07-17T00:11:16Z

## vercel/next.js — v16.3.0-canary.88

### Misc Changes

- Run more test suites under cacheComponents flag: #95878
- Unify appShells flag with Partial Prefetching: #95415
- Fix Request Insights span collection: #95818
- Revert "Replay same-document traversals that happen before hydration": #95853
- [ci] Allow running all deploy tests with builds from a private registry: #95784
- [turbopack] Only ship pages-router routes in the client chunk-group bootstrap manifest: #94671
- [turbopack] Inline the chunk group bootstrap in Next.js to drop the per-route runtime: #94666
- [turbopack] Add `chunk_group_bootstrap_params` and the chunk-loading global to the build manifest: #94663
- [turbopack] Add `registerEntry()` to handle inline bootstrapping (#94664)
- [turbopack] Add `inline_chunk_group_bootstrap` to `BrowserChunkingContext` and `chunk_group_bootstrap_params` to `ChunkGroupResult` (#94661)
- [turbopack] Create a `chunk_group_bootstrap_params()` function (#94631)
- [turbopack] Create a shared asset with browser runtime code (#94586)
- Turbopack: trace externals imported only by server actions (#95824)

### Credits 

Huge thanks to @gaearon, @acdlite, @timneutkens, @eps1lon, and @sampoder for helping!
