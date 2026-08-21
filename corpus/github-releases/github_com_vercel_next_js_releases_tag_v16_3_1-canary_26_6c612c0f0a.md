---
title: "vercel/next.js v16.3.1-canary.26 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.3.1-canary.26"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-08-20T23:57:29Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.3.1-canary.26"
---

# vercel/next.js v16.3.1-canary.26 released

> Source: github-releases | Category: changelog | 2026-08-20T23:57:29Z

## vercel/next.js — v16.3.1-canary.26

### Misc Changes

- docs: document deploymentId build ID override and Pages Router skew in 16.2: #97645
- Upgrade React from `eb8feb71-20260814` to `eafeac09-20260819`: #97636
- Turbopack: rename to use turbopack: no side effects: #94427
- refactor: move useDynamic{Route,Search}Params to reduce snapshot churn: #97360
- [PPF] unstable_navigation(): #96908
- [PPF] Scaffold unstable_navigation(): #97236
- docs: Explicit cache output description: #97548
- Improve Cache Components sync IO migration guidance: #97572
- [test] Use a non-native stub for the server externals list test: #97614
- Avoid GitHub API rate limits for create-next-app examples: #97612
- [test] Cover the prerender worker-thread backend with an addon we control: #97543
- [test] Convert the `prerender-native-module` suite to local fixture packages: #97542
- [test] Replace the `turbopack-reports` `sqlite3` dependency with a local addon fixture: #97541
- [test] Drop the dead `sqlite3` build approval from the `sharp-basic` suite: #97540
- [ci] Authenticate Turborepo remote caching with OIDC instead of a static PAT: #97590
- Remove HmrTarget: #97253
- Keep HMR instructions typed until serialization: #96569
- Serialize frozen collections by value only: #96686

### Credits 

Huge thanks to @icyJoseph, @mischnic, @lubieowoce, @aurorascharff, @eps1lon, @sokra, and @wbinnssmith for helping!
