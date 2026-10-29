---
title: "[kubernetes] From Working Group to SIG Architecture: spotlight on AI Conformance"
url: "https://kubernetes.io/blog/2026/10/29/sig-arch-ai-conformance-2026/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-10-29T15:34:48Z"
metadata:
  {}
---

# [kubernetes] From Working Group to SIG Architecture: spotlight on AI Conformance

> Source: devops | Category: infrastructure | 2026-10-29T15:34:48Z

From Working Group to SIG Architecture: spotlight on AI Conformance

In this SIG Architecture spotlight we talked with  Janet Kuo  (Google)
and  Yuan Tang  (Red Hat) about the journey of AI Conformance in
Kubernetes, from the initial  Working
Group  to the
integration  SIG Architecture 
as a subproject. 
 Introductions     Frederico Muñoz and Kirti Goyal (FK): Hi Janet, Yuan, and thank you for the opportunity to learn a
bit more about AI Conformance. Can you tell us a bit about yourselves and how you got involved in
Kubernetes?  
  Janet Kuo : I'm a Senior Staff Software Engineer at Google and have been a Kubernetes maintainer
since 2015, joining the community just as we were racing toward the 1.0 launch. I started my journey
writing the core workload controllers that standardized how applications are orchestrated on
Kubernetes. Today, I lead SIG Apps as a Co-chair &amp; TL, and also lead the
 AI Conformance program .
My current focus is to ensure Kubernetes remains the best platform for the next generation of
workloads, such as AI. 
  Yuan Tang : I’m a Senior Principal Software Engineer at Red Hat, where I lead the development of
our AI platform and drive our upstream open source strategy. I became involved in Kubernetes early
on by fostering collaborations between the Kubernetes community and projects I was leading,
including Kubeflow, Argo, and KServe. I later helped found and lead  WG Serving  and the AI Conformance program, advancing
innovation and strengthening community collaboration around running AI workloads on Kubernetes. 
 Program, Working Group, Subproject: the many shapes of AI Conformance     FK: AI Conformance started as a CNCF Program, was it then you got involved?  
  Janet Kuo:  I was actually involved from day one since I pitched the original idea. It became
obvious then that everyone was starting to run AI on Kubernetes, but vendors were building their
infrastructure stacks in different ways. I got worried about ecosystem fragmentation. So I wrote up
the initial Kubernetes AI Conformance Proposal, took it to th
