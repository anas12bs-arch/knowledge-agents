---
title: "vercel/next.js v16.5.0-canary.32 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.32"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-30T05:39:26Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.32"
---

# vercel/next.js v16.5.0-canary.32 released

> Source: github-releases | Category: changelog | 2026-10-30T05:39:26Z

## vercel/next.js — v16.5.0-canary.32

### Core Changes

- Fix hangs and crashes for 204 responses from route handlers and deduped fetches: #100159
- fix(adapter): preserve revalidation for metadata prerenders: #100861
- next-custom-transforms: Optimize server-reference transform output: #100637
- Show dev overlay errors before the indicator state is known: #100629
- Update font data: #100863

### Misc Changes

- Improve common errors in turbo-trace-server: #100862
- docs: clarify use cache is unsupported in Proxy: #100842
- Revert "perf(turbopack): canonicalize async loader availability": #100898
- [test] Cover cache reuse after revalidation and failed writes: #100652
- Turbopack: use analyzed references for fragment facades: #100852
- [ci] Pin deploy test deployments to Node.js 22.x: #100879
- create-next-app: remove App Router prompt and always use App Router: #100850
- Turbopack: fix trailing-slash package root resolution: #100726

### Credits 

Huge thanks to @lukesandberg, @aurorascharff, @sokra, @unstubbable, @jimmyhmiller, @samselikoff, @eps1lon, @timneutkens, and @mischnic for helping!
