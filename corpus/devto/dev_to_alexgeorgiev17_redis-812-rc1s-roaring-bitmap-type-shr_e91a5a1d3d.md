---
title: "Redis 8.12-rc1's roaring bitmap type shrinks a sparse bitmap from 24MB to 239KB"
url: "https://dev.to/alexgeorgiev17/redis-812-rc1s-roaring-bitmap-type-shrinks-a-sparse-bitmap-from-24mb-to-239kb-5bll"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-08T14:36:25Z"
metadata:
  tag: "devops"
---

# Redis 8.12-rc1's roaring bitmap type shrinks a sparse bitmap from 24MB to 239KB

> Source: devto | Category: news | 2026-11-08T14:36:25Z

I measured Redis 8.12-rc1's new roaring bitmap type: a 200-million-bit sparse bitmap dropped from 24MB to 239KB and BITCOUNT got about 14 times faster, but a dense bitmap came out slightly bigger than before.

Reactions: 6
