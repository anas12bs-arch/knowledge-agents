---
title: "Show HN: Durable Actors – OSS Durable Objects with configurable compute"
url: "https://github.com/TerseAI/durable-actors"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-10-07T21:24:14Z"
metadata:
  score: "29"
---

# Show HN: Durable Actors – OSS Durable Objects with configurable compute

> Source: hackernews | Category: news | 2026-10-07T21:24:14Z

Score: 29 | Comments: 20

Hi HN, we&#x27;re Thomas and Olivier from Terse (<a href="https:&#x2F;&#x2F;www.useterse.ai&#x2F;">https:&#x2F;&#x2F;www.useterse.ai&#x2F;</a>) We&#x27;ve built Durable Actors, an open-source alternative to Cloudflare&#x27;s Durable Objects.<p>A Durable Object&#x2F;Actor is a tiny server that handles one request at a time and has its own SQLite database. There&#x27;s exactly one of each in the world and it is addressed by name.<p>This is the perfect primitive for deploying multiplayer agents. Each agent can have its own Durable Actor, and each user can connect to that Actor via websocket. This is fully horizontally scalable. Your users can deploy and share agents at will without putting pressure on a central DB or websocket server.<p>Durable Actors are also great for coordinating agents within a system. Since only one request is handled at a time, you can protect critical data such as a CRM and allow multiple agents to run concurrently without worrying about data races.<p>The only alternative to this is Cloudflare&#x27;s Durable Objects. However, there is extreme lock in (they pull you into D1, R2 + workers as well) and it wasn&#x27;t originally built for agentic workfloads when it was released 5 years ago.<p>Some notable projects built on Durable Objects include RampInspect, OpenInspect as well as the multiplayer frameworks Liveblocks and PartyKit. You can now build these kinds of projects on Durable Actors.<p>Durable Actors is a version of DO that is built for concurrent agentic workloads. It is fully open source (MIT License) and includes a helm chart for you to easily self-host.<p>Some key features:<p>- Configurable compute: Specify CPU, RAM, data residency, idle-timeouts all in a decorator<p>- No outer worker: We generate a type-safe client that you can just plug into your existing tech stack.<p>- (coming soon, like today) Export SQLite table via CLI + MCP for exposing OLTP logs to your agent to help you debug.<p>And our Performance Numbers (all p95):<p>- Durable write: 85.6ms<p>- Stateful Read (data in sqlite): 2.14ms<p>- Actor Warm up: 334ms<p>Here is a little counter demo so you can see the latency yourself: <a href="https:&#x2F;&#x2F;demo.useterse.ai&#x2F;">https:&#x2F;&#x2F;demo.useterse.ai&#x2F;</a><p>Would love your feedback!
