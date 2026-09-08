---
title: "Stop rebuilding from scratch: cache Docker layers on Cloud Build"
url: "https://dev.to/gde/stop-rebuilding-from-scratch-cache-docker-layers-on-cloud-build-41m0"
source: "devto"
category: "news"
tags: ["devto", "python", "tech-article"]
date: "2026-09-08T04:58:03Z"
metadata:
  tag: "python"
---

# Stop rebuilding from scratch: cache Docker layers on Cloud Build

> Source: devto | Category: news | 2026-09-08T04:58:03Z

Cloud Build runs on ephemeral workers, so your Docker cache vanishes on every run. Here's how to persist it in Artifact Registry with BuildKit's registry cache — uv stops re-downloading dependencies, builds get faster, greener and cheaper.

Reactions: 1
