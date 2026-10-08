---
title: "ParadeDB's pg_search 0.26 cuts a ten-term BM25 search from 129ms to 29ms"
url: "https://dev.to/alexgeorgiev17/paradedbs-pgsearch-026-cuts-a-ten-term-bm25-search-from-129ms-to-29ms-5287"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-08T14:39:06Z"
metadata:
  tag: "devops"
---

# ParadeDB's pg_search 0.26 cuts a ten-term BM25 search from 129ms to 29ms

> Source: devto | Category: news | 2026-10-08T14:39:06Z

I benchmarked pg_search 0.25.11 against 0.26.0 on the same three-million-row table: a ten-term OR search dropped from 129ms to 29ms, but a single-term search got five times slower.

Reactions: 8
