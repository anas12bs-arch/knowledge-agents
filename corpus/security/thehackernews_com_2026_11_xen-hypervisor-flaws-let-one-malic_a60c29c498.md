---
title: "[hacker-news-sec] Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory"
url: "https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-11-04T17:28:38Z"
metadata:
  {}
---

# [hacker-news-sec] Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory

> Source: security | Category: security | 2026-11-04T17:28:38Z

Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory

Two flaws in the Xen hypervisor allow a malicious guest virtual machine (VM) to read and write the memory of other VMs on the same host, including dom0.

Dom0 is the VM that, by default, has full permissions and manages the others. Patches are out, and there is no known mitigation, the Xen Project said in an&nbsp;advisory&nbsp;on November 3.

All Xen versions from 4.6 onward are vulnerable,
