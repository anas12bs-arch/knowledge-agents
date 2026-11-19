---
title: "remix-run/remix test@1.2.0 released"
url: "https://github.com/remix-run/remix/releases/tag/test%401.2.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "remix"]
date: "2026-11-19T04:02:34Z"
metadata:
  repo: "remix-run/remix"
  version: "test@1.2.0"
---

# remix-run/remix test@1.2.0 released

> Source: github-releases | Category: changelog | 2026-11-19T04:02:34Z

## remix-run/remix — test@1.2.0

### Minor Changes

- `t.useFakeTimers()` now fakes `Date`, `performance.now()`, `setImmediate()`/`clearImmediate()`, and `AbortSignal.timeout()` along with the timer functions, so wall-clock code such as expiry checks and timestamps can be tested without injecting a clock. While fake timers are active, `Date.now()`, `new Date()`, and `performance.now()` read the fake clock and move forward only with `advance()` or `advanceAsync()`. `new Date(value)`, `Date.parse()`, `Date.UTC()`, and `instanceof Date` keep working. Immediates fire on the next `advance()`, and `AbortSignal.timeout(ms)` signals abort with a `TimeoutError` once the fake clock reaches `ms`. ([#12203](https://github.com/remix-run/remix/pull/12203))

  Like Node's mock timers, the fake `Date` starts at the Unix epoch (`0`) and `performance.now()` starts at `0`. Tests that used fake timers while reading the real `Date`, or while relying on real immediates or `AbortSignal.timeout()`, now see fake time instead. Pass the new `now` option to start at a specific time:

  ```ts
  let timers = t.useFakeTimers({ now: new Date('2030-01-01T00:00:00Z') })
  ```

- Added data-property mocking with `mock.property()` and `t.mock.property()`, including read/write records, one-access value overrides, and descriptor restoration. Added getter and setter spies through `mock.getter()`, `mock.setter()`, and the fourth `mock.method()` argument. Exported `MockTracker` as the shared type for standalone and test-context mocks. ([#12225](https://github.com/remix-run/remix/pull/12225))

  Test-context accessor and property mocks restore in reverse installation order after cleanup callbacks, even when a test or cleanup callback fails. Method mocks layered over getter spies preserve the accessor's backing value. Method, accessor, and property mocks can be created while `Array.isArray` is mocked, with array argument checks preserved.

- Added public `TestFn` and `TestMeta` types for reusable test callbacks and metadata, with linked API documentation for the test body and its options. ([#12226](https://github.com/remix-run/remix/pull/12226))

- Add new `t.waitFor(condition, { interval, timeout })` API to retry assertions until they pass. Polling stops when the test ends. See [Polling Assertions](https://github.com/remix-run/remix/tree/main/packages/test#polling-assertions) for usage. ([#12224](https://github.com/remix-run/remix/pull/12224))

### Patch Changes

- Fix several gaps in `t.useFakeTimers()`: ([#12203](https://github.com/remix-run/remix/pull/12203))
  - `clearTimeout()` and `clearInterval()` now cancel real timers created before fake timers were enabled. Previously the fakes ignored those timers, so a test with a `timeout` option that enabled fake timers left its real timeout timer running after it finished, which later aborted the test's signal and kept the process alive.
  - `setTimeout()` and `setInterval()` now pass extra arguments to the callback.
  - In Node, fake timers return handles with `ref()`, `unref()`, `hasRef()`, and `refresh()`, so code that calls `.unref()` on a timer no longer throws. Clearing an expired timeout's handle prevents `refresh()` from reactivating it.
  - Calling `t.useFakeTimers()` again restores the previous clock before starting a new one, so cleanup restores the original `Date`. Repeated `restore()` calls have no effect.
  - Restore fake timers synchronously on abort and before user cleanup callbacks. Finished or aborted contexts cannot enable another clock, and runner deadlines keep using real timers.
  - Reject overlapping clocks, roll back failed installations, and restore the original property descriptors without reinstalling fakes beneath spies. Restoration attempts every property, reports failures, and permits retrying failed properties.
  - Keep fake timer IDs unique across clocks so clearing a stale numeric handle cannot cancel a later test's timer.
  - Fake `AbortSignal.timeout(ms)` validates its argument synchronously using Node's numeric integ
