---
title: "[kubernetes] Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads"
url: "https://kubernetes.io/blog/2026/09/01/kubernetes-v1-37-etcd-range-stream/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-02T01:09:46Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads

> Source: devops | Category: infrastructure | 2026-09-02T01:09:46Z

Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads

I am excited to announce that etcd RangeStream is graduating to beta in
Kubernetes v1.37. Paired with etcd v3.7, it reduces the memory the API server and
etcd need to read a large collection, and makes peak usage more predictable. 
 The cost of large reads    The API server serves most list and watch requests from its in-memory watch cache.
Populating that cache requires reading a resource's full state from etcd, at
startup and on every re-initialization. For a resource with many objects, or large
ones, such as Pods, that read is expensive. 
 The API server already paginated these reads, asking etcd for a fixed number of
keys at a time rather than the whole collection at once. But a page bounded by key
count has no awareness of object size, so a page of large objects can still be
very large. That makes memory usage hard to predict, and a bad combination of
object size and concurrent reads can be enough to trigger an OOM. etcd's unary
 Range  assembles each page in full before sending it, and the API server holds it
while decoding, so the same payload sits in memory on both sides at once. Most of
that cost lands on etcd, which is also where streaming helps most. 
 Streaming reads with RangeStream    etcd v3.7 adds a streaming version of that read, the  RangeStream  RPC. It takes
the same  RangeRequest  as  Range  and returns the same result set, but instead of
building the whole response up front, etcd splits it into chunks and streams them.
Chunk size is tuned adaptively to the values being returned, so a collection of
large objects is bounded by bytes rather than by a key count, and memory is freed
as the stream progresses instead of being held until a whole page is assembled. 
 When the feature is enabled, the API server uses  RangeStream  wherever it reads a
whole collection out of etcd. This includes watch cache initialization, and the
fallback paths where a list request cannot be served from the cache and reads etcd
directly. In either case the API server dec
