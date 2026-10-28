---
title: "[infoq] Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope"
url: "https://www.infoq.com/news/2026/10/workers-kv-instant/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-28T13:50:36Z"
metadata:
  {}
---

# [infoq] Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope

> Source: engineering | Category: engineering | 2026-10-28T13:50:36Z

Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope

Cloudflare has put Quicksilver, the internal key-value store behind nearly every request it serves, into private beta as a Workers KV mode. Reads resolve in 1.62 ms at p99 against 287 ms for classic KV. The constraints decide the use case: 10,000 keys, one megabyte per namespace, and one write per namespace per second.   By Steef-Jan Wiggers
