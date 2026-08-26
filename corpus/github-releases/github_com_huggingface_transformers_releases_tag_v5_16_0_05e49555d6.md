---
title: "huggingface/transformers v5.16.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.16.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-08-26T12:59:26Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.16.0"
---

# huggingface/transformers v5.16.0 released

> Source: github-releases | Category: changelog | 2026-08-26T12:59:26Z

## huggingface/transformers — v5.16.0

# Release v5.16.0


## New Model additions

### Qwen4-Exp

<img width="2241" height="693" alt="image" src="https://github.com/user-attachments/assets/c838b5ba-ffea-42da-baa9-3f66178e3671" />

Qwen4-Exp builds on Qwen3.5's hybrid text and multimodal architecture with three key components: GatedResidual (GR), Qwen Sparse Attention (QSA), and Per-Layer Embedding (PLE).

GR is a Qwen-developed residual architecture that combines Hyper-Connection with GatedNorm. It mixes multiple residual streams with fine-grained elementwise gating before each attention and Mixture-of-Experts (MoE) block, then controls how much of the block output is injected back into each stream.

QSA uses multiple query heads to score compressed key blocks, selects the most relevant contiguous token blocks, and keeps the incomplete trailing block uncompressed. This block-level selection reduces indexing overhead and improves memory locality for long sequences. Combined with Gated DeltaNet, QSA makes Qwen4-Exp the first hybrid architecture to integrate linear and sparse attention, substantially improving inference efficiency for long-context workloads.

PLE enriches selected decoder layers with layer-specific lexical features derived from hashed token n-grams and a dilated depthwise convolution.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/qwen4_exp)
* Add Qwen4Exp model (#48337) by @Cyrilvallez in [#48337](https://github.com/huggingface/transformers/pull/48337)

### GraniteSpeech5

<img width="1600" height="1440" alt="image" src="https://github.com/user-attachments/assets/106ef712-9f45-43c9-98b7-ce6e4a7c136d" />

Granite Speech 5.0 Turbo CTC is a lightweight (~470M parameters) conformer encoder for automatic speech recognition, trained with Connectionist Temporal Classification (CTC) on BPE targets. It is a fast, encoder-only member of the [Granite Speech](https://huggingface.co/papers/2505.08699) family: transcription requires a single forward pass followed by greedy CTC decoding, with no autoregressive decoder.

Architecturally, it extends the Granite Speech conformer CTC encoder with:

1. **Frame stacking + block-wise time subsampling**: the feature extractor stacks pairs of log-mel(+delta) frames (2x), and the first two conformer blocks each subsample time by 2 through a stride-2 depthwise convolution (with a mean-pooled residual), for a total 8x time reduction at 10 ms mel hop.

2. **Block attention with Shaw's relative positional embeddings**: attention is computed over fixed-size blocks (the sequence is right-padded to a whole number of blocks, with padded frames masked out), using separate bias-free query/key/value projections.

3. **Self-conditioned CTC**: the CTC posteriors of the middle layer are projected and fed back into the hidden states, and the CTC head is shared between this mid-layer self-conditioning and the final prediction.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/granite_speech5)
* Add Granite Speech 5.0 - (#48288) by @eustlb in [#48288](https://github.com/huggingface/transformers/pull/48288)

### Step3p7

Step-3.7-Flash was proposed in [Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash/) by StepFun. It is a 198B-parameter sparse Mixture-of-Experts vision-language model, pairing a 196B-parameter MoE language backbone with a 1.8B-parameter vision encoder for native image understanding.

StepFun hasn't published a technical report for Step-3.7-Flash, so the details below are drawn from the released checkpoint's configuration rather than a paper.

- **Sparse MoE decoder**: all but the first 3 decoder layers route through a MoE block of 288 routed experts (top-8 per token) plus a single shared expert. The router scores experts with a sigmoid and a learned per-expert bias instead of an auxiliary load-balancing loss, the same strategy as [DeepSeek-V3](./deepseek_v3).
- **Gated attention**: each attenti
