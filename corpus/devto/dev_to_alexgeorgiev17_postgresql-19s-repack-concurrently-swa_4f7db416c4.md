---
title: "PostgreSQL 19's REPACK CONCURRENTLY swaps a five-second table lock for one under a second"
url: "https://dev.to/alexgeorgiev17/postgresql-19s-repack-concurrently-swaps-a-five-second-table-lock-for-one-under-a-second-34kp"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-14T15:21:18Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19's REPACK CONCURRENTLY swaps a five-second table lock for one under a second

> Source: devto | Category: news | 2026-10-14T15:21:18Z

I bloated a Postgres 19 beta table, then rewrote it with VACUUM FULL and with the new REPACK CONCURRENTLY: 4.3-5.9s of blocked client time against 0.3-0.9s, and a documented replication-slot limit I managed to actually hit.

Reactions: 5
