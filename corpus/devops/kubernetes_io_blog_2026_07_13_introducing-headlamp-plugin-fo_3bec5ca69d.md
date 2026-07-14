---
title: "[kubernetes] Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow"
url: "https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-07-14T03:23:47Z"
metadata:
  {}
---

# [kubernetes] Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow

> Source: devops | Category: infrastructure | 2026-07-14T03:23:47Z

Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow

Kubernetes has quietly become the default platform for AI and machine learning. Whether you run notebook servers for data scientists, schedule distributed training jobs, tune hyperparameters, or orchestrate multi-step ML pipelines, those workloads increasingly land on a Kubernetes cluster.  Kubeflow  is one of the most popular ways to assemble that stack, and it does so the Kubernetes-native way: every capability is exposed as a Custom Resource Definition (CRD). 
 That design is a gift to cluster operators, because it means ML workloads can be observed and managed with the same primitives as everything else in the cluster. But in practice the specialized ML dashboards that ship with these platforms hide the Kubernetes layer underneath. When a notebook is stuck or a training run fails, the operator is often left dropping back to  kubectl  to find out what actually happened at the Pod level. 
 This post introduces the  Headlamp Kubeflow plugin , which closes that gap by surfacing Kubeflow's custom resources directly inside a general-purpose Kubernetes UI. It is a worked example of a pattern any CRD-heavy platform can follow: meet operators where they already work, and show them the cluster-level truth. 
 Headlamp itself is an extensible Kubernetes web UI maintained under  Kubernetes SIG UI  and licensed under Apache 2.0. It runs as a desktop app or in-cluster, and its plugin system lets anyone add first-class views for custom resources. 
 Why operators need a different view    Purpose-built ML dashboards help data scientists submit experiments, pipelines, and
notebooks. Cluster operators and site reliability engineers (SREs) troubleshoot the
Kubernetes resources underneath, and they ask different questions: 
 
 Why is a notebook stuck? Is it  ImagePullBackOff ,  OOMKilled , or a Pod waiting on a PersistentVolumeClaim? 
 Which Run resources failed recently across namespaces? 
 Which parameter set does a Katib Experiment report as optimal? 
 Do TrainJob resources refe
