---
title: "[kubernetes] Kubernetes v1.37: Scale Workloads to Zero with HorizontalPodAutoscaler"
url: "https://kubernetes.io/blog/2026/09/02/kubernetes-v1-37-hpa-scale-to-zero-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-03T04:44:40Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Scale Workloads to Zero with HorizontalPodAutoscaler

> Source: devops | Category: infrastructure | 2026-09-03T04:44:40Z

Kubernetes v1.37: Scale Workloads to Zero with HorizontalPodAutoscaler

Kubernetes v1.37 includes API support for horizontal autoscaling of workloads down
to zero replicas. This feature is now Beta and enabled by default. A
 HorizontalPodAutoscaler 
(HPA) that uses a suitable  object metric  or  external metric  can now scale a
workload to zero replicas, then bring it back when the metric changes. 
 Before v1.37, you needed an add-on or external component, or you had to enable the
Alpha feature gate, to scale from zero. It is now part of core Kubernetes. 
 Scaling to zero removes the last idle Pod from workloads such as queue consumers and
batch processors. The savings are largest when each Pod reserves expensive resources,
including dedicated CPUs or GPUs. 
 The trade-off is cold-start time: the HPA must observe the metric, schedule a Pod, and
start the application. This works well when work can wait in a durable queue. 
 Kubernetes Services do not buffer requests while no Pods are ready, so HTTP and other
request-driven workloads need a separate buffering layer. 
 Why scaling from zero needs a different metric    The HPA commonly scales on CPU or memory usage. Both metrics come from running Pods.
Once the replica count reaches zero, there are no Pods left to measure and no signal
that can tell the HPA to scale back up. 
 Object and external metrics do not have that limitation. A queue length, for example,
exists independently of the workers that consume it. The HPA can continue reading the
queue length while no workers are running. 
 The following example scales a queue consumer to and from zero using an external
metric. 
 Configure an external metric    The following example uses a Prometheus metric named  queue_consumer_lag . It assumes
that Prometheus already collects a series similar to this one: 
      queue_consumer_lag  {  namespace  =  &#34;  default  &#34;,  name  =  &#34;  worker_tasks  &#34;}  
       Kubernetes needs a metrics adapter to make that value available through the External
Metrics API. One implementation is th
