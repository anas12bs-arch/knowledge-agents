---
title: "5 Cycles Invisible in 14,556 Files. The Cache Bug That Hid Them."
url: "https://dev.to/ofri-peretz/import-nextno-cycle-reported-0-cycles-on-nextjs-we-found-why-and-fixed-it-ln2"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-05-30T14:30:05Z"
metadata:
  tag: "javascript"
---

# 5 Cycles Invisible in 14,556 Files. The Cache Bug That Hid Them.

> Source: devto | Category: news | 2026-05-30T14:30:05Z

We found 5 import cycles in 33 files that were invisible in 14,556. The cause: a 10-hop depth limit that wrote false non-cyclic entries into a shared cache, poisoning later traversals. Here is the bug, the fix, and how to test if your own cycle detector has the same class of failure.

Reactions: 1
