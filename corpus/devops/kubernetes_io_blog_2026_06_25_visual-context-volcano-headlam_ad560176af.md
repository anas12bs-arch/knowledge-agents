---
title: "[kubernetes] Inspect Volcano workloads faster with Headlamp"
url: "https://kubernetes.io/blog/2026/06/25/visual-context-volcano-headlamp-plugin/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-06-26T08:21:52Z"
metadata:
  {}
---

# [kubernetes] Inspect Volcano workloads faster with Headlamp

> Source: devops | Category: infrastructure | 2026-06-26T08:21:52Z

Inspect Volcano workloads faster with Headlamp

Volcano  is a cloud native batch scheduler for Kubernetes, built for high-performance computing, AI/ML, and other batch workloads. 
  Headlamp  is an extensible Kubernetes web UI. With its plugin system, Headlamp can surface APIs and workflows beyond the built-in Kubernetes resources. The Volcano plugin brings core Volcano resources into Headlamp so you can inspect workload state, queue behavior, and gang scheduling details in one place. 
 Kubernetes was originally designed around long-running services, where applications are expected to start and remain available over time. Batch, AI/ML, and HPC workloads often behave differently: jobs arrive dynamically, compete for limited resources, and may need multiple workers to start together before useful work can begin. 
 Volcano extends Kubernetes with concepts such as queues, priorities, quotas, and gang scheduling. Instead of treating every Pod independently, Volcano schedules workloads with awareness of the job as a whole and the resources it needs to make progress. 
 To make these workloads easier to operate and troubleshoot, the Volcano plugin brings that scheduling context directly into Headlamp. 
 Watch this short walkthrough to see the Volcano plugin in Headlamp: 
 
  
 
 Visual context helps teams understand Volcano jobs, queues, and PodGroups faster    Working with Volcano often means moving across several related resources while trying to understand a batch workload. You might start with a Job, then look at the related PodGroup, inspect the Pods behind it, check the Queue, and finally return to the Job again. All of that is possible with CLI tools like  kubectl  and the Volcano CLI, but it can become fragmented very quickly. 
 The Volcano plugin for Headlamp makes that workflow easier by bringing the key resources together in a single UI. Instead of reconstructing relationships manually, you can move directly between Jobs, Queues, PodGroups, Pods, and events from the same interface. 
 Volcano introduces its
