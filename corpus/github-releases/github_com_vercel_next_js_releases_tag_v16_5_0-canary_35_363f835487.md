---
title: "vercel/next.js v16.5.0-canary.35 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.35"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-31T12:53:53Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.35"
---

# vercel/next.js v16.5.0-canary.35 released

> Source: github-releases | Category: changelog | 2026-10-31T12:53:53Z

## vercel/next.js — v16.5.0-canary.35

### Core Changes

- Handle cancellation errors during response clone cleanup: #100961
- Revert "Revert "Fix App Router locale path matching with Pages i18n"": #98726
- Fix prerendering of caught `'use cache'` errors: #100956

### Misc Changes

- docs: clarify blocking route response status: #100191
- docs: note per-route cost of boundary files, cached Route Handler checks, and per-instance rate limits: #100985
- docs: clarify unstable_cache cross-deployment persistence: #100983
- eval: allow static headings in prefetch-stage results: #100984
- turbopack: only add the Pages client entry when Pages routes exist: #100896
- turbopack: drop ASTs of tree-shaken modules: #100871
- [test] Cover cache reuse after failed handler writes: #100976
- Bundle Analyzer Agent Skill: Add Lodash deduplication eval: #99180
- Bundle Analyzer Agent Skill: Add server Markdown eval: #99179
- Bundle Analyzer Agent Skill: Add browser initial-load eval: #99178
- Turbopack: use memchr3 for source position scanning and count astral chars as two UTF-16 columns: #100919
- test: properly gate some cache-component tests: #100828
- next-napi-bindings: keep issue-backed client update errors recoverable: #100924
- turbopack: report chunk group consistency errors instead of panicking: #100923
- [test] Cover cache handler validation during concurrent reads: #100908

### Credits 

Huge thanks to @aurorascharff, @icyJoseph, @lukesandberg, @unstubbable, @wbinnssmith, @mischnic, @smaeda-ks, @sokra, and @timneutkens for helping!
