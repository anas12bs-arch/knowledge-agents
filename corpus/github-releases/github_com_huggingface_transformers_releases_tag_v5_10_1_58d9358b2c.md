---
title: "huggingface/transformers v5.10.1 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.10.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-06-03T15:58:40Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.10.1"
---

# huggingface/transformers v5.10.1 released

> Source: github-releases | Category: changelog | 2026-06-03T15:58:40Z

## huggingface/transformers — v5.10.1

# Release v5.10.1
v5.10.0 was yanked as we publish on a corrupted branch. Sorry everyone, this happens when we rush a release!!! 

## New Model additions

### Gemma4 unified+ Gemma4 MTP
<img width="2000" height="400" alt="image" src="https://github.com/user-attachments/assets/5e3ee940-f78d-4343-ac7a-889930800aa6" />

Gemma 4 12B Unified is an **encoder-free** multimodal model with pretrained and instruction-tuned variants. Unlike [standard Gemma 4](./gemma4), which uses dedicated encoder towers, Gemma 4 12B Unified projects raw inputs directly into the language model's embedding space through lightweight linear pipelines. This results in a simpler architecture while maintaining strong multimodal performance.

Key differences from standard Gemma 4:
- **No Vision Tower**: Raw pixel patches are projected directly into LM space via a `Dense + LayerNorm` pipeline with factorized 2D positional embeddings, replacing the vision encoder.
- **No Audio Tower**: Raw 16 kHz waveform samples are chunked into fixed-length frames and projected through a simple `RMSNorm → Linear` pipeline, replacing the mel spectrogram + Conformer encoder.
- **Shared Multimodal Pipeline**: Both vision and audio use the same `Gemma4UnifiedMultimodalEmbedder` (RMSNorm → Linear) for the final projection to text hidden space.

You can find the original Gemma 4 12B Unified checkpoints under the [Gemma 4](https://huggingface.co/collections/google/gemma-4) release.

* who needs encoders? (#46385) by @douglas-reid @sgerrard @vasqu @molbap

### Sapiens2

Sapiens2 is a family of high-resolution vision transformers pretrained on ~1 billion curated human images, designed for human-centric computer vision tasks including pose estimation, body-part segmentation, surface normal estimation, and pointmap estimation. The models scale from 0.4B to 5B parameters and train at native 1K resolution, with hierarchical 4K variants for extended spatial reasoning. Sapiens2 achieves substantial improvements over its predecessor with +4 mAP in pose estimation, +24.3 mIoU in body-part segmentation, and 45.6% error reduction in normal estimation.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/sapiens2) | [Paper](https://huggingface.co/papers/2604.21681)
* Add Sapiens2 Model (#45919) by @guarin in [#45919](https://github.com/huggingface/transformers/pull/45919)

### DeepSeek-OCR-2

DeepSeek-OCR-2 is an OCR-specialized vision-language model built on a distinctive architecture that combines a SAM ViT-B vision encoder with a Qwen2 hybrid attention encoder, connected through an MLP projector to a DeepSeek-V2 Mixture-of-Experts (MoE) language model. The model features a hybrid attention mechanism that applies bidirectional attention over image tokens and causal attention over query tokens, enabling efficient and accurate document understanding. It supports both plain OCR tasks and grounding capabilities with coordinate-aware output for document conversion to markdown format.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_ocr2)
* Add Deepseek-OCR-2 model (#45075) by @thisisiron in [#45075](https://github.com/huggingface/transformers/pull/45075)

### Mellum

Mellum is a code-focused Mixture-of-Experts language model developed by JetBrains. It is derived from the Qwen3-MoE architecture with per-layer-type RoPE and interleaved sliding window attention. The model has 12B total parameters with 2.5B active parameters per token, using 64 routed experts with 8 activated per token across 28 layers.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/mellum)
* feat: Add support for JetBrains' `Mellum` v2 code generation model (#46112) by @shadeMe in [#46112](https://github.com/huggingface/transformers/pull/46112)



## Breaking changes

The Gemma4 vision pooler now casts inputs to float32 before scaling to prevent float16 overflow (inf satura
