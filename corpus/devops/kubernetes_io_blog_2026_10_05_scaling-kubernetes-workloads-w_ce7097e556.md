---
title: "[kubernetes] Scaling Kubernetes Workloads with Node Swap"
url: "https://kubernetes.io/blog/2026/10/05/scaling-kubernetes-workloads-with-node-swap/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-10-06T01:33:38Z"
metadata:
  {}
---

# [kubernetes] Scaling Kubernetes Workloads with Node Swap

> Source: devops | Category: infrastructure | 2026-10-06T01:33:38Z

Scaling Kubernetes Workloads with Node Swap

Memory is often the first hard limit a Kubernetes cluster hits.
Nodes run out of RAM long before they run out of CPU, and the new wave of agentic AI workloads makes this worse.
These workloads demand large memory footprints to start up and run untrusted code, then sit idle waiting for the next prompt.
That idle but resident memory is expensive, and it caps how many pods a node can hold. This is where swap helps. Kubernetes support for running nodes with swap enabled reached General Availability in v1.34, and by backing that swap with fast NVMe solid state drives (SSDs), a node can page out dormant memory and pack in far more pods.
This post explains how we benchmarked that approach across three workloads, including CI/CD kernel builds, sandboxed headless browsers, and isolated Python runtimes; we found density gains of up to 3×, often with little or no latency cost. 
 The node density problem    The Kubernetes ecosystem has reached a fundamental physical resource constraint: the strict limits of hardware memory versus the growing demand for dynamic, bursty workloads in the new agentic era. 
 Historically, administrators provisioning memory-intensive workloads encountered a persistent dilemma: set memory limits too high and you waste expensive infrastructure on idle RAM; set them too low and you risk Out-Of-Memory (OOM) kills. 
 This conflict is amplified when deploying autonomous AI agents using secure execution environments like the   agent-sandbox   framework. These agentic pods require large memory footprints to initialize and execute untrusted code. However, after their burst of activity, they typically enter long-tail idle phases waiting for user prompts. Keeping this idle state in physical RAM caps cluster density and makes AI infrastructure expensive to run. 
 The solution: Kubernetes node swap    With the introduction of Kubernetes' support for running nodes with swap enabled (which reached General Availability in v1.34), this paradigm shifts. By enabling
