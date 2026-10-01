---
title: "A Kubernetes rolling update with maxUnavailable: 0 still drops requests"
url: "https://dev.to/remdore/a-kubernetes-rolling-update-with-maxunavailable-0-still-drops-requests-17jc"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-01T16:26:10Z"
metadata:
  tag: "devops"
---

# A Kubernetes rolling update with maxUnavailable: 0 still drops requests

> Source: devto | Category: news | 2026-10-01T16:26:10Z

Four replicas, maxUnavailable 0, graceful shutdown and a preStop hook. Still 20 dropped connections per deploy. The timing data showed the failures were nowhere near where I assumed.

Reactions: 5
