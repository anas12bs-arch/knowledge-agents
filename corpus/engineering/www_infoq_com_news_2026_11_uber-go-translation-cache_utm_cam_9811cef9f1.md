---
title: "[infoq] Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS"
url: "https://www.infoq.com/news/2026/11/uber-go-translation-cache/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-20T17:55:09Z"
metadata:
  {}
---

# [infoq] Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS

> Source: engineering | Category: engineering | 2026-11-20T17:55:09Z

Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS

Uber redesigned its Go-based translation cache to reduce its initial memory footprint by more than 90% while maintaining a cache hit rate above 99.9% and p99 disk-backed cache miss latency below 100 microseconds. The hybrid architecture combines in-memory keys and frequently accessed values with disk-backed storage, reducing garbage-collection overhead and memory consumption.   By Leela Kumili
