---
title: "[infoq] Uber Automates Dependency Analysis Across Its Service Mesh"
url: "https://www.infoq.com/news/2026/10/uber-automated-dependency/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-16T21:51:09Z"
metadata:
  {}
---

# [infoq] Uber Automates Dependency Analysis Across Its Service Mesh

> Source: engineering | Category: engineering | 2026-10-16T21:51:09Z

Uber Automates Dependency Analysis Across Its Service Mesh

Uber has developed an automated dependency analysis system that uses RPC middleware and production metrics to correlate caller and downstream failures. The approach classifies dependencies as fail-close, fail-open, or unknown and addresses limitations of sampled distributed tracing for rare failures across Uber’s large service mesh.   By Leela Kumili
