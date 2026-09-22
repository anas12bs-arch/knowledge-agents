---
title: "The CoreDNS Black Hole: how one dead DNS pod broke our API gateway"
url: "https://dev.to/akarshan/the-coredns-black-hole-how-one-dead-dns-pod-broke-our-api-gateway-4hh3"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-22T05:29:43Z"
metadata:
  tag: "devops"
---

# The CoreDNS Black Hole: how one dead DNS pod broke our API gateway

> Source: devto | Category: news | 2026-09-22T05:29:43Z

Our gateway 503'd a third of all requests, at random, until we restarted it. The cause was a single open socket pointing at a pod that no longer existed.

Reactions: 2
