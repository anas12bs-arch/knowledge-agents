---
title: "Show HN: Run Agent Skills with mistral.rs v0.8.10: /v1/skills support and more"
url: "https://news.ycombinator.com/item?id=48581792"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-18T19:58:18Z"
metadata:
  score: "8"
---

# Show HN: Run Agent Skills with mistral.rs v0.8.10: /v1/skills support and more

> Source: hackernews | Category: news | 2026-06-18T19:58:18Z

Score: 8 | Comments: 0

Hey all!
I&#x27;m the maintainer of mistral.rs. I just landed support for OpenAI-compatible Agent Skills via a &#x2F;v1&#x2F;skills endpoint, and it works with local open models.<p>Until now Skills have basically been locked to closed models, and with the ability to have private, local intelligence becoming increasingly important, but this feature allows you to do XYZ with local models.<p>It&#x27;s fully compatible with OpenAI&#x27;s &#x2F;v1&#x2F;skills API, so you can drop mistral.rs into your existing code with minimal difficulty.<p>We support the accompanying tools too: &#x2F;v1&#x2F;files or input_file for attaching files to your prompts, and mistral.rs also allows models to send generated files 
back using the OpenAI-compatible method.<p>It&#x27;s also easier than ever to try mistral.rs: we are including prebuilt binaries for NVIDIA CUDA, Apple Silicon, and CPU!
# Linux&#x2F;Mac
&gt; curl --proto &#x27;=https&#x27; --tlsv1.2 -sSf <a href="https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;EricLBuehler&#x2F;mistral.rs&#x2F;master&#x2F;install.sh" rel="nofollow">https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;EricLBuehler&#x2F;mistral.rs&#x2F;ma...</a> | sh
# Windows
&gt; irm <a href="https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;EricLBuehler&#x2F;mistral.rs&#x2F;master&#x2F;install.ps1" rel="nofollow">https:&#x2F;&#x2F;raw.githubusercontent.com&#x2F;EricLBuehler&#x2F;mistral.rs&#x2F;ma...</a> | iex<p>Then:
mistralrs serve --agent --isq 4 -m google&#x2F;gemma-4-E4B-it<p>Super excited for you to try this out and any feedback! Do you have any suggestions for what you would like to see in the next releases?<p>Check out the GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;EricLBuehler&#x2F;mistral.rs" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;EricLBuehler&#x2F;mistral.rs</a>
Docs &amp; Quickstart: <a href="https:&#x2F;&#x2F;ericlbuehler.github.io&#x2F;mistral.rs&#x2F;" rel="nofollow">https:&#x2F;&#x2F;ericlbuehler.github.io&#x2F;mistral.rs&#x2F;</a>
