---
title: "[hacker-news-sec] 18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers"
url: "https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-07T13:20:50Z"
metadata:
  {}
---

# [hacker-news-sec] 18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers

> Source: security | Category: security | 2026-08-07T13:20:50Z

18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers

A use-after-free bug in Linux's SCTP networking code can be turned into full root on a host, and Tencent researchers say they used it to escape a container and reach the machine underneath.

The flaw has existed since 2008. The fix already shipped: stable kernels 7.1.6, 6.18.42, 6.12.101 and 6.6.148, released August 3, close it. Anyone running an older kernel with SCTP reachable should update.
