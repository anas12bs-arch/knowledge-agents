---
title: "[infoq] Rx.NET 7.0 Reduces Deployment Size by Splitting Windows UI Support"
url: "https://www.infoq.com/news/2026/08/rx-net-7/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-08-14T08:53:36Z"
metadata:
  {}
---

# [infoq] Rx.NET 7.0 Reduces Deployment Size by Splitting Windows UI Support

> Source: engineering | Category: engineering | 2026-08-14T08:53:36Z

Rx.NET 7.0 Reduces Deployment Size by Splitting Windows UI Support

Rx.NET 7.0 has been released with a narrowly focused change aimed at reducing deployment size for Windows applications. The new version separates WPF, Windows Forms, UWP, and Windows Runtime integration from the main System.Reactive package, avoiding cases where self-contained applications could acquire tens of megabytes of unused framework dependencies.   By Edin Kapić
