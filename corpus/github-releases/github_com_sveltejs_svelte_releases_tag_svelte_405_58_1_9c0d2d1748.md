---
title: "sveltejs/svelte svelte@5.58.1 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.58.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-11-20T17:55:52Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.58.1"
---

# sveltejs/svelte svelte@5.58.1 released

> Source: github-releases | Category: changelog | 2026-11-20T17:55:52Z

## sveltejs/svelte — svelte@5.58.1

### Patch Changes

-   fix: don't throw when committing a fork whose changes were all superseded by other updates ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: apply the branch changes of blocks that re-run while effects are flushed when the batch with the effects' writes commits ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: keep values computed in a batch's view of the world local to that batch, and don't needlessly re-run deriveds while several batches are pending ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: don't skip sibling listeners added with `on()` when an earlier one calls `stopPropagation()` ([#19317](https://github.com/sveltejs/svelte/pull/19317))

-   fix: update `bind:files` when the form is reset ([#19298](https://github.com/sveltejs/svelte/pull/19298))

-   fix: restore teardown context when destroying effects after outros ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: print raw input text unchanged, respect whitespace rules ([#19292](https://github.com/sveltejs/svelte/pull/19292))

-   breaking: in experimental async mode, `getAbortSignal()` must be called before an `await` ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: remove related comments when effects are removed from server rune modules. ([#19289](https://github.com/sveltejs/svelte/pull/19289))

-   fix: commit the state that hydration ran with, so that updates while hydration is pending don't undo it ([#19347](https://github.com/sveltejs/svelte/pull/19347))

-   fix: don't run `$inspect` and `$state.eager` with the values of a fork before it is committed ([#19030](https://github.com/sveltejs/svelte/pull/19030))

-   fix: read a never-reassigned `$state.raw` declaration tag directly when it shadows reassigned state ([#19294](https://github.com/sveltejs/svelte/pull/19294))

-   fix: revert state changes in effect teardowns based on the currently committing batch ([#19030](https://github.com/sveltejs/svelte/pull/19030))

