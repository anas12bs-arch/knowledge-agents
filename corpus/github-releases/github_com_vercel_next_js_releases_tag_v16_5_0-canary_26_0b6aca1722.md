---
title: "vercel/next.js v16.5.0-canary.26 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.26"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-10-24T23:39:24Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.26"
---

# vercel/next.js v16.5.0-canary.26 released

> Source: github-releases | Category: changelog | 2026-10-24T23:39:24Z

## vercel/next.js — v16.5.0-canary.26

### Core Changes

- Turbopack: bump trace format header to TRACEv1: #99781
- Pass staged fallback params directly to adapter renders: #100456
- Fix navigation from global-not-found to app routes: #100592
- End the cache-signal read when `encryptActionBoundArgs` hits the RDC: #100622
- Ignore flaky turbo-tasks-fs watcher tests in CI: #100627

### Misc Changes

- test: enable build-error suites in deploy mode: #100482
- test: enable deploy-excluded suites verified against deployments: #100484
- Turbopack: fix trace crates after concurrent trace format changes: #100656
- [cd] Document that Turbopack team can also approve releases: #100650
- Turbopack: delta-encode trace timestamps: #99809
- docs: add turbo_tasks development guidance for agents: #100581
- Fix `pnpm new-test` unit type generating no test file: #100641
- [test] Reproduce two cache-sharing bugs: #100510
- [test] Cover cache sharing after handler failures: #100519

### Credits 

Huge thanks to @jamiboym, @sokra, @eps1lon, @mischnic, @unstubbable, @kassens, @huozhi, and @digasic for helping!
