---
title: "remix-run/remix ui@0.4.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.4.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-07-01T19:19:31Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.4.0"
---

# remix-run/remix ui@0.4.0 released

> Source: github-releases | Category: changelog | 2026-07-01T19:19:31Z

## remix-run/remix — ui@0.4.0

### Minor Changes

- BREAKING CHANGE: Replaced the styled button component API with a default `button()` mixin exported from `@remix-run/ui/button`.

  Use the mixin directly on button-like hosts instead of importing `Button` or composing the previous slot style exports:

  ```tsx
  import button from '@remix-run/ui/button'

  <button mix={button()}>Edit order</button>
  <button mix={button({ size: 'lg', tone: 'primary' })}>Add product</button>
  <button mix={button({ tone: 'ghost' })}>Cancel</button>
  ```

- Added a default `checkbox()` mixin exported from `@remix-run/ui/checkbox` for styling native checkbox inputs.

  Checkbox controls use the same keyboard focus shadow as `input()` controls and support an optional visual `state` for app-owned checked, unchecked, and mixed states.

  ```tsx
  import checkbox from '@remix-run/ui/checkbox'

  <input defaultChecked mix={checkbox()} name="permissions" value="read" />
  <input indeterminate mix={checkbox({ size: 'lg', state: 'mixed' })} />
  ```

- Added top-level component exports for headless primitives and styled components.

  Primitive-only modules import directly from their component path, while modules with styled wrappers expose lower-level behavior under `/primitives`:

  ```tsx
  import button from '@remix-run/ui/button'
  import * as select from '@remix-run/ui/select/primitives'
  ```

  BREAKING CHANGE: Removed the `@remix-run/ui/components/*` subpath exports. Import
  component modules from `@remix-run/ui/*` instead.

  BREAKING CHANGE: Removed root helper exports that were only intended for first-party
  component internals:

  - `flashAttribute`
  - `hiddenTypeahead`
  - `matchNextItemBySearchText`
  - `onKeyDown`
  - `SearchValue`
  - `wait`
  - `waitForCssTransition`

  Removed the `@remix-run/ui/scroll-lock` subpath export. Scroll locking is now an
  internal popover implementation detail.

- Added a default `input()` mixin exported from `@remix-run/ui/input` for standalone native inputs, plus `input.root()` and `input.field()` for icon-capable input layouts.

  ```tsx
  import input from '@remix-run/ui/input'

  <input mix={input()} placeholder="Limit" />

  <div mix={input.root()}>
    <SearchIcon />
    <input mix={input.field()} placeholder="Search and filter products" />
  </div>
  ```

- Added a default `radio()` mixin exported from `@remix-run/ui/radio` for styling native radio inputs.

  Radio controls use the same keyboard focus shadow as `input()` controls.

  ```tsx
  import radio from '@remix-run/ui/radio'

  <input defaultChecked mix={radio()} name="shipping-speed" value="standard" />
  <input mix={radio({ size: 'lg' })} name="shipping-speed" value="express" />
  ```

- Added styled component subpath exports under `@remix-run/ui/*` for accordion, breadcrumbs, checkbox, combobox, menu, and select. These are the package-owned implementations behind the `remix/ui/*` entrypoints.

- Added `tabs` and `tabs/primitives` exports for controlled and uncontrolled tab groups with toggle-slider active tabs, button-sized tab text, active-tab panels, keyboard activation, and bubbling tab change events.

  ```tsx
  import { Tabs, TabList, Tab, TabPanel } from '@remix-run/ui/tabs'
  ;<Tabs defaultActiveTab="overview">
    <TabList aria-label="Project sections">
      <Tab name="overview">Overview</Tab>
      <Tab name="activity">Activity</Tab>
    </TabList>
    <TabPanel name="overview">Project summary.</TabPanel>
    <TabPanel name="activity">Recent changes.</TabPanel>
  </Tabs>
  ```

- Added `toggle()` styles and `toggle/primitives` for boolean switch controls with medium and large sizes.

  ```tsx
  import toggle from '@remix-run/ui/toggle'
  import * as togglePrimitive from '@remix-run/ui/toggle/primitives'

  <input defaultChecked mix={toggle({ size: 'lg' })} />
  <button aria-label="Notifications" mix={[...toggle(), togglePrimitive.control({ defaultChecked: true })]} />
  ```

### Patch Changes

- Forward the frame's name as the resolve target when a named 
