---
title: "rust-lang/rust 1.100.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.100.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-11-12T19:54:54Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.100.0"
---

# rust-lang/rust 1.100.0 released

> Source: github-releases | Category: changelog | 2026-11-12T19:54:54Z

## rust-lang/rust — 1.100.0

<a id="1.100.0-Language"></a>

## Language

- [Stabilize never type](https://github.com/rust-lang/rust/pull/155499)
- [Lint against repeated `#[repr(..)]` attributes](https://github.com/rust-lang/rust/pull/157036)
- [Stabilize `extern "custom"`](https://github.com/rust-lang/rust/pull/158504)
- [Extend `dropping_references`, `dropping_copy_types` and `undropped_manually_drops` lints to `drop_in_place`](https://github.com/rust-lang/rust/pull/160229)
- [`unfulfilled_lint_expectations` no longer fires on `#[expect(dead_code)]` inside code that is covered by a dead parent's diagnostic](https://github.com/rust-lang/rust/pull/161005)
- [Turn the error for `repr(align)` fields in a `repr(packed)` type into a deny-by-default lint `aligned_fields_in_packed`](https://github.com/rust-lang/rust/pull/162160)
- [volatile: allow accesses to non-AM memory to trap](https://github.com/rust-lang/rust/pull/160564/)

<a id="1.100.0-Compiler"></a>

## Compiler

- [Stabilize `-Cprofile-sample-use`](https://github.com/rust-lang/rust/pull/155942)
- [Enable next solver by default in orphanck](https://github.com/rust-lang/rust/pull/160668)

<a id="1.100.0-Platform-Support"></a>

## Platform Support

- [`i686-pc-windows-gnu` is now a tier 2 without host tools target](https://github.com/rust-lang/rust/pull/161681)
- [Promote `wasm32-wasip3` to Tier 2](https://github.com/rust-lang/rust/pull/161940)
- [Add new Tier 3 target `powerpc64-sony-ps3`](https://github.com/rust-lang/rust/pull/162072)

Refer to Rust's [platform support page](https://doc.rust-lang.org/rustc/platform-support.html) for more information on Rust's tiered platform support.

<a id="1.100.0-Libraries"></a>

## Libraries

- [Stabilize custom allocators](https://github.com/rust-lang/rust/pull/156882)
- [Map `ENOTSUP` to `ErrorKind::Unsupported`](https://github.com/rust-lang/rust/pull/158580)
- [Fix soundness issues in `std::sys::pal::sgx::waitqueue::unsafe_list`](https://github.com/rust-lang/rust/pull/161334)

<a id="1.100.0-Stabilized-APIs"></a>

## Stabilized APIs

- [`impl PartialEq<Cow<'_, [U]>> for Vec<T, A>`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html#impl-PartialEq%3CCow%3C'_,+%5BU%5D%3E%3E-for-Vec%3CT,+A%3E)
- [`impl PartialEq<Cow<'_, [U]>> for &[T]`](https://doc.rust-lang.org/stable/std/primitive.slice.html#impl-PartialEq%3CCow%3C'_,+%5BU%5D%3E%3E-for-%26%5BT%5D)
- [`impl PartialEq<Cow<'_, [U]>> for &mut [T]`](https://doc.rust-lang.org/stable/std/primitive.slice.html#impl-PartialEq%3CCow%3C'_,+%5BU%5D%3E%3E-for-%26mut+%5BT%5D)
- [`std::alloc::Allocator`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html)
- [`std::alloc::Global`](https://doc.rust-lang.org/stable/std/alloc/struct.Global.html)
- [`std::alloc::System`](https://doc.rust-lang.org/stable/std/alloc/struct.System.html)
- [`impl Allocator for Global`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-Global)
- [`impl Allocator for System`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-System)
- [`impl<A: Allocator> Allocator for &A`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-%26A)
- [`impl<T: Allocator, A: Allocator> Allocator for Box<T, A>`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-Box%3CT,+A%3E)
- [`impl<A: Allocator> Allocator for &mut A`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-%26mut+A)
- [`impl<T: Allocator, A: Allocator> Allocator for Arc<T, A>`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-Arc%3CT,+A%3E)
- [`impl<T: Allocator, A: Allocator> Allocator for Rc<T, A>`](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html#impl-Allocator-for-Rc%3CT,+A%3E)
- [`Box::new_in`](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html#method.new_in)
- [`Box::from_raw_in`](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html#method.from_raw_in)
- [`Box::from
