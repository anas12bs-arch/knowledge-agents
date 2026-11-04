---
title: "PostgreSQL 19's sequence replication only catches up when you tell it to"
url: "https://dev.to/alexgeorgiev17/postgresql-19s-sequence-replication-only-catches-up-when-you-tell-it-to-2410"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-04T17:28:47Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19's sequence replication only catches up when you tell it to

> Source: devto | Category: news | 2026-11-04T17:28:47Z

PostgreSQL 19 RC1 can replicate sequence values to a logical subscriber, closing a long-standing failover gap. I measured it: an instant match on subscribe, then a frozen value through 700 more replicated rows until I ran REFRESH SEQUENCES, and a promotion I did properly still hit the exact duplicate-key error the feature is meant to prevent.

Reactions: 8
