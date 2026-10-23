---
title: "[schneier] Compromised TLS Certificates"
url: "https://www.schneier.com/blog/archives/2026/10/compromised-tls-certificates.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-10-23T16:17:30Z"
metadata:
  {}
---

# [schneier] Compromised TLS Certificates

> Source: security | Category: security | 2026-10-23T16:17:30Z

Compromised TLS Certificates

The Indian CA eMudhra Limited has eight TLS certificates with  laughably weak private keys : 
  The compromised eMudhra keys were defective at a level that’s challenging the imagination of many of the engineers studying the incident. A normal size for a NIST P-384 elliptic curve cryptography private key contains roughly 384 bits of entropy, a size allowing almost 2 384 , or a number with 116 digits, different possibilities. The private key sizes of the compromised keys ranged from 3 to 8 bits. Astonishingly, the private keys were 4, 56, 66, 115, 155, 156, 230, 237...
