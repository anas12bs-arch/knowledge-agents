---
title: "Postgres 19's REPACK rewrites a bloated table without locking out your writers"
url: "https://dev.to/remdore/postgres-19s-repack-rewrites-a-bloated-table-without-locking-out-your-writers-2ep0"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-09T13:47:27Z"
metadata:
  tag: "devops"
---

# Postgres 19's REPACK rewrites a bloated table without locking out your writers

> Source: devto | Category: news | 2026-09-09T13:47:27Z

PostgreSQL 19 beta replaces VACUUM FULL and CLUSTER with REPACK. Under eight concurrent writers VACUUM FULL let 33 writes through; REPACK let 3,988. But the swap still queues behind a slow query, and there are four tables it refuses outright.

Reactions: 11
