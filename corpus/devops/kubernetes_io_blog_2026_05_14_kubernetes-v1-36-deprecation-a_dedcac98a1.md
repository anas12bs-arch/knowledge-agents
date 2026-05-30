---
title: "[kubernetes] Kubernetes v1.36: Deprecation and removal of Service ExternalIPs"
url: "https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.36: Deprecation and removal of Service ExternalIPs

> Source: devops | Category: infrastructure | 2026-05-30T15:08:37Z

Kubernetes v1.36: Deprecation and removal of Service ExternalIPs

The  .spec.externalIPs  field for  Service  was an early attempt to provide
cloud-load-balancer-like functionality for non-cloud clusters.
Unfortunately, the API assumes that every user in the cluster is fully
trusted, and in any situation where that is not the case, it enables
various security exploits, as described in
 CVE-2020-8554 . 
 Since Kubernetes 1.21, the Kubernetes project has recommended that all users disable
 .spec.externalIPs . To make that easier, Kubernetes also added an admission controller
( DenyServiceExternalIPs ) that can be enabled to do this. At the time,
SIG Network felt that blocking the functionality by default was too large a
breaking change to consider. 
 However, the security problems are still there, and as a project we're increasingly
unhappy with the &quot;insecure by default&quot; state of the feature.
Additionally, there are now several better alternatives for non-cloud
clusters wanting load-balancer-like functionality. 
 As a result, the  .spec.externalIPs  field for Service is now formally deprecated in Kubernetes 1.36.
We expect that a future minor release of Kubernetes will drop
implementation of the behavior from  kube-proxy , and will update the
Kubernetes  conformance  criteria to require that conforming implementations
 do not  provide support. 
 A note on terminology, and what hasn't been deprecated    The phrase  external IP  is somewhat overloaded in Kubernetes: 
 
 
 The Service API has a field  .spec.externalIPs  that can be used
to add additional IP addresses that a Service will respond on. 
 
 
 The Node API's  .status.addresses  field can list addresses of
several different types, one of which is called  ExternalIP . 
 
 
 The  kubectl  tool, when displaying information about a Service of type
LoadBalancer in the default output format, will show the load
balancer IP address under the column heading  EXTERNAL-IP . 
 
 
 This deprecation is about the first of those. If you are not setting
the field  externalIPs  in
