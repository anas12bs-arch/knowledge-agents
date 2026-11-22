---
title: "How a Local-Timezone Cron Skipped One Hour on the Night the Clocks Went Back and Under-Billed 212 Customers"
url: "https://dev.to/darshan_turakhia/how-a-local-timezone-cron-skipped-one-hour-on-the-night-the-clocks-went-back-and-under-billed-212-127g"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-11-22T12:04:48Z"
metadata:
  tag: "python"
---

# How a Local-Timezone Cron Skipped One Hour on the Night the Clocks Went Back and Under-Billed 212 Customers

> Source: devto | Category: news | 2026-11-22T12:04:48Z

An hourly usage rollup scheduled in America/New_York silently skipped one run when daylight saving ended. Sixty minutes of metered events were never aggregated, and nothing alerted. A reproduction with APScheduler 3.9.1, and the watermark fix.

Reactions: 0
