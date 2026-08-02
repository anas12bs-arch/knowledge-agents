---
title: "Show HN: Draco – A single-binary, self-hostable Firecrawl alternative in Rust"
url: "https://github.com/0xchasercat/draco/"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-08-02T21:26:08Z"
metadata:
  score: "6"
---

# Show HN: Draco – A single-binary, self-hostable Firecrawl alternative in Rust

> Source: hackernews | Category: news | 2026-08-02T21:26:08Z

Score: 6 | Comments: 0

Scraping modern websites has become a massive headache. You basically have two choices: pay for an expensive API like Firecrawl&#x2F;Browserbase, or run a fleet of headless Chrome instances that eat 1GB of RAM per page and still get blocked by Cloudflare.<p>I built Draco to fix this. It’s a fast, single-binary web scraper written in Rust. You point it at a URL, and it spits out perfectly clean Markdown or structured JSON for LLMs.<p>The secret sauce is that it doesn&#x27;t just boot a browser for every request. It uses a tiered escalation engine:<p>Tier 1 (Stealth Fetch): Draco uses a custom TLS&#x2F;JA4 fingerprint to perfectly mimic a real browser&#x27;s network signature at the packet level. It turns out a lot of anti-bot walls will let you right through if your handshake looks correct. In my benchmarks against sites like Cloudflare and Target, Playwright ate ~500MB of RAM and timed out. Draco bypassed them in under a second using just 20MB of RAM.<p>Tier 2 (V8 Isolate): If it hits a React&#x2F;Next.js SPA that needs rendering, Draco boots an in-process V8 engine in single-digit milliseconds. It hydrates the DOM and intercepts the hidden JSON APIs the page is calling—giving you the raw data without the overhead of a graphical browser.<p>Tier 3 (Real Browser): If it hits an absolute wall, it seamlessly falls back to detecting and driving a real browser on your machine.<p>I also built in all the tooling to make it a complete drop-in replacement for the hosted services:<p>Daemon Mode: Run draco serve and you get a persistent HTTP server with a Firecrawl-compatible REST API. You can swap out your API keys and self-host immediately.<p>Built-in MCP Server: It natively exposes a Model Context Protocol server so you can plug it directly into Claude Desktop or your AI agents.<p>Web Search: Built-in parallel multi-engine web search (bypassing the need for a Google Search API key).<p>Interact Mode: Drive a page statefully like a devtools console, persisting cookies across navigations(for LLM&#x27;s mainly).<p>It’s completely open source (MIT&#x2F;Apache-2.0). I just wanted to put this out there for anyone tired of fighting headless Chromium or paying per-page scraping costs. Grab the binary and throw a difficult URL at it.<p>Note that it&#x27;s still a WIP so there might be some unexpected breakages of uncommon sites but for the most part its quite capable, it can handle cf-protected sites and heavy SPA&#x27;s while everything else fails partially or completely while taking longer or more resources. (tested on example.com, hackernews, cloudflare, glassdoor, bluff.com, target.com, stake.com and thrill.com)<p>┏━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ Rank ┃ Tool           ┃ Score ┃ Pass ┃ Avg Time ┃ Avg RAM ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│  #1  │ Draco          │ 769.7 │ 8&#x2F;8  │     3.45 │  216.50 │
│  #2  │ Obscura        │ 384.5 │ 4&#x2F;8  │     2.68 │   87.59 │
│  #3  │ BrowserOxide   │ 373.4 │ 4&#x2F;8  │     6.42 │  105.95 │
│  #4  │ Playwright     │ 342.2 │ 4&#x2F;8  │     1.71 │  535.07 │
│  #5  │ Bouncy         │ 196.6 │ 2&#x2F;8  │     0.59 │   19.38 │
└──────┴────────────────┴───────┴──────┴──────────┴─────────┘<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;0xchasercat&#x2F;draco&#x2F;" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;0xchasercat&#x2F;draco&#x2F;</a>
