---
title: "vercel/next.js v16.5.0-canary.46 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.46"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-10T02:26:28Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.46"
---

# vercel/next.js v16.5.0-canary.46 released

> Source: github-releases | Category: changelog | 2026-11-10T02:26:28Z

## vercel/next.js — v16.5.0-canary.46

### Core Changes

- Resolve parallel route params from the URL when predicting routes: #101477
- Prevent prerenders from changing foreground response status: #101295
- Release fetch cache locks when origin fetch throws synchronously: #101461
- Don't block the dev overlay on the npm registry version check: #100628
- Fix deployed RSC responses after static-to-partial revalidation: #101454
- docs: enable the testing API at build and server startup: #101443

### Misc Changes

- turbo-tasks: pack CellKey into one word: #101393
- Turbopack: use bincode fixint encoding for ids and persisted hashes: #101419
- [evals] Move fixtures to AI SDK 7: #101470
- Turbopack: migrate CSS snapshot tests to execution tests: #101232
- Turbopack: migrate basic snapshot tests to execution tests: #101231
- Turbopack: migrate tree-shaking and scope-hoisting snapshot tests to execution tests: #101230
- Turbopack: migrate ESM export optimization snapshot tests to execution tests: #101229
- Turbopack: migrate CommonJS tree-shaking snapshot tests to execution tests: #101228
- Turbopack: migrate comptime snapshot tests to execution tests: #101227
- Turbopack: migrate import and resolution snapshot tests to execution tests: #101211
- Require real router interactions in navigation tests: #101462
- [create-next-app] Output next steps commands when creating app from template: #99769

### Credits 

Huge thanks to @lukesandberg, @acdlite, @unstubbable, @swarnava, @sokra, @ShakilUrRehman21, and @aurorascharff for helping!
