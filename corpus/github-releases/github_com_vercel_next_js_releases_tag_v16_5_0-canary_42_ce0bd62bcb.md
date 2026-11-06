---
title: "vercel/next.js v16.5.0-canary.42 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.42"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-06T02:55:51Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.42"
---

# vercel/next.js v16.5.0-canary.42 released

> Source: github-releases | Category: changelog | 2026-11-06T02:55:51Z

## vercel/next.js — v16.5.0-canary.42

### Core Changes

- Persist Request Insights session history: #97795
- Show route module loading and preparation in Request Insights: #97362
- Improve Request Insights request and fetch details: #96925
- Automatically compress route handler responses if not already compressed: #101220
- experimental_prepare: Don't refetch on commit due to stale inlining hints: #101234
- Bump to swc v83: #101079
- [image-optimizer] Remove optimizeImage from the public next/image-optimizer-transform API: #101133

### Misc Changes

- Add a server-router regression gate: pnpm test-routing: #100812
- [turbopack] Fix GC/eviction race by dropping task resurrection: #100370
- docs: buffer and re-serialize in the BFF proxy Route Handler example: #101199
- Turbopack: test strict receivers in minified mixed chunks: #101239
- Turbopack: retry chunk loads that failed with component chunks: #101179
- Bump to swc v84: #101194
- docs: require Cache Components compatibility for new e2e tests: #101222
- [ci] Resolve the PR to comment on from the workflow run alone: #101090
- test: capture finished OTel spans from console output in otel-middleware-trace: #100664
- Turbopack: keep IIFEs with a PURE-annotated callee in production builds: #100477
- docs: clarify directory-specific test gate guidance: #101200
- eval: verify independent dashboard streaming: #101155
- Turbopack: generate import.meta.glob as a synthetic module: #100535
- Turbopack: report unknown module types at the import: #100534
- Turbopack: use flat module context ids for dynamic requests: #100681
- Turbopack: read block-scoping support during codegen: #101157
- Make Firebase tracing fixture independent of backend connectivity: #101180
- Pin Tailwind to 4.3.3 in no-double-tailwind-execution test: #101176

### Credits 

Huge thanks to @jamiboym, @lukesandberg, @DavidIlie, @icyJoseph, @eps1lon, @timneutkens, @mischnic, @acdlite, @sokra, @aurorascharff, @bgw, and @wbinnssmith for helping!
