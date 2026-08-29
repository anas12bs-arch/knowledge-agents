---
title: "[kubernetes] Kubernetes v1.37: Pod Certificates and Cluster Trust Bundles"
url: "https://kubernetes.io/blog/2026/08/28/kubernetes-v1-37-pod-certificates-and-cluster-trust-bundles/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-08-29T03:47:41Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: Pod Certificates and Cluster Trust Bundles

> Source: devops | Category: infrastructure | 2026-08-29T03:47:41Z

Kubernetes v1.37: Pod Certificates and Cluster Trust Bundles

Pod Certificate / Cluster Trust Bundles Blog Post    Kubernetes brings a wealth of features that make it easy to run your production
workloads securely and reliably. While aspects like scheduling, health checks
and resource limits are probably at the front of your mind, one other important
feature of Kubernetes is production identity — how your workload can
authenticate to other systems in order to do its job. 
 Up until now, the primary production identity mechanism built into Kubernetes
has been service account JWTs (JSON Web Tokens). These are
cryptographically-signed tokens, issued by the control plane of your cluster,
that let anyone in the world understand who is calling when your workload uses
them. 
 In Kubernetes 1.37, the foundations of a new built-in production identity
technology have gone GA. Pod Certificates (and the closely-associated Cluster
Trust Bundles) build X.509 certificate issuance for TLS and mTLS directly into
core Kubernetes. 
 Why? 
 Service account JWTs have a lot going for them: 
 
 They are built directly into Kubelet, and work pretty magically. They are
written to your workload container’s filesystem before your workload starts
up, and automatically kept up to date. 
 The issuance system follows least-privilege principles; the node restriction
admission plugin ensures that tokens can only be requested by the Kubelet that
is actually currently running your pod. 
 They can be federated, allowing you to use them to authenticate to other
systems outside of Kubernetes. Service account JWTs underpin the pod-to-cloud
authentication store for all of the largest cloud providers, and have
widespread support across many additional services and software packages. If
it can understand JWTs, you can authenticate to it with a service account
token. 
 
 However, service account JWTs have one big downside — they are bearer tokens.
With bearer tokens, if you  have  the token, then you  are  the identity
asserted by the token. And since you necessarily
