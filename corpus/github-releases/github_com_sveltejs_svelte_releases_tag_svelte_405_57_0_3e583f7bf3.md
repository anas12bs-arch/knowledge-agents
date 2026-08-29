---
title: "sveltejs/svelte svelte@5.57.0 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.57.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-08-29T03:48:23Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.57.0"
---

# sveltejs/svelte svelte@5.57.0 released

> Source: github-releases | Category: changelog | 2026-08-29T03:48:23Z

## sveltejs/svelte — svelte@5.57.0

### Minor Changes

-   feat: export `RenderOutput`, `SyncRenderOutput`, `Csp` and `Sha256Source` from `svelte/server` ([#18648](https://github.com/sveltejs/svelte/pull/18648))

-   feat: add `has` function to `createContext` ([#18472](https://github.com/sveltejs/svelte/pull/18472))

-   feat: support `defaultValue` on `<select>` ([#18591](https://github.com/sveltejs/svelte/pull/18591))

-   feat: add getOrInsert/getOrInsertComputed to SvelteMap ([#18728](https://github.com/sveltejs/svelte/pull/18728))

### Patch Changes

-   fix: block template store subscriptions on the promise that assigns the store ([#18582](https://github.com/sveltejs/svelte/pull/18582))

-   fix: route $derived teardown errors through invoke_error_boundary ([#18486](https://github.com/sveltejs/svelte/pull/18486))

-   fix: track SvelteDate snapshots in reactions ([#18700](https://github.com/sveltejs/svelte/pull/18700))

-   fix: remove `<svelte:head>` anchors on unmount ([#18697](https://github.com/sveltejs/svelte/pull/18697))

-   fix: warn on undeclared shorthand event handlers on `<svelte:window>`, `<svelte:document>` and `<svelte:body>` ([#18480](https://github.com/sveltejs/svelte/pull/18480))

-   perf: reuse the cached value in the `<option>`/`<select>` value guard ([#18713](https://github.com/sveltejs/svelte/pull/18713))

-   fix: prevent malformed AST output for `<select>` with static `value` attribute ([#18449](https://github.com/sveltejs/svelte/pull/18449))

-   fix: apply ownership mutation ignores to binding assignments ([#18718](https://github.com/sveltejs/svelte/pull/18718))

-   fix: prevent onoutroend from firing twice when compilerOptions.hmr is true ([#18655](https://github.com/sveltejs/svelte/pull/18655))

-   fix: preserve whitespace after inline elements when printing ([#18685](https://github.com/sveltejs/svelte/pull/18685))

-   perf: fold SSR block-open markers into the branch's first push ([#18712](https://github.com/sveltejs/svelte/pull/18712))

-   fix: run `onDestroy` callbacks when a server render throws ([#18585](https://github.com/sveltejs/svelte/pull/18585))

-   fix: report `derived_invalid_export` for `export let x = $derived(...)` in runes mode ([#18692](https://github.com/sveltejs/svelte/pull/18692))

-   fix: never apply class hash to elements inside `<svelte:head>` ([#18160](https://github.com/sveltejs/svelte/pull/18160))

-   fix: keep `defaultChecked` on hydrated radio inputs with spread attributes ([#18701](https://github.com/sveltejs/svelte/pull/18701))

-   fix: accept `onfocusin`/`onfocusout` in `a11y_mouse_events_have_key_events` ([#18689](https://github.com/sveltejs/svelte/pull/18689))

-   perf: O(n²)→O(n) Map lookups for legacy `$:` reactive statement ordering ([#18602](https://github.com/sveltejs/svelte/pull/18602))

-   fix: distinct memoizer on style/class directives ([#18466](https://github.com/sveltejs/svelte/pull/18466))

-   fix: measure nested transitions before applying their starting styles ([#18647](https://github.com/sveltejs/svelte/pull/18647))

-   fix: don't turn component instances stored in `$state` into state proxies ([#18646](https://github.com/sveltejs/svelte/pull/18646))

-   perf: emit `$.only_child` for elements with a single child ([#18717](https://github.com/sveltejs/svelte/pull/18717))

-   fix: omit `bind:focused` from SSR output (it has no HTML attribute) ([#18724](https://github.com/sveltejs/svelte/pull/18724))

-   fix: more robust rendering of Svelte custom element slots ([#18710](https://github.com/sveltejs/svelte/pull/18710))

-   perf: optimize simple object destructuring in `@const` tags ([#18390](https://github.com/sveltejs/svelte/pull/18390))

-   fix: properly apply static textarea value attribute during CSR ([#18727](https://github.com/sveltejs/svelte/pull/18727))

-   fix: end a restored reaction context at the end of its synchronous segment ([#18694](https://github.com/sveltejs/svelte/pull/18694))

-   fix: keep the dependencies of a reaction that throws, so deriveds i
