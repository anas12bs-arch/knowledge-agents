---
title: "[infoq] Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact"
url: "https://www.infoq.com/news/2026/09/uber-m3db-subcluster-sharding/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-21T18:41:28Z"
metadata:
  {}
---

# [infoq] Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact

> Source: engineering | Category: engineering | 2026-09-21T18:41:28Z

Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact

Uber has redesigned shard placement in M3DB with fixed size subclusters to limit the impact of node failures, maintenance, and cluster scaling. The approach bounds shard dependencies, preserves replica isolation, and uses a greedy algorithm to select shard migrations while avoiding a separate rebalancing pass and unnecessary data movement.   By Leela Kumili
