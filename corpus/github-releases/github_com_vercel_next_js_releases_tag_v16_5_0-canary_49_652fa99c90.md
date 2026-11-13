---
title: "vercel/next.js v16.5.0-canary.49 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.49"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-13T00:46:59Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.49"
---

# vercel/next.js v16.5.0-canary.49 released

> Source: github-releases | Category: changelog | 2026-11-13T00:46:59Z

## vercel/next.js — v16.5.0-canary.49

### Core Changes

- Optimize NFT base path mapping: #101151
- Fix `ImageResponse` prerendering with `--debug-prerender`: #101678
- Upgrade React from `1620f7b9-20261111` to `df6aa4ec-20261112`: #101673
- Fix ESLint link rule for constant and mapped hrefs: #101641
- Complete metadata references and fix descriptor resolution: #101547
- docs: clarify dynamicParams with Cache Components: #100249
- Test Proxy Link headers across cache revalidation: #101620
- Remove obsolete prerender abort workarounds: #101621
- Use forward slashes in route bundle stats chunk paths: #101617
- Preserve build diagnostics during worker shutdown: #101598

### Misc Changes

- turbo-tasks-backend: keep the active count inline: #101486
- turbopack: use static for shared rcstr! values and hardcode magic identifiers: #101686
- docs: clarify synchronous IO after request data: #101685
- turbo-persistence: remove ParallelScheduler::block_in_place: #101544
- Turbopack: release freed memory right after project shutdown: #101529
- turbo-tasks-backend: read collectibles and update the reader dependency atomically: #101548
- [internal-skills] fetch CI status on demand instead of blocking on --wait: #101661
- Fix pnpm-lock.yaml for bench/large-app-router after React upgrade: #101642
- bench: add generated large App Router benchmark for Turbopack scaling: #101502
- test: fix flaky vary-params-base-dynamic prefetch collection: #101531
- test: fit cold-cache npm install in create-next-app template test timeout: #101625
- docs: add native DOM examples to Activity guide: #101581
- turbo-persistence: report batch_get misses from batch_lookup_entry: #101615
- create-next-app: exit with code 1 when installation fails: #101624
- Strengthen documentation review criteria: #101622
- Turbopack: skip unmatched siblings when building app loader trees: #101535
- docs: explain runtime config removal on the middleware-to-proxy error page: #101616
- Turbopack: start whole-app client style groups earlier in production builds: #101612
- turbo-tasks: don't make parentless transient tasks aggregation roots: #101614
- turbo-tasks: avoid redundant aggregation roots and root-upper optimization cascades: #101604
- turbo-persistence: make batch_get callback-oriented: #100678

### Credits 

Huge thanks to @lukesandberg, @mischnic, @aurorascharff, @sokra, @unstubbable, @eps1lon, and @icyJoseph for helping!
