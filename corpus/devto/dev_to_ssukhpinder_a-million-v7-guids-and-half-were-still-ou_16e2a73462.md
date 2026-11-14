---
title: "A Million v7 GUIDs and Half Were Still Out of Order"
url: "https://dev.to/ssukhpinder/a-million-v7-guids-and-half-were-still-out-of-order-20k6"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-14T14:46:05Z"
metadata:
  tag: "programming"
---

# A Million v7 GUIDs and Half Were Still Out of Order

> Source: devto | Category: news | 2026-11-14T14:46:05Z

I switched a table to Guid.CreateVersion7() keys for the time-ordering, then benchmarked whether they actually come out sorted. In a tight loop they do not, and here is why.

Reactions: 1
