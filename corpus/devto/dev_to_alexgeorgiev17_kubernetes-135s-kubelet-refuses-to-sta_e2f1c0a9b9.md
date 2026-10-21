---
title: "Kubernetes 1.35's kubelet refuses to start on a cgroup v1 host by default"
url: "https://dev.to/alexgeorgiev17/kubernetes-135s-kubelet-refuses-to-start-on-a-cgroup-v1-host-by-default-4o3h"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-10-21T11:42:50Z"
metadata:
  tag: "devops"
---

# Kubernetes 1.35's kubelet refuses to start on a cgroup v1 host by default

> Source: devto | Category: news | 2026-10-21T11:42:50Z

On a cgroup v1 host, Kubernetes 1.35 and 1.37's kubelet crash-looped 82 times in 90 seconds instead of booting; the documented fix stops the crash but needs an undocumented second flag for kubeadm, and quietly breaks Memory QoS.

Reactions: 6
