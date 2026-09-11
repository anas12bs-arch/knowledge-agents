---
title: "[kubernetes] Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize (Alpha)"
url: "https://kubernetes.io/blog/2026/09/10/kubernetes-v1-37-scheduler-preemption-for-in-place-pod-resize-alpha/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-11T05:19:42Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize (Alpha)

> Source: devops | Category: infrastructure | 2026-09-11T05:19:42Z

Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize (Alpha)

In Kubernetes, resource allocation has historically been a static decision made during a Pod's initial scheduling and placement. With the graduation of the core  in-Place Pod resize  feature to General Availability in v1.35, application developers and cluster operators gained the powerful ability to dynamically adjust CPU and memory allocations of running containers without incurring disruptive restarts or application downtime. 
 However, in-place resizing introduced a unique resource scheduling gap: if a running Pod requested a resource scale-up that exceeded the host node's allocatable headroom, the Kubelet was forced to mark the request as  Deferred . The Pod would remain parked in this state indefinitely, waiting for resources on the node to naturally free up. 
 To bridge this scheduling gap, Kubernetes v1.37 introduces  scheduler preemption for in-place Pod resize  (Alpha), behind the  InPlacePodVerticalScalingSchedulerPreemption  feature gate.
This feature allows the Kubernetes scheduler to actively free up capacity on a fully-utilized node by preempting lower-priority workloads, enabling the pending in-place resizes of critical, higher-priority applications to succeed. 
 The &quot;deferred&quot; resize challenge    To understand why this preemption mechanism is needed, it is helpful to look at how Kubernetes handles running Pod resizing. When a user or controller (such as the  Vertical Pod Autoscaler ) updates the resource requests of an active container, the Kubelet evaluates whether the underlying node has enough spare allocatable capacity to fulfill the increase. 
 If the node's resources are fully utilized and cannot satisfy the new limits, the Kubelet sets the container's  resizeStatus  (reported in the Pod's  status.containerStatuses[] ) to  Deferred . Unlike an  Infeasible  resize request (which is immediately rejected because it exceeds physical machine boundaries, namespace limit ranges, or admission quotas) a  Deferred  status indicates that the r
