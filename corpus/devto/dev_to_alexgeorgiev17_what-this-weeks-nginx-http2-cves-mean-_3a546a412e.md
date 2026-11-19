---
title: "What this week's nginx HTTP/2 CVEs mean for the server I actually run"
url: "https://dev.to/alexgeorgiev17/what-this-weeks-nginx-http2-cves-mean-for-the-server-i-actually-run-3nbf"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-19T12:28:43Z"
metadata:
  tag: "devops"
---

# What this week's nginx HTTP/2 CVEs mean for the server I actually run

> Source: devto | Category: news | 2026-11-19T12:28:43Z

I checked Ubuntu 24.04's own nginx package against this week's HTTP/2 RCE advisories: still listed vulnerable with no fix, and the documented mitigation doesn't even parse on it. Disabling HTTP/2 as a stopgap cost 45-70% more time in my own benchmark, up to 4x on a single connection.

Reactions: 11
