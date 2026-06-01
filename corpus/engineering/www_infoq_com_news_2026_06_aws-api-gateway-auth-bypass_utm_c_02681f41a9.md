---
title: "[infoq] A Trailing Slash Bypassed AWS API Gateway Authorization"
url: "https://www.infoq.com/news/2026/06/aws-api-gateway-auth-bypass/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-01T19:24:00Z"
metadata:
  {}
---

# [infoq] A Trailing Slash Bypassed AWS API Gateway Authorization

> Source: engineering | Category: engineering | 2026-06-01T19:24:00Z

A Trailing Slash Bypassed AWS API Gateway Authorization

A security researcher found that adding a trailing slash to AWS HTTP API paths bypassed Lambda authorizer authentication entirely, enabling unauthenticated wire transfers at a fintech. The root cause is a path normalization mismatch between HTTP API's greedy route matching and its authorization layer. The same vulnerability class appeared in gRPC-Go via CVE-2026-33186.   By Steef-Jan Wiggers
