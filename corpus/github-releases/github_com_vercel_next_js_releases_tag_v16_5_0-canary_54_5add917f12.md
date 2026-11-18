---
title: "vercel/next.js v16.5.0-canary.54 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.54"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-18T00:08:12Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.54"
---

# vercel/next.js v16.5.0-canary.54 released

> Source: github-releases | Category: changelog | 2026-11-18T00:08:12Z

## vercel/next.js — v16.5.0-canary.54

### Core Changes

- Reject the experimental testing API opt-in without Cache Components: #101952
- Preserve CSP nonces on static fallback bootstrap scripts: #101953
- Turbopack: separate file tracing from NFT manifest emission, add dev flag: #101941
- Clarify the agent handoff for worktree upgrades: #101939
- refactor: Derive whether PPR is enabled from cacheComponents config in base-server: #101936
- refactor: Derive whether PPR is enabled from cacheComponents config: #101929
- perf(build): resolve adapter app page entries via a lookup map: #101880
- turbo-tasks-backend: stop checking keyed dependencies once a dependent is stale: #101736
- Run the dev Cache Components validation in an OTel trace of its own: #100690
- turbo-tasks-backend: delay collectible propagation until tasks are clean: #101748
- Write short client reference manifest chunk lists as array literals: #101846
- Fix canary lint: remove `as any` casts in load-manifest.test.ts (@next/internal/no-as-any): #101910
- Evaluate JS manifests with compileFunction instead of a new context: #101787

### Misc Changes

- turbopack-tracing: sync new vercel/nft unit tests: #101973
- [test] Cover HTTP methods on prerendered App Pages: #101945
- docs: clarify instant layout opt-out scope: #101944
- docs: clarify Vitest Link navigation testing limits: #101943
- docs: document instant testing in the Playwright guide: #101924
- Wait for hydration in back-before-hydration third-party write test: #101940
- review: add [team-members] section to review/OWNERS: #101883
- fix(routing): prefer exact pathnames after rewrites: #101934
- chore: don't build tracing-napi by default: #101923
- Bump to swc 84.1.1: #101860
- Turbopack: keep mangled compact re-exports in import order: #101920
- docs: clarify Vitest Node.js compatibility: #101908
- docs: fix import/export mismatches in API reference snippets: #101921
- docs: fix BlogNavLink imports in active link examples: #101919
- Turbopack: list ESM namespace keys in code unit order for the general export registration: #101749
- docs: clarify native history URL hook update timing: #101907
- turbopack: narrow chunk group reads on warm rebuilds: #101782
- turbo-tasks-fs: skip compare-before-write in directories created by the filesystem: #101813
- Turbopack: opt-in atomic file writes, used for client reference manifests: #101786
- Turbopack: keep metric-adjusted fallback face for next/font/google when `fallback` is set: #100305

### Credits 

Huge thanks to @mischnic, @unstubbable, @aurorascharff, @sokra, @lubieowoce, @jimmyhmiller, @icyJoseph, @0badran, @lukesandberg, and @sleitor for helping!
