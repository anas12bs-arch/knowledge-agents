---
title: "vercel/next.js v16.3.0 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-08-03T21:52:32Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0"
---

# vercel/next.js v16.3.0 released

> Source: github-releases | Category: changelog | 2026-08-03T21:52:32Z

## vercel/next.js — v16.3.0

### Core Changes
- Update vendored lodash to 4.17.23 to fix CVE-2025-13465: #91558
- Fix invalid HTML response for route-level RSC requests in deployment adapter: #91541
- Normalize encoded dynamic placeholders in app routes: #91603
- Fix(pages-router): restore Content-Length and ETag for /_next/data/ JSON responses: #90304
- Update tokio from 1.43.0 to 1.47.3: #90945
- [turbopack] Simplify snapshotting logic: #91178
- Turbopack: enable server HMR for app route handlers: #91466
- turbo-tasks-backend: batch find_and_schedule_dirty using for_each_task_meta: #91497
- [turbopack] Use bail! instead of panic! for duplicate module ident error: #91636
- Skip loadBindings() Lightning CSS check during next start: #91538
- turbo-tasks-backend: batch schedule dirty tasks in aggregation_update: #91461
- Turbopack: Add importModule() support to webpack loaders: #89630
- turbo-persistence: fix mmap page alignment and improve error context in MetaFile::open_internal: #91640
- turbopack-css: demote recoverable CSS parse warnings to Warning severity: #91524
- feat(node-streams): add config flag, define-env, and env precedence test: #90427
- Rename /_next/webpack-hmr to /_next/hmr: #91415
- Add per-slot error attribution for instant validation using slot markers and config depth preference: #91610
- Handle encoded params further: #91627
- [turbopack] Respect `{eval:true}` in worker_threads constructors: #91666
- Fix missing route in otel spans without base-server: #91665
- [turbopack] Optimize compaction cpu usage: #91468
- Fix layout segment optimization: move app-page imports to server-utility transition: #91701
- Fix server actions in standalone mode with `cacheComponents`: #91711
- turbo-persistence: remove Unmergeable mmap advice: #91713
- turbopack: move "compact database" tracing span to backend layer: #91693
- Turbopack: lazy require metadata and handle TLA: #91705
- Fix adapter outputs for dynamic metadata routes: #91680
- Turbopack: fix webpack loader runner layer: #91727
- [turbopack] Remove incorrect debug_assert in try_read_task_cell: #91699
- Add module count field to module graph tracing spans: #91697
- turbopack-cli: add --persistent-caching flag for filesystem-backed cache: #91657
- Turbopack: pull in updated vercel/nft tests: #91651
- [turbopack] Improve regressed build speed on cross-compiled MUSL: #91477
- [Segment Bundling] [Scaffolding] Ensure inlining hint correctness: #91320
- [Segment Bundling] [Scaffolding] Track which segments can be omitted from prefetch: #91438
- Avoid deprecated TS node10 moduleResolution defaults: #91847
- [turbopack] Rebuild the docker build scripts: #91799
- Fix TS6 baseUrl deprecation for extended tsconfig: #91855
- Add `next internal post-build` CLI command for Turbopack database compaction: #91336
- Turbopack: Define `Effect` as a trait instead of a closure: #89080
- Turbopack: Implement TraceRawVcs and NonLocalValue correctly for Effects: #89133
- turbo-tasks-backend: improve print_cache_item_size instrumentation: #91742
- Turbopack: switch from base40 to base38 hash encoding (remove ~ and . from charset): #91832
- Use charCodeAt for normalizePathTrailingSlash: #91380
- Turbopack: Only patch lockfile when bindings fails to load: #91379
- [create-next-app] Skip interactive prompts when CLI flags are provided: #91840
- [devtools] Make instant navs panel draggable: #91914
- [Segment Bundling] Bundle static prefetches based on size: #91439
- turbo-tasks-backend: assert non-transient task_ids in track_modification: #91924
- fix(turbopack): preserve resolveExtensions priority in read_matches fast path: #91856
- turbopack: Remove Vc::resolve(), migrate all callsites to Vc::to_resolved(): #91725
- turbo-tasks: add hashed cell mode for hash-based change detection without cell data: #91576
- [cna] Upgrade to Biome 2.4 with Tailwind support: #86065
- [devtools] Show `AggregateError.errors` in the error overlay: #91835
- Narrow the opengraph-image fu
