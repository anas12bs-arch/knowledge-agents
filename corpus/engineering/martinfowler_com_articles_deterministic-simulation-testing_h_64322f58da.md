---
title: "[martin-fowler] Deterministic Simulation Testing"
url: "https://martinfowler.com/articles/deterministic-simulation-testing.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "martin-fowler"]
date: "2026-11-17T17:57:14Z"
metadata:
  {}
---

# [martin-fowler] Deterministic Simulation Testing

> Source: engineering | Category: engineering | 2026-11-17T17:57:14Z

Deterministic Simulation Testing

Distributed systems are hard to test because partial failures overlap
     with live traffic and the same fault can produce different execution traces
     on different runs.  Unmesh Joshi  describes how
     deterministic simulation testing addresses this by replacing real clocks,
     networks, and storage with simulated components driven by a single-threaded
     execution loop. This allows simulating both hard failures and routine
     slowdowns&#x2014;such as network and disk latency spikes&#x2014;and more importantly
     makes every execution reproducible. This article explains the technique
     using a quorum key-value store as a running example, with code from
     Tickloom, a Java implementation of the approach. 

  more…
