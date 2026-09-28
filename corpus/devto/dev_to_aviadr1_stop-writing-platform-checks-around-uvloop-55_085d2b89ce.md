---
title: "Stop writing platform checks around uvloop"
url: "https://dev.to/aviadr1/stop-writing-platform-checks-around-uvloop-555f"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-09-28T19:26:00Z"
metadata:
  tag: "python"
---

# Stop writing platform checks around uvloop

> Source: devto | Category: news | 2026-09-28T19:26:00Z

uvloop doesn't run on Windows, so cross-platform asyncio code grows an if/else at every entry point. winuvloop replaces that branch with one import.

Reactions: 0
