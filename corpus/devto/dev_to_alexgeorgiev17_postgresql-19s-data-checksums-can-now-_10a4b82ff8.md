---
title: "PostgreSQL 19's data checksums can now be switched on without stopping the server"
url: "https://dev.to/alexgeorgiev17/postgresql-19s-data-checksums-can-now-be-switched-on-without-stopping-the-server-fn"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-22T18:22:49Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19's data checksums can now be switched on without stopping the server

> Source: devto | Category: news | 2026-09-22T18:22:49Z

I measured PostgreSQL 19 beta's online checksum conversion against the old offline tool: roughly 1.3s of hard downtime the old way versus 2.8s of background work and 799MB of extra WAL the new way, with zero drop in concurrent write throughput.

Reactions: 11
