---
title: "sveltejs/svelte svelte@5.56.0 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.56.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-05-30T14:31:15Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.56.0"
---

# sveltejs/svelte svelte@5.56.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:15Z

## sveltejs/svelte — svelte@5.56.0

### Minor Changes

-   feat: allow declarations in the template ([#18282](https://github.com/sveltejs/svelte/pull/18282))

### Patch Changes

-   perf: use `createElement` instead of `createElementNS` for HTML elements ([#18262](https://github.com/sveltejs/svelte/pull/18262))

-   perf: store `current_sources` as a `Set` for O(1) membership checks ([#18278](https://github.com/sveltejs/svelte/pull/18278))

-   perf: deduplicate identical hoisted templates within a component ([#18320](https://github.com/sveltejs/svelte/pull/18320))

-   perf: hoist `rest_props` exclude list as a module-scope `Set` ([#18252](https://github.com/sveltejs/svelte/pull/18252))

