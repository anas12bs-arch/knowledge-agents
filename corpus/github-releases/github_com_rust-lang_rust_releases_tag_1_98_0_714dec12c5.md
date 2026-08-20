---
title: "rust-lang/rust 1.98.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.98.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-08-20T18:06:46Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.98.0"
---

# rust-lang/rust 1.98.0 released

> Source: github-releases | Category: changelog | 2026-08-20T18:06:46Z

## rust-lang/rust — 1.98.0

<a id="1.98.0-Language"></a>

## Language

- [Allow shortening lifetime of `&mut` when unsize-coercing, even in an invariant position.](https://github.com/rust-lang/rust/pull/149219) For example, you can now coerce a `Cell<&'long mut i32>` to a `Cell<&'short mut dyn Send>`. Such shortenings were already previously allowed when coercing a `&mut` to a `&`, or coercing a `&` to a `&`.
- [Add deny-by-default `invalid_runtime_symbol_definitions` lint and warn-by-default `suspicious_runtime_symbol_definitions` lint](https://github.com/rust-lang/rust/pull/155521)
  - The lints currently specifically targets `core` runtime symbols like `memcmp`, `memset`, `strlen`, ... and is planned to be expanded in the next few releases.
- [Add warn-by-default `c_void_returns` lint to check `core::ffi::c_void` as a return type](https://github.com/rust-lang/rust/pull/156379)

<a id="1.98.0-Platform-Support"></a>

## Platform Support

- [Add `powerpc64-unknown-linux-gnuelfv2` as Tier 3](https://github.com/rust-lang/rust/pull/144220)
- [Add `aarch64-unknown-linux-pauthtest` as Tier 3 target](https://github.com/rust-lang/rust/pull/155722)
- [Promote `thumbv7a-none-eabi` to Tier 2](https://github.com/rust-lang/rust/pull/155763)
- [Promote `thumbv7a-none-eabihf` to Tier 2](https://github.com/rust-lang/rust/pull/155763)
- [Promote `thumbv7r-none-eabi` to Tier 2](https://github.com/rust-lang/rust/pull/155763)
- [Promote `thumbv7r-none-eabihf` to Tier 2](https://github.com/rust-lang/rust/pull/155763)
- [Promote `thumbv8r-none-eabihf` to Tier 2](https://github.com/rust-lang/rust/pull/155763)

Refer to Rust's [platform support page](https://doc.rust-lang.org/rustc/platform-support.html) for more information on Rust's tiered platform support.

<a id="1.98.0-Libraries"></a>

## Libraries

- [Change `Location<'_>` lifetime to `'static` in `Panic[Hook]Info`](https://github.com/rust-lang/rust/pull/146561)
- [Document panic in `RangeInclusive::from(legacy::RangeInclusive)`](https://github.com/rust-lang/rust/pull/155421)
- [Document that `ManuallyDrop`'s `Box` interaction has been fixed](https://github.com/rust-lang/rust/pull/155750)
- [Stabilize LoongArch CRC Intrinsics](https://github.com/rust-lang/rust/issues/156908)
- [The `derive` macro is available at `{core,std}::derive`.](https://github.com/rust-lang/rust/issues/154645) This was previously [unintentionally stabilized in 1.96](https://github.com/rust-lang/rust/issues/159856), but is now [explicitly accepted](https://github.com/rust-lang/rust/issues/154645) as a stabilized API.
  - Please note that the MSRV for `{core,std}::derive` will be 1.96, and not 1.98.

<a id="1.98.0-Stabilized-APIs"></a>

## Stabilized APIs

- [`str::substr_range`](https://doc.rust-lang.org/stable/std/primitive.str.html#method.substr_range)
- [`[T]::subslice_range`](https://doc.rust-lang.org/stable/std/primitive.slice.html#method.subslice_range)
- [`core::fmt::NumBuffer`](https://doc.rust-lang.org/stable/core/fmt/struct.NumBuffer.html)
- [`<{integer}>::format_into`](https://doc.rust-lang.org/stable/core/primitive.usize.html#method.format_into)
- [`Send/Sync for std::process::CommandArgs`](https://doc.rust-lang.org/stable/std/process/struct.CommandArgs.html#impl-Send-for-CommandArgs%3C'a%3E)
- [`{fN}::algebraic_add`](https://doc.rust-lang.org/stable/core/primitive.f32.html#method.algebraic_add)
- [`{fN}::algebraic_sub`](https://doc.rust-lang.org/stable/core/primitive.f32.html#method.algebraic_sub)
- [`{fN}::algebraic_mul`](https://doc.rust-lang.org/stable/core/primitive.f32.html#method.algebraic_mul)
- [`{fN}::algebraic_div`](https://doc.rust-lang.org/stable/core/primitive.f32.html#method.algebraic_div)
- [`{fN}::algebraic_rem`](https://doc.rust-lang.org/stable/core/primitive.f32.html#method.algebraic_rem)
- [`NonZero<{integer}>::from_str_radix`](https://doc.rust-lang.org/stable/core/num/struct.NonZero.html#method.from_str_radix-4)
- [`String::from_utf16le`](https://doc.rust-lang.org/stable/std/string/struct.String.html#method.from_utf1
