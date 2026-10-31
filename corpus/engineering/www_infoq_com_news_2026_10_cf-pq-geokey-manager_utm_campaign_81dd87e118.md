---
title: "[infoq] Cloudflare’s Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption"
url: "https://www.infoq.com/news/2026/10/cf-pq-geokey-manager/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-31T23:35:30Z"
metadata:
  {}
---

# [infoq] Cloudflare’s Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption

> Source: engineering | Category: engineering | 2026-10-31T23:35:30Z

Cloudflare’s Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption

Cloudflare has moved a post-quantum rebuild of GeoKey Manager into closed beta, guarding geo-fenced keys with hybrid ML-KEM-768 and X25519 instead of the attribute-based encryption used since 2022. Keys live only in kernel memory on verified regional servers, and any failed check rejects the request, a fail-closed choice practitioners ask could cause a regional outage. GA is planned for Q1 2027.   By Steef-Jan Wiggers
