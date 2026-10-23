---
title: "[traversy] A Bad Week for the Web: What’s Confirmed and What to Do"
url: "https://www.youtube.com/watch?v=RE2c_eH0Sq4"
source: "youtube"
category: "video"
tags: ["youtube", "video", "tutorial", "traversy"]
date: "2026-10-23T16:17:50Z"
metadata:
  {}
---

# [traversy] A Bad Week for the Web: What’s Confirmed and What to Do

> Source: youtube | Category: video | 2026-10-23T16:17:50Z

A Bad Week for the Web: What’s Confirmed and What to Do

Three separate security incidents hit three different parts of the stack in one week: PHP2Shell, the Railway environment variable breach, and eMudhra's compromised certificate authority keys. Here's what happened, what's actually confirmed, and what you need to do, if anything. As promised, the incident numbers and dates are below.

Facts as of October 23, 2026. These stories are still moving, so check the sources for updates.

PHP2SHELL
- CVE-2026-109618 (GHSA-w8hw-w9fx-j79w) and CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp)
- CVSS v4.0 9.2, Critical. The 10.0 going around came from the leak, not from PHP.
- Unauthenticated remote code execution in PHP itself, affecting versions back to 5.4
- Oct 17: Amazon saw the first exploitation attempt on its honeypots
- Oct 20: details leaked ahead of the planned Oct 22 disclosure
- Oct 21: fixes released and CISA published an alert
- Fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. One-time source patches exist for 7.4, 8.0 and 8.1.
- No confirmed break-ins reported as of Oct 22
- Found by Wiz Research, Calif and OpenAI's security team

NODE.JS
- Oct 21: security release fixing 10 CVEs
- CVE-2026-111497: Brotli decompression flaw, rated High, no workaround
- Fixed in Node 22.23.4, 24.22.1 and 26.12.1. The same release blocks the eight eMudhra intermediates.

RAILWAY
- Status page incident QH8L8B3E
- Oct 21: Railway disclosed that an unauthorized party got into the systems that store customer environment variables and, for some customers, obtained the decrypted values. Builds and deploys were paused.
- Oct 22: builds back for Pro and Enterprise (06:29 UTC) and Hobby (21:08 UTC)
- Oct 23: builds and deployments running normally on every plan, including Free and Trial (08:09 UTC update)
- Earlier platform incidents: Vercel (disclosed Apr 1
