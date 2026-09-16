---
title: "[devops-com] How I Consolidated Duplicate Delivery Pipelines With Parameters and Build Tags"
url: "https://devops.com/how-i-consolidated-duplicate-delivery-pipelines-with-parameters-and-build-tags/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "devops-com"]
date: "2026-09-16T22:20:56Z"
metadata:
  {}
---

# [devops-com] How I Consolidated Duplicate Delivery Pipelines With Parameters and Build Tags

> Source: devops | Category: infrastructure | 2026-09-16T22:20:56Z

How I Consolidated Duplicate Delivery Pipelines With Parameters and Build Tags

Two modules in a repository had near-identical Azure DevOps build and release definitions. A third would have required another pair. The delivery chain used five definitions: one change decider, two builds, and two releases. I consolidated it into one decider, one generic build, and one release with a deployment stage for each onboarded module. The [&#8230;]
