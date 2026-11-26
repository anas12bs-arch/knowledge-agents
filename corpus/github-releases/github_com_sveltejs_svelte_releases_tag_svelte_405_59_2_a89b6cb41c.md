---
title: "sveltejs/svelte svelte@5.59.2 released"
url: "https://github.com/sveltejs/svelte/releases/tag/svelte%405.59.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "svelte"]
date: "2026-11-26T00:14:38Z"
metadata:
  repo: "sveltejs/svelte"
  version: "svelte@5.59.2"
---

# sveltejs/svelte svelte@5.59.2 released

> Source: github-releases | Category: changelog | 2026-11-26T00:14:38Z

## sveltejs/svelte — svelte@5.59.2

### Patch Changes

-   fix: catch errors in deferred await block branches with error boundaries ([#19028](https://github.com/sveltejs/svelte/pull/19028))

-   chore: bump devalue to 6.0.4 ([#18857](https://github.com/sveltejs/svelte/pull/18857))

-   fix: don't keep a stale value for a derived that disconnects while another batch is pending ([#19426](https://github.com/sveltejs/svelte/pull/19426))

-   fix: treat `<!--` and `-->` in `<style>` as CSS tokens, not as a comment ([#19370](https://github.com/sveltejs/svelte/pull/19370))

-   fix: exclude comments after the initializer from the `{@const}` declarator range ([#19394](https://github.com/sveltejs/svelte/pull/19394))

-   fix: object props on a custom element are set as properties even after spreading onto an unregistered element with the same tag ([#19441](https://github.com/sveltejs/svelte/pull/19441))

-   fix: avoid naming a component after a reserved `$`-prefixed binding when its filename starts with `$` ([#19414](https://github.com/sveltejs/svelte/pull/19414))

-   perf: process successive batches iteratively instead of recursively, avoiding slow stack capture in dev ([#19391](https://github.com/sveltejs/svelte/pull/19391))

-   fix: correctly apply styles to elements with `duration: 0` transitions ([#19444](https://github.com/sveltejs/svelte/pull/19444))

-   fix: hint at missing `lang="ts"` when TypeScript syntax fails to parse ([#19428](https://github.com/sveltejs/svelte/pull/19428))

-   fix: use comments instead of text for custom renderers ([#19376](https://github.com/sveltejs/svelte/pull/19376))

-   fix: handle `?.` in directive names like `use:a?.b` ([#19404](https://github.com/sveltejs/svelte/pull/19404))

-   fix: keep the comments around a parenthesized template expression in its `leadingComments` and `trailingComments` ([#19389](https://github.com/sveltejs/svelte/pull/19389))

-   fix: avoid quadratic work when flushing effects that write state ([#19395](https://github.com/sveltejs/svelte/pull/19395))

-   fix: escape comment terminators in all commented-out CSS ([#19380](https://github.com/sveltejs/svelte/pull/19380))

-   fix: handle attribute name casing consistently between server and client ([`9672188`](https://github.com/sveltejs/svelte/commit/967218863c0565f7677cb86c55efad1a20a732da))

-   fix: respect length bound when destructuring array-like values ([`dba8d14`](https://github.com/sveltejs/svelte/commit/dba8d14bfa2b26e0fdbb03b31f967e37ac185f59))

-   fix: leave reactive classes and `$state` proxies unchanged when a write is refused with `state_unsafe_mutation` ([#19405](https://github.com/sveltejs/svelte/pull/19405))

-   fix: remove `{#each}` items when outros of zero and non-zero duration run together ([#19042](https://github.com/sveltejs/svelte/pull/19042))

-   fix: prevent `hydratable` promise placeholders from colliding with serialized strings ([#19406](https://github.com/sveltejs/svelte/pull/19406))

-   fix: give class static blocks their own scope ([#19335](https://github.com/sveltejs/svelte/pull/19335))

-   fix: make dev element metadata non-enumerable to avoid traversing component graphs during structural comparisons ([#19316](https://github.com/sveltejs/svelte/pull/19316))

-   fix: escape double quotes in attribute values when printing ([#19365](https://github.com/sveltejs/svelte/pull/19365))

-   fix: ignore commas in comments when removing unused CSS selectors ([#19382](https://github.com/sveltejs/svelte/pull/19382))

