---
title: "40 Bytes a Call, Just to Pass Four Ints"
url: "https://dev.to/ssukhpinder/40-bytes-a-call-just-to-pass-four-ints-1n3h"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-21T16:07:29Z"
metadata:
  tag: "programming"
---

# 40 Bytes a Call, Just to Pass Four Ints

> Source: devto | Category: news | 2026-10-21T16:07:29Z

A params array allocates a fresh array on every call. Switching the parameter to params ReadOnlySpan<int> dropped that to zero bytes and ran 2.5x faster, measured.

Reactions: 0
