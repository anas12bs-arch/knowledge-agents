---
title: "sveltejs/svelte svelte@5.56.1 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.56.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-06-01T23:59:54Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.56.1"
---

# sveltejs/svelte svelte@5.56.1 released

> Source: github-releases | Category: changelog | 2026-06-01T23:59:54Z

## sveltejs/svelte — svelte@5.56.1

### Patch Changes

-   fix: error at compile time on duplicate snippet/declaration tag definitions ([#18351](https://github.com/sveltejs/svelte/pull/18351))

-   fix: parse declaration tag contents more robustly ([#18353](https://github.com/sveltejs/svelte/pull/18353))

-   fix: correctly transform references to earlier declarators in a declaration tag (e.g. `{let a = $state(0), b = $derived(a * 2)}`) ([#18348](https://github.com/sveltejs/svelte/pull/18348))

-   fix: avoid spurious `state_referenced_locally` warnings for `$derived` declarations in declaration tags ([#18348](https://github.com/sveltejs/svelte/pull/18348))

-   fix: tolerate whitespace before `let`/`const` in declaration tags ([#18348](https://github.com/sveltejs/svelte/pull/18348))

-   fix: prevent infinite loop when a tag's expression ends with a trailing `/` at the end of the input ([#18350](https://github.com/sveltejs/svelte/pull/18350))

-   fix: more robust parsing of declaration tags with regards to `type` ([#18330](https://github.com/sveltejs/svelte/pull/18330))

-   fix: preserve newlines in spread input values when the `type` attribute is applied after `value` ([#18345](https://github.com/sveltejs/svelte/pull/18345))

-   fix: update `SvelteURLSearchParams` when setting duplicate keys to the same joined value ([#18336](https://github.com/sveltejs/svelte/pull/18336))

-   fix: check references for blockers on server, too ([#18352](https://github.com/sveltejs/svelte/pull/18352))

