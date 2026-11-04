---
title: "remix-run/remix test@1.1.0 released"
url: "https://github.com/remix-run/remix/releases/tag/test%401.1.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-11-04T22:47:02Z"
metadata:
  repo: "remix-run/remix"
  version: "test@1.1.0"
---

# remix-run/remix test@1.1.0 released

> Source: github-releases | Category: changelog | 2026-11-04T22:47:02Z

## remix-run/remix — test@1.1.0

### Minor Changes

- Add new APIs to the mock function context for both `mock` and `t.mock`: ([#12097](https://github.com/remix-run/remix/pull/12097))
  - `mockImplementation(implementation)` changes the default implementation.
  - `mockImplementationOnce(implementation, onCall?)` replaces one call at a zero-based index, defaulting to the next call.
  - `resetCalls()` clears the call history.
  - `callCount()` returns the number of recorded invocations, including calls still executing.
  - `restore()` restores a standalone mock's original implementation.

  Replacement controls preserve generic and overloaded function signatures. Test context mocks restore in registration order alongside cleanup callbacks, even after failures. Cleanup errors retain their original stack traces and are reported alongside test failures.

### Patch Changes

- Fix syntax errors in browser tests that dynamically import modules by preserving quotes around rewritten module URLs. ([#12102](https://github.com/remix-run/remix/pull/12102))

- Fix browser test runs in WebKit stalling until the progress timeout once earlier files' results fill the runner page. The running file was placed below those results, out of view, where WebKit throttles its timers. It now runs at the top of the page. ([#12162](https://github.com/remix-run/remix/pull/12162))
