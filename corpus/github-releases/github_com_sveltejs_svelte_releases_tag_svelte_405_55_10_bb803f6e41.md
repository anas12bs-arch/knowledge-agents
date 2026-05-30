---
title: "sveltejs/svelte svelte@5.55.10 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.55.10"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-05-30T14:31:15Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.55.10"
---

# sveltejs/svelte svelte@5.55.10 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:15Z

## sveltejs/svelte — svelte@5.55.10

### Patch Changes

-   fix: unlink errored and otherwise finished batch ([#18264](https://github.com/sveltejs/svelte/pull/18264))

-   perf: walk composedPath() directly in delegated event propagation ([#18268](https://github.com/sveltejs/svelte/pull/18268))

-   fix: transfer effects when merging batches ([#18254](https://github.com/sveltejs/svelte/pull/18254))

-   fix: allow `$derived(await ...)` in disconnected effect roots ([#18273](https://github.com/sveltejs/svelte/pull/18273))

-   fix: remove temporary raw-text hydration markers ([#18269](https://github.com/sveltejs/svelte/pull/18269))

-   fix: propagate async `@const` blockers through closure references so template expressions like `{(() => host)()}` correctly wait for the awaited value ([#18309](https://github.com/sveltejs/svelte/pull/18309))

-   fix: properly unlink batches ([#18298](https://github.com/sveltejs/svelte/pull/18298))

-   fix: settle discarded batch ([#18290](https://github.com/sveltejs/svelte/pull/18290))

-   fix: declare `let:` directives before `{@const}` declarations on slotted elements ([#18271](https://github.com/sveltejs/svelte/pull/18271))

-   fix: resume outro-ed branches if they were kept around ([#18291](https://github.com/sveltejs/svelte/pull/18291))

-   fix: avoid waterfall-warning when async resolves to same value ([#18297](https://github.com/sveltejs/svelte/pull/18297))

-   fix: correctly coordinate component-level effects inside async blocks ([#18260](https://github.com/sveltejs/svelte/pull/18260))

-   fix: make unnecessary commit work less likely ([#18263](https://github.com/sveltejs/svelte/pull/18263))

-   chore: add tag name to `a11y_click_events_have_key_events` warning ([#18272](https://github.com/sveltejs/svelte/pull/18272))

-   fix: catch rejected promises while merging/committing ([#18266](https://github.com/sveltejs/svelte/pull/18266))

