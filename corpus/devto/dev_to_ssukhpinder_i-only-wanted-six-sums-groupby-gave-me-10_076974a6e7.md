---
title: "I Only Wanted Six Sums. GroupBy Gave Me 100 MB"
url: "https://dev.to/ssukhpinder/i-only-wanted-six-sums-groupby-gave-me-100-mb-4p4"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-31T12:53:08Z"
metadata:
  tag: "programming"
---

# I Only Wanted Six Sums. GroupBy Gave Me 100 MB

> Source: devto | Category: news | 2026-10-31T12:53:08Z

I used GroupBy().ToDictionary() to get six per-region totals and it allocated 100 MB. AggregateBy, the LINQ method that shipped in .NET 9, does the same job in one pass for about a kilobyte. Here are the measured numbers and the honest caveat.

Reactions: 0
