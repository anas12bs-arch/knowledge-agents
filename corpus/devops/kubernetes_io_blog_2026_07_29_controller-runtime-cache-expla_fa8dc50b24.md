---
title: "[kubernetes] How the controller-runtime Cache Actually Works, and Why Your Controller Does Not Crash the API Server"
url: "https://kubernetes.io/blog/2026/07/29/controller-runtime-cache-explained/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-07-30T00:10:12Z"
metadata:
  {}
---

# [kubernetes] How the controller-runtime Cache Actually Works, and Why Your Controller Does Not Crash the API Server

> Source: devops | Category: infrastructure | 2026-07-30T00:10:12Z

How the controller-runtime Cache Actually Works, and Why Your Controller Does Not Crash the API Server

Kubernetes has long been the default platform for distributed workloads, and writing your own
controller for it is now a matter of a few hours. The common path — Golang, using  kubebuilder  on top of
 controller-runtime  — gives you a project scaffold, types, and a reconciler. For typical
scenarios that is more than enough. But as soon as load grows or the controller starts behaving
in ways you did not expect, a whole class of edge cases shows up. Most of them trace back to
the same root cause: a fuzzy mental model of how  controller-runtime  works inside. If you
write Kubernetes controllers in Go, this article should help you build a coherent picture and
avoid expensive surprises in production. 
 This article walks through the internals of  controller-runtime  and, along the way, shows which
architectural decisions are baked into Kubernetes itself. The starting point is how
controllers actually read objects from the Kubernetes API. 
 A common misconception goes like this:  r.Get()  inside  Reconcile  queries  kube-apiserver 
directly;  r.List()  returns a fresh, live view of the world; and after  r.Update()  you can
re-read the object and immediately see the new state. In practice the model is the opposite:
 controller-runtime  operates against a local copy of the data populated through  list  +  watch .
Reads inside a reconciler cost almost nothing and do not load the control plane even at
hundreds of calls per second — but the price of this design is that a controller can quietly
consume gigabytes of memory, perform hidden  O(n)  scans, and regularly trip over stale reads. 
 This post is aimed at engineers who already write controllers in Go with  controller-runtime 
but want to consolidate the pieces into a single mental model rather than carry around a bag
of isolated observations. The focus is the practical impact on production clusters: memory,
network traffic, read consistency, and reconciler behavior. 
 TL;DR    If you take only one idea from this article
