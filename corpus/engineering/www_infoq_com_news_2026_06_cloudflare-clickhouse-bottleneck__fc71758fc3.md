---
title: "[infoq] Cloudflare Identifies Query Planning Bottleneck in ClickHouse"
url: "https://www.infoq.com/news/2026/06/cloudflare-clickhouse-bottleneck/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-06T08:16:21Z"
metadata:
  {}
---

# [infoq] Cloudflare Identifies Query Planning Bottleneck in ClickHouse

> Source: engineering | Category: engineering | 2026-06-06T08:16:21Z

Cloudflare Identifies Query Planning Bottleneck in ClickHouse

Cloudflare recently described how a slowdown in its billing pipeline was traced to contention inside the query planning stage of ClickHouse. The team profiled the bottleneck and patched ClickHouse to replace an exclusive lock with a shared lock, drop the per-query copy of the parts list, and improve part filtering.   By Renato Losio
