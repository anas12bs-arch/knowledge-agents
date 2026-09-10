---
title: "nginx will proxy the new HTTP QUERY method. It will never cache one."
url: "https://dev.to/remdore/nginx-will-proxy-the-new-http-query-method-it-will-never-cache-one-3f8i"
source: "devto"
category: "news"
tags: ["devto", "ai", "tech-article"]
date: "2026-09-10T11:45:25Z"
metadata:
  tag: "ai"
---

# nginx will proxy the new HTTP QUERY method. It will never cache one.

> Source: devto | Category: news | 2026-09-10T11:45:25Z

RFC 10008 made QUERY explicitly cacheable. I built a QUERY-only API and found nginx forwards it happily and caches it never: four identical QUERY requests hit the backend four times, four POSTs hit it once.

Reactions: 11
