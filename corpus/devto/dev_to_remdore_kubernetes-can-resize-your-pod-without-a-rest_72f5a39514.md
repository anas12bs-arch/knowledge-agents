---
title: "Kubernetes can resize your pod without a restart. Your app might not notice."
url: "https://dev.to/remdore/kubernetes-can-resize-your-pod-without-a-restart-your-app-might-not-notice-2a7c"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-08T13:39:40Z"
metadata:
  tag: "devops"
---

# Kubernetes can resize your pod without a restart. Your app might not notice.

> Source: devto | Category: news | 2026-09-08T13:39:40Z

In-place pod resize is GA. I resized CPU and memory on running Node and Java pods and watched what the process inside actually saw. CPU: fine. Memory: the JVM kept its old heap and died with 2 GiB spare.

Reactions: 7
