---
title: "[kubernetes] Kubernetes Changed Block Tracking API - Beta Differences"
url: "https://kubernetes.io/blog/2026/09/14/csi-changed-block-tracking-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-14T22:05:37Z"
metadata:
  {}
---

# [kubernetes] Kubernetes Changed Block Tracking API - Beta Differences

> Source: devops | Category: infrastructure | 2026-09-14T22:05:37Z

Kubernetes Changed Block Tracking API - Beta Differences

Changed Block Tracking (CBT) support for CSI drivers
 shipped as Alpha  in
September 2025. With the March 2026  v1.0.0  release of the
 external-snapshot-metadata 
project, the feature moved to  Beta . 
 If you aren't yet familiar with  changed block tracking  for storage in
Kubernetes, the
 Alpha announcement  covers
the motivation, the three primary components (the CSI  SnapshotMetadata 
gRPC service, the SnapshotMetadataService CRD, and the
 external-snapshot-metadata  sidecar), and a walkthrough of how to use the
API. CBT currently applies to block volumes; file-volume and network
file-share changed-list tracking is not covered by this feature. This post
focuses on what is different in Beta. 
 What's new in Beta    The main change in that release was the promotion of the
SnapshotMetadataService CRD from  v1alpha1  to  v1beta1 . The CRD used to
advertise a driver's metadata service now serves
 cbt.storage.k8s.io/v1beta1 . The schema itself is unchanged, but this
release  removed   v1alpha1  (rather than serving it alongside the new version).
If you are upgrading from Alpha, you need to: 
 
 Re-apply the CRD definition shipped with  v1.0.0 . 
 Update SnapshotMetadataService manifests to use
 apiVersion: cbt.storage.k8s.io/v1beta1 . 
 Update any client or controller code that talks to the CRD. 
 
 This is a one-time change. There is no automatic conversion between the two
versions. 
 Compatibility    
 Minimum Kubernetes version:  1.33  
 CSI spec:  1.10 or newer  
 Container image:  registry.k8s.io/sig-storage/csi-snapshot-metadata:v1.0.0  
 
 Trying it out    The  Getting Started section in the Alpha
blog  still
applies. In short: 
 
 Make sure your CSI driver supports volume snapshots and ships the
 external-snapshot-metadata  sidecar. 
 Install the SnapshotMetadataService CRD (the  v1beta1  definition from
the  v1.0.0  release). 
 Create a SnapshotMetadataService resource for your driver. 
 Use a client —  snapshot-metadata-lister , or your own implementation
