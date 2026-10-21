---
title: "[infoq] Article: Distributed Spring Batch Without a Message Broker"
url: "https://www.infoq.com/articles/spring-batch-without-broker/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-21T11:42:39Z"
metadata:
  {}
---

# [infoq] Article: Distributed Spring Batch Without a Message Broker

> Source: engineering | Category: engineering | 2026-10-21T11:42:39Z

Article: Distributed Spring Batch Without a Message Broker

Distributed Spring Batch partitioning already needs a shared, persistent job repository. This article makes that database the whole coordination plane and drops the message broker, sizing work to the live node count, a per-job master with no standing coordinator, compare-and-set claiming that prevents double-execution, two-phase heartbeat failover, and where a broker is still the right choice.   By Janardhan Reddy Chejarla
