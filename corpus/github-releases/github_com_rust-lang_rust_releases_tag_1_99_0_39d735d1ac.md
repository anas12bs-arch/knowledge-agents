---
title: "rust-lang/rust 1.99.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.99.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-10-01T16:26:57Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.99.0"
---

# rust-lang/rust 1.99.0 released

> Source: github-releases | Category: changelog | 2026-10-01T16:26:57Z

## rust-lang/rust — 1.99.0

<a id="1.99.0-Language"></a>

## Language

- [Add allow-by-default `raw_borrows_via_references` lint that checks for references that decay immediately into raw borrows](https://github.com/rust-lang/rust/pull/138230)
- [Extend `unconditional_panic` lint to function calls that panic when the chunks/windows size is zero](https://github.com/rust-lang/rust/pull/153563)
- [Stabilize C-variadic function definitions](https://github.com/rust-lang/rust/pull/155697)
- [Stabilize the ability to use `#[unsafe(naked)]` functions to define C-variadic functions (`#![feature(c_variadic_naked_functions)]`).](https://github.com/rust-lang/rust/pull/159746)
- [Trait methods are now resolved on an adjusted never type (producing a FCW)](https://github.com/rust-lang/rust/pull/156047)
- [Coerce from inference variables to trait objects if the inference variable is related via subtyping to a type that is known to be `Sized`](https://github.com/rust-lang/rust/pull/157820)
- [Stabilize `#[my_macro] mod foo;`](https://github.com/rust-lang/rust/pull/157857). This allows outlined modules (`mod foo;`) anywhere in the body of a custom attribute or derive macro.
- [Fix the `overflowing_literals` lint with repeated negation](https://github.com/rust-lang/rust/pull/158302). For instance, it will now no longer lint on `--128_i8`, which is already detected by the `arithmetic_overflow` lint.
- [Add POSIX symbols to the `invalid_runtime_symbol_definitions` and `suspicious_runtime_symbol_definitions` lints](https://github.com/rust-lang/rust/pull/158522)
- [Lint unused `#[path]` attributes on inline modules](https://github.com/rust-lang/rust/pull/158835)
- [Enable `unreachable_cfg_select_predicates` lint as part of `unused` lint group](https://github.com/rust-lang/rust/pull/159179)
- [Stabilize passing 128-bit integers via vector registers with `asm!` on x86](https://github.com/rust-lang/rust/pull/159525)
- [Explicitly document that some allocations are allowed to grow in-place (but none are allowed to shrink)](https://github.com/rust-lang/rust/pull/159729)
- We now [guarantee](https://github.com/rust-lang/rust/pull/159730) that the contents of an `UnsafeCell` can be accessed without going through `get`
  - [The `invalid_reference_casting` lint was adjusted accordingly](https://github.com/rust-lang/rust/pull/159960)
- [Account for globally enabled target features in `global_asm!`](https://github.com/rust-lang/rust/pull/160594)
- [Warn if an invalid `doc` attribute is used on a macro invocation](https://github.com/rust-lang/rust/pull/161003)

<a id="1.99.0-Compiler"></a>

## Compiler

- [Convert `-Ctarget-cpu` into a target-modifier for AVR, AMDGCN and NVPTX](https://github.com/rust-lang/rust/pull/150732)
- [Enable `static_position_independent_executables` on all gnu targets](https://github.com/rust-lang/rust/pull/158510)
- When providing a suggestion about a missing method, rustc now prefers an exactly matching name from a [doc alias attribute](https://doc.rust-lang.org/rustdoc/advanced-features.html#add-aliases-for-an-item-in-documentation-search) over a similarity search from other method names. If your new users sometimes expect a method under a different name, adding a doc alias will now help them find it via rustc suggestions, in addition to helping them find it via rustdoc search: [When suggesting method names, prefer *exact* doc aliases over similar names](https://github.com/rust-lang/rust/pull/160369)

<a id="1.99.0-Platform-Support"></a>

## Platform Support

- [Promote `riscv64-unknown-linux-musl` to Tier 2 with host tools](https://github.com/rust-lang/rust/pull/158766)

Refer to Rust's [platform support page](https://doc.rust-lang.org/rustc/platform-support.html) for more information on Rust's tiered platform support.

<a id="1.99.0-Libraries"></a>

## Libraries

- Iteration on `RangeInclusive` (`a..=b` ranges) is now [optimized better in some circumstances](https://github.com/rust-lang/rust/pull/155114). As a side effect of this, the behavior of `RangeInclu
