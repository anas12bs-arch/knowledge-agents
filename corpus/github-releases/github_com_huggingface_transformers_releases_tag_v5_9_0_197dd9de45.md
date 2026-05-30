---
title: "huggingface/transformers v5.9.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.9.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-05-30T14:31:29Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.9.0"
---

# huggingface/transformers v5.9.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:29Z

## huggingface/transformers — v5.9.0

# Release v5.9.0


## New Model additions

### Cohere2Moe

Command A+ is a Mixture-of-Experts (MoE) language model from Cohere that features a hybrid attention pattern combining sliding window and full attention layers. The model incorporates both shared and routed experts and supports a very large context window for processing extensive text sequences.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/cohere2_moe)
* Add new cohere2_moe model (#46115) by @Cyrilvallez in [#46115](https://github.com/huggingface/transformers/pull/46115)

### Parakeet tdt (#44171)

* Parakeet tdt (#44171) by @lmaksym

### HRM-Text

HRM-Text is an improved autoregressive language-modeling variant of the Hierarchical Reasoning Model (HRM) that uses a hierarchical recurrent forward pass with two transformer stacks - one for slow, abstract planning (H) and one for fast, detailed computation (L) - reused inside a nested recurrence. It features PrefixLM attention where instruction tokens attend bidirectionally while response tokens attend causally, per-head sigmoid output gates, and parameterless RMSNorm. The model is designed as a base language model without instruction tuning or chat templates.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hrm_text) | [Paper](https://huggingface.co/papers/2506.21734)
* Add hrm text (#46025) by @abcd1927 in [#46025](https://github.com/huggingface/transformers/pull/46025)



## Breaking changes

The `text_embeds` input for SAM3, EdgeTAM, and SAM3-Lite-Text models now expects full text embeddings instead of just pooler outputs, aligning with other models in the library — users must update their inputs accordingly.
* 🚨Fix memory leaks caused by lru decorators in vision models (#45922) by @yonigozlan



## Audio

Audio support was expanded with the addition of AudioFlamingoNext model checkpoints and improved compilability of audio/vision encoders via standalone pure functions. Additional improvements include better error messaging when loading audio from video files and new documentation for audio/video processors.


* user friendly error when loading audio from video (#45221) by @eustlb in [#45221]
* [docs] adding audio/video processors (#45795) by @stevhliu in [#45795]
* Support Audio Flamingo Next checkpoints (#44830) by @lashahub in [#44830]
* Extract dynamic vision/audio tensors into standalone pure functions (#45396) by @IlyasMoutawwakil in [#45396]


## Generation

Fixed generation issues including `inputs_embeds` and `per_layer_inputs` handling for Gemma4, an `AttributeError` in RAG's `generate()` caused by missing config fields, and flaky VLM generation tests by blocking special image tokens during sampling.


* Fix Gemma4 generation from inputs_embeds and per_layer_inputs (#46049) by @Cyrilvallez in [#46049]
* Fix AttributeError in RAG generate() for missing config fields (#46035) by @Sriniketh24 in [#46035]
* Block image_start/end_token_id in generation test sampling (#45914) by @Rocketknight1 in [#45914]


## Bugfixes and improvements

* Remove mask visualization tool from `masking_utils.py` (#46066) by @Cyrilvallez in [#46066]
* fix: owned_by field in GET /v1/models returns list instead of string (#46006) by @nileshpatil6 in [#46006]
* [CB] Remove OpenTelemetry (#45984) by @remi-or in [#45984]
* docs(readme): use canonical `huggingface.co` domain in prose links (#46042) by @kiwigitops in [#46042]
* Fix remaining RAG doc examples that crash on current transformers (#46044) by @Sriniketh24 in [#46044]
* Init the actual tensor, not a copy (#46030) by @Rocketknight1 in [#46030]
* docs: sync legacy ACL anthology URLs and update metrics across i18n READMEs (#46027) by @irfaan101 in [#46027]
* [MultimodalLM] add language_model to the get/set_input_embeddings logic (#46029) by @eustlb in [#46029]
* [`HRM Text`] Add integration tests (#46033) by @vasqu in [#46033]
* hy_v3: add XP
