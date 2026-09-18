---
title: "remix-run/remix ui@0.10.0 released"
url: "https://github.com/remix-run/remix/releases/tag/ui%400.10.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-09-18T22:56:07Z"
metadata:
  repo: "remix-run/remix"
  version: "ui@0.10.0"
---

# remix-run/remix ui@0.10.0 released

> Source: github-releases | Category: changelog | 2026-09-18T22:56:07Z

## remix-run/remix — ui@0.10.0

### Minor Changes

- BREAKING CHANGE: Navigations that specify a named frame that is not currently mounted now perform a document navigation instead of reloading the top frame. Fresh links, forms, and `navigate()` calls are left to the browser, preserving native form methods and bodies, while back and forward traversal reloads the destination document. Omit the target when the navigation should always reload the top frame:

  ```diff
  -<a href="/account" data-rmx-target="optional-account">
  +<a href="/account">
  ```

- BREAKING CHANGE: The default `resolveFrame` now only fetches same-origin sources and follows same-origin redirects. Apps that load cross-origin frame content must provide a custom `resolveFrame` to `run()`.

  Validate navigation source overrides regardless of the target, falling back to document navigation for invalid or cross-origin overrides.

- BREAKING CHANGE: Raw HTML props now require an opaque value created by `unsafeHTML()`. This applies to `innerHTML` and both iframe `srcDoc` spellings (`srcDoc` and `srcdoc`). It prevents attacker-controlled prop spreads from activating HTML parsing with plain strings or JSON-shaped objects. `outerHTML` is not supported because it would replace a reconciler-owned element. `unsafeHTML()` is an explicit authorization boundary; it does not sanitize or otherwise modify its input.

  ```diff
  -import type { Handle } from 'remix/ui'
  +import { unsafeHTML } from 'remix/ui'
  +import type { Handle } from 'remix/ui'

   function Content(handle: Handle<{ html: string }>) {
  -  return () => <div innerHTML={handle.props.html} />
  +  return () => <div innerHTML={unsafeHTML(handle.props.html)} />
   }
  ```

### Patch Changes

- Ignore invalid host prop names and reserved DOM mutation properties during server rendering and client reconciliation. Block `javascript:` URLs in executable URL attributes while preserving other URL schemes and non-executable attributes. Use the `on()` mixin for events; the explicit `innerHTML` API and standard DOM, `data-*`, `aria-*`, SVG, and custom-element properties continue to work as before.

- Fix duplicated text during hydration when a browser splits long server-rendered text into multiple DOM nodes, including chunks that span adjacent text children (see #11591).

- Avoid attaching duplicate event handlers when a client entry imports and renders another client entry, including through fragments and wrapper components. Preserve deferred removal and exit animations when removing nested client entries (see #11844).

- Restore the previous named frame from `handle.frames.get(name)` when a more recently mounted frame with the same name unmounts.
