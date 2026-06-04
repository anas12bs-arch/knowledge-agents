---
title: "[infoq] 30+ Updates per Second per Account: Uber Scales Ledger Processing with Batching"
url: "https://www.infoq.com/news/2026/06/uber-payment-batching-system/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-04T18:36:34Z"
metadata:
  {}
---

# [infoq] 30+ Updates per Second per Account: Uber Scales Ledger Processing with Batching

> Source: engineering | Category: engineering | 2026-06-04T18:36:34Z

30+ Updates per Second per Account: Uber Scales Ledger Processing with Batching

Uber introduced a high-throughput financial ledger processing system designed to handle hot account write contention at scale. Using 250ms batching, Redis coordination, and optimistic atomic updates, the system supports 30+ updates per second per account while preserving consistency and auditability, reducing multi-hour processing pipelines to minutes in its distributed accounting infrastructure.   By Leela Kumili
