---
title: "huggingface/transformers v5.13.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.13.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-07-11T09:53:03Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.13.1"
---

# huggingface/transformers v5.13.1 released

> Source: github-releases | Category: changelog | 2026-07-11T09:53:03Z

## huggingface/transformers — v5.13.1

# Patch release v5.13.1 

This patch is focused on enabling `transformers` for the latest release of vllm! 

- Be more defensive with remap_legacy_layer_types for custom models (#47245) from @hmellor 
- Fix custom code which doesn't know about the new linear layer type names (#47174) from @hmellor 
- Fix case where _LazyAutoMapping.register is passed a str key (#47148) from @hmellor 
