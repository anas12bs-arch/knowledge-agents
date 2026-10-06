---
title: "[kubernetes] The Shift to cgroup v2 in Kubernetes: What You Need to Know"
url: "https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-10-06T23:23:27Z"
metadata:
  {}
---

# [kubernetes] The Shift to cgroup v2 in Kubernetes: What You Need to Know

> Source: devops | Category: infrastructure | 2026-10-06T23:23:27Z

The Shift to cgroup v2 in Kubernetes: What You Need to Know

In Linux,  cgroups  (control groups) are a kernel feature used for managing system resources.
Kubernetes uses cgroups to allocate resources like CPU and memory to containers,
ensuring that applications run smoothly without interfering with each other.
With the release of Kubernetes v1.31, support for v1 cgroup management moved into
 maintenance mode .
Support for v2 cgroup management has been stable since Kubernetes v1.25. 
 Compared with cgroup v1, cgroup v2 provides a single unified hierarchy,
a more consistent interface, and a stronger foundation for resource isolation
and modern resource-management features. 
 Deprecation of cgroup v1    Kubernetes has  deprecated cgroup v1 .
Starting with Kubernetes v1.35,  failCgroupV1  defaults to  true , so the kubelet does not start
on a cgroup v1 node by default. Administrators can temporarily set  failCgroupV1: false  in the
 kubelet configuration file , but removal will
follow the  Kubernetes deprecation policy .
Further removal work is tracked in  KEP-5573: Remove cgroup v1 support . 
 If you are still on a release older than v1.35, migrate every Linux node to
cgroup v2 before upgrading, or plan to set the temporary  failCgroupV1: false 
override. If you are already on v1.35 or later, confirm that every Linux node
runs cgroup v2 (or that you intentionally keep the override). Under the default
configuration, a remaining cgroup v1 node fails during kubelet startup. 
 For kubeadm-managed clusters, Kubernetes v1.35 also makes this an earlier, stricter check. The
 SystemVerification  preflight check, provided by  k8s.io/system-validators , returns an error during
 kubeadm init ,  kubeadm join , and  kubeadm upgrade  when it detects cgroup v1 with kubelet v1.35 or
later; with an older kubelet, the check remains a warning. See
 kubernetes/system-validators#1.12.1 release notes  for details. 
 The top FAQs cover three main areas: why to migrate, the benefits and drawbacks,
and key points to keep in mind when using cgroup v2.
