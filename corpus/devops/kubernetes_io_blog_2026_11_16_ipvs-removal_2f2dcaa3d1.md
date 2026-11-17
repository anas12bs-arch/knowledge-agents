---
title: "[kubernetes] Scheduling the removal of the kube-proxy IPVS backend"
url: "https://kubernetes.io/blog/2026/11/16/ipvs-removal/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-11-17T01:00:04Z"
metadata:
  {}
---

# [kubernetes] Scheduling the removal of the kube-proxy IPVS backend

> Source: devops | Category: infrastructure | 2026-11-17T01:00:04Z

Scheduling the removal of the kube-proxy IPVS backend

The  ipvs  backend for kube-proxy was an experiment in providing a
service proxy implementation with better performance than the
 iptables  backend. While it succeeded in that goal, the kernel IPVS
API has turned out to be a bad match for the Kubernetes Services API,
and the  ipvs  backend was never able to implement all of the edge
cases of Kubernetes Service functionality correctly. 
 In Kubernetes 1.29, the project introduced the  nftables  backend for
kube-proxy, which became GA in 1.33. Part of the plan behind adding
the  nftables  backend was the idea that it would eventually replace
both the  iptables  and  ipvs  backends. Because the  ipvs  backend in
particular is complex, not 100% feature complete, and architecturally
quite different from the other two backends (and thus more work to
maintain), Kubernetes SIG Network decided to officially  deprecate it
as of Kubernetes 1.35 . Although it currently remains available in
kube-proxy (with a warning about its deprecation), we (Kubernetes SIG
Network) now plan to remove it in Kubernetes 1.40. All  ipvs  users
should therefore be planning to migrate to either the  nftables  or
 iptables  backends. 
 Why was the  ipvs  backend written?    The  ipvs  backend was originally designed to fix two different kinds
of performance problems in the  iptables  backend: 
 
 
 First,  iptables  had problems with  data plane  latency (the speed
at which clients could establish new connections to services),
because kube-proxy would write a separate iptables rule to match
each service IP, so every new connection would need to be matched
against a long series of rules that was  O(n)  in the number of
services in the cluster. 
 
 
 Second, it had an even larger problem with  control plane  latency
(the speed at which kube-proxy could process changes to services and
endpoints and update the data plane rules), because kube-proxy would
rewrite the entire iptables ruleset every time any service or
endpoint changed. While the list of r
