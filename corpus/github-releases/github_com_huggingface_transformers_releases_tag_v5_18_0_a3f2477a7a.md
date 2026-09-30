---
title: "huggingface/transformers v5.18.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.18.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-09-30T23:46:47Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.18.0"
---

# huggingface/transformers v5.18.0 released

> Source: github-releases | Category: changelog | 2026-09-30T23:46:47Z

## huggingface/transformers — v5.18.0

## New Model additions


### Nemotron 3 Diarization

<img width="1680" height="900" alt="image" src="https://github.com/user-attachments/assets/fe735cb3-9e5b-43ad-8f60-9dec8425aec7" />

Nemotron 3 Diarization is an open-weight streaming speaker diarization model designed to determine "who spoke when" in real-world audio. It supports both streaming and offline inference, handles up to eight speakers, and orders speaker outputs by each speaker's first arrival in the input audio.

The model uses the Arrival-Order Speaker Cache (AOSC) [1](https://huggingface.co/papers/2507.18446) and FIFO queue introduced for Streaming Sortformer [1](https://huggingface.co/papers/2507.18446), [2](https://huggingface.co/papers/2409.06656). A single checkpoint supports configurable latency profiles, from an 80 ms input buffer to a 30.4 s offline-style buffer, and configurable output frame resolution in multiples of 10 ms. With chunked inference, the maximum audio duration is not limited.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron3_diarization)
* Add Nemotron3Diarization (#49056) by @eustlb in [#49056](https://github.com/huggingface/transformers/pull/49056)

### NemotronH Omni

NemotronH Omni is a multimodal reasoning model from NVIDIA that pairs the [NemotronH](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h) hybrid
Mamba-Transformer language model with a [RADIO](https://huggingface.co/docs/transformers/main/en/model_doc/radio) vision encoder and an optional Parakeet-based sound encoder.
Image (and video) patches are projected through a RADIO tower and a pixel-shuffle MLP into the language model's
embedding space at the `<image>` / `<video>` context-token positions; audio clips are projected in the same way at
`<audio>` positions. The result is a single autoregressive model that reasons jointly over text, images, video and
sound.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/nemotron_h_omni)
* Add support for Nemotron Omni (#46509) by @meatybobby in [#46509](https://github.com/huggingface/transformers/pull/46509)

### HyperCLOVAX Vision V2

HyperCLOVAX Vision V2 is a multimodal vision-language model developed by NAVER. It combines the [HyperClovaX](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax) language model backbone with a [Qwen2.5-VL](https://huggingface.co/docs/transformers/main/en/model_doc/qwen2_5_vl) vision encoder. The model supports text, image, and video inputs and is capable of chain-of-thought reasoning via built-in thinking tokens (`<think>...</think>`).

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hyperclovax_vision_v2)
* add HyperClovaX Vision (#44314) by @jp1924 in [#44314](https://github.com/huggingface/transformers/pull/44314)

### GTE

GTE was proposed in [mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval](https://huggingface.co/papers/2407.19669) by Xin Zhang, Yanzhao Zhang, Dingkun Long, Wen Xie, Ziqi Dai, Jialong Tang, Huan Lin, Baosong Yang, Pengjun Xie, Fei Huang, Meishan Zhang, Wenjie Li and Min Zhang.

GTE is a BERT-style bidirectional encoder that replaces absolute position embeddings with RoPE, uses a gated MLP, and applies layer normalization after each residual connection. The same architecture backs Alibaba's `gte-*-v1.5`, `gte-multilingual-*` and `gte-en-mlm-*` checkpoints as well as Snowflake's `snowflake-arctic-embed-m-v2.0`.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/gte)
* model: Add GTE to Transformers (#48416) by @harshaljanjani in [#48416](https://github.com/huggingface/transformers/pull/48416)


## Breaking changes

* 🚨 [ROCm] gpt-oss: route FA3 to aiter-flash-attn, generate ROCm fixtures (#46837) by @Abdennacer-Badaoui
* 🚨 Speed up detr image processing (#48066) by @guarin
* 🚨 Remap inde
