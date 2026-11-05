---
title: "PostgreSQL 19's pg_stat_lock only counts waits that cross deadlock_timeout"
url: "https://dev.to/alexgeorgiev17/postgresql-19s-pgstatlock-only-counts-waits-that-cross-deadlocktimeout-15lj"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-05T17:44:38Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19's pg_stat_lock only counts waits that cross deadlock_timeout

> Source: devto | Category: news | 2026-11-05T17:44:38Z

PostgreSQL 19rc1 adds a cumulative lock-wait view, pg_stat_lock. I measured it against real contention and found it records nothing below deadlock_timeout (1s by default) and nothing while a wait is still in progress.

Reactions: 8
