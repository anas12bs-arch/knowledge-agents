---
title: "[kubernetes] Kubernetes v1.37: Metrics API graduates to stable"
url: "https://kubernetes.io/blog/2026/08/27/kubernetes-v1-37-metrics-api-ga/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-08-28T12:18:55Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Metrics API graduates to stable

> Source: devops | Category: infrastructure | 2026-08-28T12:18:55Z

Kubernetes v1.37: Metrics API graduates to stable

Kubernetes v1.37 promotes the  metrics.k8s.io  API to stable ( v1 ). This
API provides CPU and memory usage for nodes and Pods, and is the API behind
commands such as  kubectl top  and resource-metrics-based autoscaling. 
 For cluster operators and application developers, this graduation means that
the API now has the stability guarantees associated with a Kubernetes stable
API. The  v1  API has the same resource types and fields as  v1beta1 ; this is
an API-version graduation, not a change to the metrics that are collected or
returned. 
 A long-lived API reaches stable    The resource Metrics API was introduced as alpha in Kubernetes v1.6 and became
beta in v1.8. It has remained unchanged and has been used in production for
years by clients including the HorizontalPodAutoscaler (HPA) and  kubectl top .
Kubernetes v1.37 formally graduates that proven API to  metrics.k8s.io/v1 . 
 The API exposes two resource types: 
 
  NodeMetrics , for CPU and memory usage for a node. 
  PodMetrics , for CPU and memory usage for a Pod, with a per-container
breakdown in its  containers  field. 
 
 The API remains intentionally small. It provides the resource metrics needed
for autoscaling and basic inspection; it is not a replacement for a full
monitoring pipeline or the custom metrics ( custom.metrics.k8s.io ) API. 
 What changed with the v1.37 release?    The  v1  API surface is identical to  v1beta1 , except for the API version.
There are no renamed fields, new fields, or changes to the meaning of the
returned CPU and memory values. 
 For example, a client can retrieve node metrics from the stable endpoint: 
     kubectl get --raw /apis/metrics.k8s.io/v1/nodes
      Likewise, it can retrieve metrics for the pods in a namespace: 
     kubectl get --raw /apis/metrics.k8s.io/v1/namespaces/default/pods
       kubectl top  supports both API versions. It prefers  v1  when available and
automatically falls back to  v1beta1  on clusters that do not yet serve  v1 .
The HPA controller c
