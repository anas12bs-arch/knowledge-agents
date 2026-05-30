---
title: "infiniflow/infinity ⭐4539"
url: "https://github.com/infiniflow/infinity"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "ai-native", "approximate-nearest-neighbor-search", "bm25", "cpp20"]
date: "2026-05-30T14:31:08Z"
metadata:
  stars: "4539"
  language: "C++"
---

# infiniflow/infinity ⭐4539

> Source: github-trending | Category: tool | 2026-05-30T14:31:08Z

**infiniflow/infinity** — ⭐ 4539

Language: C++ | Topics: ai-native, approximate-nearest-neighbor-search, bm25, cpp20, cpp20-modules, embedding

The AI-native database built for LLM applications, providing incredibly fast hybrid search of dense vector, sparse vector, tensor (multi-vector), and full-text.

<div align="center">
  <img width="187" src="https://github.com/infiniflow/infinity/assets/7248/015e1f02-1f7f-4b09-a0c2-9d261cd4858b" alt="Infinity logo"/>
</div>


<p align="center">
    <b>The AI-native database built for LLM applications, providing incredibly fast hybrid search of dense embedding, sparse embedding, tensor and full-text</b>
</p>

<h4 align="center">
  <a href="https://infiniflow.org/docs/dev/category/get-started">Document</a> |
  <a href="https://infiniflow.org/docs/dev/benchmark">Benchmark</a> |
  <a href="https://twitter.com/infiniflowai">Twitter</a> |
  <a href="https://discord.gg/jEfRUwEYEV">Discord</a>
</h4>


Infinity is a cutting-edge AI-native database that provides a wide range of search capabilities for rich data types such as dense vector, sparse vector, tensor, full-text, and structured data. It provides robust support for various LLM applications, including search, recommenders, question-answering, conversational AI, copilot, content generation, and many more **RAG** (Retrieval-augmented Generation) applications.

- [Key Features](#-key-features)
- [Get Started](#-get-started)
- [Document](#-document)
- [Roadmap](#-roadmap)
- [Community](#-community)

## ⚡️ Performance

<div class="column" align="middle">
  <img src="https://github.com/user-attachments/assets/c4c98e23-62ac-4d1a-82e5-614bca96fe0a" alt="Infinity performance comparison"/>
</div>

## 🌟 Key Features

Infinity comes with high performance, flexibility, ease-of-use, and many features designed to address the challenges facing the next-generation AI applications:

### 🚀 Incredibly fast

- Achieves 0.1 milliseconds query latency and 15K+ QPS on million-scale vector datasets.
- Achieves 1 millisecond latency and 12K+ QPS in full-text search on 33M documents.

> See the [Benchmark report](https://infiniflow.org/docs/dev/benchmark) for more information.

### 🔮 Powerful search

- Supports a hybrid search of dense embedding, sparse embedding, tensor, and full text, in addition to filtering.
- Supports several types of rerankers including RRF, weighted sum and **ColBERT**.

### 🍔 Rich data types

Supports a wide range of data types including strings, numerics, vectors, and more.

### 🎁 Ease-of-use

- Intuitive Python API. See the [Python API](https://infiniflow.org/docs/dev/pysdk_api_reference)
- A single-binary architecture with no dependencies, making deployment a breeze.
- Embedded in Python as a module and friendly to AI developers.  

## 🎮 Get Started

This section provides guidance on deploying the Infinity database using Docker, with the client and server as separate processes. 

### Prerequisites

- CPU: x86_64 with AVX2 support.
- OS:
  - Linux with glibc 2.17+.
  - Windows 10+ with WSL/WSL2.
  - MacOS
- Python: Python 3.11+.


### Install Infinity server

#### Linux x86_64 & MacOS x86_64

```bash
sudo mkdir -p /var/infinity && sudo chown -R $USER /var/infinity
docker pull infiniflow/infinity:nightly
docker run -d --name infinity -v /var/infinity/:/var/inf
