---
title: "vercel/next.js v16.3.0-canary.37 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.37"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-06-02T13:00:43Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.37"
---

# vercel/next.js v16.3.0-canary.37 released

> Source: github-releases | Category: changelog | 2026-06-02T13:00:43Z

## vercel/next.js — v16.3.0-canary.37

### Misc Changes

- Switch `TotalOrderF64` to `f64` in `ConstantNumber` to correctly handle `NaN === NaN` and `0 === -0` inside the Turbopack analyzer: #94172
- Use `serde_json::Number` in `CompileTimeDefineValue` and remove `TotalOrderF64`: #94177
- docs: bodySizeLimit measures raw HTTP body: #94137
- Update ctor from 0.10 to 1.0.6: #94045
- Include `--port` in `next internal query-trace` startup hint and help example: #93961
- Turbopack: refactor NFT to add Endpoint.traced_files: #94224
- Turbopack: show codeframe when tracing too much: #94207
- fix(instrumentation): await instrumentation in RouteModule.prepare: #94306
- [turbopack] Function pointers are copy: #94273
- docs: accuracy and pappercuts: #94299

### Credits 

Huge thanks to @sampoder, @icyJoseph, @sokra, @mischnic, and @lukesandberg for helping!

