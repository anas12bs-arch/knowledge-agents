---
title: "Docker Engine 29.8's --umask flag fixes permissions docker exec used to reset"
url: "https://dev.to/alexgeorgiev17/docker-engine-298s-umask-flag-fixes-permissions-docker-exec-used-to-reset-edj"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-23T16:59:17Z"
metadata:
  tag: "devops"
---

# Docker Engine 29.8's --umask flag fixes permissions docker exec used to reset

> Source: devto | Category: news | 2026-09-23T16:59:17Z

Docker Engine 29.8 added a native --umask flag. I measured the entrypoint-script workaround it replaces: correct on the main process (640) but silently wrong under docker exec and healthchecks (644), a gap the new flag closes across both.

Reactions: 13
