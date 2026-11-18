---
title: "sveltejs/svelte svelte@5.58.0 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.58.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-11-18T07:11:40Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.58.0"
---

# sveltejs/svelte svelte@5.58.0 released

> Source: github-releases | Category: changelog | 2026-11-18T07:11:40Z

## sveltejs/svelte — svelte@5.58.0

### Minor Changes

-   feat: include `snippetName` in `render` entries of the dev `__svelte_meta` stack ([#19283](https://github.com/sveltejs/svelte/pull/19283))

-   feat: include the `component` instance an element was rendered in for Svelte devtools to track ([#19286](https://github.com/sveltejs/svelte/pull/19286))

### Patch Changes

-   perf: let the garbage collector free each component's AST after it is compiled ([#19241](https://github.com/sveltejs/svelte/pull/19241))

-   fix: render the same `<title>` on the server as on the client and ignore titles inside failed boundaries ([#19176](https://github.com/sveltejs/svelte/pull/19176))

-   fix: allow `autocorrect` on all elements ([#19105](https://github.com/sveltejs/svelte/pull/19105))

-   fix: parse snippet type parameters containing arrow function types ([#19141](https://github.com/sveltejs/svelte/pull/19141))

-   fix: keep directive values that match the directive name in `print` ([#19229](https://github.com/sveltejs/svelte/pull/19229))

-   fix: correctly assign dev element locations after components during hydration ([#19287](https://github.com/sveltejs/svelte/pull/19287))

-   perf: don't compare the whole template on every expression when a source is parsed again ([#19215](https://github.com/sveltejs/svelte/pull/19215))

-   docs: avoid binding to read-only current values in Spring and Tween examples ([#19226](https://github.com/sveltejs/svelte/pull/19226))

-   fix: keep positions right after optional properties in template type annotations ([#19217](https://github.com/sveltejs/svelte/pull/19217))

-   perf: speed up server rendering of pages with many or deeply nested components ([#19177](https://github.com/sveltejs/svelte/pull/19177))

-   fix: remove all of the server-rendered content when hydrating a different branch that contains a failed boundary ([#19166](https://github.com/sveltejs/svelte/pull/19166))

-   fix: preserve effect tree order across batch traversal passes ([#19132](https://github.com/sveltejs/svelte/pull/19132))

-   fix: reset dev update counters for sources written during batch traversal ([#19092](https://github.com/sveltejs/svelte/pull/19092))

-   chore: bump esrap ([#19290](https://github.com/sveltejs/svelte/pull/19290))

-   fix: don't leak reactive context past nested awaits in production ([#19134](https://github.com/sveltejs/svelte/pull/19134))

