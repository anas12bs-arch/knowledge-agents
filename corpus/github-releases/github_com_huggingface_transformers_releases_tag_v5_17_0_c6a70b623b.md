---
title: "huggingface/transformers v5.17.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.17.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-09-09T17:22:47Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.17.0"
---

# huggingface/transformers v5.17.0 released

> Source: github-releases | Category: changelog | 2026-09-09T17:22:47Z

## huggingface/transformers — v5.17.0

# Release v5.17.0


## New Model additions

### HYV4

<img width="1503" height="827" alt="image" src="https://github.com/user-attachments/assets/e6ed85ee-eb1d-40eb-a0d4-c649f6337ca9" />


Hy4-Preview is a 780B-parameter mixture-of-experts language model that activates 49B parameters per
token. Each MoE layer holds 256 routed experts plus one always-active shared expert and routes every
token to 8 of them. The context window is 1M tokens.

The architecture combines four features:

- **Multi-head Latent Attention (MLA)** compresses keys and values into a low-rank latent
  (`kv_lora_rank`) that `kv_b_proj` expands back to one key/value per query head.
- **DeepSeek Sparse Attention (DSA)** selects `index_topk` keys per query with a lightweight indexer.
  Following [IndexShare](https://huggingface.co/papers/2603.12201), only the layers marked `"full"`
  in `indexer_types` run an indexer; `"shared"` layers reuse the previous full layer's selection.
- **Gated MLA with learnable attention sinks**, where each head owns a sink logit that participates
  in the softmax and contributes no value, as in [GPT-OSS](./gpt_oss).
- **Independent Hyper-Connections (iHC)** replace the plain residual path with `hc_mult` parallel
  residual streams that are collapsed before, and redistributed after, every sublayer.

The implementation does not execute the multi-token prediction (MTP) layers. Released checkpoints
keep those weights so that other runtimes can use them for speculative decoding; they are ignored
at load time.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4)
* Add h4 (#48473) by @ArthurZucker in [#48473](https://github.com/huggingface/transformers/pull/48473)

### VibeVoice

<img width="2140" height="1188" alt="image" src="https://github.com/user-attachments/assets/29ccea01-a855-4d4f-a6af-61bc4fc883a4" />

[VibeVoice](https://huggingface.co/papers/2508.19205) is a novel framework for synthesizing high-fidelity, long-form speech with multiple speakers by employing a next-token diffusion approach within a Large Language Model (LLM) structure. It's designed to capture the authentic conversational "vibe" and is particularly suited for generating audio content like podcasts and multi-participant audiobooks.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/vibevoice)
* Implement VibeVoice  (#40546) by @pengzhiliang in [#40546](https://github.com/huggingface/transformers/pull/40546)

### NeoMME

NeoMME is a family of efficient 260M and 800M parameter multimodal-native multilingual foundation encoders from H Company. It processes multilingual text tokens and raw image patches in a single bidirectional Transformer encoder, without a separately pretrained vision tower or causal language model.

NeoMME-Retriever is a model fine-tuned from the NeoMME backbone for visual document retrieval with joint late-interaction and dense objectives. It takes text queries and documents (text or page screenshots) and produces multi-vector embeddings for MeanMaxSim scoring (late-interaction) and mean-pooled embeddings for cosine similarity (dense).

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/neomme)
* Add NeoMME and NeoMME-Retriever (#47992) by @tonywu71 in [#47992](https://github.com/huggingface/transformers/pull/47992)

### Fun-ASR-Nano

Fun-ASR-Nano is an 800M-parameter end-to-end speech recognition model developed by Alibaba DAMO Academy's FunAudioLLM team. It achieves state-of-the-art performance on Chinese, English, and Japanese ASR benchmarks while being significantly smaller than comparable models.

Key features are
- **Chinese, English, and Japanese**, including 7 Chinese dialects and 26 regional accents
- **Hotword customization** for domain-specific vocabulary
- **Native punctuation** output (no separate punctuation model needed)

**Links:** [Documentation](https://huggin
