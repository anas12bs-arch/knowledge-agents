---
title: "Stop Formatting Currency With Regex. `Intl.NumberFormat` Does It."
url: "https://dev.to/parsajiravand/stop-formatting-currency-with-regex-intlnumberformat-does-it-220b"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-20T12:00:03Z"
metadata:
  tag: "programming"
---

# Stop Formatting Currency With Regex. `Intl.NumberFormat` Does It.

> Source: devto | Category: news | 2026-10-20T12:00:03Z

A hand-rolled formatMoney() with toFixed() and a comma regex looks fine in a US demo and quietly breaks the moment a real user, a negative balance, or a non-dollar locale shows up. Intl.NumberFormat has handled all of it, built into every modern browser, since before most teams' codebases existed.

Reactions: 6
