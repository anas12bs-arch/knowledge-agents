---
title: "Containerd 2.4's switch to klauspost's gzip decoder speeds up real image layers by 18%"
url: "https://dev.to/alexgeorgiev17/containerd-24s-switch-to-klausposts-gzip-decoder-speeds-up-real-image-layers-by-18-2jne"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-07T14:25:46Z"
metadata:
  tag: "devops"
---

# Containerd 2.4's switch to klauspost's gzip decoder speeds up real image layers by 18%

> Source: devto | Category: news | 2026-11-07T14:25:46Z

I benchmarked containerd 2.4's swap from Go's stdlib gzip to klauspost/compress on real container layers: 18% faster decompression against the 40-50% the upstream PR reported, but allocations dropped by over 300x.

Reactions: 7
