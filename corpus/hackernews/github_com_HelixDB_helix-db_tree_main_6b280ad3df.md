---
title: "Show HN: HelixDB – A graph database built on object storage"
url: "https://github.com/HelixDB/helix-db/tree/main"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-10T21:21:00Z"
metadata:
  score: "64"
---

# Show HN: HelixDB – A graph database built on object storage

> Source: hackernews | Category: news | 2026-06-10T21:21:00Z

Score: 64 | Comments: 27

Hey HN, it’s been just over a year since we launched HelixDB (<a href="https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43975423">https:&#x2F;&#x2F;news.ycombinator.com&#x2F;item?id=43975423</a>), a project a friend and I started in college. It’s an OLTP graph database built on object-storage, with native vector search and full-text search (FTS).<p>Why graph, vector and FTS? Graph databases provide a natural cognitive model for data, vectors allow for a semantic understanding of the entities and relationships in the graph, and FTS provides more specific filtering. Many AI-driven applications attempt to combine all of these functionalities by stitching together multiple disconnected systems, but even then there’s no native way to perform joins or queries that span all systems. You still need to handle this logic at the application level.<p>Helix started as a graph DB, but we moved to a hybrid graph&#x2F;vector approach after attempting to build an AI memory system, which led us down the GraphRAG and HybridRAG rabbit hole, where we would need separate graph and vector databases.<p>We knew scalability would be a challenge at each stage of our product&#x27;s development, however our initial focus this past year was to prove out the product through local deployments and was only meant to be run on a single node. Scaling graph DBs remained a difficult and expensive problem we’d have to solve later.
Some common ways other graph DBs solve scaling is by duplicating entire datasets across distributed machines (extremely expensive per node), or by sharding the data.<p>Sharding databases is effective and affordable, however, graph data doesn’t have explicit partitions like relational databases do. For example, sharding a relational DB involves splitting up tables. When it comes to graph DBs, the edges can span across any of the partitions, and hopping across multiple machines when traversing nodes is ineffective and computationally expensive.<p>Replicating graph DBs for high availability and better throughput drastically increases the operational cost of the db and still has a limit of how big you can vertically scale. The workload that we’re used for requires storing a huge amount of data for agents, where only a subset of that data is ever needed at any one time. So rather than having the whole thing in memory, we can store it all in object-storage and get the bits we need when they’re needed.<p>Agents benefit from better context, which is achieved from more and better data (more relationships etc). By using S3 as the persistence&#x2F;data layer there is <i>no limit</i> to how big the graph can be or how many relationships you can have, and we can scale to serve throughput and requests by horizontally spinning up nodes and caching relevant subsets of the graph on each node. This way, you get extremely low latency for “hot” data and a p99 of ~100ms for writes and ~50ms for reads from cold storage (S3). Plus you get the benefit of dirt cheap storage.<p>Workloads that HelixDB is currently supporting:
- Huge amounts of data (TBs) from which the agents need to search and traverse over
- Offering affordable graph storage for companies where cost of graph data is a bottleneck
- Consolidating multiple databases, enabling AI agents to have autonomy over companies, helping them become more autonomous.
- AI memory
- Company brains<p>We’re currently working on our own generalised AI memory layer which will use HelixDB under the hood and be completely open-source. Also, we’re finishing up on pre-filtering for vector search which will allow you to pre-filter based on relationships in the graph, metadata, and sub-graphs. And lastly, GA cloud will be available in the coming weeks.<p>If you want to run Helix locally (either on-disk or in-memory), you can find more info on our github (<a href="https:&#x2F;&#x2F;github.com&#x2F;HelixDB&#x2F;helix-db" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;HelixDB&#x2F;helix-db</a>) or via our docs (<a href="https:&#x2F;&#x2F;docs.helix-db.com&#x2F;database&#x2F;local-development">https:&#x2F;&#x2F;docs.helix-db.com&#x2F;database&#x2F;local-development</a>). If you’re interested in getting started with our distributed cloud, please email us founders@helix-db.com.<p>Many thanks! Comments and feedback welcome!
