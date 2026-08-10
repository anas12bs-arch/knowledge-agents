---
title: "huggingface/transformers v5.15.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.15.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-08-10T10:54:02Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.15.0"
---

# huggingface/transformers v5.15.0 released

> Source: github-releases | Category: changelog | 2026-08-10T10:54:02Z

## huggingface/transformers — v5.15.0

# Release v5.15.0

## New Model additions

### Meta Muse Glimmer

Muse Glimmer, released today, is Meta’s new multimodal model, especially designed for agentic use cases. Distilled from Muse to 30B parameters, and released under the Apache 2.0 license, it can be deployed to local setups for privacy-aware applications such as coding, document analysis, personal assistants, Claw- or Hermes-like setups.

Muse Glimmer is a dense 30B parameter model consisting of:
- 2B ViT-style encoder for vision (Perception Encoder)
- 28B parameter text decoder

We're covering it in the following blogpost: http://hf.co/blog/muse-glimmer

<img width="960" height="1787" alt="image" src="https://github.com/user-attachments/assets/3d8e548e-f84f-4269-8bd0-a12722d7ab01" />

---

### GraniteMoeSWA & GraniteSWA

<img width="1013" height="389" alt="image" src="https://github.com/user-attachments/assets/2c2b87f0-466a-413a-a4be-25ceae49c9a5" />

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/granitemoe_swa)
* Add Granite-swa and Granitemoe-swa model support (#47179) by @daviswer in [#47179](https://github.com/huggingface/transformers/pull/47179)

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/granite_swa)
* Add Granite-swa and Granitemoe-swa model support (#47179) by @daviswer in [#47179](https://github.com/huggingface/transformers/pull/47179)

---

### A.X-K1 & A.X-K2

<img width="580" height="319" alt="image" src="https://github.com/user-attachments/assets/a20665bb-43ee-4af0-bb6f-80da495ea4f3" />

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/axk2)
* Add AXK2 from SKT (#47528) by @vasqu in [#47528](https://github.com/huggingface/transformers/pull/47528)

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/axk1)
* add_axk1 (#46867) by @kmswin1 in [#46867](https://github.com/huggingface/transformers/pull/46867)

---

### Cosmos3 Edge

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/16e41b90-11a5-4f22-8c56-11162b9c0a5f" />

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/cosmos3_edge)
* Add Cosmos3 Edge model support (#47181) by @atharvajoshi10 in [#47181](https://github.com/huggingface/transformers/pull/47181)


## Breaking changes

Kernels are now opt-in rather than mandatory for linear attention models (Mamba, GDN, Conv-only, etc.), so users who relied on automatic kernel selection must explicitly enable kernels to maintain previous behavior.
* 🚨 [`Kernels`] Refactor all linear attn models & native kernels fallback (#47630) by @vasqu

The cache cropping API now only accepts negative values (relative offsets) instead of absolute sizes, so users calling crop methods directly must update their code to pass negative values accordingly.
* 🚨 [cache] Cropping can only be done with negative values (#47720) by @Cyrilvallez

T5 and its model family (MT5, LongT5, etc.) now support SDPA and other attention backends via `ALL_ATTENTION_FUNCTIONS`, meaning the default attention implementation may change and users relying on the previous eager-only path should explicitly set `attn_implementation="eager"` if needed.
* 🚨 Enable SDPA (and other attention backends) for T5 and propagate to the T5 family (#47014) by @jiqing-feng

Several small private helper functions (e.g., `_is_url`, `_build_image_tokens`) have been removed from multimodal processor files, so users or downstream libraries that imported these private functions directly must remove or replace those references.
* :rotating_light: Processors update the rest (#46556) by @zucchini-nlp


## Attention

This release includes several attention fixes and improvements, including correcting Multi-Head Latent Attention (MLA) cache compression, optimizing Flash Attention max sequence length computation in vision models, and fixi
