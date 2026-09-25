---
title: "Kubernetes 1.37's kyaml output closes a YAML bug that still deletes data on apply"
url: "https://dev.to/alexgeorgiev17/kubernetes-137s-kyaml-output-closes-a-yaml-bug-that-still-deletes-data-on-apply-527a"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-09-25T15:20:27Z"
metadata:
  tag: "devops"
---

# Kubernetes 1.37's kyaml output closes a YAML bug that still deletes data on apply

> Source: devto | Category: news | 2026-09-25T15:20:27Z

I fed Kubernetes 1.37 a batch of Norway-bug values by hand: 8 got rejected outright, 2 got rejected as numbers, and 2 vanished from the object with no error at all. kyaml output survives all of them.

Reactions: 7
