---
title: "48 Bytes a Call I Kept Handing the Garbage Collector"
url: "https://dev.to/ssukhpinder/48-bytes-a-call-i-kept-handing-the-garbage-collector-3p8j"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-21T11:42:49Z"
metadata:
  tag: "webdev"
---

# 48 Bytes a Call I Kept Handing the Garbage Collector

> Source: devto | Category: news | 2026-10-21T11:42:49Z

A hot-path helper took params object[] and minted a fresh array on every call. Switching params to ReadOnlySpan<T> (C# 13+) dropped the per-call allocation to zero — though the throughput came out a tie.

Reactions: 0
