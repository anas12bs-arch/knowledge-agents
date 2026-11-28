---
title: "rust-lang/rust 1.100.1 released"
url: "https://github.com/rust-lang/rust/releases/tag/1.100.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "rust"]
date: "2026-11-28T02:07:41Z"
metadata:
  repo: "rust-lang/rust"
  version: "1.100.1"
---

# rust-lang/rust 1.100.1 released

> Source: github-releases | Category: changelog | 2026-11-28T02:07:41Z

## rust-lang/rust — 1.100.1

<a id="1.100.1"></a>

- [library: fix regression where some types were not inferred as having `Iterator` impls](https://github.com/rust-lang/rust/issues/166229)
  - This backports a change to the unstable `const` version of `Iterator`, which unintentionally caused existing code to not be seen as implementing `Iterator` when a valid implementation was present.

