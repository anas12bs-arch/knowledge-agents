---
title: "[kubernetes] Kubernetes v1.37: Memory QoS Graduates to Beta"
url: "https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-14T22:05:37Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Memory QoS Graduates to Beta

> Source: devops | Category: infrastructure | 2026-09-14T22:05:37Z

Kubernetes v1.37: Memory QoS Graduates to Beta

Memory QoS has graduated to Beta in Kubernetes v1.37 and is now enabled by
default. On Linux nodes running cgroup v2, the feature uses the memory controller
to give the kernel better guidance on how to treat container memory. It was first introduced as
Alpha in v1.22, and expanded in v1.36 with tiered memory reservation. 
 This post covers what changed in v1.37, what the Beta promotion means for
cluster operators, and how to configure the feature. 
 What changed in v1.37    Memory QoS is Beta and enabled by default    The  MemoryQoS  feature gate is now Beta in v1.37.
This means every v1.37  kubelet  has the feature gate turned on without any
configuration change. Turning on the feature by default is safe because the
default  kubelet  configuration does not enable memory throttling or memory
reservation. No  memory.high ,  memory.min , or  memory.low  values are
written to cgroups unless you explicitly configure them. 
 You can opt into specific behaviors through  kubelet  configuration fields: 
 
 Set  memoryThrottlingFactor  (for example,  0.9 ) to enable  memory.high  throttling on Burstable and BestEffort containers. The default is  null , which means no throttling. 
 Set  memoryReservationPolicy  to  TieredReservation  to enable tiered memory protection via  memory.min  and  memory.low . The default is  None , which means no memory reservation. 
 
 Default  memoryThrottlingFactor  changed to null    In earlier Alpha releases,  memoryThrottlingFactor  defaulted to  0.9 , which
meant enabling the feature gate caused the  kubelet  to set
 memory.high  on containers. In v1.37, the default is  null , so the  kubelet 
does not set  memory.high  unless you configure a value. 
 This change was made because, with the feature gate now on by default, an
automatic  memory.high  could throttle workloads that were previously running
without throttling. Making it  null  ensures that upgrading to v1.37 does not
change runtime behavior for existing clusters. 
 If your  kubele
