---
title: "TIGER-AI-Lab/VLM2Vec ⭐678"
url: "https://github.com/TIGER-AI-Lab/VLM2Vec"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "benchmark", "contrastive-learning", "embedding", "image-retrieval"]
date: "2026-08-24T00:04:05Z"
metadata:
  stars: "678"
  language: "Python"
---

# TIGER-AI-Lab/VLM2Vec ⭐678

> Source: github-trending | Category: tool | 2026-08-24T00:04:05Z

**TIGER-AI-Lab/VLM2Vec** — ⭐ 678

Language: Python | Topics: benchmark, contrastive-learning, embedding, image-retrieval, mmeb, multimodal

This repo contains the code for "VLM2Vec / MMEB" [ICLR 2025], "VLM2Vec-V2 / MMEB-V2" [TMLR 2026], and "MMEB-V3" [COLM 2026]

# MMEB-V3: Measuring the Performance Gaps of Omni-Modality Embedding Models

<a target="_blank" href="https://github.com/TIGER-AI-Lab/VLM2Vec">
<img style="height:22pt" src="https://img.shields.io/badge/-MMEB--V3%20Code-green?style=flat&logo=github"></a>
<a target="_blank" href="https://huggingface.co/datasets/VLM2Vec/MMEB-V3">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Dataset(MMEB--V3)-red?style=flat"></a>
<a target="_blank" href="https://arxiv.org/abs/2604.23321">
<img style="height:22pt" src="https://img.shields.io/badge/-V3 Paper-black?style=flat&logo=arxiv"></a>
<a target="_blank" href="https://arxiv.org/abs/2507.04590">
<img style="height:22pt" src="https://img.shields.io/badge/-V2 Paper-black?style=flat&logo=arxiv"></a>
<a target="_blank" href="https://arxiv.org/abs/2410.05160">
<img style="height:22pt" src="https://img.shields.io/badge/-V1 Paper-black?style=flat&logo=arxiv"></a>
<a target="_blank" href="https://github.com/TIGER-AI-Lab/VLM2Vec">
<img style="height:22pt" src="https://img.shields.io/badge/-Code-green?style=flat&logo=github"></a>
<a target="_blank" href="https://tiger-ai-lab.github.io/VLM2Vec/">
<img style="height:22pt" src="https://img.shields.io/badge/-🌐%20Website-red?style=flat"></a>
<a target="_blank" href="https://huggingface.co/datasets/TIGER-Lab/MMEB-V2">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Dataset(V2)-red?style=flat"></a>
<a target="_blank" href="https://huggingface.co/datasets/TIGER-Lab/MMEB-eval">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Dataset(V1)-red?style=flat"></a>
<a target="_blank" href="https://huggingface.co/VLM2Vec">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Models-red?style=flat"></a>
<a target="_blank" href="https://huggingface.co/spaces/TIGER-Lab/MMEB-Leaderboard">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Leaderboard-red?style=flat"></a>
<a target="_blank" href="https://x.com/WenhuChen/status/1844577017930694984">
<img style="height:22pt" src="https://img.shields.io/badge/-Tweet-blue?style=flat&logo=twitter"></a>
<br>

This repository contains the code and data interface for **MMEB-V3**, a comprehensive benchmark for evaluating **omni-modality embedding models** across text, image, video, audio, visual document, and agent-centric retrieval scenarios.

MMEB-V3 extends MMEB-V2 toward a fuller modality setting by adding **111 new tasks**, resulting in **190 tasks** in total. It introduces three major new evaluation categories:

- **Audio Tasks**: audio classification, cross-modal audio retrieval, and audio temporal grounding.

- **Text Retrieval**: instruction-following retrieval, reasoning retrieval, long-context retrieval, multi-condition retrieval, and general text retrieval.

- **Agent Tasks**: tool retrieval, GUI control, and agent memory retrieval.

In addition, MMEB-V3 introduces **OmniSET** (*Omni-modality Semantic Equivalence Tuples*), a diagnostic component that groups semanticall
