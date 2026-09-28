---
title: "[infoq] Meta’s ZGateway Cuts ZippyDB Connections 19x While Handling 1B+ Operations per Second"
url: "https://www.infoq.com/news/2026/09/meta-zgateway-zippydb-proxy/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-09-28T19:25:50Z"
metadata:
  {}
---

# [infoq] Meta’s ZGateway Cuts ZippyDB Connections 19x While Handling 1B+ Operations per Second

> Source: engineering | Category: engineering | 2026-09-28T19:25:50Z

Meta’s ZGateway Cuts ZippyDB Connections 19x While Handling 1B+ Operations per Second

Meta has introduced ZGateway, a stateless proxy for ZippyDB that centralizes connection management, traffic routing, caching, load balancing, and admission control. The gateway handles more than 1 billion operations per second and about 40% of ZippyDB traffic, while Meta’s model estimates a 19x reduction in persistent connections.   By Leela Kumili
