---
title: "Valkey 9.2's forkless BGSAVE cuts my memory spike from 350MB to 10MB"
url: "https://dev.to/alexgeorgiev17/valkey-92s-forkless-bgsave-cuts-my-memory-spike-from-350mb-to-10mb-23km"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-04T15:31:42Z"
metadata:
  tag: "devops"
---

# Valkey 9.2's forkless BGSAVE cuts my memory spike from 350MB to 10MB

> Source: devto | Category: news | 2026-10-04T15:31:42Z

Valkey 9.2.0-rc1's opt-in forkless snapshot held the memory spike during BGSAVE to about 10MB against fork()'s 350MB on a 1.1GB dataset, but took 70% longer and cost 15% of write throughput to do it.

Reactions: 6
