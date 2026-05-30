---
title: "rust-lang/rust 1.96.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.96.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-05-30T14:31:26Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.96.0"
---

# rust-lang/rust 1.96.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:26Z

## rust-lang/rust — 1.96.0

<a id="1.96.0-Language"></a>

## Language

- [Allow passing `expr` metavariable to `cfg`](https://github.com/rust-lang/rust/pull/146961)
- [Always coerce never types in tuple expressions](https://github.com/rust-lang/rust/pull/147834)
- [Avoid incorrect inference guidance of function arguments in rare cases](https://github.com/rust-lang/rust/pull/150316)
- [Support s390x vector registers in inline assembly](https://github.com/rust-lang/rust/pull/154184)
- [Allow using constants of type `ManuallyDrop` as patterns (fixing a regression introduced in 1.94.0)](https://github.com/rust-lang/rust/pull/154891)

<a id="1.96.0-Compiler"></a>

## Compiler

- [Enable link relaxation feature for LoongArch Linux targets](https://github.com/rust-lang/rust/pull/153427)
- [Update `riscv64gc-unknown-fuchsia` baseline to RVA22 + vector](https://github.com/rust-lang/rust/pull/155072)

<a id="1.96.0-Libraries"></a>

## Libraries

- [Support iterating over ranges of `NonZero` integers](https://github.com/rust-lang/rust/pull/127534)
- [refactor 'valid for read/write' definition: exclude null; add that as an exception on individual methods instead](https://github.com/rust-lang/rust/pull/152615)
- [Fix SGX delayed host lookup via ToSocketAddr](https://github.com/rust-lang/rust/pull/152851)

<a id="1.96.0-Stabilized-APIs"></a>

## Stabilized APIs

- [`assert_matches!`](https://doc.rust-lang.org/stable/std/macro.assert_matches.html)
- [`debug_assert_matches!`](https://doc.rust-lang.org/stable/std/macro.debug_assert_matches.html)
- [`From<T> for AssertUnwindSafe<T>`](https://doc.rust-lang.org/stable/std/panic/struct.AssertUnwindSafe.html#impl-From%3CT%3E-for-AssertUnwindSafe%3CT%3E)
- [`From<T> for LazyCell<T, F>`](https://doc.rust-lang.org/stable/std/cell/struct.LazyCell.html#impl-From%3CT%3E-for-LazyCell%3CT,+F%3E)
- [`From<T> for LazyLock<T, F>`](https://doc.rust-lang.org/stable/std/sync/struct.LazyLock.html#impl-From%3CT%3E-for-LazyLock%3CT,+F%3E)
- [`core::range::RangeToInclusive`](https://doc.rust-lang.org/stable/core/range/struct.RangeToInclusive.html)
- [`core::range::RangeToInclusiveIter`](https://doc.rust-lang.org/stable/core/range/struct.RangeToInclusiveIter.html)
- [`core::range::RangeFrom`](https://doc.rust-lang.org/stable/core/ops/struct.RangeFrom.html)
- [`core::range::RangeFromIter`](https://doc.rust-lang.org/stable/core/ops/struct.RangeFromIter.html)
- [`core::range::Range`](https://doc.rust-lang.org/stable/std/range/struct.Range.html)
- [`core::range::RangeIter`](https://doc.rust-lang.org/stable/std/range/struct.RangeIter.html)

<a id="1.96.0-Cargo"></a>

## Cargo

- [Allow a dependency to specify both a git repository and an alternate registry.](https://github.com/rust-lang/cargo/pull/16810/) Just like with crates.io, the git repository will be used locally, but the registry version will be used when published.
- [Added `target.'cfg(..)'.rustdocflags` support in configuration.](https://github.com/rust-lang/cargo/pull/16846)
- Fixed [CVE-2026-5222](https://blog.rust-lang.org/2026/05/25/cve-2026-5222/) and [CVE-2026-5223](https://blog.rust-lang.org/2026/05/25/cve-2026-5223/).

<a id="1.96-Rustdoc"></a>

## Rustdoc

- [Deprecation notes are now rendered like any other documentation](https://github.com/rust-lang/rust/pull/149931). Previously they used the css `white-space: pre-wrap;` property and stripped any `<p>` elements from the rendered html, however this caused issues and unintuitive behavior. The new behavior should be more predictable, however some multi-line deprecation notes will now be rendered as as single lines. If this is undesirable, you can use the standard markdown method of forcing a linebreak, which is two spaces followed by a newline (`"\n"`).
- [Don't emit rustdoc `missing_doc_code_examples` lint on impl items](https://github.com/rust-lang/rust/pull/154048)
- [Separate methods and associated functions in sidebar](https://github.com/rust-lang/rust/pull/154644)

<a id="1.96.0-Compatibility-Notes"></a>

## Compatibility No
