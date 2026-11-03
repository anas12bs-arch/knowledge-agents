---
title: "vercel/next.js v16.5.0-canary.38 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.38"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-03T09:23:21Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.38"
---

# vercel/next.js v16.5.0-canary.38 released

> Source: github-releases | Category: changelog | 2026-11-03T09:23:21Z

## vercel/next.js — v16.5.0-canary.38

### Core Changes

- Fix blocking revalidation for `fetch` and `unstable_cache`: #101077

### Misc Changes

- Turbopack: avoid invalidating per-module analysis when the encryption key changes: #100950
- turbo-tasks: add cancelable cell reads via Vc::lazy_reader(): #101008
- Turbopack: use simd-utf16-len for source position column counting: #100973
- Fix layout client chunk leakage across async server imports: #101040
- Pin Tailwind to 4.3.3 in create-next-app: #101061

### Credits 

Huge thanks to @unstubbable, @sokra, @lukesandberg, @mischnic, and @jamiboym for helping!
