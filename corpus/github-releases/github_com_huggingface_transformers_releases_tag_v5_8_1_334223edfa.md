---
title: "huggingface/transformers v5.8.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.8.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-05-30T14:31:29Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.8.1"
---

# huggingface/transformers v5.8.1 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:29Z

## huggingface/transformers — v5.8.1

# Patch release v5.8.1 
This release is mainly to fix the Deepseek V4 integration!!! 

<img width="714" height="774" alt="image" src="https://github.com/user-attachments/assets/0d85e891-a0ff-436e-a9d4-b6633096f2b5" />


* [fix] Add fatal_error to ContinuousBatchingManager so the serving... by @qgallouedec, @remi-or
* Fix WeightConverter regex incorrectly matching shared_experts as experts by @silencelamb, @claude
* Fix deepseek v4 by @ArthurZucker (#45892)
* Deepseek v4 csa mask collapse by @ArthurZucker, @Sawyer117 (#45928)
