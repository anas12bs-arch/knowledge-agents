---
title: "[infoq] How Netflix Scaled Its Real-Time Service Map"
url: "https://www.infoq.com/news/2026/08/netflix-service-topology/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-08-11T12:34:19Z"
metadata:
  {}
---

# [infoq] How Netflix Scaled Its Real-Time Service Map

> Source: engineering | Category: engineering | 2026-08-11T12:34:19Z

How Netflix Scaled Its Real-Time Service Map

Netflix has described how it redesigned the streaming pipeline behind Service Topology, its real-time service dependencies map, to support production scale. The system uses three stages to separate intermediary resolution from enrichment and persistence, propagates backpressure to Kafka rather than dropping records, and uses server-sent events instead of gRPC for high-volume internal transfers.   By Eran Stiller
