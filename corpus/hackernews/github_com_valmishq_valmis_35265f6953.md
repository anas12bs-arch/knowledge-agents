---
title: "Show HN: I built an open-source alternative to Claude Cowork"
url: "https://github.com/valmishq/valmis"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-02T15:26:45Z"
metadata:
  score: "5"
---

# Show HN: I built an open-source alternative to Claude Cowork

> Source: hackernews | Category: news | 2026-07-02T15:26:45Z

Score: 5 | Comments: 0

Hey HN,<p>A few months ago, I tried to automate some of my work with the popular AI agent OpenClaw, and then I quickly realized how difficult it is to get it to work with APIs and third-party services securely, which is essential for a lot of work-related tasks.<p>Then I realized OpenClaw is more of a personal assistant and it was not designed to get actual work done as a coworker. So I started to build Valmis, an alternative to OpenClaw that works with more than 100 apps and services, with security being the priority.<p>Valmis addresses the security issue by designing a proxy system: dockerized agent runtime can only request the host machine to make API requests by providing the relevant credential ID. The host then makes the actual request and returns the JSON data to the agent runtime. With this design, you can even turn off the internet access of the agent container while making it work.<p>Our proxy system now supports 100+ business and productivity integrations, including all Google Workspace apps, Slack, Notion, HubSpot, Salesforce, and Figma.<p>One of the coolest features of Valmis is the automated workflow. You can automate multi-step workflows using our workflow builder. Each workflow can be triggered by cron, webhooks, app events, and it supports conditions and loops.<p>I&#x27;d be happy to answer any questions in the comment section.
