---
title: "[infoq] Article: Two Misconfigurations That Caused Spark OOM Failures on Kubernetes"
url: "https://www.infoq.com/articles/spark-oom-kubernetes-misconfigurations/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-03T15:57:37Z"
metadata:
  {}
---

# [infoq] Article: Two Misconfigurations That Caused Spark OOM Failures on Kubernetes

> Source: engineering | Category: engineering | 2026-06-03T15:57:37Z

Article: Two Misconfigurations That Caused Spark OOM Failures on Kubernetes

After migrating Spark pipelines to Azure Kubernetes Service, two infrastructure settings interacted destructively: spark.kubernetes.local.dirs.tmpfs=true backed shuffle spill with RAM instead of disk, and a hard podAffinity rule forced all executors onto one node. Together, they caused repeated OOM kills invisible to standard diagnostics.   By Pranav Bhasker
