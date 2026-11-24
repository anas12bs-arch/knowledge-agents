---
title: "huggingface/transformers v5.24.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.24.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-11-24T23:50:48Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.24.1"
---

# huggingface/transformers v5.24.1 released

> Source: github-releases | Category: changelog | 2026-11-24T23:50:48Z

## huggingface/transformers — v5.24.1

# Patch release v5.24.1

A patch to fix a bunch of stuff for vLLM, a few distributed issues, and some model fixes (llama4, dory); see the full list

### vLLM related
- Fix backward compatibility of the cache rename for remote code (#51085) by @hmellor
- Restore modeling_attn_mask_utils for remote code (one-off to unblock vLLM) (#51124) by @hmellor 
- Expose past_key_values in MBartDecoderLayer.forward signature for remote code (#51177) by @hmellor 
- [OmniASR] Support a padding_mask kept on the CPU in the audio encoder (#51100) by @El-euchidali

### Model fixes
- Fix Llama4 forward crash on missing image_outputs (#51144) by @kylesayrs
- Fix dory static cache (#50993) by @ArthurZucker 

### Distributed
- Allow expert parallelism alone with tp_plan={} (#50996) by @3outeille 
- Fix strided checkpoint reads on PyTorch 2.9 (#51042) by @satsuki2486441738

**Full Changelog**: https://github.com/huggingface/transformers/compare/v5.24.0...v5.24.1
