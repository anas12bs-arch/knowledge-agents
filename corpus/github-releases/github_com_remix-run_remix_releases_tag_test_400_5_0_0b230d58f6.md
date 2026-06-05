---
title: "remix-run/remix test@0.5.0 released"
url: "https://github.com/remix-run/remix/releases/tag/test%400.5.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-06-05T22:45:48Z"
metadata:
  repo: "remix-run/remix"
  version: "test@0.5.0"
---

# remix-run/remix test@0.5.0 released

> Source: github-releases | Category: changelog | 2026-06-05T22:45:48Z

## remix-run/remix — test@0.5.0

### Minor Changes

- Add timeout and abort signal support to `@remix-run/test`.

  Tests and lifecycle hooks can now pass `{ timeout, signal }`. Timed-out tests fail and abort `t.signal`, so async work that accepts an `AbortSignal` can cancel promptly. Tests and suites can also use string `skip`/`todo` reasons, and reporters display those reasons when a pending result is reported.

  ```ts
  it('loads data', { timeout: 5_000 }, async (t) => {
    let response = await fetch('/api/data', { signal: t.signal })
    assert.equal(response.status, 200)
  })

  it('depends on external credentials', { skip: 'requires API credentials' }, () => {})
  ```

### Patch Changes

- Ignore browser-cancelled script requests in `remix-test` browser runs so iframe navigation can finish cleanly on Windows while still reporting real script load failures.
