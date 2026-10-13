---
title: "Changing def to async def let one blocking call freeze an entire FastAPI app"
url: "https://dev.to/remdore/changing-def-to-async-def-let-one-blocking-call-freeze-an-entire-fastapi-app-4cjd"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-13T22:00:18Z"
metadata:
  tag: "webdev"
---

# Changing def to async def let one blocking call freeze an entire FastAPI app

> Source: devto | Category: news | 2026-10-13T22:00:18Z

The same requests.get was harmless in a def endpoint and froze the server in an async def one: an unrelated endpoint went from 1.6 ms to 34 seconds. Plus FastAPI's 40-thread cliff, why asyncio.to_thread barely helps CPU work, and a watchdog that names the blocking line.

Reactions: 13
