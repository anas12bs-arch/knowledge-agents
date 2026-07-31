---
title: "[kubernetes] Kubernetes v1.37 Sneak Peek"
url: "https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-07-31T17:54:26Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37 Sneak Peek

> Source: devops | Category: infrastructure | 2026-07-31T17:54:26Z

Kubernetes v1.37 Sneak Peek

As we get closer to the release date for Kubernetes v1.37, the project develops and matures,
features may be deprecated, removed, or replaced with better ones for the project's overall
health. This blog outlines some of the planned changes for the Kubernetes v1.37 release that the
release team feels you should be aware of for the continued maintenance of your Kubernetes
environment and keeping up to date with the latest changes. The information below reflects the
current status of the v1.37 release and may change before the actual release date. 
 Deprecations and removals for Kubernetes v1.37    Kubectl:  kubectl run --filename/-f  to be deprecated    The  --filename  (or  -f ) flag for  kubectl run  is being deprecated as the generated pod is always built purely from CLI arguments like  NAME  and  --image . 
 See  kubernetes/kubernetes#138671  for the original issue and discussion. 
 Kubelet: Static Pods can no longer reference Secrets or ConfigMaps    Static Pods were never meant to read API resources directly, since they aren't created through the API server — but a bug let them reference Secrets or ConfigMaps via fields like  configMapRef  or  secretRef . That bug is now fixed: as of v1.37 these references are strictly prohibited, and the  PreventStaticPodAPIReferences  feature gate that previously let you opt out of the restriction has been removed. 
 See  kubernetes/kubernetes#140226  for the original issue and discussion. 
 Deprecating kube-proxy's support for  ipvs  mode     kube-proxy  support for  ipvs  mode was introduced in v1.8 to resolve  iptables  performance bottlenecks. However, since the kernel  ipvs  API alone cannot fully implement Kubernetes Services,  ipvs  mode continues to use  iptables  underneath ( KEP-3866, &quot;The ipvs mode of kube-proxy will not save us&quot; ). 
 Clusters running  kube-proxy  in ipvs mode (or mode: ipvs in KubeProxyConfiguration) would now be logging a deprecation warning on startup. The deprecation timeline looks l
