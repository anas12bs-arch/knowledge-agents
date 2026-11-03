---
title: "tailwindlabs/tailwindcss v4.3.4 released"
url: "https://github.com/tailwindlabs/tailwindcss/releases/tag/v4.3.4"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "tailwindcss"]
date: "2026-11-03T02:05:56Z"
metadata:
  repo: "tailwindlabs/tailwindcss"
  version: "v4.3.4"
---

# tailwindlabs/tailwindcss v4.3.4 released

> Source: github-releases | Category: changelog | 2026-11-03T02:05:56Z

## tailwindlabs/tailwindcss — v4.3.4

### Added

- Add `@tailwindcss/turbopack`, a Turbopack loader for using Tailwind CSS with Next.js ([#20367](https://github.com/tailwindlabs/tailwindcss/pull/20367))

### Fixed

- Ensure watch mode detects changes to symlinked `@source` files whose real paths aren't otherwise scanned ([#20356](https://github.com/tailwindlabs/tailwindcss/pull/20356))
- Ensure variants using `@scope` wrap generated utilities instead of nesting inside them ([#20369](https://github.com/tailwindlabs/tailwindcss/pull/20369))
- Ensure nested `@scope` rules preserve their scoping semantics when flattened ([#20369](https://github.com/tailwindlabs/tailwindcss/pull/20369))
- Preserve declarations directly inside `@scope` by wrapping them in `:where(:scope)` ([#20369](https://github.com/tailwindlabs/tailwindcss/pull/20369))
- Ensure generated utilities include a space in empty `var()` fallbacks (e.g. `var(--tw-blur,)` → `var(--tw-blur, )`) ([#20373](https://github.com/tailwindlabs/tailwindcss/pull/20373))
- Canonicalization: convert arbitrary breakpoint and container query variants to named equivalents (e.g. `max-[64rem]:flex` → `max-lg:flex`) ([#20380](https://github.com/tailwindlabs/tailwindcss/pull/20380))
- Prevent `@tailwindcss/vite` from crashing on every edit under Vite's experimental `bundledDev` mode ([#20379](https://github.com/tailwindlabs/tailwindcss/pull/20379))
- Ensure `@tailwindcss/oxide` falls back to WASM on platforms without native bindings ([#20383](https://github.com/tailwindlabs/tailwindcss/pull/20383))
- Extract class candidates from Ruby `%w` and `%W` literals using angle brackets or custom delimiters (e.g. `%w<flex>`, `%w|flex|`), including in Slim and Haml templates ([#20387](https://github.com/tailwindlabs/tailwindcss/pull/20387))
- Preserve whitespace in `--default(…)` values in functional `@utility` definitions (e.g. `--default(box alphabetic)` no longer becomes `boxalphabetic`) ([#20392](https://github.com/tailwindlabs/tailwindcss/pull/20392))
- Ensure automatic source detection respects negation-based `.gitignore` files (e.g. `/*` followed by `!/…` patterns) ([#20397](https://github.com/tailwindlabs/tailwindcss/pull/20397))
- Ensure root `theme('…')` namespace lookups in JavaScript plugins and config files return the full namespace object instead of the value of its `DEFAULT` key ([#20399](https://github.com/tailwindlabs/tailwindcss/pull/20399))
- Skip ignored directories when generating watch globs instead of walking their contents on every rebuild ([#20408](https://github.com/tailwindlabs/tailwindcss/pull/20408))
- Drop invalid UTF-8 candidates during class detection ([#20389](https://github.com/tailwindlabs/tailwindcss/pull/20389))
- Prevent `@tailwindcss/vite` from forcing full-page reloads for scanned files that Vite does not handle as modules (e.g. `.php` files) ([#20414](https://github.com/tailwindlabs/tailwindcss/pull/20414))
- Canonicalization: don't merge utilities that reference different theme variables set to CSS-wide keywords like `unset` ([#20417](https://github.com/tailwindlabs/tailwindcss/pull/20417))
- Don't generate utilities when a modifier is used that would otherwise be silently ignored (e.g. `rounded-sm/[5]`, `shadow-sm/foo`, `stroke-2/50`) ([#20419](https://github.com/tailwindlabs/tailwindcss/pull/20419))
- Preserve `and`, `or`, and `not` inside selectors in `supports-[…]` variants (e.g. `supports-[selector(a:not(.foo))]:flex`) ([#20420](https://github.com/tailwindlabs/tailwindcss/pull/20420))
- Don't warn about Angular's `::ng-deep` and `:host-context()` when optimizing CSS ([#20434](https://github.com/tailwindlabs/tailwindcss/pull/20434))
- Don't generate CSS for candidates containing an empty additional modifier (e.g. `bg-red-500/50/` and `group-hover/foo//bar:flex`) ([#20466](https://github.com/tailwindlabs/tailwindcss/pull/20466))
- Ensure `min-*`, `max-*`, and container query variants with decimal values are sorted numerically (e.g. `min-[40.25rem]` before `min-[40.5rem]`) ([#20512](https://githu
