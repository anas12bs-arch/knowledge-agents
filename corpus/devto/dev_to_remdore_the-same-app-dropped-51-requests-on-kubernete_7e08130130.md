---
title: "The same app dropped 51 requests on Kubernetes and none on DigitalOcean's App Platform"
url: "https://dev.to/remdore/the-same-app-dropped-51-requests-on-kubernetes-and-none-on-digitaloceans-app-platform-12mc"
source: "devto"
category: "news"
tags: ["devto", "webdev", "tech-article"]
date: "2026-10-09T18:50:35Z"
metadata:
  tag: "webdev"
---

# The same app dropped 51 requests on Kubernetes and none on DigitalOcean's App Platform

> Source: devto | Category: news | 2026-10-09T18:50:35Z

I deployed the worst version of my app, one that exits the instant it gets SIGTERM, to App Platform and redeployed it four times under load. 278,014 requests, none lost to a deploy. Then I found the one window where requests still fail, and the setting that closes it.

Reactions: 7
