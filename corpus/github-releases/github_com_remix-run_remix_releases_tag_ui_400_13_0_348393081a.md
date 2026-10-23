---
title: "remix-run/remix ui@0.13.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.13.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-10-23T20:00:32Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.13.0"
---

# remix-run/remix ui@0.13.0 released

> Source: github-releases | Category: changelog | 2026-10-23T20:00:32Z

## remix-run/remix — ui@0.13.0

### Minor Changes

- BREAKING CHANGE: Prop types for the previously removed styled `Accordion`, `Select`, and `Combobox` components have also been removed: `AccordionProps`, `AccordionItemProps`, `AccordionTriggerProps`, `AccordionContentProps`, `SelectProps`, `SelectOptionProps`, `ComboboxProps`, and `ComboboxOptionProps`. Accordion's unused `headingLevel` prop and corresponding context fields, along with the `AccordionHeadingLevel` type, have also been removed. ([#11986](https://github.com/remix-run/remix/pull/11986))

- BREAKING CHANGE: The toggle mixin is now exported as `toggle` instead of `control`. Since `toggle` consists of a single mixin, it can now be called directly as `toggle()` rather than grouped under `toggle.control()`. ([#11986](https://github.com/remix-run/remix/pull/11986))

  ```diff
  -import * as toggle from '@remix-run/ui/toggle'
  +import { toggle } from '@remix-run/ui/toggle'

  -<input mix={toggle.control({ defaultChecked: true })} />
  +<input mix={toggle({ defaultChecked: true })} />
  ```

  The options type has also been renamed from `ToggleControlOptions` to `ToggleOptions`:

  ```diff
  -import type { ToggleControlOptions } from '@remix-run/ui/toggle'
  +import type { ToggleOptions } from '@remix-run/ui/toggle'
  ```

- Check the user's current motion preference with `prefersReducedMotion()` from `@remix-run/ui/animation`. It returns `false` during server rendering or when `matchMedia` is unavailable, so it can be called safely from component render functions as well as browser event handlers. ([#11993](https://github.com/remix-run/remix/pull/11993))

  ```tsx
  import { animateLayout, prefersReducedMotion, spring } from '@remix-run/ui/animation'

  function Card() {
    return () => (
      <div mix={animateLayout(prefersReducedMotion() ? false : { ...spring('snappy') })}>Details</div>
    )
  }
  ```

### Patch Changes

- Server rendering skips setup and render for animation mixins, keyboard and outside-click helpers, typeahead behavior, and popover anchor and focus helpers. Mixins that provide initial attributes, styles, or ARIA props still run on the server. ([#12019](https://github.com/remix-run/remix/pull/12019))

- Bumped `@remix-run/*` dependencies:
  - [`component@1.1.0`](https://github.com/remix-run/remix/releases/tag/component@1.1.0)
