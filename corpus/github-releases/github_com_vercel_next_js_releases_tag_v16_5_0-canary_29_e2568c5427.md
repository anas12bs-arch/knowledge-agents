---
title: "vercel/next.js v16.5.0-canary.29 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.29"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-28T07:01:45Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.29"
---

# vercel/next.js v16.5.0-canary.29 released

> Source: github-releases | Category: changelog | 2026-10-28T07:01:45Z

## vercel/next.js — v16.5.0-canary.29

### Core Changes

- Create cache directory before persisting Chrome DevTools workspace UUID: #100802
- Upgrade React from `ab0d927f-20261020` to `dc9aed36-20261027`: #100791
- [testmode] Fix compressed HTTP responses with test proxy: #100805
- chore(deps): bump sharp@0.35.5: #99714
- Turbopack: Auto-detect pnpm GVS and configure an additional root for it: #99758
- Persist storage cache in Docker environments: #100790
- Persist fully static PPR payloads in filesystem cache: #100759
- Stamp FileSystemCache revalidations and entries with the monotonic clock: #100357

### Example Changes

- examples: add eve example: #100758

### Misc Changes

- turbo-bitset: make block storage pluggable: #100779
- Use fixed encoding for our 'id' types: #100764
- [RFC] Remove worktree guidance from AGENTS.md: #100659
- eval: resolve and classify the audit suite: #100748
- turbo-tasks-backend: resolve task priority when creating child contexts: #100767
- Add server-only leak pass to next-bundle-optimizer: #100330
- Turbopack: Fix webpack loaders if source file exists in an additional root: #100744
- [CI] fix incorrect VERCEL_TEST_PROJECT in non-cache-components deploy…: #100788
- ci: run changed deploy tests with both builders: #100591
- Turbopack: compute client reference manifest parts once per reference, not per page: #100443
- turbo-bitset: remove FixedBitSet and RoaringBitmap comparisons: #100724
- turbopack: use Bitset for persisted chunk group sets: #100630
- turbopack: use Bitset in compute_merged_modules: #100568
- turbopack: use Bitset in collect_graph: #100567
- turbopack: use Bitset in compute_chunk_group_info: #100643
- turbo-bitset: add Bitset, a fast bitset over a bounded bit range: #100566
- turbopack: speed up and share reverse postorder ranks: #100452
- test: remove some more dev/prod gating: #100717
- ci: Only run upload-adapter-test-results on release: #100595
- Optimize persistence CPU: #100737
- eval: split Next.js evals by purpose: #100742

### Credits 

Huge thanks to @sokra, @chadhietala, @lukesandberg, @kassens, @styfle, @aurorascharff, @wbinnssmith, @bgw, @namtran1812, @skrabe, and @mischnic for helping!
