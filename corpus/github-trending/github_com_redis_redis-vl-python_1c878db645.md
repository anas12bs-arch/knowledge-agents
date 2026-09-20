---
title: "redis/redis-vl-python ⭐427"
url: "https://github.com/redis/redis-vl-python"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "anthropic", "embedding", "huggingface", "large-language-models"]
date: "2026-09-20T00:29:39Z"
metadata:
  stars: "427"
  language: "Python"
---

# redis/redis-vl-python ⭐427

> Source: github-trending | Category: tool | 2026-09-20T00:29:39Z

**redis/redis-vl-python** — ⭐ 427

Language: Python | Topics: anthropic, embedding, huggingface, large-language-models, llm, llmcache

Redis Vector Library. The AI-native Python client for Redis.

<div align="center">
    <img width="300" src="https://raw.githubusercontent.com/redis/redis-vl-python/main/docs/_static/Redis_Logo_Red_RGB.svg" alt="Redis">
    <h1>Redis Vector Library</h1>
    <p><strong>The AI-native Redis Python client</strong></p>
</div>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pypi](https://badge.fury.io/py/redisvl.svg)](https://pypi.org/project/redisvl/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/redisvl)
[![GitHub stars](https://img.shields.io/github/stars/redis/redis-vl-python)](https://github.com/redis/redis-vl-python/stargazers)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Language](https://img.shields.io/github/languages/top/redis/redis-vl-python)
![GitHub last commit](https://img.shields.io/github/last-commit/redis/redis-vl-python)

**[Documentation](https://docs.redisvl.com)** • **[Recipes](https://github.com/redis-developer/redis-ai-resources)** • **[GitHub](https://github.com/redis/redis-vl-python)**

</div>

---

## Introduction

Redis Vector Library (RedisVL) is the production-ready Python client for AI applications built on Redis. **Lightning-fast vector search meets enterprise-grade reliability.**

Perfect for building **RAG pipelines** with real-time retrieval, **AI agents** with memory and semantic routing, and **recommendation systems** with fast search and reranking.

<div align="center">

| **🎯 Core Capabilities** | **🚀 AI Extensions** | **🛠️ Dev Utilities** |
|:---:|:---:|:---:|
| **[Index Management](#index-management)**<br/>*Schema design, data loading, CRUD ops* | **[Semantic Caching](#semantic-caching)**<br/>*Reduce LLM costs & boost throughput* | **[CLI](#command-line-interface)**<br/>*Index management from terminal* |
| **[Vector Search](#retrieval)**<br/>*Similarity search with metadata filters* | **[LLM Memory](#llm-memory)**<br/>*Agentic AI context management* | **Async Support**<br/>*Async indexing and search for improved performance* |
| **[Complex Filtering](#retrieval)**<br/>*Combine multiple filter types* | **[Semantic Routing](#semantic-routing)**<br/>*Intelligent query classification* | **[Vectorizers](#vectorizers)**<br/>*8+ embedding provider integrations* |
| **[Hybrid Search](#retrieval)**<br/>*Combine semantic & full-text signals* | **[Embedding Caching](#embedding-caching)**<br/>*Cache embeddings for efficiency* | **[Rerankers](#rerankers)**<br/>*Improve search result relevancy* |
|  |  | **[MCP Server](#mcp-server)**<br/>*Expose one or more existing Redis indexes to MCP clients* |

</div>



# 💪 Getting Started

## Installation

Install `redisvl` into your Python (>=3.10) environment using `pip`:

```bash
pip install redisvl
```

Install the MCP server extra when you want to expose one or more existing Redis indexes through MCP:

```bash
pip install redisvl[mcp]
```

> For more detailed instructions, visit the [
