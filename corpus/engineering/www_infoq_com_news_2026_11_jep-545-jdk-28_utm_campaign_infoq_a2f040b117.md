---
title: "[infoq] JEP 545 Moves ZGC Memory Preparation off the Startup Path in JDK 28"
url: "https://www.infoq.com/news/2026/11/jep-545-jdk-28/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-23T19:34:25Z"
metadata:
  {}
---

# [infoq] JEP 545 Moves ZGC Memory Preparation off the Startup Path in JDK 28

> Source: engineering | Category: engineering | 2026-11-23T19:34:25Z

JEP 545 Moves ZGC Memory Preparation off the Startup Path in JDK 28

JEP 545, Faster Startup and Warmup with ZGC, has been integrated into JDK 28, moving heap memory preparation onto concurrent worker threads. ZGC now pre-touches memory as it expands and upgrades small pages to large ones on Linux 6.1 and later, but the 2 MB initial heap behind the JEP's 38% startup and 90% warmup gains requires the adaptive heap sizing flag from JEP 546, which is off by default.   By A N M Bazlur Rahman
