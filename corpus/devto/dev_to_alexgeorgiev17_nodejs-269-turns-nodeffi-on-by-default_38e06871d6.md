---
title: "Node.js 26.9 turns node:ffi on by default at 37 nanoseconds a call"
url: "https://dev.to/alexgeorgiev17/nodejs-269-turns-nodeffi-on-by-default-at-37-nanoseconds-a-call-ngj"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-18T15:04:21Z"
metadata:
  tag: "devops"
---

# Node.js 26.9 turns node:ffi on by default at 37 nanoseconds a call

> Source: devto | Category: news | 2026-09-18T15:04:21Z

Node.js 26.9 enables node:ffi by default. I measured a trivial FFI call at 37ns against 35ns for a compiled N-API addon and 3ns for plain JS, then found where it helps, where it silently corrupts data, and where it segfaults.

Reactions: 12
