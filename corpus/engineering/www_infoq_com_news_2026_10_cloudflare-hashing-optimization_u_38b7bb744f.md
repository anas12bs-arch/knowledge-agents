---
title: "[infoq] Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing"
url: "https://www.infoq.com/news/2026/10/cloudflare-hashing-optimization/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-24T23:38:20Z"
metadata:
  {}
---

# [infoq] Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing

> Source: engineering | Category: engineering | 2026-10-24T23:38:20Z

Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing

Cloudflare recently documented how it reduced the memory footprint of its internal load-balancing service by more than 100 TB by optimizing the Rust implementation of consistent hashing in pingora-ketama. The changes compacted hash-ring entries and used statistical analysis of hash distribution and collision rates to reduce the number of hashes per backend by about 90%.   By Renato Losio
