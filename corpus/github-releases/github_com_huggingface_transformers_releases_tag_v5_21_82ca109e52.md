---
title: "huggingface/transformers v5.21 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.21"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-26T18:55:39Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.21"
---

# huggingface/transformers v5.21 released

> Source: github-releases | Category: changelog | 2026-10-26T18:55:39Z

## huggingface/transformers — v5.21

# Release v5.21.0


## New Model additions

### MiniCPM-OCR

MiniCPM-OCR is a document-understanding model from OpenBMB's MiniCPM-V family. It keeps the MiniCPM-V 4.6 architecture, which pairs a SigLIP vision encoder and a window-attention merger with a Qwen3.5 language model. It is specialized for reading text-dense images such as scanned pages, screenshots, receipts and tables.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/minicpm_ocr) | [Paper](https://huggingface.co/papers/2509.18154)
* Feat test (#49920) by @guarin in [#49920](https://github.com/huggingface/transformers/pull/49920)

### Flint
<img width="3200" height="1800" alt="flint_benchmarks_nvfp4" src="https://github.com/user-attachments/assets/c45955fb-dfcc-4266-8223-b0d70efb9a5b" />

Flint is Recursive's mixture-of-experts language model. Compared to a standard SwiGLU MoE transformer such as Qwen3-MoE, it uses hybrid attention (sliding-window attention with rotary embeddings over the current token and the previous 512 tokens in most layers, and full attention without positional encoding in the remaining layers). It also has learned attention sinks, as in GPT-OSS, with per-head RMS-normalized queries and keys. Each sparse layer routes a token to 6 of 256 experts by sigmoid score and adds an ungated shared expert, and the first two layers are dense.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/flint)
* Add Flint model support. (#49824) by @lovishmadaan in [#49824](https://github.com/huggingface/transformers/pull/49824)

### UltraVBert

UltraVBert extends ModernVBert by pairing the UltraBERT text encoder with a SigLIP vision encoder for visual document understanding and retrieval. Its image processor splits each page into 512-pixel tiles plus a global view. The connector merges each 4 x 4 block of vision patches into one token, so a tile becomes 64 image tokens, and RMS-normalizes them to the scale of UltraBERT's token embeddings. The `max_image_tiles` setting (27 by default) caps the number of tiles per page.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/ultravbert)
* Add UltraVBERT (#49685) by @athrael-soju in [#49685](https://github.com/huggingface/transformers/pull/49685)

### Gradium Phonon TTS

Gradium Phonon TTS is Gradium's family of on-device text-to-speech models, trained with the Pocket TTS recipe. A causal transformer reads a voice prompt and the text, then emits one continuous 32-dimensional audio latent per step at 12.5 Hz through a one-step flow head, and an end-of-speech head decides when the utterance ends. The latents are decoded to 24 kHz audio by a Pocket TTS audio tokenizer. Unlike Pocket TTS, voice conditioning uses 512-dimensional latents from a separate, unreleased speaker codec, so voices come as precomputed latents and cannot be cloned from a recording.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/gradium_phonon_tts)
* Add GradiumPhononTTS (#49791) by @eustlb in [#49791](https://github.com/huggingface/transformers/pull/49791)

### Pocket TTS

Pocket TTS is Kyutai's 100M-parameter text-to-speech model, built as a Continuous Audio Language Model that runs faster than real time on CPU. A causal transformer emits one continuous audio latent per frame (12.5 Hz) through a one-step flow head, and an end-of-speech head decides when to stop. A Mimi-based audio tokenizer encodes voice prompts and decodes the generated latents to 24 kHz audio. Two flow heads are released, Lagrangian self-distillation (default) and drifting, and voices can be cloned from a recording, passed as precomputed latents, or loaded from cached KV states.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/pocket_tts) | [Paper](https://huggingface.co/papers/2509.06926 (the Continuous Audio Language Models paper, arXiv 2509.06926). It is the only
