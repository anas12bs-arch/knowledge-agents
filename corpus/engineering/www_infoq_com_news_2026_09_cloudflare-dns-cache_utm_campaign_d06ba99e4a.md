---
title: "[infoq] Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache"
url: "https://www.infoq.com/news/2026/09/cloudflare-dns-cache/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-23T16:59:05Z"
metadata:
  {}
---

# [infoq] Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache

> Source: engineering | Category: engineering | 2026-09-23T16:59:05Z

Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache

Cloudflare redesigned the in-memory representation of its Big Pineapple DNS cache, reducing the per-entry footprint by 56% and freeing roughly 100 TB of working-set memory across its fleet. The Rust-based changes also increased cache insertion throughput by 43% and reduced lookup latency by 19%, while enabling Cloudflare to increase cache capacity without additional memory.   By Leela Kumili
