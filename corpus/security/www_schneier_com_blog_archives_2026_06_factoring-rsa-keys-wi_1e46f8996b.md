---
title: "[schneier] Factoring RSA Keys with Many Zeros"
url: "https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-06-29T17:29:12Z"
metadata:
  {}
---

# [schneier] Factoring RSA Keys with Many Zeros

> Source: security | Category: security | 2026-06-29T17:29:12Z

Factoring RSA Keys with Many Zeros

Interesting research on a  new class  of weak RSA keys: keys with lots of zeros. It turns out that these keys are out in the wild. 
  The badkeys project is an open-source service that checks public keys for known vulnerabilities. While developing this tool, Hanno collected a massive number of real-world keys from public sources, including Certificate Transparency logs, internet-wide TLS and SSH scans, PGP keys, and many others. By searching this dataset for unexpectedly sparse RSA moduli, we uncovered a large number of keys in the wild with the patterns in Figure 1...
