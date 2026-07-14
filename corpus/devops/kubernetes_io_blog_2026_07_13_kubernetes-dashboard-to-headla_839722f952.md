---
title: "[kubernetes] Kubernetes Dashboard to Headlamp: A Step-by-Step Guide"
url: "https://kubernetes.io/blog/2026/07/13/kubernetes-dashboard-to-headlamp/"
source: "devops"
category: "infrastructure"
tags: ["devops", "infrastructure", "cloud", "kubernetes", "kubernetes"]
date: "2026-07-14T03:23:47Z"
metadata:
  {}
---

# [kubernetes] Kubernetes Dashboard to Headlamp: A Step-by-Step Guide

> Source: devops | Category: infrastructure | 2026-07-14T03:23:47Z

Kubernetes Dashboard to Headlamp: A Step-by-Step Guide

1. Before you start: know what is changing    Kubernetes Dashboard and Headlamp both show what is running in a cluster, but they work differently. When Headlamp runs on the desktop, it uses your existing kubeconfig to connect to one or more clusters and can be extended with plugins. When Headlamp runs inside a cluster, it uses a Kubernetes ServiceAccount to access the API and follow RBAC rules. Kubernetes Dashboard, in contrast, only runs in-cluster and always relies on service account tokens. Understanding these models early helps you choose the right setup and permissions. 
 1.1 How Kubernetes Dashboard works    Dashboard is a web app that runs inside your cluster. 
 
 You install it in the cluster, often with Helm. 
 You usually run one Dashboard per cluster. 
 You often reach it with  kubectl port-forward  or an ingress. 
 You log in with a Bearer token. That token is often from a service account. 
 It includes forms that help you create resources. 
 It leans on tables and lists for navigation. 
 
 It feels like this: a UI that lives with the cluster. 
 1.2 How Headlamp works    Headlamp acts more like a Kubernetes client with a UI. 
 
 It can run on your desktop or in a cluster. 
 It reads your kubeconfig, like kubectl does. 
 It can show more than one cluster in one place. 
 It favors YAML when you create or change resources. 
 It includes list views and a visual map. 
 You can add features with plugins. 
 
 Headlamp is a UI that follows your identity, not your cluster. 
 1.3 What stays the same    Many workflows will feel familiar: 
 
 Browse workloads and resources 
 Filter by namespace 
 Inspect YAML, events, and status 
 View logs 
 Take actions your RBAC allows 
 
 1.4 What changes    A few things will feel different: 
 
 Login shifts from pasted tokens to kubeconfig (and sometimes SSO). 
 Creation shifts from forms to &quot;apply YAML.&quot; 
 Multi-cluster becomes normal, not a special case. 
 The map view helps you see how resources connect. 
 
 2. P
