---
title: "vercel/next.js v16.5.0-canary.48 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.48"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-12T04:01:11Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.48"
---

# vercel/next.js v16.5.0-canary.48 released

> Source: github-releases | Category: changelog | 2026-11-12T04:01:11Z

## vercel/next.js — v16.5.0-canary.48

### Core Changes

- Prerender route handlers that await immediates: #101593
- Fix orphaned detached telemetry flush processes: #101588
- Upgrade React from `e84e1492-20261031` to `1620f7b9-20261111`: #101587
- docs: clarify tag invalidation client effects: #101504
- Keep dev overlay errors across no-op webpack hot updates: #101532

### Misc Changes

- Turbopack: don't grow effect vectors inside the analyzer arena: #101480
- Fix metadata route selection with `--debug-build-paths`: #101585
- eval: generate the docs pointer from the tested Next.js package: #101558
- Turbopack: scale default disk write concurrency: #101519
- eval: correct graders for Proxy, instant navigation, and category prefetching: #101523
- docs: clarify Server Actions configuration: #101549
- Turbopack: add build cache portability e2e test and fix location-dependent tasks: #100780
- Turbopack: replace SwcComments with a lightweight MutableComments store: #101543
- turbo-tasks-backend: merge aggregated data updates for new followers: #100435
- test: fix keep-alive socket reuse in CSS HMR race helper: #101530
- turbo-tasks: count task executions in task statistics: #101025
- test: fix repeated-slashes router push navigation race: #101528
- next-core: deserialize next.config env and output file tracing globs into typed maps: #100971
- turbo-tasks: add OrderedJsonValue/OrderedJsonMap with key-order-sensitive equality: #100964
- turbo-tasks: use OrderedAutoMap/OrderedAutoSet for order-observing values: #100940
- auto-hash-map: add positional access and IndexMap/IndexSet conversions for ordered maps: #101497
- test: close lingering prerender-export server connections: #101527
- test: fix flaky app-root-params-getters/simple: #101525
- test: fix flaky dev-validation-worker-source-maps: #101524
- turbo-tasks-malloc: use official mimalloc Rust bindings (v3.6.1): #101518
- docs: explain complementary Web Vitals and custom metrics APIs: #98968

### Credits 

Huge thanks to @unstubbable, @timneutkens, @jimmyhmiller, @aurorascharff, @sokra, @lukesandberg, and @adityareddy-dev for helping!
