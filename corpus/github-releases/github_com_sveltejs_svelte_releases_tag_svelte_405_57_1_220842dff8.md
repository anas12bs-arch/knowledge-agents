---
title: "sveltejs/svelte svelte@5.57.1 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.57.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-09-19T00:46:33Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.57.1"
---

# sveltejs/svelte svelte@5.57.1 released

> Source: github-releases | Category: changelog | 2026-09-19T00:46:33Z

## sveltejs/svelte — svelte@5.57.1

### Patch Changes

-   fix: cancel deferred event listeners during cleanup ([#18749](https://github.com/sveltejs/svelte/pull/18749))

-   fix: preserve global CSS in components without scopable elements ([#18793](https://github.com/sveltejs/svelte/pull/18793))

-   fix: reduce SSR render result garbage collection ([#18798](https://github.com/sveltejs/svelte/pull/18798))

-   fix: resolve the fallback of an each block in the enclosing scope ([#18803](https://github.com/sveltejs/svelte/pull/18803))

-   perf: speed up parser interactions with Acorn or avoid them where possible ([#18740](https://github.com/sveltejs/svelte/pull/18740))

-   fix: prevent effect tree of batches from interfering with each other ([#18508](https://github.com/sveltejs/svelte/pull/18508))

-   fix: serialize input default values during server rendering ([#18733](https://github.com/sveltejs/svelte/pull/18733))

-   fix: remove `WAS_MARKED` flag in favor of `Set` ([#18127](https://github.com/sveltejs/svelte/pull/18127))

-   fix: throw `set_context_after_init` when `setContext` is called after an `await` during SSR ([#18739](https://github.com/sveltejs/svelte/pull/18739))

-   fix: make Object.hasOwn reactive for state proxy ownership changes ([#18838](https://github.com/sveltejs/svelte/pull/18838))

-   fix: keep `$state.eager` when used as a variable initializer ([#18809](https://github.com/sveltejs/svelte/pull/18809))

-   perf: avoid regex matching in parser where possible ([#18736](https://github.com/sveltejs/svelte/pull/18736))

-   fix: in non-async mode, only push variable to current_sources when active_reaction is updating ([#18550](https://github.com/sveltejs/svelte/pull/18550))

-   fix: recognise `aria-braillelabel` and `aria-brailleroledescription` as known ARIA attributes ([#18765](https://github.com/sveltejs/svelte/pull/18765))

