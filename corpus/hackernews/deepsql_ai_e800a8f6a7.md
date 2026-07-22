---
title: "Show HN: DeepSQL – A self-hostable AI DBA agent for Postgres and MySQL"
url: "https://deepsql.ai/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-22T17:06:59Z"
metadata:
  score: "7"
---

# Show HN: DeepSQL – A self-hostable AI DBA agent for Postgres and MySQL

> Source: hackernews | Category: news | 2026-07-22T17:06:59Z

Score: 7 | Comments: 4

Hi HN - I&#x27;m Venkat, founder of Stayflexi (YC), CMU CS grad and Ex-Oracle Query Engine team (patents in core databases)<p>DeepSQL started as an internal tool to stop our own databases from becoming the bottleneck they were becoming (13,000+ hotels in production). It worked well enough that we&#x27;re releasing it.<p>DeepSQL is an AI agent that operates a database the way a senior DBA and Data Engineer would<p>1. Fixes slow queries (we cutdown DB spend by 4x)
2. Fixes DB bloat (blocks unnecessary schema changes, in vibecoded setup)
2. BI dashboards(we removed spend on tableau, retool and appsmith)
3. Security (We could redact access to sensitive, PII data to our employees) while engaging everyone in the org to interact with our database<p>How it works
1. Deepsql learns your data and relationships from your code base, rules and query logs
2. Deepsql agent has 20 background jobs that continuously monitor the schema changes, bottlenecks, and come up with solutions before the problem arises. (Schema bloat issues are irreversible)
3. Deepsql Brain has CLI and MCP surfaces that can directly work with Claude &#x2F; Codex and Cursor. 
4. Deepsql digest delivers the daily database health report.
5. Your team can connect to deepsql with their favourate surface areas - Web UI, CLI, MCP or Slack.<p>One line install:
curl -fsSL <a href="https:&#x2F;&#x2F;install.deepsql.ai&#x2F;install.sh" rel="nofollow">https:&#x2F;&#x2F;install.deepsql.ai&#x2F;install.sh</a> | bash<p>For community support:
<a href="https:&#x2F;&#x2F;discord.gg&#x2F;duEJq7AeeG" rel="nofollow">https:&#x2F;&#x2F;discord.gg&#x2F;duEJq7AeeG</a><p>Or just email me for expert level setup guidance
venkat@stayflexi.com
