---
title: "[kubernetes] Spotlight on SIG Apps"
url: "https://kubernetes.io/blog/2026/09/22/sig-apps-spotlight/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-09-22T23:43:09Z"
metadata:
  {}
---

# [kubernetes] Spotlight on SIG Apps

> Source: devops | Category: infrastructure | 2026-09-22T23:43:09Z

Spotlight on SIG Apps

As Kubernetes adoption has grown, the conversation has shifted beyond running containers to managing increasingly complex application lifecycles. Modern platforms support stateless web services, stateful databases, batch processing, AI workloads, and platform services. At the same time, they must remain reliable during upgrades, scaling events, and infrastructure failures. 
 Every Kubernetes user relies on SIG Apps, whether they realize it or not. Deployments, StatefulSets, DaemonSets, Jobs, and CronJobs form the foundation of how applications are deployed, updated, scaled, and operated across the Kubernetes ecosystem. 
 SIG Apps is focused on improving workload resilience, refining application lifecycle management, and addressing the operational challenges that emerge when applications encounter node failures, rollout disruptions, and increasingly complex infrastructure environments. 
 In this spotlight, we sit down with two of the three SIG Apps chairs   Janet Kuo   and   Maciej Szulik   to discuss the evolution of Kubernetes workload management, the challenges of balancing application reliability with operational simplicity, and the future of application lifecycle management within one of Kubernetes’ most influential Special Interest Groups. 
 Introducing SIG Apps     Natalie Fisher: Can you introduce yourself, your role, and how you got involved in SIG Apps?  
 Janet Kuo: I'm a Senior Staff Software Engineer at Google and have been a Kubernetes maintainer since 2015, joining the community just as we were racing toward the 1.0 launch. In those early days, my focus was on building the core Workloads API, specifically developing controllers like Deployment, ReplicaSet, StatefulSet, and DaemonSet, defining their rollout behaviors, and bringing them from initial designs to GA. That hands-on work was my entry point into SIG Apps. 
 Since then, I've stayed deeply involved in both the technical and community sides of Kubernetes. I have led SIG Apps as Co-Chair and Tec
