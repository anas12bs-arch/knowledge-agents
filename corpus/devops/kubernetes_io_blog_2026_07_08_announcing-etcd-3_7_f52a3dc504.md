---
title: "[kubernetes] Announcing etcd v3.7.0"
url: "https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-07-08T19:50:33Z"
metadata:
  {}
---

# [kubernetes] Announcing etcd v3.7.0

> Source: devops | Category: infrastructure | 2026-07-08T19:50:33Z

Announcing etcd v3.7.0

This article is a mirror of the  original announcement   
 Today, SIG etcd is releasing  etcd v3.7.0 , the latest minor release of the popular distributed key-value store and core Kubernetes component. v3.7 ships the long-requested RangeStream feature, delivers several other performance improvements, removes the last remnants of the legacy v2store, and completes a major protobuf overhaul. 
 You can download etcd v3.7.0 here: 
 
  Source code  
  Binaries  
  Official container images  
 
 This release also includes new versions of the two core etcd dependencies,  bbolt v1.5.0  and  raft v3.7.0 . 
 For instructions on installing etcd, see the  install documentation . For the full list of changes, see the  etcd v3.7 changelog . 
 A heartfelt thank you to all the contributors who made this release possible! 
 Major features    The most significant changes in v3.7.0 include: 
 
   RangeStream   — stream large result sets in chunks instead of buffering the whole response. 
  Keys-only range requests, faster and more reliable leases,  and several other   performance improvements  . 
 etcd now  boots entirely from v3store , eliminating a long-standing dependency on the legacy v2 store 
 A completed   protobuf overhaul  , replacing outdated protobuf libraries with fully supported ones. 
 etcd v3.7 ships with  bbolt v1.5.1  and  raft v3.7.0 . 
 
 Features    RangeStream    In etcd v3.6 and earlier, it is challenging to work with requests that return large result sets. The database would buffer the full result set before sending, leading to unpredictable latency and memory usage, both on the server and the client.  The RangeStream RPC  lets calling applications accept result sets in chunks, reducing latency and making buffering memory usage more predictable. 
 Instructions on how to use RangeStream  in gRPC calls  and  in etcdctl  can be found in the etcd documentation. Users should try it out for their own applications. 
 In coordinated releases, the RangeStream feature w
