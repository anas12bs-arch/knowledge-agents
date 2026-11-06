---
title: "Why Node.js HTTP backpressure must count bytes, not string length"
url: "https://dev.to/ali_ahmed_44ee99051e327ce/why-nodejs-http-backpressure-must-count-bytes-not-string-length-4554"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-11-06T02:55:06Z"
metadata:
  tag: "opensource"
---

# Why Node.js HTTP backpressure must count bytes, not string length

> Source: devto | Category: news | 2026-11-06T02:55:06Z

Node's OutgoingMessage counted buffered strings in UTF-16 code units, so multi-byte bodies were under-counted up to 3× and write() kept saying there was room. My fix, and how I verified it.

Reactions: 1
