---
title: "[high-scalability] Lessons Learned Running Presto at Meta Scale"
url: "http://highscalability.com/blog/2023/7/16/lessons-learned-running-presto-at-meta-scale.html"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "high-scalability"]
date: "2026-05-30T15:08:40Z"
metadata:
  {}
---

# [high-scalability] Lessons Learned Running Presto at Meta Scale

> Source: engineering | Category: engineering | 2026-05-30T15:08:40Z

Lessons Learned Running Presto at Meta Scale

Presto    is a free, open source SQL query engine. We&rsquo;ve been using it at Meta for the past ten years, and learned a lot while doing so. Running anything at scale - tools, processes, services - takes problem solving to overcome unexpected challenges. Here are four things we learned while scaling up Presto to Meta scale, and some advice if you&rsquo;re interested in running your own queries at scale.  
  Scaling Presto rapidly to meet growing demands: What challenges did we face?  
 &nbsp; 
  Deploying new Presto releases
