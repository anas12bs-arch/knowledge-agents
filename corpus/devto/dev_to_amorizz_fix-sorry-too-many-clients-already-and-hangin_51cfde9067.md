---
title: "Fix 'sorry, too many clients already' and hanging queries in Node pg"
url: "https://dev.to/amorizz/fix-sorry-too-many-clients-already-and-hanging-queries-in-node-pg-fmp"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-26T18:25:11Z"
metadata:
  tag: "programming"
---

# Fix 'sorry, too many clients already' and hanging queries in Node pg

> Source: devto | Category: news | 2026-11-26T18:25:11Z

A leaked pg pool client makes request 11 wait forever, and 10 default pools hit max_connections. Measured on pg 8.23.1, Postgres 17.12.

Reactions: 2
