---
title: "vercel/next.js v16.3.0-canary.96 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.96"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-07-25T00:18:16Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.96"
---

# vercel/next.js v16.3.0-canary.96 released

> Source: github-releases | Category: changelog | 2026-07-25T00:18:16Z

## vercel/next.js — v16.3.0-canary.96

### Misc Changes

- [sourcemaps] Use file: sourcemaps for Turbopack to improve dev performance: #95946
- Give RouteCacheEntry a single hidden class across its lifecycle: #96164
- Keep optimistic-route param handling monomorphic: #96169
- Store RouteTree slots in a Map to keep slot access monomorphic: #96168
- Make reifyRouteTree object literals match the canonical RouteTree key order: #96162
- Keep VaryPath monomorphic by making isRootParam required: #96122
- docs: expand and modernize the Single-Page Applications guide: #95860
- docs: navigation interrupts after streaming has started (notFound, forbidden, unauthorized): #95851
- docs: reframe prefetching around automatic vs. controllable behavior: #95896
- docs(view-transitions): fix the skill install command: #96142
- Include additional prerender metadata about build-time routes: #96080
- Optimize app page entry analysis: #96058
- [ts-plugin] Preserve TypeScript quick info metadata: #95863
- [turbopack] Import Webpack's tests for tree-shaking: #95811
- [turbopack] Drop dead `require()` calls: #95718
- [turbopack] Track usage of modules imported with `require()`: #95717
- Return plain text 404 for non-document requests to unknown paths: #95930
- [RSC HMR] Fix a flurry of refetches when a editing component imported from many routes: #96102
- [turbopack] Track re-exports in `import_usage` inside of `compute_import_usage`: #95989

### Credits 

Huge thanks to @gaearon, @acdlite, @aurorascharff, @gnoff, @timneutkens, @devjiwonchoi, and @sampoder for helping!
