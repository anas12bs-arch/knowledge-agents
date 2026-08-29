---
title: "Docker Says 'Healthy' and the Pod Keeps Sending Broken Traffic"
url: "https://dev.to/jtorchia/docker-says-healthy-and-the-pod-keeps-sending-broken-traffic-ghj"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-08-29T03:47:51Z"
metadata:
  tag: "devops"
---

# Docker Says "Healthy" and the Pod Keeps Sending Broken Traffic

> Source: devto | Category: news | 2026-08-29T03:47:51Z

Docker's HEALTHCHECK is information, not a routing guarantee. If Kubernetes or Swarm isn't reading it, your container can be "healthy" and still keep taking requests that are going to fail.

Reactions: 2
