---
title: "Turning on Postgres logical replication without a restart"
url: "https://dev.to/alexgeorgiev17/turning-on-postgres-logical-replication-without-a-restart-4b35"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-24T15:02:14Z"
metadata:
  tag: "devops"
---

# Turning on Postgres logical replication without a restart

> Source: devto | Category: news | 2026-11-24T15:02:14Z

PostgreSQL 19 lets you create a logical replication slot while wal_level is still replica. I measured zero downtime against the old way's 0.33-0.36s outage, and found it costs nothing extra in WAL volume for a plain update workload.

Reactions: 7
