---
title: "[kubernetes] Kubernetes v1.36: Mixed Version Proxy Graduates to Beta"
url: "https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-05-30T15:08:37Z"
metadata:
  {}
---

# [kubernetes] Kubernetes v1.36: Mixed Version Proxy Graduates to Beta

> Source: devops | Category: infrastructure | 2026-05-30T15:08:37Z

Kubernetes v1.36: Mixed Version Proxy Graduates to Beta

Back in Kubernetes 1.28, we introduced the  Mixed Version Proxy (MVP)  as an Alpha feature (under the feature gate  UnknownVersionInteroperabilityProxy ) in a  previous blog post . The goal was simple but critical: make cluster upgrades safer by ensuring that requests for resources not yet known to an older API server are correctly routed to a newer peer API server, instead of returning an incorrect  404 Not Found . 
 We are excited to announce that the Mixed Version Proxy is moving to Beta in Kubernetes 1.36 and will be enabled by default! The feature has evolved significantly since its initial release, addressing key gaps and modernizing its architecture. 
 Here is a look at how the feature has evolved and what you need to know to leverage it in your clusters. 
 What problem are we solving?    In a highly available control plane undergoing an upgrade, you often have API servers running different versions. These servers might serve different sets of APIs (Groups, Versions, Resources).
Without MVP, if a client request lands on an API server that does not serve the requested resource (e.g., a new API version introduced in the upgrade), that server returns a  404 Not Found . This is technically incorrect because the resource is available in the cluster, just not on that specific server. This can lead to serious side effects, such as mistaken garbage collection or blocked namespace deletions.
MVP solves this by proxying the request to a peer API server that can serve it. 
 
sequenceDiagram
participant Client
participant API_Server_A as API Server A (Older/Different)
participant API_Server_B as API Server B (Newer/Capable)
Client->>API_Server_A: 1. Request for Resource (e.g., v2)
Note over API_Server_A: Determines it cannot serve locally
API_Server_A->>API_Server_A: 2. Looks up capable peer in Discovery Cache
API_Server_A->>API_Server_B: 3. Proxies request (adds x-kubernetes-peer-proxied header)
API_Server_B->>API_Server_B: 4. Processes request locally
API_Server_B-->
