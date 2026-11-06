---
title: "I Stamped Every Row With DateTime.Now and Paid Twice"
url: "https://dev.to/ssukhpinder/i-stamped-every-row-with-datetimenow-and-paid-twice-4fcg"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-06T10:01:06Z"
metadata:
  tag: "programming"
---

# I Stamped Every Row With DateTime.Now and Paid Twice

> Source: devto | Category: news | 2026-11-06T10:01:06Z

DateTime.Now is DateTime.UtcNow plus a trip through your local time zone rules, and that trip isn't free in a hot loop. I counted: on a box with a real time zone it roughly doubles the cost of reading the clock.

Reactions: 0
