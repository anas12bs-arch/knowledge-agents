---
title: "[infoq] How Uber Builds Zone-Failure-Resilient OpenSearch Clusters"
url: "https://www.infoq.com/news/2026/07/uber-opensearch-zone-failure/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-17T10:12:19Z"
metadata:
  {}
---

# [infoq] How Uber Builds Zone-Failure-Resilient OpenSearch Clusters

> Source: engineering | Category: engineering | 2026-07-17T10:12:19Z

How Uber Builds Zone-Failure-Resilient OpenSearch Clusters

Uber explained how it keeps its OpenSearch deployments running during a zone outage. It does this by using OpenSearch's built-in shard allocation and its own isolation-group system, which relies on the Odin container orchestration platform. This way, it maintains both query and ingestion capabilities.   By Claudio Masolo
