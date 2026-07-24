---
title: "[devops-com] When the Message Broker Becomes the Bottleneck: Scaling Push and SMS With MongoDB Polling"
url: "https://devops.com/when-the-message-broker-becomes-the-bottleneck-scaling-push-and-sms-with-mongodb-polling/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "devops-com"]
date: "2026-07-24T06:12:37Z"
metadata:
  {}
---

# [devops-com] When the Message Broker Becomes the Bottleneck: Scaling Push and SMS With MongoDB Polling

> Source: devops | Category: infrastructure | 2026-07-24T06:12:37Z

When the Message Broker Becomes the Bottleneck: Scaling Push and SMS With MongoDB Polling

A back-end team extracted notification delivery from a large Ruby monolith into a centralized Go service, only to discover that their shared RabbitMQ cluster could not reliably support the new workload. Here&#8217;s how they solved the problem using MongoDB as a polling queue and the trade-offs that came with it. The Scaling Problem Inside the [&#8230;]
