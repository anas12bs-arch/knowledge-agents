---
title: "Redis 8.4's digest-based SET option cuts a 1MB compare-and-set from 4.3ms to 1.6ms"
url: "https://dev.to/alexgeorgiev17/redis-84s-digest-based-set-option-cuts-a-1mb-compare-and-set-from-43ms-to-16ms-1f8f"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-19T19:29:36Z"
metadata:
  tag: "devops"
---

# Redis 8.4's digest-based SET option cuts a 1MB compare-and-set from 4.3ms to 1.6ms

> Source: devto | Category: news | 2026-10-19T19:29:36Z

Redis 8.4 adds IFEQ, IFNE, IFDEQ and IFDNE to SET. I measured a 1MB compare-and-set drop from about 4.3ms to 1.6ms using the new digest option, then found the official Python client silently drops the server's own GET reply on one code path.

Reactions: 2
