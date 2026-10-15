---
title: "[kubernetes] Why Is My Kubernetes Job Still Pending? Tracing Kueue Admission with Headlamp"
url: "https://kubernetes.io/blog/2026/10/14/tracing-kueue-admission-with-headlamp/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-10-15T05:11:00Z"
metadata:
  {}
---

# [kubernetes] Why Is My Kubernetes Job Still Pending? Tracing Kueue Admission with Headlamp

> Source: devops | Category: infrastructure | 2026-10-15T05:11:00Z

Why Is My Kubernetes Job Still Pending? Tracing Kueue Admission with Headlamp

You submit a  Kubernetes Job  and
wait for its Pods to appear. A minute passes. Then another. The Job is still suspended, there are no
application logs, and there may not even be a Pod to inspect. 
 In a cluster managed by  Kueue , this can be completely normal. Kueue
may still be deciding whether the Job can use the requested resources. The useful question is not
only “Why is the Pod pending?” It is first “Has Kueue admitted the Workload?” 
 The  Kueue plugin for Headlamp  brings that
investigation into the Headlamp UI. Instead of reconstructing the admission path from several
commands and large YAML objects, you can begin with the Workload, read its condition message, and
follow links through the LocalQueue, ClusterQueue, ResourceFlavor, and Cohort. 
 This article follows that Headlamp-first path. The command line appears only in a short optional
section for reproducing the example. 
 Before you begin    You need a Kubernetes cluster with  Kueue installed ,
a  Headlamp installation , and the
  0.1.0-alpha  Kueue plugin .
Your Kubernetes identity must be allowed to read the Kueue resources used in this article. 
 The alpha release provides read-only views for Kueue  v1beta2  Cohorts, ClusterQueues, LocalQueues,
ResourceFlavors, and Workloads. It does not add its own create, edit, stop, resume, or delete
workflows. Headlamp still provides its standard YAML and resource actions where your permissions
allow them. 
 First, separate admission from Pod scheduling    Kueue and the Kubernetes scheduler answer different questions. 
 
 
 Kueue admission: Should this Workload start now, considering queue policy, quota, ResourceFlavors,
admission checks, and other waiting Workloads? 
 
 
 Pod scheduling: After the Workload is admitted and the Job resumes, which nodes can run its Pods? 
 
 
 That boundary changes the investigation. If the Workload is not admitted, stay in the Kueue section
of Headlamp. If it is admitted but its Pods are still  Pending , move to Headlamp's nor
