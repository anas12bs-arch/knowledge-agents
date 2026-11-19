---
title: "How an emptyDir With medium: Memory Made Our Export Pods OOMKilled While the Heap Sat at 210 MB"
url: "https://dev.to/darshan_turakhia/how-an-emptydir-with-medium-memory-made-our-export-pods-oomkilled-while-the-heap-sat-at-210-mb-1p4n"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-11-19T12:28:41Z"
metadata:
  tag: "programming"
---

# How an emptyDir With medium: Memory Made Our Export Pods OOMKilled While the Heap Sat at 210 MB

> Source: devto | Category: news | 2026-11-19T12:28:41Z

Our report-export pods died with exit code 137 every few hours, but the Node heap never passed 210 MB against a 1 GiB limit. The missing memory was a tmpfs scratch volume that Kubernetes bills to the container

Reactions: 1
