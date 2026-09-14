---
title: "[infoq] Agoda Replaces 72-Shard SQL Server Price Cache with DragonflyDB"
url: "https://www.infoq.com/news/2026/09/agoda-price-cache-dragonflydb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-14T18:44:46Z"
metadata:
  {}
---

# [infoq] Agoda Replaces 72-Shard SQL Server Price Cache with DragonflyDB

> Source: engineering | Category: engineering | 2026-09-14T18:44:46Z

Agoda Replaces 72-Shard SQL Server Price Cache with DragonflyDB

Agoda migrated its 1.5 TB hotel Price Cache from 72 SQL Server shards to DragonflyDB to handle growing read and write volumes. The migration used staged dual reads, parity validation, gradual traffic shifting, and decentralized failover detection. Agoda reports an approximately eightfold reduction in P99 read latency, with two DragonflyDB clusters providing high availability.   By Leela Kumili
