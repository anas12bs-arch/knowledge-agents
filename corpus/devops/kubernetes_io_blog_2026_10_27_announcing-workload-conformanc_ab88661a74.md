---
title: "[kubernetes] Announcing the Workload Conformance Working Group"
url: "https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-10-27T12:45:57Z"
metadata:
  {}
---

# [kubernetes] Announcing the Workload Conformance Working Group

> Source: devops | Category: infrastructure | 2026-10-27T12:45:57Z

Announcing the Workload Conformance Working Group

We are excited to announce that the Kubernetes community now has a  Workload Conformance Working Group .
The working group is writing a shared standard for how  workloads  behave at runtime on Kubernetes.
To get it right, we need input from the people who build those workloads and from the people who run the clusters they're deployed on. 
 Why workloads need a shared standard     Certified Kubernetes  tests the cluster, and  Kubernetes AI Conformance  tests whether a cluster can run AI and ML workloads.
Nothing comparable exists for the workloads themselves, so cluster operators still check each application by hand before routine maintenance or a Kubernetes upgrade. 
 The problems they find are familiar. A routine  node drain  is often how you discover that an application can't tolerate disruption.
An upgrade can break an application that still depends on a  removed API version .
Others show up in day-to-day operation: workloads that ask for privileges they don't need, or reserve resources they never use. 
 Kubernetes already documents much of this, including  security  and  handling disruptions .
Even so, every cluster operator ends up repeating the same assessment, and application maintainers get the same questions from each environment they support.
A common specification with repeatable tests would give both groups the same baseline to start from. 
 What the working group will deliver    The  charter  sets out three deliverables: 
 
 A specification of workload behavior for each Kubernetes minor version. 
 A method for testing each requirement against a running workload. 
 Upstream conformance tooling that implements those tests. 
 
 The first step is deciding which workloads and behaviors the specification covers.
The scope includes security, resilience during disruptions, resource use, networking, storage, API usage, and observability, but the group hasn't yet agreed on specific requirements or on how to test them.
However, one rule is already set: every req
