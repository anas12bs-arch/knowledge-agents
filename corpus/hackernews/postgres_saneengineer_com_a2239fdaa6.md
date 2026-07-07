---
title: "Show HN: PostgreSQL performance and cost across 23 EC2 instance types"
url: "https://postgres.saneengineer.com"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-07T16:07:03Z"
metadata:
  score: "35"
---

# Show HN: PostgreSQL performance and cost across 23 EC2 instance types

> Source: hackernews | Category: news | 2026-07-07T16:07:03Z

Score: 35 | Comments: 0

Hey! I&#x27;m Andrei.<p>I got frustrated by how people tend to build overcomplicated backend systems, being &quot;motivated&quot; by big tech case studies and popular books.<p>So, I started exploring lean architecture, and building my digital garden of ideas, approaches and data that align with this direction.<p>Here I want to present one of the tools – Sizing tool for PostgreSQL. I&#x27;ve benchmarked PostgreSQL on different EC2 instances and disks, with different initial data sets to see performance that these instances can give you. And I&#x27;ve built a tool to visualize this data, which I welcome you to explore.<p>So, you can put your usual input parameters, like needed RPS and disk size as input, and find out which instance will be the most cost-efficient for your needs.<p>You can read about the methodology here: <a href="https:&#x2F;&#x2F;postgres.saneengineer.com&#x2F;about" rel="nofollow">https:&#x2F;&#x2F;postgres.saneengineer.com&#x2F;about</a><p>I&#x27;ve tested one workload – mixed 90&#x2F;10 read&#x2F;write, and only selected configurations. But it is extensible, and I (and you – benchmark is open source: <a href="https:&#x2F;&#x2F;github.com&#x2F;anivaniuk&#x2F;sanebench" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;anivaniuk&#x2F;sanebench</a>) can run more configurations to have more data represented.<p>Does it look interesting? What workload should I benchmark next?
