---
title: "[infoq] Article: Removing a Hidden Round Trip from a Multi-Region AWS API"
url: "https://www.infoq.com/articles/aws-multi-region-signing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-13T13:05:37Z"
metadata:
  {}
---

# [infoq] Article: Removing a Hidden Round Trip from a Multi-Region AWS API

> Source: engineering | Category: engineering | 2026-07-13T13:05:37Z

Article: Removing a Hidden Round Trip from a Multi-Region AWS API

When a series of regional outages forced a rethink of a multi-region AWS API, the team discovered that an obstacle to global failover was hiding in plain sight: a pre-flight discovery call baked into every client session years earlier as the only available option. This article describes what it took to remove it, and what the rollout actually cost.   By Suresh Gururajan
