---
title: "vercel/next.js v16.3.0-canary.34 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.0-canary.34"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-05-30T14:31:13Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.0-canary.34"
---

# vercel/next.js v16.3.0-canary.34 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:13Z

## vercel/next.js — v16.3.0-canary.34

### Misc Changes

- Update `shortcircuit_if_known` to `eval_shortcircuit()`: #94163
- Remove dead code from `JsValue::Binary` in `is_truthy`: #94165
- Produce valid file URLs for `import.meta.url` on Windows in Turbopack: #94179
- [turbopack] Store TaskDirtyCause in Dirtyness and pass to NativeFunction::span: #94057
- Turbopack: cleanup ModuleHotReferenceAssetReference: #94206
- [feat] updated the documentation for deployment to point to new next.js Docker official guide.: #94185
- docs: correct custom server optimization guidance: #94229
- Add Errors/Insights tab split to the instant error overlay: #94073
- Replace VcStorage with real TurboTasks in tests/benches
: #93955
- Redesign the unrendered-segment instant validation overlay: #93879
- turbopack tracing: add chunk_name to `get HMR events` span: #94061
- Turbopack: reduce hmr chunk list subscriptions: #94062
- [turbopack] Separate `JsValue` into it's own folder in the analyzer: #94208
- feat(image-optimization): add experimental flag `imgOptOperationCache`: #94246

### Credits 

Huge thanks to @sampoder, @sokra, @mischnic, @kristiyan-velkov, @timneutkens, @aurorascharff, @lukesandberg, @wbinnssmith, and @styfle for helping!

