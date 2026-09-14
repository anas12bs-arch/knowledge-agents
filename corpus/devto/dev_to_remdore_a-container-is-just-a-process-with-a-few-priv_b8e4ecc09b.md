---
title: "A container is just a process with a few private views. I built one in thirty lines."
url: "https://dev.to/remdore/a-container-is-just-a-process-with-a-few-private-views-i-built-one-in-thirty-lines-26di"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-14T18:44:55Z"
metadata:
  tag: "devops"
---

# A container is just a process with a few private views. I built one in thirty lines.

> Source: devto | Category: news | 2026-09-14T18:44:55Z

There is no container object in the Linux kernel. I built a working container by hand with unshare, pivot_root and a cgroup: PID 1 in its own namespaces, host filesystem gone, and a 20MB memory cap the kernel enforced with a SIGKILL.

Reactions: 13
