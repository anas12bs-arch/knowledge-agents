---
title: "Show HN: WaveHouse – Supabase for ClickHouse"
url: "https://wavehouse.dev"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-20T19:24:02Z"
metadata:
  score: "6"
---

# Show HN: WaveHouse – Supabase for ClickHouse

> Source: hackernews | Category: news | 2026-08-20T19:24:02Z

Score: 6 | Comments: 0

While building an IoT telemetry solution, we ran into hurdles with Clickhouse. For one, you can&#x27;t insert quickly AND durably into Clickhouse without setting up something like Kafka, which gets complicated for quick projects wanting to make use of Clickhouse&#x27;s powerful features. Then, trying to actually query Clickhouse and show data in a UI required a whole backend API to handle auth and permissions.<p>We figured that all these parts together – fast, durable ingest, row-level and column-level security and roles, and realtime streaming – were a lot of scaffolding to have to rebuild for every project we wanted to use Clickhouse in. So, we built them all into a single Go binary to be deployed alongside Clickhouse, to help lower Clickhouse&#x27;s barrier to entry. We call it WaveHouse.<p>Would love any feedback as we work on improving and adding more features to this OSS project!
