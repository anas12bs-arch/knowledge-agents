---
title: "[kubernetes] Kubernetes v1.38 Sneak Peek"
url: "https://kubernetes.io/blog/2026/11/23/kubernetes-v1-38-sneak-peek/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-11-23T19:34:25Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.38 Sneak Peek

> Source: devops | Category: infrastructure | 2026-11-23T19:34:25Z

Kubernetes v1.38 Sneak Peek

As we get closer to the release date for Kubernetes v1.38, the project develops and matures,
features may be deprecated, removed, or replaced with better ones for the project's overall health.
This blog post outlines some of the planned changes for the Kubernetes v1.38 release that the
release team feels you should be aware of for the continued maintenance of your Kubernetes
environment and keeping up to date with the latest changes. The information listed below is based
on the current status of the v1.38 release and may change before the actual release date. 
 Deprecations and removals for Kubernetes v1.38    kubectl: WebSocket opt-out environment variables removed     kubectl  has used WebSockets instead of SPDY by default for  kubectl exec ,  attach  and  cp  since
v1.30, and for  kubectl port-forward  since v1.31. The  KUBECTL_REMOTE_COMMAND_WEBSOCKETS  and
 KUBECTL_PORT_FORWARD_WEBSOCKETS  environment variables let you turn that behavior off. These
variables are going to be removed in v1.38.  kubectl  will then always try WebSockets first and fall
back to SPDY when it needs to (the same as the current default behavior). If your scripts or CI
environments set either of these environment variables, you can remove them since they will no
longer have any effect. 
 To learn more, refer to
 KEP-4006: Transition from SPDY to WebSockets . 
 kubectl:  name  dropped from kuberc credential plugin allowlist entries    The  kuberc  file keeps kubectl user preferences separate from cluster credentials in the
kubeconfig, including an allowlist of the credential plugins  kubectl  is allowed to run. In the
beta  kubectl.config.k8s.io/v1beta1  API, an allowlist entry can use  name  as an alias for
 command . The  name  field (not  command ) has been deprecated since v1.36. 
 With  kuberc  expected to graduate to stable in v1.38, the new  kubectl.config.k8s.io/v1  API will
not include  name . If any of your allowlist entries use  name , change them to  command  now. 
 To learn
