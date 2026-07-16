---
title: "huggingface/transformers v5.14.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.14.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-07-16T10:34:18Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.14.1"
---

# huggingface/transformers v5.14.1 released

> Source: github-releases | Category: changelog | 2026-07-16T10:34:18Z

## huggingface/transformers — v5.14.1

# Patch release v5.14.1

This patch solves a few issues which appeared when integrating Inkling model, most notably an issue affecting models using EncoderDecoderCache during assisted generation. It also fixes an issue that could appear during prefill with StaticCache and sdpa without padding for Inkling which uses a position_bias. 
It contains the following commits:

- Fix sdpa prefill with position_bias (#47359) by @Cyrilvallez
- Fix assisted decoding for models with EncoderDecoder cache & OlmoHybrid (#47361) by @Cyrilvallez
- [FP8] Bump kernels version (#47344) by @vasqu 
- Fix deepgemm on multiple devices (#47323) by @IlyasMoutawwakil 
