---
title: "rust-lang/rust 1.95.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.95.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-05-30T14:31:26Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.95.0"
---

# rust-lang/rust 1.95.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:26Z

## rust-lang/rust — 1.95.0

<a id="1.95-Language"></a>

## Language

- [Stabilize `if let` guards on match arms](https://github.com/rust-lang/rust/pull/141295)
- [`irrefutable_let_patterns` lint no longer lints on let chains](https://github.com/rust-lang/rust/pull/146832)
- [Support importing path-segment keywords with renaming](https://github.com/rust-lang/rust/pull/146972)
- [Stabilize inline assembly for PowerPC and PowerPC64](https://github.com/rust-lang/rust/pull/147996)
- [const-eval: be more consistent in the behavior of padding during typed copies](https://github.com/rust-lang/rust/pull/148967)
- [Const blocks are no longer evaluated to determine if expressions involving fallible operations can implicitly be constant-promoted.](https://github.com/rust-lang/rust/pull/150557). Expressions whose ability to implicitly be promoted would depend on the result of a const block are no longer implicitly promoted.
- [Make operational semantics of pattern matching independent of crate and module](https://github.com/rust-lang/rust/pull/150681)

<a id="1.95-Compiler"></a>

## Compiler

- [Stabilize `--remap-path-scope` for controlling the scoping of how paths get remapped in the resulting binary](https://github.com/rust-lang/rust/pull/147611)
- [Apply patches for CVE-2026-6042 and CVE-2026-40200 to vendored musl](https://github.com/rust-lang/rust/pull/155171)

<a id="1.95-Platform-Support"></a>

## Platform Support

- [Promote `powerpc64-unknown-linux-musl` to Tier 2 with host tools](https://github.com/rust-lang/rust/pull/149962)
- [Promote `aarch64-apple-tvos` to Tier 2](https://github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-tvos-sim` to Tier 2](https://github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-watchos` to Tier 2](https://github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-watchos-sim` to Tier 2](https://github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-visionos` to Tier 2](https://github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-visionos-sim` to Tier 2](https://github.com/rust-lang/rust/pull/152021)

Refer to Rust's [platform support page](https://doc.rust-lang.org/rustc/platform-support.html) for more information on Rust's tiered platform support.

<a id="1.95-Libraries"></a>

## Libraries

- [`thread::scope`: document how join interacts with TLS destructors](https://github.com/rust-lang/rust/pull/149482)
- [Speed up `str::contains` on aarch64 targets with `neon` target feature enabled by default](https://github.com/rust-lang/rust/pull/152176)

<a id="1.95-Stabilized-APIs"></a>

## Stabilized APIs

- [`MaybeUninit<[T; N]>: From<[MaybeUninit<T>; N]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-From%3CMaybeUninit%3C%5BT;+N%5D%3E%3E-for-%5BMaybeUninit%3CT%3E;+N%5D)
- [`MaybeUninit<[T; N]>: AsRef<[MaybeUninit<T>; N]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsRef%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>: AsRef<[MaybeUninit<T>]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsRef%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>: AsMut<[MaybeUninit<T>; N]>`](https://doc.rust-lang.org/beta/std/mem/union.MaybeUninit.html#impl-AsMut%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>: AsMut<[MaybeUninit<T>]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsMut%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`[MaybeUninit<T>; N]: From<MaybeUninit<[T; N]>>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-From%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`Cell<[T; N]>: AsRef<[Cell<T>; N]>`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html#impl-AsRef%3C%5BCell%3CT%3E;+N%5D%3E-for-Cell%3C%5BT;+N%5D%3E)
- [`Cell<[T; N]>: AsRef<[Cell<T>]>`](https://doc.rust-lang.org/stable/std/cell/struct.Ce
