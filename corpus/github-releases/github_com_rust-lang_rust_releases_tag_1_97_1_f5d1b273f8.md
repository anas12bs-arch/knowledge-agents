---
title: "rust-lang/rust 1.97.1 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.97.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-07-16T14:15:19Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.97.1"
---

# rust-lang/rust 1.97.1 released

> Source: github-releases | Category: changelog | 2026-07-16T14:15:19Z

## rust-lang/rust — 1.97.1

<a id="1.97.1"></a>

- [rustc: Fix miscompilation in LLVM optimization](https://github.com/rust-lang/rust/issues/159035) This backports an LLVM submodule bump to include the LLVM-side fix and a revert of the rustc change that is one known trigger for the bug. The rustc side revert should not be strictly necessary but is done out of abundance of caution.

