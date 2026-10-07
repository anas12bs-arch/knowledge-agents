---
title: "unclecode/crawl4ai ⭐84874"
url: "https://github.com/unclecode/crawl4ai"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "rag", "ai", "ai-agents", "crawler", "data-extraction"]
date: "2026-10-07T09:05:08Z"
metadata:
  stars: "84874"
  language: "Python"
---

# unclecode/crawl4ai ⭐84874

> Source: github-trending | Category: tool | 2026-10-07T09:05:08Z

**unclecode/crawl4ai** — ⭐ 84874

Language: Python | Topics: ai, ai-agents, crawler, data-extraction, llm, markdown

Open-source web crawler and scraper for LLMs and AI agents: any website into clean, LLM-ready Markdown. Run it yourself, or use Crawl4AI Cloud with one key.

# 🚀🤖 Crawl4AI: the open-source web crawler for LLMs and AI agents

<div align="center">

<a href="https://trendshift.io/repositories/11716" target="_blank"><img src="https://trendshift.io/api/badge/repositories/11716" alt="unclecode%2Fcrawl4ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/unclecode/crawl4ai?style=social)](https://github.com/unclecode/crawl4ai/stargazers)
[![PyPI version](https://badge.fury.io/py/crawl4ai.svg)](https://badge.fury.io/py/crawl4ai)
[![Downloads](https://static.pepy.tech/badge/crawl4ai/month)](https://pepy.tech/project/crawl4ai)
[![Discord](https://img.shields.io/badge/Discord-join%20us-5865F2?logo=discord&logoColor=white)](https://discord.gg/jP8KfhDhyN)
[![Crawl4AI Cloud](https://img.shields.io/badge/Crawl4AI_Cloud-try_it_free-f5a300?style=flat&labelColor=0d0d10)](https://crawl4ai.com/?ref=readme-badge)

**Latest: [v0.9.4](https://github.com/unclecode/crawl4ai/releases/tag/v0.9.4) (23 Sep 2026)** · [all releases →](https://github.com/unclecode/crawl4ai/releases)

<a href="https://crawl4ai.com/?ref=readme-banner">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/cloud-launch-banner-dark.svg">
    <img alt="Crawl4AI Cloud is live. Soft launch: free credit to start, no card. Get your key." src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/cloud-launch-banner-light.svg" width="960">
  </picture>
</a>

</div>

Crawl4AI turns any website into clean, LLM-ready Markdown for RAG, AI agents and data pipelines. Run the open-source web crawler and scraper yourself, free forever, or use it hosted with one key: scrape, search and extract through one API, with MCP for your agent.

## Two ways to use Crawl4AI

### 🐍 Run it yourself: open source, forever

```bash
pip install -U crawl4ai
crawl4ai-setup        # installs the browser, once
```

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://news.ycombinator.com")
        print(result.markdown)

asyncio.run(main())
```

Docker server, CLI and every option: [Installation](#installation) · [docs.crawl4ai.com](https://docs.crawl4ai.com)

### ☁️ Or use the cloud: no browsers, no proxies

1. [![Get a key in 10 seconds](https://img.shields.io/badge/Get_a_key_in_10_seconds-%241_pass%2C_no_signup-f5a300?style=for-the-badge&labelColor=0d0d10)](https://crawl4ai.com/?ref=readme)  
   Verify your email and free credit to start is yours. No card. Soft launch: prices can change, what you buy stays yours.
2. Get any page as Markdown:

   ```bash
   curl -s https://api.crawl4ai.com/scrape \
     -H "Authorization: Bearer $CRAWL4AI_KEY" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://news.ycombinator.com"}' | jq -r .markdown
   ```

   The same key works fo
