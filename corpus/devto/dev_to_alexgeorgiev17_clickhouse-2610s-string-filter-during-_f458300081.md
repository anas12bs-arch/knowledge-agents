---
title: "ClickHouse 26.10's string filter during scan cuts a selective LIKE query's memory 25-fold"
url: "https://dev.to/alexgeorgiev17/clickhouse-2610s-string-filter-during-scan-cuts-a-selective-like-querys-memory-25-fold-228j"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-12T12:10:15Z"
metadata:
  tag: "devops"
---

# ClickHouse 26.10's string filter during scan cuts a selective LIKE query's memory 25-fold

> Source: devto | Category: news | 2026-11-12T12:10:15Z

I benchmarked ClickHouse 26.10's new apply_string_filters_during_scan setting against 26.9: a selective LIKE query's peak memory dropped from 37.6MB to 1.5MB, but a plain WHERE equality got none of it until I rewrote it as PREWHERE.

Reactions: 5
