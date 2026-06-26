---
title: "[kubernetes] Introducing the Cluster API plugin for Headlamp"
url: "https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-06-26T08:21:52Z"
metadata:
  {}
---

# [kubernetes] Introducing the Cluster API plugin for Headlamp

> Source: devops | Category: infrastructure | 2026-06-26T08:21:52Z

Introducing the Cluster API plugin for Headlamp

Headlamp  is an open-source, extensible Kubernetes SIG UI
project designed to let you explore, manage, and debug cluster resources directly
from a browser. 
  Cluster API (CAPI)  is a Kubernetes sub-project
that brings declarative, Kubernetes-style APIs to cluster lifecycle management. It
lets platform teams provision, upgrade, and manage the lifecycle of Kubernetes
clusters using standard Kubernetes objects stored and reconciled in a management
cluster. 
 Managing Cluster API resources has historically required raw  kubectl  commands and
deep familiarity with ownership hierarchies. The Headlamp Cluster API plugin brings
visual clarity, faster debugging, and simplified operations for platform teams,
directly inside Headlamp. 
 What this plugin provides    The Cluster API plugin adds a dedicated Cluster API section to Headlamp and brings
full visibility into core CAPI resources through consistent list and detail views. 
 
 
 
 Feature 
 Description 
 
 
 
 
  Cluster overview  
 View clusters with live control plane and worker replica status. 
 
 
  Machine visibility  
 Inspect MachineDeployments, MachineSets, Machines, and MachinePools with status and conditions. 
 
 
  Cluster API dashboard  
 Get a centralized view of Cluster API resource health, active condition issues, provider information, and remediation guidance. 
 
 
  Control plane monitoring  
 Track KubeadmControlPlane replicas, versions, and associated Machines. 
 
 
  Scale from the UI  
 Scale MachineDeployments and MachineSets directly from Headlamp. 
 
 
  Owned resource hierarchy  
 Trace relationships between clusters, deployments, sets, and machines. 
 
 
  KubeadmConfig inspection  
 View bootstrap configs, files, kubelet args, and join/init settings. 
 
 
  Topology awareness  
 Automatically detect and label ClusterClass-managed resources. 
 
 
  Map view  
 Visualize Cluster, Control Plane, and Worker relationships. 
 
 
  Dynamic API versioning  
 Supports both v1beta1 and v1beta2 Cluster
