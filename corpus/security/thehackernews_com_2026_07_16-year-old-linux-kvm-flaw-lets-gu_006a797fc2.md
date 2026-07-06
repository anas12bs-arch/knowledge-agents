---
title: "[hacker-news-sec] 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems"
url: "https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-07-06T20:14:23Z"
metadata:
  {}
---

# [hacker-news-sec] 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

> Source: security | Category: security | 2026-07-06T20:14:23Z

16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

A use-after-free bug in Linux's KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed 'Januscape' and tracked as&nbsp;CVE-2026-53359, the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased exploit
