---
title: "`shutdown -h now` destroyed 13 of our 48 Ceph OSDs. Here is how we got the data back"
url: "https://dev.to/anderson_leite/shutdown-h-now-destroyed-13-of-our-48-ceph-osds-here-is-how-we-got-the-data-back-4ali"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-03T02:04:46Z"
metadata:
  tag: "devops"
---

# `shutdown -h now` destroyed 13 of our 48 Ceph OSDs. Here is how we got the data back

> Source: devto | Category: news | 2026-11-03T02:04:46Z

A planned power-down killed the RocksDB index on 13 OSDs. Every supported repair tool refused to run, because each one opens the database it is supposed to repair. This is what worked.

Reactions: 0
