---
title: "vercel/next.js v16.5.0-canary.62 released"
url: "https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.62"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "next.js"]
date: "2026-11-24T04:27:22Z"
metadata:
  repo: "vercel/next.js"
  version: "v16.5.0-canary.62"
---

# vercel/next.js v16.5.0-canary.62 released

> Source: github-releases | Category: changelog | 2026-11-24T04:27:22Z

## vercel/next.js — v16.5.0-canary.62

### Core Changes

- switchyard: name gone workers by token, and test the worker events and route table: #102168
- switchyard: no guessed Content-Type after 103 Early Hints: #102034
- switchyard: run Go code on at most 4 threads: #101901
- Link Node crypto prerender errors to the crypto error page: #102252
- Fix fast setImmediate running before microtasks queued by nextTick: #102237
- Turbopack: diff server HMR pulls against a Rust-owned loaded-module set: #102016
- Fix webpack runtime CSS ordering before first app router commit: #102027
- Document Next.js DevTools and improve badge controls: #102015
- Restrict proxy.go to App Router applications: #102011

### Misc Changes

- Turbopack: resolve globalThis.process and global.process in the analyzer: #102240
- docs: clarify placeholder params for empty data sources: #102149
- docs: distinguish prefetch = 'partial' from the partialPrefetching flag: #102234
- fix(next-napi-bindings): enable LSE atomics on Linux arm64: #102243
- turbopack-core: return chunk group kinds instead of cloned chunk groups from ChunkGroupInfo lookups: #102162
- docs: document Tailwind Turbopack loader setup in CSS guide: #102235
- docs: remove non-existent renderType from onRequestError example: #74448
- docs: clarify use server export rules: #102232
- Fix nondeterministic usages of turbo-tasks `read_dir()`: #102229
- chore: Add ast-grep rule to require read_dir determinism comments: #102227
- docs: Add DETERMINISM comments to all turbo-tasks-fs read_dir calls : #102226
- test: avoid idle-callback starvation in css-client-nav: #102132
- test: wait for use-cache recovery reload: #102224
- docs(agents): add rust-turbopack skill for Rust tests and benchmarks: #102179
- [ci] Fix staging Proxy routing for deploy tests: #102225
- docs(agents): add rebase-pr skill for rebasing and restacking PRs: #102178
- docs(agents): add CI reading guide to pr-status-triage: #102176
- turbo-tasks: fix reversed TaskInput::is_resolved documentation: #102184
- turbopack: use boxed slices for long-lived list task inputs: #102134
- docs(agents): add run-tests skill for test bootstrap and flakes: #102177
- docs: fix mismatched filenames, languages and invalid JS in code examples: #100201

### Credits 

Huge thanks to @jamiboym, @aurorascharff, @mischnic, @icyJoseph, @ali-vercel, @lubieowoce, @lukesandberg, @wbinnssmith, @sokra, @hyungjikim, @unstubbable, @timneutkens, and @deveshasawa28 for helping!
