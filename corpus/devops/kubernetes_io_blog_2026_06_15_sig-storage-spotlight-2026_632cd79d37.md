---
title: "[kubernetes] Spotlight on SIG Storage"
url: "https://kubernetes.io/blog/2026/06/15/sig-storage-spotlight-2026/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-06-16T18:12:01Z"
metadata:
  {}
---

# [kubernetes] Spotlight on SIG Storage

> Source: devops | Category: infrastructure | 2026-06-16T18:12:01Z

Spotlight on SIG Storage

In our ongoing SIG Spotlight series, we shine a light on the groups that keep the Kubernetes project
moving forward. This time, we catch up with   SIG
Storage  , the group responsible
for persistent data, volume management, and the interfaces that connect Kubernetes workloads to the
storage systems beneath them. 
 We spoke with  Xing Yang , Co-Chair of SIG Storage and Software
Engineer at VMware by Broadcom, about the SIG's history, the features shipping in recent Kubernetes
releases, and where storage in Kubernetes is headed as AI workloads become the norm. 
 Introductions     Could you introduce yourself and share your role(s) within SIG Storage?  
 My name is  Xing Yang , a software engineer at VMware by Broadcom. I'm a co-chair in SIG Storage,
alongside another co-chair  Saad Ali  from Google. There are also two Tech Leads in SIG Storage:
 Michelle Au  from Google and  Jan Šafránek  from Red Hat. 
  What first drew you to storage in Kubernetes, and how did you start contributing?  
 I have always been working in the storage domain, so SIG Storage was a natural place for me to get
started when I began to learn Kubernetes. I started attending  SIG Storage meetings , trying to figure
out what I could do to help. This was before the first  Container Storage Interface  (CSI) release —
lots of things were still evolving. It was a very exciting time. 
  What subprojects or areas do you actively maintain or review today?  
 I'm a maintainer in Kubernetes CSI. There are multiple CSI sidecars — such as  csi-provisioner ,
 csi-attacher ,  csi-resizer , and  csi-snapshotter  — that we need to release following every
Kubernetes release. I'm also a co-chair for a  Data Protection Working Group  co-sponsored by SIG
Storage and  SIG Apps . Several features have come out of that WG aimed at filling gaps in data
protection support within Kubernetes. One is  Volume Group
Snapshot , which provides
crash-consistent group snapshots for multiple volumes used by an application.  Chan
