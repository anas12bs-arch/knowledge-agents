---
title: "Traefik 3.8's tap middleware triples request latency even with an instant local receiver"
url: "https://dev.to/alexgeorgiev17/traefik-38s-tap-middleware-triples-request-latency-even-with-an-instant-local-receiver-421a"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-09T19:45:29Z"
metadata:
  tag: "devops"
---

# Traefik 3.8's tap middleware triples request latency even with an instant local receiver

> Source: devto | Category: news | 2026-11-09T19:45:29Z

I measured Traefik 3.8.0-rc.1's new tap middleware: it roughly triples per-request latency with a zero-delay receiver, and the overhead is strictly additive, confirmed by matching a 50ms receiver delay to a 100ms latency increase.

Reactions: 7
