---
title: "Docker Engine 29.9.1 fixes a docker save bug that left deleted layers on disk"
url: "https://dev.to/alexgeorgiev17/docker-engine-2991-fixes-a-docker-save-bug-that-left-deleted-layers-on-disk-516a"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-20T12:00:05Z"
metadata:
  tag: "devops"
---

# Docker Engine 29.9.1 fixes a docker save bug that left deleted layers on disk

> Source: devto | Category: news | 2026-10-20T12:00:05Z

I reproduced a Docker Engine 29.8.2 bug where docker save followed by docker rmi left 100% of a 4.5MB image's layers on disk, confirmed 29.9.1 fixes it, and found no prune command could see the leak on the broken version.

Reactions: 7
