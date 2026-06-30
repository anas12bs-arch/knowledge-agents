---
title: "[infoq] Article: Scaling Java-Based Real-Time Systems: The Hidden Tradeoffs of Event-Driven Design"
url: "https://www.infoq.com/articles/tradeoffs-event-driven-design/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-06-30T11:19:30Z"
metadata:
  {}
---

# [infoq] Article: Scaling Java-Based Real-Time Systems: The Hidden Tradeoffs of Event-Driven Design

> Source: engineering | Category: engineering | 2026-06-30T11:19:30Z

Article: Scaling Java-Based Real-Time Systems: The Hidden Tradeoffs of Event-Driven Design

Event-driven architecture promises scalability, but in Java-based real-time systems the tradeoffs only surface in production. Drawing on a Java/Kafka contact center platform handling 80k BHCC across 10k agents, this article details where the design breaks down—state management, partition limits, deduplication, JVM tuning, cascading consumer failures—and the Redis-backed patterns that fixed each.   By Sagar Deepak Joshi
