---
title: "MongoDB 8.3's arrayIndexAs cuts a map-with-index workaround's overhead by up to 31%"
url: "https://dev.to/alexgeorgiev17/mongodb-83s-arrayindexas-cuts-a-map-with-index-workarounds-overhead-by-up-to-31-409p"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-12T00:47:00Z"
metadata:
  tag: "devops"
---

# MongoDB 8.3's arrayIndexAs cuts a map-with-index workaround's overhead by up to 31%

> Source: devto | Category: news | 2026-10-12T00:47:00Z

I benchmarked MongoDB 8.3's new arrayIndexAs against the range-and-arrayElemAt workaround it replaces: 134ms versus 102ms server-side at 320,000 elements, a gap that shrinks to about 5% once ten clients compete for the same CPU cores.

Reactions: 11
