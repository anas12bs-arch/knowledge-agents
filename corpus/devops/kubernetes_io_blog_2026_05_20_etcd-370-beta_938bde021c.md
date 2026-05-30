---
title: "[kubernetes] Announcing etcd 3.7.0-beta.0"
url: "https://kubernetes.io/blog/2026/05/20/etcd-370-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [kubernetes] Announcing etcd 3.7.0-beta.0

> Source: devops | Category: infrastructure | 2026-05-30T15:08:37Z

Announcing etcd 3.7.0-beta.0

SIG-Etcd announces the availability of the  first beta release of etcd v3.7.0 . This new version of the popular distributed database and key Kubernetes component includes the long-requested RangeStream feature, as well as a refactoring and cleanup of multiple legacy components and interfaces. v3.7 will deliver improved security, better operational reliability, and an improved experience for working with large resultsets. 
 First, however, the project needs users to test the beta. You can find v3.7.0-beta.0 here: 
 
  Source code  
  Binaries  
  Official container images  
 
 Please try it out and report issues  in the etcd repo . 
 This beta also determines the EOL of version 3.4. 
 RangeStream    In etcd v3.6 and earlier, it is challenging to work with requests that return large resultsets. The client or requesting application is forced to wait for the full result set, leading to unpredictable latency and memory usage.  The RangeStream RPC  lets calling applications accept result sets in chunks, reducing latency and making buffering memory usage more predictable. 
 Much of the work on RangeStream was done by a relatively new contributor to etcd,  Jeffrey Ying , a software engineer at Google. New contributors can have a substantial impact on etcd development. 
 &quot;I've always been fascinated by database internals, and building RangeStream was a great opportunity to solve a bottleneck we were hitting in production with Kubernetes. It was the perfect opportunity to collaborate across projects and improve the ecosystem as a whole. Jumping into etcd as a new contributor had a bit of a learning curve, but the community is incredibly welcoming. The leads were very receptive to my ideas and helped me iterate quickly, while maintaining the project's high bar for reliability and code quality,&quot; said Jeffrey. 
 Instructions on how to use RangeStream  in gRPC calls  and  in etcdctl  can be found in the etcd documentation. Users should try it out for their own applica
