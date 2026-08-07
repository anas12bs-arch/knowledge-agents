---
title: "[hacker-news-sec] New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts"
url: "https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "hacker-news-sec"]
date: "2026-08-07T00:28:10Z"
metadata:
  {}
---

# [hacker-news-sec] New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts

> Source: security | Category: security | 2026-08-07T00:28:10Z

New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts

Zapscape, a new Linux kernel vulnerability, could allow an attacker with kernel privileges inside an L1 guest virtual machine (VM) to escape KVM isolation and execute code on the host. The risk applies when nested virtualization is exposed to untrusted guests.

The flaw is tracked as&nbsp;CVE-2026-64561&nbsp;and affects KVM/x86's shadow memory management unit (MMU), which manages shadow page
