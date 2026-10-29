---
title: "huggingface/transformers v5.21.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.21.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-29T08:44:16Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.21.1"
---

# huggingface/transformers v5.21.1 released

> Source: github-releases | Category: changelog | 2026-10-29T08:44:16Z

## huggingface/transformers — v5.21.1

# Patch release v5.21.1 

** Fix rope_scaling setter for configs that assign it during init (#50080 ) 

We broke remote code loading in vllm, this fixes it sorry everyone!
