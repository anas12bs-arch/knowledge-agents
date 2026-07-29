---
title: "[schneier] Long-Lived Vulnerability in Microsoft Secure Boot"
url: "https://www.schneier.com/blog/archives/2026/07/long-lived-vulnerability-in-microsoft-secure-boot.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-07-29T11:50:55Z"
metadata:
  {}
---

# [schneier] Long-Lived Vulnerability in Microsoft Secure Boot

> Source: security | Category: security | 2026-07-29T11:50:55Z

Long-Lived Vulnerability in Microsoft Secure Boot

Microsoft&#8217;s Secure Boot has had a  serious vulnerability  for most of its existence. 
  An industry-wide standard Microsoft invented to protect Windows, and later Linux, devices from firmware infections has been trivial to bypass for 13 of its 14 years of existence. The discovery was made by researchers at security firm ESET after identifying 11 firmware images, at least one from 2013, that were known to be defective but remained signed by the software company anyway. 
 The images are known as  shims , which were invented to extend Secure Boot to Linux devices and utility software. Using a technique simple enough to be performed by novice hackers, these old, forgotten shims can be used to completely circumvent the protection, which is embedded into the UEFI (Unified Extensible Firmware Interface) of the device&#8217;s motherboard. The gaffe is the result of the failure by Microsoft, which oversees the signing of shims, to revoke the publicly available images once vulnerabilities were found in them...
