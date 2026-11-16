---
title: "PostgreSQL 19's pg_plan_advice turned a 28ms query into 264ms under load"
url: "https://dev.to/alexgeorgiev17/postgresql-19s-pgplanadvice-turned-a-28ms-query-into-264ms-under-load-46o5"
source: "devto"
category: "news"
tags: ["devto", "devops", "tech-article"]
date: "2026-11-16T17:33:31Z"
metadata:
  tag: "devops"
---

# PostgreSQL 19's pg_plan_advice turned a 28ms query into 264ms under load

> Source: devto | Category: news | 2026-11-16T17:33:31Z

I tested PostgreSQL 19 RC2's new planner-hint extension, pg_plan_advice: forcing a plan made throughput 9x worse under ten clients, and in every scenario I could construct the planner's own choice already beat anything I forced.

Reactions: 15
