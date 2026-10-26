---
title: "StartsWith Was Asking ICU Every Time"
url: "https://dev.to/ssukhpinder/startswith-was-asking-icu-every-time-58m7"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-26T18:54:28Z"
metadata:
  tag: "programming"
---

# StartsWith Was Asking ICU Every Time

> Source: devto | Category: news | 2026-10-26T18:54:28Z

The default StartsWith and IndexOf overloads compare text the culture-aware way, through ICU, not the literal char match you probably meant. I benchmarked the gap on two million lines and found IndexOf was the one quietly costing me.

Reactions: 0
