---
title: "[kubernetes] See your serverless: introducing the Headlamp plugin for Knative"
url: "https://kubernetes.io/blog/2026/06/25/headlamp-knative-plugin/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-06-26T08:21:52Z"
metadata:
  {}
---

# [kubernetes] See your serverless: introducing the Headlamp plugin for Knative

> Source: devops | Category: infrastructure | 2026-06-26T08:21:52Z

See your serverless: introducing the Headlamp plugin for Knative

Headlamp  is an open-source, extensible Kubernetes SIG UI project designed to let you explore, manage, and debug cluster resources. 
  Knative  brings serverless workloads to Kubernetes, handling traffic routing, autoscaling, and revision management so teams can deploy and iterate without fighting infrastructure. But operating Knative workloads day-to-day can be difficult, there's still a lot of jumping between the  kn  CLI,  kubectl , and the Kubernetes UI to get a full picture of what's running. 
 We built the  Headlamp Knative plugin  to bridge that very gap, allowing operators to inspect, understand and act on their workloads all from a single place. This plugin was built as part of the LFX mentorship. Here's a tour of what we shipped. 
 Here is a short walkthrough of the Knative plugin for Headlamp: 
 
  
 
 Integrating Knative resources with Headlamp's map view    Headlamp's resource mapping works for Knative CRDs too. You can see how KServices, Revisions, and DomainMappings relate to each other in a single graph view. 
   
 KService management: edit traffic splits, restart pods, and view logs    A KService is the top-level resource in Knative: it manages the lifecycle of Routes, Configurations, Revisions, and everything needed to run and expose your application. 
 The plugin gives KServices a full detail view with an  Edit Mode  toggle for making live changes to traffic splits, autoscaling annotations, and more. Common actions like viewing the YAML, opening logs, triggering a redeploy, or restarting backing pods are surfaced in the header, gated by your current RBAC permissions. 
   
 Traffic splitting: route across revisions for gradual rollouts and testing    Knative makes it possible to route traffic across multiple Revisions of the same service. This is useful for canary releases, gradual rollouts, tagged preview URLs, and A/B testing. 
 The plugin shows the traffic assigned to each Revision, the latest ready Revision, readiness status, age, and config
