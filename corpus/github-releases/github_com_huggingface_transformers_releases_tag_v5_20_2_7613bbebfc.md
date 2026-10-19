---
title: "huggingface/transformers v5.20.2 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.20.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-19T19:30:39Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.20.2"
---

# huggingface/transformers v5.20.2 released

> Source: github-releases | Category: changelog | 2026-10-19T19:30:39Z

## huggingface/transformers — v5.20.2

# Patch release: v5.20.2

This patch notably solves an issue where some inputs could loose their original type inside `prepare_inputs_for_generation` in `generate`, leading to problems with multimodal models. It also fixes some other issues listed on the below commits.

It contains the following commits:

- Fix inputs dict casting in generate (#49731) by @Cyrilvallez
- Fix zero expert gradients in bfloat16 with expert parallelism and ep_size < fsdp_size (#49688) by @qgallouedec 
- Declare the input modalities of the VLMs that report text only (#49677) by @qgallouedec 
- Avoid a host-to-device copy in eager_mask (#49684) by @hmellor 

