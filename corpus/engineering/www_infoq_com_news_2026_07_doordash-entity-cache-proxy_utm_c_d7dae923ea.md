---
title: "[infoq] DoorDash Uses Envoy and Valkey for a 1.5M RPS Proxy Cache with 99.99999% Availability"
url: "https://www.infoq.com/news/2026/07/doordash-entity-cache-proxy/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-20T14:27:06Z"
metadata:
  {}
---

# [infoq] DoorDash Uses Envoy and Valkey for a 1.5M RPS Proxy Cache with 99.99999% Availability

> Source: engineering | Category: engineering | 2026-07-20T14:27:06Z

DoorDash Uses Envoy and Valkey for a 1.5M RPS Proxy Cache with 99.99999% Availability

DoorDash has developed Entity Cache, a transparent proxy caching platform built on Envoy and Valkey to reduce redundant service-to-service requests across its microservices architecture. Operating within DoorDash’s service mesh, the platform serves over 1.5M requests per second with 99.99999% availability through caching, event-driven invalidation, failure handling, and performance optimizations.   By Leela Kumili
