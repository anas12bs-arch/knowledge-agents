---
title: "[kubernetes] Kubernetes v1.37: KubeletInUserNamespace (aka Rootless mode) Graduates to Beta"
url: "https://kubernetes.io/blog/2026/09/04/kubernetes-v1-37-rootless-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-05T01:11:18Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: KubeletInUserNamespace (aka Rootless mode) Graduates to Beta

> Source: devops | Category: infrastructure | 2026-09-05T01:11:18Z

Kubernetes v1.37: KubeletInUserNamespace (aka Rootless mode) Graduates to Beta

Kubernetes v1.37 promotes the  KubeletInUserNamespace  feature gate to beta.
With this feature enabled, all of the node components (kubelet, CRI and OCI runtimes,
CNI plugins, and kube-proxy) can run as a non-root user on the host, using a
 Linux user namespace .
This technique is also known as  rootless mode .
The work started as an experiment in 2018, and was merged into Kubernetes v1.22 (2021)
as an alpha feature (Kubernetes Enhancement Proposal  KEP-2033 ). 
 This feature should not be confused with  user namespaces for pods 
( hostUsers: false  with the  UserNamespacesSupport  feature gate, GA since v1.36),
which puts pods in user namespaces but still runs the node components as root.
These two features do not conflict.
Moreover, they can be combined to nest Kubernetes inside Kubernetes without resorting to
the full  privileged: true . 
 Why run the node components in a user namespace?    Because the node components have historically had container-breakout vulnerabilities
that could compromise full root privileges on the host. 
 Examples of such vulnerabilities include: 
 
  CVE-2022-0811 
(&quot;cr8escape&quot;): CRI-O could be tricked into setting arbitrary sysctls, such as
 kernel.core_pattern , resulting in arbitrary code execution as root on the host 
  CVE-2023-27561 :
runc could be tricked into bypassing the masked paths of a container via a volume
mount race, exposing the host's procfs files (a regression of CVE-2019-19921) 
  CVE-2024-10220 :
the kubelet could be made to execute arbitrary commands as root via  gitRepo  volumes
( gitRepo  volumes had a similar vulnerability,
 CVE-2018-11235 , back in 2018 too) 
  CVE-2025-31133 :
runc could be tricked into bind-mounting attacker-controlled paths and writing to the
host's procfs files, such as  /proc/sysrq-trigger  and
 /proc/sys/kernel/core_pattern  
  CVE-2026-53488 :
containerd could be tricked into executing arbitrary commands on the host, via
crafted labels in a container image 
 
 By running the
