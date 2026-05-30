---
title: "[kubernetes] Kubernetes v1.36: Advancing Workload-Aware Scheduling"
url: "https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.36: Advancing Workload-Aware Scheduling

> Source: devops | Category: infrastructure | 2026-05-30T15:08:37Z

Kubernetes v1.36: Advancing Workload-Aware Scheduling

AI/ML and batch workloads introduce unique scheduling challenges that go beyond simple Pod-by-Pod scheduling.
In Kubernetes v1.35, we introduced the first tranche of  workload-aware scheduling  improvements,
featuring the foundational Workload API alongside basic  gang scheduling  support built on a Pod-based framework,
and an  opportunistic batching  feature to efficiently process identical Pods. 
 Kubernetes v1.36 introduces a significant architectural evolution by cleanly separating API concerns:
the Workload API acts as a static template, while the new PodGroup API handles the runtime state.
To support this, the  kube-scheduler  features a new  PodGroup scheduling cycle  that enables atomic workload processing
and paves the way for future enhancements. This release also debuts the first iterations of  topology-aware scheduling 
and  workload-aware preemption  to advance scheduling capabilities. Additionally,
 ResourceClaim support for workloads  unlocks  Dynamic Resource Allocation
( DRA )  for PodGroups. Finally,
to demonstrate real-world readiness, v1.36 delivers the first phase of integration between the Job controller and the new API. 
 Workload and PodGroup API updates    The Workload API now serves as a static template, while the new PodGroup API describes the runtime object.
Kubernetes v1.36 introduces the Workload and PodGroup APIs as part of the
 scheduling.k8s.io/v1alpha2   API group ,
completely replacing the previous  v1alpha1  API version. 
 In v1.35, Pod groups and their runtime states were embedded within the Workload resource.
The new model decouples these concepts: the Workload now serves as a static template object,
while the PodGroup manages the runtime state. This separation also improves performance and scalability
as the PodGroup API allows per-replica sharding of status updates. 
 Because the Workload API acts merely as a template, the  kube-scheduler 's logic is streamlined.
The scheduler can directly read the PodGroup, which contains a
