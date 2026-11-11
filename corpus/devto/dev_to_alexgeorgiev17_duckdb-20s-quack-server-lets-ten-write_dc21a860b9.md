---
title: "DuckDB 2.0's quack server lets ten writers share one file for under 2ms a query"
url: "https://dev.to/alexgeorgiev17/duckdb-20s-quack-server-lets-ten-writers-share-one-file-for-under-2ms-a-query-1ged"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-11T17:11:38Z"
metadata:
  tag: "programming"
---

# DuckDB 2.0's quack server lets ten writers share one file for under 2ms a query

> Source: devto | Category: news | 2026-11-11T17:11:38Z

DuckDB 2.0 ships a built-in server so several processes can finally write to one database file. Ten concurrent clients landed 1,000 inserts with no errors, at a cost of roughly 1.7ms extra per query and a frozen local catalog while connected.

Reactions: 7
