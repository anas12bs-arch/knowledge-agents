---
title: "Deno 2.6's minimum dependency age flag ignores year and month durations"
url: "https://dev.to/alexgeorgiev17/deno-26s-minimum-dependency-age-flag-ignores-year-and-month-durations-1ac5"
source: "devto"
category: "news"
tags: ["devto", "javascript", "tech-article"]
date: "2026-09-17T18:39:38Z"
metadata:
  tag: "javascript"
---

# Deno 2.6's minimum dependency age flag ignores year and month durations

> Source: devto | Category: news | 2026-09-17T18:39:38Z

I tested Deno 2.6's --min-dep-age flag against 20 popular npm packages: a 30-day policy held back 12 of them, including a full major-version rollback for vitest, but the same flag silently does nothing when given a duration in months or years.

Reactions: 12
