---
title: "FastAPI's new app.frontend() fixes a route-order bug in manual SPA serving"
url: "https://dev.to/alexgeorgiev17/fastapis-new-appfrontend-fixes-a-route-order-bug-in-manual-spa-serving-4mm8"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-09-20T13:45:40Z"
metadata:
  tag: "webdev"
---

# FastAPI's new app.frontend() fixes a route-order bug in manual SPA serving

> Source: devto | Category: news | 2026-09-20T13:45:40Z

I tested FastAPI 0.138's app.frontend() against the two patterns it replaces. A catch-all route declared before an API route returns HTTP 200 with the wrong body; app.frontend() gets the order right regardless, at the same ~440 req/s.

Reactions: 1
