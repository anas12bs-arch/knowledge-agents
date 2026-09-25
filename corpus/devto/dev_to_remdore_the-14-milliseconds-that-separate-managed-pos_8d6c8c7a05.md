---
title: "The 1.4 milliseconds that separate managed Postgres from a local one"
url: "https://dev.to/remdore/the-14-milliseconds-that-separate-managed-postgres-from-a-local-one-26de"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-25T19:20:11Z"
metadata:
  tag: "devops"
---

# The 1.4 milliseconds that separate managed Postgres from a local one

> Source: devto | Category: news | 2026-09-25T19:20:11Z

One app, two identical Postgres 17 databases, same region. Local was 4 to 7 times faster on reads because of network latency paid per query. Managed capped at 25 connections with 11 already used, and failed outright past 20 clients until I added the pooler.

Reactions: 1
