---
title: "[kubernetes] Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta"
url: "https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-16T01:40:52Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta

> Source: devops | Category: infrastructure | 2026-09-16T01:40:52Z

Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta

With the release of Kubernetes v1.37, the  Pod-Level Resource Managers 
feature has graduated to  Beta  status (disabled by default)! 
 First introduced as an Alpha feature in
 Kubernetes v1.36 ,
this enhancement builds on
 Pod-Level Resources  by
equipping Kubelet's Topology Manager, CPU Manager, and Memory Manager to use
Pod-level resource declarations ( .spec.resources ) directly when making
hardware placement decisions. 
 Bringing pod-level resources to node managers    Before this feature, obtaining exclusive NUMA-aligned CPU cores or memory for
latency-critical applications forced cluster operators into an all-or-nothing
choice: assign integer resource requests to  every  container in the Pod, or
forfeit exclusive NUMA alignment entirely. For modern workloads running
lightweight sidecars (such as logging agents or telemetry exporters), allocating
dedicated physical cores to auxiliary containers was wasteful. 
 Pod-Level Resource Managers solves this challenge by enabling hybrid allocation
models. The Kubelet can reserve exclusive NUMA-aligned resources for primary
application containers while placing non-Guaranteed sidecars into a pod-isolated
shared pool. This ensures primary workloads get unthrottled, NUMA-local
performance while sidecars benefit from running in a pod-isolated shared pool,
enjoying local NUMA alignment and protection from external node interference
without consuming dedicated physical cores. 
 What's new in Beta    Graduating to Beta brings key operational and API enhancements: 
 
  Graduation to Beta:  Controlled by the  PodLevelResourceManagers  feature
gate, available to opt in (disabled by default) in Kubernetes v1.37. 
  PodResources API Reporting:  The  v1  PodResources gRPC service
( PodResourcesLister ) introduces top-level  cpu_ids  and  memory  fields on
 PodResources  responses. Monitoring tools and device plugins can query
pod-level exclusive assignments directly without double-counting container
allocations. 
 
 Getting starte
