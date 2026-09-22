---
title: "[hacker-news-sec] New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory"
url: "https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-09-22T14:50:40Z"
metadata:
  {}
---

# [hacker-news-sec] New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory

> Source: security | Category: security | 2026-09-22T14:50:40Z

New Linux Kernel Flaw Gives ARM64 KVM Guests Read-Write Access to Host Memory

A new flaw in the Linux kernel's KVM virtualization code for ARM64 processors can leave a freed piece of host memory exposed to a guest virtual machine on hosts with nested virtualization enabled.

The bug, tracked as&nbsp;CVE-2026-89775, allows a guest to read and write host kernel memory, and the researcher who found it says it can be used to escape the guest and run code on the host machine.
