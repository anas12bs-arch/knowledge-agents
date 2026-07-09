---
title: "rust-lang/rust 1.97.0 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.97.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-07-09T14:09:23Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.97.0"
---

# rust-lang/rust 1.97.0 released

> Source: github-releases | Category: changelog | 2026-07-09T14:09:23Z

## rust-lang/rust — 1.97.0

<a id="1.97.0-Language"></a>

## Language

- [Consider `Result<T, Uninhabited>` and `ControlFlow<Uninhabited, T>` to be equivalent to `T` for must use lint](https://github.com/rust-lang/rust/pull/148214)
- [Add allow-by-default `dead_code_pub_in_binary` lint for unused pub items in binary crates](https://github.com/rust-lang/rust/pull/149509)
- [Stabilize the `div32`, `lam-bh`, `lamcas`, `ld-seq-sa` and `scq` target features](https://github.com/rust-lang/rust/pull/154510)
- [Stabilize `cfg(target_has_atomic_primitive_alignment)`](https://github.com/rust-lang/rust/pull/155006)
- [Allow trailing `self` in imports in more cases](https://github.com/rust-lang/rust/pull/155137)

<a id="1.97.0-Platform-Support"></a>

## Platform Support

- [nvptx64-nvidia-cuda: drop support for old architectures and old ISAs](https://github.com/rust-lang/rust/pull/152443)

Refer to Rust's [platform support page](https://doc.rust-lang.org/rustc/platform-support.html) for more information on Rust's tiered platform support.

<a id="1.97.0-Stabilized-APIs"></a>

## Stabilized APIs

- [`Default for RepeatN`](https://doc.rust-lang.org/stable/std/iter/struct.RepeatN.html#impl-Default-for-RepeatN%3CA%3E)
- [`Copy for ffi::FromBytesUntilNulError`](https://doc.rust-lang.org/stable/std/ffi/struct.FromBytesUntilNulError.html#impl-Copy-for-FromBytesUntilNulError)
- [`Send for std::fs::File` on UEFI](https://github.com/rust-lang/rust/pull/154003)
- [`<{integer}>::isolate_highest_one`](https://doc.rust-lang.org/stable/std/primitive.u32.html#method.isolate_highest_one)
- [`<{integer}>::isolate_lowest_one`](https://doc.rust-lang.org/stable/std/primitive.u32.html#method.isolate_lowest_one)
- [`<{integer}>::highest_one`](https://doc.rust-lang.org/stable/std/primitive.u32.html#method.highest_one)
- [`<{integer}>::lowest_one`](https://doc.rust-lang.org/stable/std/primitive.u32.html#method.lowest_one)
- [`<{integer}>::bit_width`](https://doc.rust-lang.org/stable/std/primitive.u32.html#method.bit_width)
- [`NonZero<{integer}>::isolate_highest_one`](https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.isolate_highest_one)
- [`NonZero<{integer}>::isolate_lowest_one`](https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.isolate_lowest_one)
- [`NonZero<{integer}>::highest_one`](https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.highest_one)
- [`NonZero<{integer}>::lowest_one`](https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.lowest_one)
- [`NonZero<{integer}>::bit_width`](https://doc.rust-lang.org/stable/std/num/struct.NonZero.html#method.bit_width)

These previously stable APIs are now stable in const contexts:

- [`char::is_control`](https://doc.rust-lang.org/stable/std/primitive.char.html#method.is_control)

<a id="1.97.0-Cargo"></a>

## Cargo

- [Stabilize `build.warnings` config.](https://github.com/rust-lang/cargo/pull/16796) This controls how lint warnings from local packages are treated. Useful for enforcing a warning-free build in CI, replacing `-Dwarnings`. [docs](https://doc.rust-lang.org/nightly/cargo/reference/config.html#buildwarnings)
- [Stabilize `resolver.lockfile-path` config.](https://github.com/rust-lang/cargo/pull/16694) This allows specifying the path to the lockfile to use when resolving dependencies. Useful when working with read-only source directories. [docs](https://doc.rust-lang.org/nightly/cargo/reference/config.html#resolverlockfile-path)
- [cargo-clean: Error when `--target-dir` doesn't look like a Cargo target directory.](https://github.com/rust-lang/cargo/pull/16712) This prevents accidental deletion of non-target directories.
- [Add `-m` shorthand for `--manifest-path`](https://github.com/rust-lang/cargo/pull/16858)
- [Remove `curl` dependency from `crates-io` crate](https://github.com/rust-lang/cargo/pull/16936)

<a id="1.97.0-Rustdoc"></a>

## Rustdoc

- [Stabilize `--emit` flag](https://github.com/rust-lang/rust/pull/146220)
- [Stabilize `--remap-path-prefix`](https://github.
