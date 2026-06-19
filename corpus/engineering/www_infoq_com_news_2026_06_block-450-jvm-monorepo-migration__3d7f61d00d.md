---
title: "[infoq] Behind the Scenes:  Block 450 JVM Repositories Into Monorepo to Reduce Dependency Drift"
url: "https://www.infoq.com/news/2026/06/block-450-jvm-monorepo-migration/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-19T18:20:36Z"
metadata:
  {}
---

# [infoq] Behind the Scenes:  Block 450 JVM Repositories Into Monorepo to Reduce Dependency Drift

> Source: engineering | Category: engineering | 2026-06-19T18:20:36Z

Behind the Scenes:  Block 450 JVM Repositories Into Monorepo to Reduce Dependency Drift

Block, Inc. describes migrating ~450 JVM repositories into a monorepo across Cash App and Square engineering to reduce dependency drift and coordination overhead. The system supports ~8,800 weekly builds with ~10 min p90 CI time. The approach improves cross-service changes, build visibility, and developer experience through dependency graph–based builds, selective CI, and custom IDE tooling.   By Leela Kumili
