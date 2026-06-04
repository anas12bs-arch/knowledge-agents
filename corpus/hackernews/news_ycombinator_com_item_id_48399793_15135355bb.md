---
title: "Ask HN: Why is it still so hard for LLMs to query NoSQL databases?"
url: "https://news.ycombinator.com/item?id=48399793"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-04T22:57:35Z"
metadata:
  score: "3"
---

# Ask HN: Why is it still so hard for LLMs to query NoSQL databases?

> Source: hackernews | Category: news | 2026-06-04T22:57:35Z

Score: 3 | Comments: 0

LLMs are good at SQL. It&#x27;s precise, expressive, and unambiguous. If you connect an MCP server to Postgres, then the agent can query it directly. The same cannot be said for NoSQL, and given how many people use NoSQL databases, I’m surprised there isn’t more discussion about it.<p>Part of the problem is diversity. MongoDB, DynamoDB, Cassandra, Redis, and Neo4j all have different query models. There&#x27;s no shared interface for an LLM to reason about. So instead of writing a query, the agent has to write code: SDK calls, manual aggregation, pagination logic. It becomes more complex, harder to review, and quickly breaks on anything non-trivial.<p>We ran into this problem with DynamoDB specifically and ended up building our own solution. I wrote about it here if anyone&#x27;s curious: https:&#x2F;&#x2F;dynamosql.hashnode.dev&#x2F;why-llm-agents-still-can-t-query-nosql-databases. But I&#x27;m more interested in how others have handled this. Why is it still such an unresolved problem?
