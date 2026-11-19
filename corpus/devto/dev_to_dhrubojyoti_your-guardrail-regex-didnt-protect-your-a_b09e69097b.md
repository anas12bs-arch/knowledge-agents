---
title: "Your guardrail regex didn't protect your agent. It froze your entire Python event loop."
url: "https://dev.to/dhrubojyoti/your-guardrail-regex-didnt-protect-your-agent-it-froze-your-entire-python-event-loop-4k4h"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-11-19T12:28:43Z"
metadata:
  tag: "python"
---

# Your guardrail regex didn't protect your agent. It froze your entire Python event loop.

> Source: devto | Category: news | 2026-11-19T12:28:43Z

Pydantic AI v2.70.0 and pydantic-ai-harness 0.70.0 patched two high-severity ReDoS advisories (GHSA-5m5q-5qj4-gx9h, GHSA-m4cr-m4qc-9hh3) where synchronous regexes blocked the asyncio event loop before size limits ran.

Reactions: 1
