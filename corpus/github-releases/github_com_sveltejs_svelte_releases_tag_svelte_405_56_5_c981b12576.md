---
title: "sveltejs/svelte svelte@5.56.5 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.56.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-07-14T12:13:25Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.56.5"
---

# sveltejs/svelte svelte@5.56.5 released

> Source: github-releases | Category: changelog | 2026-07-14T12:13:25Z

## sveltejs/svelte — svelte@5.56.5

### Patch Changes

-   chore: drop dead code that make TSGO fail ([#18496](https://github.com/sveltejs/svelte/pull/18496))

-   fix: don't (re)connect deriveds when read inside branch/root effects ([#18527](https://github.com/sveltejs/svelte/pull/18527))

-   fix: skip unnecessary derived effect in earlier batch ([#18525](https://github.com/sveltejs/svelte/pull/18525))

-   fix: avoid declaration tag warning in event handlers ([#18500](https://github.com/sveltejs/svelte/pull/18500))

-   fix: abort deriveds own AbortSignal when it disconnects ([#18400](https://github.com/sveltejs/svelte/pull/18400))

-   fix: ensure `$state.eager()` is correctly transormed for SSR output ([#18530](https://github.com/sveltejs/svelte/pull/18530))

-   fix: correctly transform declaration tags during SSR ([#18492](https://github.com/sveltejs/svelte/pull/18492))

-   fix: transform computed keys in keyed `{#each}` destructuring patterns ([#18521](https://github.com/sveltejs/svelte/pull/18521))

-   fix: chain preprocessor sourcemaps with an empty `sources[0]` instead of dropping them ([#18518](https://github.com/sveltejs/svelte/pull/18518))

-   fix: clear previous_task reference after abort in Tween to prevent memory leak on interrupted tweens ([#18541](https://github.com/sveltejs/svelte/pull/18541))

-   fix: don't treat declaration tags as parts inside each blocks ([#18507](https://github.com/sveltejs/svelte/pull/18507))

