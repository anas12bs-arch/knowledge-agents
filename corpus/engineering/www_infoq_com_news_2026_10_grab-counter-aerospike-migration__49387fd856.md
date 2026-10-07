---
title: "[infoq] Grab Redesigns Counter Service Storage for 50% Lower P99 Latency"
url: "https://www.infoq.com/news/2026/10/grab-counter-aerospike-migration/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-07T16:21:18Z"
metadata:
  {}
---

# [infoq] Grab Redesigns Counter Service Storage for 50% Lower P99 Latency

> Source: engineering | Category: engineering | 2026-10-07T16:21:18Z

Grab Redesigns Counter Service Storage for 50% Lower P99 Latency

Grab migrated its high-volume Counter Service from a wide column database to Aerospike using storage abstraction, shadow traffic, data parity validation, and gradual traffic migration. The redesigned data model consolidated time buckets into map-based records. Grab reports about 50% lower production p99 read latency, 1 TB versus 3 TB of disk usage, and 45% to 50% lower cost per node.   By Leela Kumili
