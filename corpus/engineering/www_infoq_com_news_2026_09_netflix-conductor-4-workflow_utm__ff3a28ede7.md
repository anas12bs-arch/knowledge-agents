---
title: "[infoq] Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows"
url: "https://www.infoq.com/news/2026/09/netflix-conductor-4-workflow/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-11T17:22:39Z"
metadata:
  {}
---

# [infoq] Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows

> Source: engineering | Category: engineering | 2026-09-11T17:22:39Z

Netflix Reworks Conductor for 420 Million Monthly Workflow Executions and 10X Larger Workflows

Netflix has reworked its Conductor workflow orchestration engine to handle larger workloads, increasing supported workflow size from about 2,500 to 30,000 tasks and reducing p99 workflow evaluation latency by about 40%. Conductor 4.0 separates workflow metadata from task data, moves evaluation to asynchronous processing, and introduces dynamic worker allocation and concurrency controls.   By Leela Kumili
