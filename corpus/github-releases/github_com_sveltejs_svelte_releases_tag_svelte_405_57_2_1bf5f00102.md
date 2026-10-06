---
title: "sveltejs/svelte svelte@5.57.2 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.57.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-10-06T14:47:32Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.57.2"
---

# sveltejs/svelte svelte@5.57.2 released

> Source: github-releases | Category: changelog | 2026-10-06T14:47:32Z

## sveltejs/svelte — svelte@5.57.2

### Patch Changes

-   fix: don't create async deriveds for a component destroyed while waiting for its top-level `await` ([#18931](https://github.com/sveltejs/svelte/pull/18931))

-   fix: prevent untracked derived reads from retaining disconnected dependencies ([#18829](https://github.com/sveltejs/svelte/pull/18829))

-   fix: error if `{:else}` is followed by another `{:else}` or `{:else if ...}` ([#18900](https://github.com/sveltejs/svelte/pull/18900))

-   fix: avoid tracking SvelteURLSearchParams during URL updates ([#18791](https://github.com/sveltejs/svelte/pull/18791))

-   fix: restore hydration state when custom element attribute updates throw ([#18467](https://github.com/sveltejs/svelte/pull/18467))

-   fix: attach event handlers that are assigned after a top-level `await` in production ([#18933](https://github.com/sveltejs/svelte/pull/18933))

-   fix: flush anything pending before invoking flushSync callback function ([#18878](https://github.com/sveltejs/svelte/pull/18878))

-   fix: preserve location information for `await` wrappers ([#18859](https://github.com/sveltejs/svelte/pull/18859))

-   fix: keep a reactive assignment with no dependencies when `migrate` cannot turn it into a declaration ([#18817](https://github.com/sveltejs/svelte/pull/18817))

-   fix: don't hang `migrate` on a declaration that shares a line with its script tag ([#18816](https://github.com/sveltejs/svelte/pull/18816))

-   fix: prevent duplicate subscriptions when reconnecting deriveds ([#18899](https://github.com/sveltejs/svelte/pull/18899))

-   fix: recover when an unexpected node replaces a nested boundary comment during hydration ([#18925](https://github.com/sveltejs/svelte/pull/18925))

-   fix: print `{#await}` blocks that only have a pending branch ([#18908](https://github.com/sveltejs/svelte/pull/18908))

-   fix: don't warn about a redundant `link` role on `<area>` elements without an `href` ([#18872](https://github.com/sveltejs/svelte/pull/18872))

-   fix: don't throw `state_unsafe_mutation` when the focused element is removed while `bind:activeElement` is used ([#18921](https://github.com/sveltejs/svelte/pull/18921))

-   fix: don't overwrite an unchanged spread `value`, preserving incomplete number input ([#18864](https://github.com/sveltejs/svelte/pull/18864))

-   fix: read batch-local array on each-block commit ([#18879](https://github.com/sveltejs/svelte/pull/18879))

-   fix: error at compile time when a declaration in a snippet redeclares one of its parameters ([#18842](https://github.com/sveltejs/svelte/pull/18842))

-   fix: error when using `let:` directives on a component with a `children` snippet ([#18873](https://github.com/sveltejs/svelte/pull/18873))

-   fix: ignore stale boundary reset callbacks ([#18886](https://github.com/sveltejs/svelte/pull/18886))

-   fix: handle deferred transitions aborted before initialization ([#18776](https://github.com/sveltejs/svelte/pull/18776))

-   fix: prevent hydration mismatch recovery from being intercepted by error boundaries ([#18841](https://github.com/sveltejs/svelte/pull/18841))

-   fix: preserve dynamic element connections during hydration ([#18855](https://github.com/sveltejs/svelte/pull/18855))

