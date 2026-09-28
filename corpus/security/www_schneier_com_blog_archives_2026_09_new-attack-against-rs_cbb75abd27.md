---
title: "[schneier] New Attack Against RSA"
url: "https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-09-28T12:03:35Z"
metadata:
  {}
---

# [schneier] New Attack Against RSA

> Source: security | Category: security | 2026-09-28T12:03:35Z

New Attack Against RSA

ArsTechnica is  reporting  on a &#8220;new&#8221; attack against RSA, one that bypasses factoring. 
 First, this attack isn&#8217;t new. The original research is from  2007 . What is new is the implementation. 
 Second, it is a forgery attack. It allows an attacker to forge digital signatures. It does not recover the private key from the public key. 
 Third, the attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in practice. 
 Fourth, speed is all relative. This is not a polynomial-time algorithm; it&#8217;s a subexponential-time algorithm. But it is somewhat faster than factoring. The authors were able to forge messages for 1024-bit RSA with 1380 CPU core-years (over five real-world months)...
