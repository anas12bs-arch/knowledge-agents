---
title: "Docker Reported Exit 0. The Kernel Had Already OOM-Killed It."
url: "https://dev.to/hoelee/docker-reported-exit-0-the-kernel-had-already-oom-killed-it-2ojp"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-24T23:38:29Z"
metadata:
  tag: "devops"
---

# Docker Reported Exit 0. The Kernel Had Already OOM-Killed It.

> Source: devto | Category: news | 2026-10-24T23:38:29Z

A container on my NAS kept stopping unexpectedly while Docker reported exit 0 and OOMKilled=false. The honest evidence was in dmesg: six cgroup OOM kills.

Reactions: 1
