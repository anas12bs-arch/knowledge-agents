---
title: "[infoq] eMudhra Intermediate CA Compromise"
url: "https://www.infoq.com/news/2026/10/emudhra-ca-compromise/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-10-21T23:13:45Z"
metadata:
  {}
---

# [infoq] eMudhra Intermediate CA Compromise

> Source: engineering | Category: engineering | 2026-10-21T23:13:45Z

eMudhra Intermediate CA Compromise

Private keys for eight eMudhra intermediate CA certificates have been compromised, allowing attackers to forge certificates for any site. The keys were revealed due to low entropy, not through a known breach. Browsers blocked them using revocation lists, but other software had to remove the emSign ECC G3 root. Unpatched systems remain exposed to forged certificates, including client auth and mTLS.   By Chris Swan
