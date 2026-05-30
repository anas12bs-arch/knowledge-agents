---
title: "remix-run/remix test@0.4.2 released"
url: "https://github.com/remix-run/remix/releases/tag/test%400.4.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-05-30T14:31:17Z"
metadata:
  repo: "remix-run/remix"
  version: "test@0.4.2"
---

# remix-run/remix test@0.4.2 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:17Z

## remix-run/remix — test@0.4.2


### Patch Changes

- Fix browser tests so bare package imports resolve with browser and ESM conditions, matching the asset server and avoiding CommonJS entries for packages like `clsx` (see #11478).

- Update the optional `playwright` peer dependency range to match the workspace Playwright catalog version.

- Run browser and E2E tests sequentially within each Playwright project so `remix-test` avoids launching extra browsers at the same time and reduces timing flakes on constrained CI runners.

- Report `beforeAll`, `afterEach`, and `afterAll` hook failures as failed test results so `remix-test` exits non-zero when lifecycle hooks throw.

- Use OS-assigned ports for browser test servers so parallel `remix-test` runs do not fail when the fixed port window is exhausted.
