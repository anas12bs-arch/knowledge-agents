---
title: "[kubernetes] Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used (Beta)"
url: "https://kubernetes.io/blog/2026/09/21/kubernetes-v1-37-pvc-last-used-time/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-21T22:14:06Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used (Beta)

> Source: devops | Category: infrastructure | 2026-09-21T22:14:06Z

Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used (Beta)

Kubernetes v1.37 promotes the  PersistentVolumeClaimUnusedSinceTime  feature gate to Beta (enabled by
default). With this feature, the PersistentVolumeClaim (PVC) protection controller adds an  Unused 
condition to each PVC, telling you whether any running pod currently references it — no custom
tooling or cross-referencing required. 
 For the API definition of PVC conditions, see the
 PersistentVolumeClaim API reference .
Read on to learn how the  Unused  condition works and how to use it. 
 Why track PVC usage?    In large-scale Kubernetes clusters, it is common for users to create PVCs and then delete the
associated pods without cleaning up the storage, because Kubernetes does not automatically delete
PVCs when their pods are removed (to protect against accidental data loss). Over time, these
 orphaned  PVCs may accumulate, silently consuming storage capacity and driving up cloud costs. 
 Before Kubernetes v1.37, it was easy to identify an unused PersistentVolume, but much harder to
determine whether a PVC was still being used. Doing so required cross-referencing pods,
PersistentVolumes, and PVCs over a potentially large window of time. Administrators often resorted
to custom monitoring pipelines or scripts to answer a seemingly simple question:
 &quot;Is anything actually using this volume?&quot;  
 The  PersistentVolumeClaimUnusedSinceTime  feature solves this by making the answer available
natively in the PVC status. Once the feature is enabled, every PVC gets an  Unused  condition managed
by the PVC protection controller. 
 User stories    
  Storage administrator : &quot;I want to know which PVCs in my cluster are not being used by any pod
so I can safely identify orphaned volumes and schedule them for deletion.&quot; 
  DevOps engineer : &quot;I want to list PVCs that have the  Unused  condition set to  True  so I
can automate cleanup in development environments.&quot; 
 
 How does it work?    The PVC protection controller — which already watches pods to
