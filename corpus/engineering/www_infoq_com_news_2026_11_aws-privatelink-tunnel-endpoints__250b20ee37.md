---
title: "[infoq] AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account"
url: "https://www.infoq.com/news/2026/11/aws-privatelink-tunnel-endpoints/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-11-18T16:26:06Z"
metadata:
  {}
---

# [infoq] AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account

> Source: engineering | Category: engineering | 2026-11-18T16:26:06Z

AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account

AWS has detailed tunnel endpoints, a PrivateLink endpoint type that gives a consumer VPC access to an entire network segment in another account rather than one resource at a time, over an overlapping address space and with consumer-initiated connections only. The consumer must wrap traffic in GENEVE; only TCP and DNS pass, and access logs cannot attribute traffic to a workload behind the endpoint.   By Steef-Jan Wiggers
