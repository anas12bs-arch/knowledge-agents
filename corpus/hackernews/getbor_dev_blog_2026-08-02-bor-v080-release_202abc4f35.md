---
title: "Show HN: Bor – Open-source policy management for Linux desktops"
url: "https://getbor.dev/blog/2026-08-02-bor-v080-release/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-02T10:19:34Z"
metadata:
  score: "4"
---

# Show HN: Bor – Open-source policy management for Linux desktops

> Source: hackernews | Category: news | 2026-08-02T10:19:34Z

Score: 4 | Comments: 0

Hi HN! I&#x27;ve been working on Bor, an open-source system for centralized Linux desktop management.<p>Bor consists of a lightweight Go agent and a central server. Policies are streamed to clients over mTLS&#x2F;gRPC in real time—no polling—and currently support Firefox, Chrome, KDE, dconf, polkit and package management, with more coming.<p>Version 0.8 introduces several new policy types - Thunderbird, Microsoft Edge for Business and FirewallD zones, along with a number of improvements and fixes.<p>I&#x27;d love feedback on the architecture, policy model, and whether this is something you&#x27;d consider for managing Linux workstations.
