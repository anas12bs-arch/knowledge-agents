---
title: "[infoq] Pods as Workers, Not Agents: Rethinking the Deployment Unit for AI Agents on Kubernetes"
url: "https://www.infoq.com/news/2026/08/pod-deployment-unit-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-08-06T06:14:23Z"
metadata:
  {}
---

# [infoq] Pods as Workers, Not Agents: Rethinking the Deployment Unit for AI Agents on Kubernetes

> Source: engineering | Category: engineering | 2026-08-06T06:14:23Z

Pods as Workers, Not Agents: Rethinking the Deployment Unit for AI Agents on Kubernetes

Running AI agents on Kubernetes raises a key question: should each agent get its own Pod? The kagent project argues no—agents are bursty, short-lived, can spawn subagents, and may wait for human approval, making one Pod per agent wasteful. Agent-substrate adds a control plane to schedule logical “Actors” onto long-lived worker Pods.   By Mark Silvester
