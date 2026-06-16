---
title: "huggingface/transformers v5.12.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.12.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-06-16T18:13:27Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.12.1"
---

# huggingface/transformers v5.12.1 released

> Source: github-releases | Category: changelog | 2026-06-16T18:13:27Z

## huggingface/transformers — v5.12.1

# Patch release v5.12.1
Updated the lower bound for PEFT and a fix for auto tokenizer to properly resolve the mistral tokenizer (when `mistral-common` is installed). This is similar to v.5.10.3 minus the fixes that were already included in the main release - vLLM will first target 5.10.3 :hugs: 

* Fix `peft` lower bound #46605 by @hmellor (#46605)
* mistral common backend fix #46667 by @itazap (#46667)


**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.12.0...v5.12.1
