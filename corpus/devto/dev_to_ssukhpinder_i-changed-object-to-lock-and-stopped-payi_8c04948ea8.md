---
title: "I Changed object to Lock and Stopped Paying the Monitor Tax"
url: "https://dev.to/ssukhpinder/i-changed-object-to-lock-and-stopped-paying-the-monitor-tax-4486"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-05T09:55:42Z"
metadata:
  tag: "programming"
---

# I Changed object to Lock and Stopped Paying the Monitor Tax

> Source: devto | Category: news | 2026-11-05T09:55:42Z

The .NET 9 System.Threading.Lock type lets the same lock keyword skip Monitor. I benchmarked it: about 13% faster uncontended for a one-word field change, plus the caveat that it's still not for async.

Reactions: 0
