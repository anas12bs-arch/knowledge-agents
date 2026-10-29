---
title: "vercel/next.js v16.5.0-canary.30 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.30"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-29T02:25:55Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.30"
---

# vercel/next.js v16.5.0-canary.30 released

> Source: github-releases | Category: changelog | 2026-10-29T02:25:55Z

## vercel/next.js — v16.5.0-canary.30

### Core Changes

- Ignore expected upgrade nudges in Agent Feedback: #100840
- Add model metadata to Agent Feedback: #100806
- Use fast-jwt instead of jsonwebtoken: #100818
- Update font data: #100813
- Turbopack: wait for trace file changes after format errors: #99847
- Add a CLI for reviewing agent feedback: #100739

### Misc Changes

- Add criteria for Vercel Agent code review: #100846
- Add experimental.hydrationChangeEvent flag: #99610
- Turbopack: Move reference to bincode's virtue dependency into a vercel-labs owned fork repository: #100847
- bench: fix nested-deps-app-router-many-pages build harness: #100820
- Fix `export const foo = function bar(){}` in server reference transform: #100830
- turbo-persistence: use partition_point for batch lookup bounds: #100821
- ci: don't run non-adapter + cache components deploy tests in PRs: #100824
- Enforce strict rustdoc (incl. private items) across the Rust workspace: #100768
- Drain the maintainer auto-close queue in one run: #100733
- test: fix native addon compilation on Node.js 26: #100819
- turbo-persistence: parallelize large batch_get reads: #100620
- Turbopack: ignore fully dynamic alternatives when tracing file paths: #100651
- docs: scope whole-route dynamic rendering claim for cookies to the previous model: #100811
- docs: note Suspense requirement for connection() with Cache Components: #100810
- docs: forward allow-listed headers and catch fetch errors in BFF proxy example: #100808

### Credits 

Huge thanks to @acdlite, @bgw, @aurorascharff, @sokra, @mischnic, @devjiwonchoi, @lukesandberg, and @icyJoseph for helping!
