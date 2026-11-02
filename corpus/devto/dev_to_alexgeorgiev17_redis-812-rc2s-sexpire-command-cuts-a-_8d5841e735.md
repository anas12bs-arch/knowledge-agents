---
title: "Redis 8.12 RC2's SEXPIRE command cuts a set membership check from two round trips to one"
url: "https://dev.to/alexgeorgiev17/redis-812-rc2s-sexpire-command-cuts-a-set-membership-check-from-two-round-trips-to-one-2mi4"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-02T20:02:46Z"
metadata:
  tag: "devops"
---

# Redis 8.12 RC2's SEXPIRE command cuts a set membership check from two round trips to one

> Source: devto | Category: news | 2026-11-02T20:02:46Z

Redis 8.12 RC2 adds per-member TTLs to sets. A membership check dropped from roughly 585 to 290 microseconds over 2,000 calls, but setting the TTL itself wasn't faster, and converting a small intset cost 15 times more memory.

Reactions: 7
