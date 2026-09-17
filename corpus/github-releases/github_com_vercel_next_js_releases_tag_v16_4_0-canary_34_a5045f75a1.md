---
title: "vercel/next.js v16.4.0-canary.34 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.4.0-canary.34"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-09-17T00:39:48Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.4.0-canary.34"
---

# vercel/next.js v16.4.0-canary.34 released

> Source: github-releases | Category: changelog | 2026-09-17T00:39:48Z

## vercel/next.js — v16.4.0-canary.34

### Misc Changes

- Store code generation AST paths in a shared trie: #98581
- Turbopack: Remove wasmer from lockfile by deleting dead feature option from our wasm crate: #98761
- Prefer using join over try_join when you don't want a vec: #98547
- Preserve committed app route response status during fallback: #98649
- docs: scope React cache() guidance to the render pass: #98741
- fix(next-custom-transforms): never place generated imports before directives: #98717
- Pin tasks during construction: #98688
- fix(use-cache): track root params read in "use cache" as vary params: #98674
- [test] Fix Webpack deployment failures in PostCSS tests: #98710
- Revert "Fix App Router locale path matching with Pages i18n": #98715

### Credits 

Huge thanks to @lukesandberg, @bgw, @alangenfeld, @icyJoseph, @mischnic, @jimmyhmiller, @aryabyte21, @unstubbable, and @timneutkens for helping!
