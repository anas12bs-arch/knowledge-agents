---
title: "Show HN: Awsmux – Multi-account AWS CLI, up to 5.4x faster, 7.4x fewer tokens"
url: "https://github.com/0hardik1/awsmux"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-07-25T22:07:53Z"
metadata:
  score: "5"
---

# Show HN: Awsmux – Multi-account AWS CLI, up to 5.4x faster, 7.4x fewer tokens

> Source: hackernews | Category: news | 2026-07-25T22:07:53Z

Score: 5 | Comments: 0

awsmux fans one AWS CLI command out across hundreds of accounts and regions in
parallel and merges the results into a single stream. There&#x27;s an MCP server
built in for agents.<p>In a 150-session benchmark, agents using awsmux beat agents using the raw AWS
CLI in every test: up to 5.4x faster, up to 2.9x cheaper, up to 7.4x fewer
tokens.<p>Single Go binary, stdlib plus cobra only. Feedback welcome.
