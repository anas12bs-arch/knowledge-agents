---
title: "modelscope/ms-swift ⭐14332"
url: "https://github.com/modelscope/ms-swift"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "deepseek-r1", "embedding", "grpo", "internvl"]
date: "2026-05-30T14:31:07Z"
metadata:
  stars: "14332"
  language: "Python"
---

# modelscope/ms-swift ⭐14332

> Source: github-trending | Category: tool | 2026-05-30T14:31:07Z

**modelscope/ms-swift** — ⭐ 14332

Language: Python | Topics: deepseek-r1, embedding, grpo, internvl, liger, llama

Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.6, DeepSeek-V4, GLM-5.1, InternLM3, Llama4, ...) and 300+ MLLMs (Qwen3-VL, Qwen3-Omni, InternVL3.5, Ovis2.5, GLM4.5v, Gemma4, Llava, Phi4, ...) (AAAI 2025).

# SWIFT (Scalable lightWeight Infrastructure for Fine-Tuning)

<p align="center">
    <br>
    <img src="asset/banner.png"/>
    <br>
<p>
<p align="center">
<a href="https://modelscope.cn/home">ModelScope Community Website</a>
<br>
        <a href="README_CN.md">中文</a> &nbsp ｜ &nbsp English &nbsp
</p>

<p align="center">
<img src="https://img.shields.io/badge/python-3.12-5be.svg">
<img src="https://img.shields.io/badge/pytorch-%E2%89%A52.0-orange.svg">
<a href="https://github.com/modelscope/modelscope/"><img src="https://img.shields.io/badge/modelscope-%E2%89%A51.23-5D91D4.svg"></a>
<a href="https://pypi.org/project/ms-swift/"><img src="https://badge.fury.io/py/ms-swift.svg"></a>
<a href="https://github.com/modelscope/ms-swift/blob/main/LICENSE"><img src="https://img.shields.io/github/license/modelscope/ms-swift"></a>
<a href="https://pepy.tech/project/ms-swift"><img src="https://pepy.tech/badge/ms-swift"></a>
<a href="https://github.com/modelscope/ms-swift/pulls"><img src="https://img.shields.io/badge/PR-welcome-55EB99.svg"></a>
</p>

<p align="center">
<a href="https://trendshift.io/repositories/11937" target="_blank"><img src="https://trendshift.io/api/badge/repositories/11937" alt="modelscope/ms-swift | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
        <a href="https://arxiv.org/abs/2408.05517">Paper</a> &nbsp ｜ <a href="https://swift.readthedocs.io/en/latest/">English Documentation</a> &nbsp ｜ &nbsp <a href="https://swift.readthedocs.io/zh-cn/latest/">中文文档</a> &nbsp
</p>

## 📖 Table of Contents
- [Groups](#-Groups)
- [Introduction](#-introduction)
- [News](#-news)
- [Installation](#%EF%B8%8F-installation)
- [Quick Start](#-quick-Start)
- [Usage](#-Usage)
- [License](#-License)
- [Citation](#-citation)


## ☎ Groups

You can contact us and communicate with us by adding our group:


[Discord Group](https://discord.gg/yeN59wxjwe)              |  WeChat Group
:-------------------------:|:-------------------------:
<img src="asset/discord_qr.jpg" width="200" height="200">  |  <img src="asset/wechat.png" width="200" height="200">


## 📝 Introduction
🍲 **ms-swift** is a large model and multimodal large model fine-tuning and deployment framework provided by the ModelScope community. It now supports training (pre-training, fine-tuning, human alignment), inference, evaluation, quantization, and deployment for 600+ text-only large models and 400+ multimodal large models. Large models include: Qwen3, Qwen3.5, InternLM3, GLM4.5, Mistral, DeepSeek-R1, Llama4, etc. Multimodal large models include: Qwen3-VL, Qwen3-Omni, Llava, InternVL3.5, MiniCPM-V-4, Ovis2.5, GLM4.5-V, DeepSeek-VL2, etc.

🍔 In addition, ms-swift integrates the latest training technologies, including Megatron parallelism techniques such as TP, PP, CP, EP to accelerate training, as well as numerous GRPO algorithm family reinforcement learning algorithms including: GRPO, DAPO, GSPO, SAPO, CISPO, RLOO, Reinforce++, etc. to enhance m
