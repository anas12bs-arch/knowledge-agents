---
title: "[cncf] Optimizing Kubernetes admission control: Where Kyverno’s CEL admission cost actually goes"
url: "https://www.cncf.io/blog/2026/11/18/optimizing-kubernetes-admission-control-where-kyvernos-cel-admission-cost-actually-goes/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "cncf"]
date: "2026-11-18T16:26:07Z"
metadata:
  {}
---

# [cncf] Optimizing Kubernetes admission control: Where Kyverno’s CEL admission cost actually goes

> Source: devops | Category: infrastructure | 2026-11-18T16:26:07Z

Optimizing Kubernetes admission control: Where Kyverno’s CEL admission cost actually goes

Kyverno&#8217;s CEL (Common Expression Language)-based engines exist to evaluate policy expressions. So when we profiled the admission path, we expected to find the bulk of the cost in CEL evaluation. It was not there. About 86%...
