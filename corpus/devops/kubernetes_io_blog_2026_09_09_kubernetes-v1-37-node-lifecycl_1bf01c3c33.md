---
title: "[kubernetes] Kubernetes v1.37: Introducing Node Lifecycle Conditions"
url: "https://kubernetes.io/blog/2026/09/09/kubernetes-v1-37-node-lifecycle-conditions/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-10T01:34:05Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Introducing Node Lifecycle Conditions

> Source: devops | Category: infrastructure | 2026-09-10T01:34:05Z

Kubernetes v1.37: Introducing Node Lifecycle Conditions

Kubernetes has many ways to describe what is happening on a Node. Readiness,
taints, Pod state, labels, annotations, and provider-specific APIs each expose
part of the picture. What has been missing is a shared, Kubernetes-owned way to
say that a Node is  draining ,
undergoing maintenance, or undergoing  Graceful Node Shutdown . 
 Kubernetes v1.37 introduces five well-known  Node conditions 
that provide that description: 
 
  DrainInProgress  
  Drained  
  MaintenancePlanned  
  MaintenanceInProgress  
  GracefulNodeShutdownInProgress  
 
 The new Node lifecycle conditions    
 
 
 Condition 
 What it reports 
 
 
 
 
  DrainInProgress  
 The Node is actively being drained according to the administrator's chosen drain criteria. 
 
 
  Drained  
 The Node has reached the drain criteria selected by the administrator. 
 
 
  MaintenancePlanned  
 The Node is expected to undergo a change in the future. 
 
 
  MaintenanceInProgress  
 The Node is actively undergoing maintenance. 
 
 
  GracefulNodeShutdownInProgress  
 Graceful Node Shutdown is determined to be in progress on the Node. 
 
 
 
 Maintenance can include hardware or software rollout, remediation,
decommissioning, or debugging. Whether maintenance requires a drain depends on
its impact. A Kubernetes upgrade usually should follow a drain, while a kernel
live patch might not need one. 
 Like other Node conditions, each lifecycle condition uses  status  to report
whether the observation is active: 
 
  True : the lifecycle state is currently observed. 
  False : the lifecycle state is not currently observed. 
  Unknown : Kubernetes cannot determine whether the lifecycle state is active. 
 
 The  reason  provides a stable, machine-readable cause for the current status,
and  message  can provide additional human-readable detail. 
 For example, an authorized maintenance controller could publish: 
      # Node .status excerpt  
        status  :  
         conditions  :  
        -  type  :     MaintenancePlanne
