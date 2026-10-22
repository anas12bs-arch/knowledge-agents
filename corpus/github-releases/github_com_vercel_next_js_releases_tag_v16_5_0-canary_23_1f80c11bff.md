---
title: "vercel/next.js v16.5.0-canary.23 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.23"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-22T23:33:01Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.23"
---

# vercel/next.js v16.5.0-canary.23 released

> Source: github-releases | Category: changelog | 2026-10-22T23:33:01Z

## vercel/next.js — v16.5.0-canary.23

### Core Changes

- Upgrade React from `a6792708-20261019` to `ab0d927f-20261020`: #100527
- Preserve deferred middleware instrumentation spans when the adapter throws: #100552
- Fix cache revalidation queued during streaming: #100448
- Remove unnecessary `as any` casts: #100418
- Update font data: #100490
- Turbopack: preserve chunk load promise identity: #100421
- Emit instrumentation lifecycle spans in the request that registered it: #100350
- docs: note that instrumentation-time spans don't join request traces: #100324
- Keep middleware and render in one OpenTelemetry trace as siblings: #100294
- Start the request span before route module preparation: #100349
- Fix prerender manifest update race in dev: #100521
- Report process memory footprint (RSS) in TurboMalloc and trace samples: #99527
- Preserve cached values for the final runtime prerender: #100447
- Calling server actions in GSP fails `__next_require__ is not a function`: #99912
- fix: persist cacheControl for Pages Router ISR entries in FileSystemC…: #100495

### Misc Changes

- [cd] Move release un-draft to a follow-up job: #100571
- Fix analyzer cell creation order: #100562
- [ci] Run flakiness detection under concurrent load: #100525
- [test] Avoid port collisions in concurrent OpenTelemetry tests: #100538
- [test] Avoid port collisions in concurrent keep-alive tests: #100537
- turbopack: use reverse postorder priority in compute_binding_usage_info: #100440
- turbo-tasks: unemit taken collectibles in a single backend operation: #100437
- Bump turbo to 2.11.10: #100549
- Turbopack: lazily compile lazy import.meta.glob matches: #100523
- turbo-tasks: batch invalidation via Invalidator::invalidate_all: #100485
- turbo-tasks: make scope_unbounded worker churn test deterministic: #100515
- Turbopack: test import.meta.glob code splitting with an execution test: #100532
- Turbopack: fix chunking for lazy import.meta.glob matches: #100522
- [test] Stabilize the cache revalidation navigation test: #100514
- Bump to swc v82.2.0: #100508
- turbo-tasks-backend: skip dirtying removed cell dependents: #100460
- docs: use the exported unstable_doesMiddlewareMatch name in proxy unit testing: #100499
- turbo-tasks-backend: restore invalidated tasks with batched optional reads: #100465
- Durable use cache: don't crash on Node workers: #100505

### Credits 

Huge thanks to @eps1lon, @zydo, @unstubbable, @sokra, @jamiboym, @sokra, @lubieowoce, @mischnic, @icyJoseph, @koreahghg and @lukesandberg for helping!
