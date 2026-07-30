---
title: "Show HN: Supapool – a Supabase per coding agent in ~400 ms"
url: "https://supapool.io/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-30T20:17:14Z"
metadata:
  score: "15"
---

# Show HN: Supapool – a Supabase per coding agent in ~400 ms

> Source: hackernews | Category: news | 2026-07-30T20:17:14Z

Score: 15 | Comments: 0

hi HN,<p>I built supapool.io, an ephemeral full copy of supabase&#x27;s services that you can spin up in ~400 ms (Auth, postgres, storage, realtime).<p>so if you run multiple coding agents in parallel in different worktrees, they can now have their own copy of supabase without making changes that conflict with eachother.<p>&gt; why not use supabase docker locally?<p>when I run 3-4 instances locally, my macbook gets hot and sometimes freezes.<p>&gt; why not use supabase branches?<p>branches take minutes to setup, and are designed for persistence. this is expensive, and for a dev environment, it is too slow.<p>&gt; why not use mocks?<p>mocks are bad for agents. i expect agents to test their migrations, SQL against real prod service behavior. agents hallucinate working mocks often. However, upside of mocks is that its faster and runs locally, but with supapool, the upside is less convincing.<p>&gt; how does it work&#x2F;how is this economically viable?<p>starting supabase in 400ms requires a few things:
1. a pool of ready supabase instances running warm, and colocated with region failover (us-east, us-west, europe-west, asia-southeast)
2. fast autoscaling when pool starts to shrink with microVM&#x2F;firecracker
3. gutting strong persistence guarantees. dev agents don&#x27;t need WAL, fsync, PITR, replication. anything for HA on a ephemeral supabase instance is bloat<p>its in beta right now, and i&#x27;m using our gcp credits to bankroll this, so its free. the eventual pricing will be something like $&#x2F;instance second and more cost effective than branching or self hosting&#x2F;maintaining a supabase cluster.<p>would love to get your feedback if you use supabase, and if you think there&#x27;s something better that would fit your local coding agent setup. Thanks!
