---
title: "vercel/next.js v16.5.0-canary.53 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.53"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-17T01:01:11Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.53"
---

# vercel/next.js v16.5.0-canary.53 released

> Source: github-releases | Category: changelog | 2026-11-17T01:01:11Z

## vercel/next.js — v16.5.0-canary.53

### Core Changes

- Lint against new `as any` casts and require a reason to disable it: #101255
- [no-unsafe-inline] Stop inlining the Turbopack chunk group bootstrap: #97574
- Omit required-server-files from the Node.js proxy adapter output: #101865
- Fix duplicate useServerInsertedHTML output in prerendered HTML with cacheComponents: #101147
- Add experimental native Go proxy support: #101464
- Point to environment variables in conflicting bundler error: #101826
- Tolerate dangling symlinks when detecting root convention files: #101827

### Misc Changes

- Fix lint and types CI on uncached @turbopack/nft native builds: #101896
- turbo-persistence: eagerly open SST files in the background: #101768
- Fix Rust build regression in bootstrap metadata embedding: #101888
- test: deflake native-route-go cold Go build tests: #101879
- turbo-tasks-backend: remove redundant backend field from ExecuteContext: #101849
- Escalate React internals coupling to the React maintainers: #101878
- Coalesce Turbopack server component HMR updates reliably: #101877
- Turbopack: don't read files excluded from output file traces: #101829
- turbo-tasks: support Vec in keyed cells: #101806
- docs: align agent PR description guidance with PR template: #101866
- turbo-tasks-backend: remove keyed dependency edges per task in batches: #101734
- docs: link cache APIs to distributed tag coordination: #101843
- docs: clarify view transitions during history navigation: #101863
- [test] Stabilize cached navigations consistency checks: #101861
- Turbopack: respect adjustFontFallback: false for next/font/google: #101397
- Turbopack: skip dangling symlinks when tracing dynamic paths: #101828

### Credits 

Huge thanks to @lukesandberg, @wbinnssmith, @sokra, @jamiboym, @eps1lon, @acdlite, @mischnic, @lubieowoce, @timneutkens, @aurorascharff, and @unstubbable for helping!
