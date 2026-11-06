---
title: "tailwindlabs/tailwindcss v4.3.5 released"
url: "https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.5"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "tailwindcss"]
date: "2026-11-06T22:04:56Z"
metadata:
  repo: "tailwindlabs/tailwindcss"
  version: "v4.3.5"
---

# tailwindlabs/tailwindcss v4.3.5 released

> Source: github-releases | Category: changelog | 2026-11-06T22:04:56Z

## tailwindlabs/tailwindcss — v4.3.5

### Fixed

- Canonicalization: improve performance in projects with many functional variant values (e.g. a `matchVariant` plugin with thousands of values) ([#20663](https://github.com/tailwindlabs/tailwindcss/pull/20663))
- Don't crash or create a fallback with the wrong color for a `color-mix(…)` without a color interpolation method (e.g. `color-mix(var(--color-red-500))` or `color-mix(currentcolor 50%, transparent)`) ([#20658](https://github.com/tailwindlabs/tailwindcss/pull/20658), [#20666](https://github.com/tailwindlabs/tailwindcss/pull/20666))
- Ensure `@tailwindcss/oxide-wasm32-wasi` loads instead of hanging forever (e.g. with `NAPI_RS_FORCE_WASI=error` or in WebContainers) ([#20667](https://github.com/tailwindlabs/tailwindcss/pull/20667))
- Remove `as: '*.css'` from the `@tailwindcss/turbopack` setup in its README, because it breaks CSS modules ([#20660](https://github.com/tailwindlabs/tailwindcss/pull/20660))
- Ignore `<!--` and `-->` between top-level rules in CSS instead of throwing or swallowing the next rule (e.g. `a { color: red } --> b { color: blue }`) ([#20665](https://github.com/tailwindlabs/tailwindcss/pull/20665))
- Ensure `@tailwindcss/oxide-wasm32-wasi` detects changed and new source files after the first scan (e.g. in WebContainers) ([#20487](https://github.com/tailwindlabs/tailwindcss/pull/20487))
- Prevent type errors with `skipLibCheck: false` caused by imports of unshipped modules in the `@tailwindcss/node` type declarations ([#20632](https://github.com/tailwindlabs/tailwindcss/pull/20632))
