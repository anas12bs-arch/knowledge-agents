---
title: "[kubernetes] Kubernetes v1.37: Advancing Workload-Aware Scheduling"
url: "https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-09T00:27:08Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Advancing Workload-Aware Scheduling

> Source: devops | Category: infrastructure | 2026-09-09T00:27:08Z

Kubernetes v1.37: Advancing Workload-Aware Scheduling

AI/ML and complex batch workloads continue to push the boundaries of Kubernetes scheduling. Following the foundational workload-centric enhancements introduced in previous releases, Kubernetes v1.37 delivers the next major milestone in the Workload-Aware Scheduling (WAS) journey. In this release, the core Workload and PodGroup APIs—enabling gang scheduling—along with Workload-Aware Preemption (WAP) and shared DRA ResourceClaims for PodGroups, all graduate to Beta, solidifying their role in the Kubernetes ecosystem. 
 To address the hierarchical scheduling requirements of modern high-performance distributed workloads, v1.37 introduces the new  CompositePodGroup  API.
This new API allows expressing multi-level topology constraints, gang scheduling, and preemption policies for complex, heterogeneous groups of Pods. Crucially, this architectural expansion unlocks native scheduling support for advanced workload structures commonly managed by higher-order extension APIs such as JobSet and LeaderWorkerSet (LWS). 
 Alongside these API additions, v1.37 focuses on streamlining adoption by introducing a new set of  controller integration APIs  and the  workloadbuilder  Go library. These provide standardized building blocks that significantly simplify how out-of-tree controllers can integrate with WAS capabilities.
Utilizing these new tools, the native Job controller integration has been upgraded to fully consume the expanded WAS APIs—enabling advanced scheduling policies, flexible disruption modes, and topology-aware scheduling for standard batch workloads. 
 Gang scheduling and Workload / PodGroup APIs    Kubernetes v1.37 delivers a major milestone:  Workload  /  PodGroup  APIs and  gang scheduling 
are officially graduating to Beta. This graduation signals that native, &quot;all-or-nothing&quot;
scheduling for workloads is solidifying for wider adoption. 
 Key updates to the API and gang scheduling algorithm in this release include: 
 Beta graduation and API versioning cha
