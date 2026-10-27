---
title: "Every Comma Was Costing Me an Array"
url: "https://dev.to/ssukhpinder/every-comma-was-costing-me-an-array-4lg2"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-27T12:46:04Z"
metadata:
  tag: "programming"
---

# Every Comma Was Costing Me an Array

> Source: devto | Category: news | 2026-10-27T12:46:04Z

A nightly CSV job was burning 150 MB a pass on string.Split. Swapping to ReadOnlySpan<char>.Split with a stack-allocated Span<Range> dropped per-line allocations to zero and cut the time to a third.

Reactions: 0
