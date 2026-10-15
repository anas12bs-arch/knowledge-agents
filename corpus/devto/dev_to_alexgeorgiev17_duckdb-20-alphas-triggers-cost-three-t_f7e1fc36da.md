---
title: "DuckDB 2.0 alpha's triggers cost three times more per row than per statement"
url: "https://dev.to/alexgeorgiev17/duckdb-20-alphas-triggers-cost-three-times-more-per-row-than-per-statement-13cj"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-15T21:37:11Z"
metadata:
  tag: "programming"
---

# DuckDB 2.0 alpha's triggers cost three times more per row than per statement

> Source: devto | Category: news | 2026-10-15T21:37:11Z

I benchmarked DuckDB 2.0 alpha's new triggers on a 500,000-row insert: row-level triggers cost about 3x a plain insert, statement-level ones with transition tables cost about 1.3x. Half the documented trigger matrix isn't implemented yet.

Reactions: 5
