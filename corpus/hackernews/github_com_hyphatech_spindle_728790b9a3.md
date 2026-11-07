---
title: "Show HN: Spindle – a full-featured, type-safe web framework for OCaml 5"
url: "https://github.com/hyphatech/spindle"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-11-07T14:25:36Z"
metadata:
  score: "17"
---

# Show HN: Spindle – a full-featured, type-safe web framework for OCaml 5

> Source: hackernews | Category: news | 2026-11-07T14:25:36Z

Score: 17 | Comments: 4

Spindle is a multicore-by-design, eio-native web framework for modern OCaml.<p>Its central idea is to provide an expressive, type-driven API and derive the rest: codecs, request validation, OpenAPI spec and frontend schemas (Zod and Melange). This keeps contracts in sync between server and client without maintaining separate definitions.<p>The framework includes an RFC-strict HTTP server, composable dependencies, WebSockets, SSE and high-level primitives for building MCP servers. It also provides production-ready essentials like distributed tracing, OT-compatible metrics, logging and other features you would expect. Speed was never the goal but the benchmarks show it running x2 faster than NestJS and x5 faster than FastAPI on a single core.<p>Give it a try.<p>Documentation: <a href="https:&#x2F;&#x2F;hyphatech.github.io&#x2F;spindle&#x2F;" rel="nofollow">https:&#x2F;&#x2F;hyphatech.github.io&#x2F;spindle&#x2F;</a>
