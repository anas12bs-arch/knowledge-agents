---
title: "[kubernetes] Kubernetes v1.37: DRA Updates"
url: "https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-03T19:49:04Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.37: DRA Updates

> Source: devops | Category: infrastructure | 2026-09-03T19:49:04Z

Kubernetes v1.37: DRA Updates

Kubernetes 1.37 is here and  Dynamic Resource Allocation (DRA)  keeps pushing past where it started! This release brings DRA Extended Resource support to GA, a milestone the team has been building toward for three straight releases. Several more features graduate to Beta or GA. A fresh batch of alpha features rounds out the release. 
 I'll dive into what's new for DRA in Kubernetes 1.37! 
 What's stable in 1.37     DRA Extended Resource support  has graduated to GA. This is the mechanism that lets DRA drivers satisfy requests made through the traditional extended resource API, think  example.com/gpu  in a Pod spec, without requiring a separate device plugin alongside the DRA driver. An extended resource name can be set directly on a DeviceClass, and Pods requesting it get matched to a device through DRA with no ResourceClaim needed on the workload's part. 
 It's been on a steady path since KEP acceptance in 1.34. Alpha landed in 1.35, Beta in 1.36, and now it's Stable. For cluster operators, this is what makes DRA adoption gradual. Existing workloads written against extended resources keep working unmodified while the backend allocation logic moves over to DRA. 
  ResourceClaims status with possible standardized network interface data  adds a  devices  field to ResourceClaim  .status , letting DRA drivers report per-device status, including, for network devices, the interface name, MAC address, and IP addresses. This gives users and controllers visibility into device state that was previously invisible once a device was configured in a Pod, and makes it possible to build things like network services that rely on a device's reported IPs. 
  DRA: device taints and tolerations  is now Stable; DRA drivers can mark devices as tainted so they're skipped for new Pod scheduling, and cluster admins can apply the same taints cluster-wide via a DeviceTaintRule, without reconfiguring drivers. Pods already using a tainted device can be evicted automatically, unless their Resou
