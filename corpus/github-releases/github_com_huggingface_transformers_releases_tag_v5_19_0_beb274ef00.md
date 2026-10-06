---
title: "huggingface/transformers v5.19.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.19.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-06T19:54:06Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.19.0"
---

# huggingface/transformers v5.19.0 released

> Source: github-releases | Category: changelog | 2026-10-06T19:54:06Z

## huggingface/transformers — v5.19.0

# Release v5.19.0


## New Model additions

### EmbeddingGemma2

<img width="2716" height="2308" alt="image" src="https://github.com/user-attachments/assets/84734e74-163d-4d12-b166-ffcf6749d563" />

EmbeddingGemma 2 is a multimodal embedding model from Google built on the Gemma 4 architecture. It encodes text, images, audio, and video, individually or combined in one input, into a shared 768-dimensional vector space for cross-modal retrieval, semantic similarity, clustering, and classification. It uses Matryoshka Representation Learning, so embeddings can be truncated to 512, 256, or 128 dimensions. It also offers configurable visual and video token budgets, and unused vision or audio towers can be disabled at load time to save memory.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/embedding_gemma2)
* Smthn smthn (#49364) by @vasqu in [#49364](https://github.com/huggingface/transformers/pull/49364)



## Breaking changes

All MoE models whose routers compute logits now return them when `output_router_logits=True`, following the Qwen3-MoE pattern (a `router_logits` recorder on the base model, `MoeModelOutputWithPast` from the backbone, and a MoE causal LM output from the head), so code that relied on the previous outputs or their absence should read the router logits from these output classes.
* 🚨 Return router logits from every MoE model that computes them (#48920) by @qgallouedec

`Owlv2ForObjectDetection.embed_image_query` now selects the query box with the highest objectness score, as in the original OWLv2 notebook, instead of the OWL-ViT heuristic, so image-guided query embeddings and detections may differ from earlier releases.
* 🚨 Select the OWLv2 image query by objectness (#49200) by @qgallouedec

The `"paged|"` prefix for SDPA and flash attention implementations is deprecated, so users should set the regular attention implementation (e.g. `sdpa` or `flash_attention_2`) for continuous batching instead of `paged|sdpa` or `paged|flash_attention_2`.
* 🚨 Attention 🚨 Deprecate "paged|" prefix for SDPA and flash  (#49112) by @remi-or

The regular flash and SDPA attention functions (`flash_attention.py`, `sdpa_attention.py`) now support continuous batching directly, and `"paged|..."` implementations for these are redirected to them, while eager still requires the `"paged|eager"` prefix.
* 🚨 Attention 🚨 Make regular attention support CB (#49101) by @remi-or

In continuous batching, the cache update for the index-based and block-table paths is now fused into a single call, which slightly changes the cache update function's behavior and affects any custom code that calls the separate update paths.
* 🚨 [CB] 🚨 Fuse update for index and block table path (#49088) by @remi-or

Continuous batching internals changed in preparation for removing `"paged"`: `max
* 🚨 [CB] 🚨 Little fixes before removing "paged" (#49069) by @remi-or



## Parallelization

Expert parallelism gains a token-dispatch implementation, selected via the new `ep_dispatch_experts` plan rule and now the default for Qwen3 MoE and Mellum, which removes the requirement that EP size equal TP size. The `Trainer` was also adapted to work with expert parallelism, and the docs now note that PEFT adapters support tensor parallelism. A CI-related fix for pipeline-parallel chart2table inference was also included.


* [`distributed`]: adapt Trainer to work Expert Parallel (#48873) by @3outeille in [#48873]
* [`distributed`] Add expert-parallel token dispatch, default for Qwen3 MoE (#48865) by @3outeille in [#48865]
* Fix pp chart2table inference (#49225) by @zucchini-nlp in [#49225]
* [docs] TP for PEFT adapters (#49060) by @stevhliu in [#49060]


## Cache

This release fixes quantized cache handling: `generate` no longer mutates the user's `cache_config`, and `QuantizedLayer.reorder_cache` is repaired. It also adds per-layer cache configuration, so `DynamicCache` and `StaticCache` initialize
