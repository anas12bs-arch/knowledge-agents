---
title: "[infoq] Cursor Uses S3 WAL to Scale Git Storage to More than 300 Pushes per Second"
url: "https://www.infoq.com/news/2026/09/cursor-continuity-git-storage/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-30T23:45:36Z"
metadata:
  {}
---

# [infoq] Cursor Uses S3 WAL to Scale Git Storage to More than 300 Pushes per Second

> Source: engineering | Category: engineering | 2026-09-30T23:45:36Z

Cursor Uses S3 WAL to Scale Git Storage to More than 300 Pushes per Second

Cursor has introduced Continuity, a Git storage architecture that uses an S3 backed write ahead log as the source of truth. The design turns local NVMe repositories into warm caches and separates replica coordination from consistency. Cursor reports linear read scaling with up to 100 replicas and more than 300 pushes per second with S3 Express One Zone in synthetic tests.   By Leela Kumili
