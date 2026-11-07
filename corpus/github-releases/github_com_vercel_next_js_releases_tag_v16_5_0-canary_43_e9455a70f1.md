---
title: "vercel/next.js v16.5.0-canary.43 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.43"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-07T01:46:38Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.43"
---

# vercel/next.js v16.5.0-canary.43 released

> Source: github-releases | Category: changelog | 2026-11-07T01:46:38Z

## vercel/next.js — v16.5.0-canary.43

### Core Changes

- fix(app-render): stop prerendered Link headers from accumulating on revalidation: #100960
- Align eslint-config-next TypeScript peer with typescript-eslint: #101247
- Reduce header allocations in NodeNextResponse: #101225
- [image-optimizer] Move next/image-optimizer-transform under the next/experimental namespace: #101252
- [image-optimizer] Don't use NextConfigComplete for the imageOptimizerTransform public API: #101184
- Improve Request Insights context menus and trace interactions: #97796
- Build and analyze in one pass: #99962

### Misc Changes

- docs: clarify SVG handling in the Image Optimization API: #101301
- Turbopack: use hash collections for turbo-tasks values whose order is unobserved: #100939
- Turbopack: don't split page entries into a facade: #101152
- Turbopack: replace Next.js entry kinds with an opaque entry tag: #101291
- docs: map BFF proxy example routes to fixed backend endpoints: #101286
- docs: explain ESLint setup with TypeScript 7: #101246
- Durable use cache conditional reads: #101283
- docs: read the URL in history API event handlers instead of calling hooks: #101224
- review: escalate Next.js concepts in Turbopack code: #101278
- test: enable HMR dependency acceptance coverage for webpack: #101196
- test: Replace `itTurbopack` with test gates: #101195

### Credits 

Huge thanks to @styfle, @lukesandberg, @linyiru, @icyJoseph, @kassens, @mischnic, @eps1lon, @bgw, @DavidIlie, and @wbinnssmith for helping!
