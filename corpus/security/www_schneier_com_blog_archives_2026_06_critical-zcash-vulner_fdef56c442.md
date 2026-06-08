---
title: "[schneier] Critical Zcash Vulnerability Found and Fixed"
url: "https://www.schneier.com/blog/archives/2026/06/critical-zcash-vulnerability-found-and-fixed.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-06-08T21:25:11Z"
metadata:
  {}
---

# [schneier] Critical Zcash Vulnerability Found and Fixed

> Source: security | Category: security | 2026-06-08T21:25:11Z

Critical Zcash Vulnerability Found and Fixed

If you&#8217;re a user&#8212;owner?&#8212;of this cryptocurrency,  this  is important: 
  On May 29, the security researcher Taylor Hornby found a critical vulnerability in Zcash Orchard privacy pool using Claude Opus 4.8. The Zcash team hired Hornby specifically to look for this kind of issue. He found one fast enough to be embarrassing. 
 The Orchard pool is the newest and most advanced shielded transaction system in the cryptocurrency Zcash. Introduced in 2022, it allows users to send and receive ZEC while keeping transaction details private. It uses zero-knowledge proofs to validate transactions without revealing amounts or participants. The bug: a specific check that was supposed to validate transaction inputs wasn&#8217;t actually enforcing the rules it appeared to enforce. An attacker could have exploited the flaw to feed false inputs into that check and generate ZEC from nothing, with the zero-knowledge proof system blessing the fraudulent transaction as valid...
