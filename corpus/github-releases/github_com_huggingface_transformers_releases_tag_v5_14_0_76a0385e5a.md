---
title: "huggingface/transformers v5.14.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.14.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-07-15T19:39:18Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.14.0"
---

# huggingface/transformers v5.14.0 released

> Source: github-releases | Category: changelog | 2026-07-15T19:39:18Z

## huggingface/transformers — v5.14.0

# Release v5.14.0

## New Model additions

### Inkling (fresh from Thinking Machines): 975B total, 41B active

* Add Inkling model #47347 by @molbap @Cyrilvallez @eustlb and @zucchini-nlp 

<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/051f819a-512f-4987-9bee-6e2fa2af3db7" />


Inkling is a general-purpose multimodal model that accepts text, image and audio inputs and
generates text outputs. It is intended for use in English and other languages, and across
multiple coding languages. The model is designed to be used by developers building AI-
powered applications, including agentic and tool-use systems, coding assistants, chatbots, and
retrieval-augmented generation systems, and is suitable for general-purpose conversational
use, instruction-following, and other natural language and multimodal tasks. It is released with
open weights to support research, fine-tuning and integration into third-party products by
downstream developers.




### TIPSv2
<img width="1555" height="1306" alt="image" src="https://github.com/user-attachments/assets/2d9f21e5-05f8-4c36-93ef-22f03c089f52" />

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/tipsv2)
* Add TIPSv2 (#46347) by @Ternura143 in [#46347](https://github.com/huggingface/transformers/pull/46347)

### TIPSv2 DPT
<img width="794" height="245" alt="image" src="https://github.com/user-attachments/assets/09c0d4da-6c1c-4229-bf02-a512ed435e50" />

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/tipsv2_dpt)
* Add TIPSv2 (#46347) by @Ternura143 in [#46347](https://github.com/huggingface/transformers/pull/46347)



## :rotating_light:  Breaking changes

GPTNeoX now remaps `embed_out` to `lm_head` and GPTBigCode has `_supports_attention_backend = True` enabled for vLLM compatibility; users relying on the previous weight naming or attention backend behavior for these models should update their code accordingly.
* :rotating_light: Fix GPTBigCode and GPTNeoX for the Transformers modelling backend for vLLM (#47198) by @hmellor


## Kernels

Several kernel-related fixes and improvements were made, including pinning the `kernels` dependency to a compatible version in the benchmark workflow, removing a deprecated `package_name` argument from `LocalLayerRepository`, and making the DeepGEMM Triton fallback more robust when `CUDA_HOME` is unset or misconfigured. Additionally, SDPA prefill was updated to leverage the FlashAttention kernel with `StaticCache`, yielding significant performance gains (up to 260% faster for large input sizes).


* Pin kernels to compatible version in benchmark workflow (#47339) by @tarekziade in [#47339]
* [Fix] Remove deprecated argument from `kernels` call (#47100) by @remi-or in [#47100]
* [Fix] Make DeepGEMM triton fallback more robust (#47126) by @remi-or in [#47126]
* [sdpa] Allow prefill to use FA kernel with StaticCache (#47094) by @Cyrilvallez in [#47094]


## Generation

Generation improvements include adding Multi-Token Prediction (MTP) decoding support, static ensemble verification for speculative decoding to improve draft token acceptance rates, and a fix for crashes in greedy assisted generation with different tokenizers. A misleading double-negative warning message for `synced_gpus` in continuous batching mode was also corrected.


* [generation] Fix misleading synced_gpus warning in continuous batching (#47158) by @Partha-Shankar in [#47158]
* [generate] Add proper MTP support (#46229) by @Cyrilvallez in [#46229]
* Fix crash in greedy assisted generation with different tokenizers (#46936) by @Sunt-ing in [#46936]
* [Generation] Add static ensemble verification for lossy speculative decoding (#45979) by @kasakh in [#45979]


## Performance

Fixed a Flash Attention performance regression affecting models like Qwen3-VL and resolved a MoE decode optimization bug where the grouped-to-
