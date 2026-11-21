---
title: "huggingface/transformers v5.24.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.24.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-11-21T12:34:13Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.24.0"
---

# huggingface/transformers v5.24.0 released

> Source: github-releases | Category: changelog | 2026-11-21T12:34:13Z

## huggingface/transformers — v5.24.0

# Release v5.24.0

## New Model additions

### Inkling 2 Mini

Inkling 2 Mini is a multimodal model from Thinking Machines Lab that takes text and images as input and generates text. It is based on Inkling 2 Small, but has 24 decoder layers instead of 48. To make up for the smaller depth, layers 6 to 17 are looped three times, and a learned message-passing mechanism mixes the residuals of the previous pass into the attention and MoE inputs of each loop layer. The decoder routes each token to 8 of 128 experts. A research checkpoint with a variable number of loop passes is also released, so you can trade speed against quality at inference time. Both checkpoints contain NVFP4 and MXFP8 layers that are dequantized at load time.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2_loop) | [Blog Post](https://huggingface.co/blog/inkling2mini)

- Add Inkling2 Mini ([#51050](https://github.com/huggingface/transformers/pull/51050)) by [@guarin](https://github.com/guarin)

### Apertus 1.5

Apertus 1.5 is a multimodal model from the Swiss AI Initiative that accepts text, images and audio and generates text. It extends the Apertus language model with the EMU3.5 vision tokenizer (an image-only VQGAN) and WavTokenizer for audio. Images and audio are converted into discrete tokens that the language backbone processes alongside text in a shared input vocabulary. Image and audio generation are not supported.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/apertus1p5)

- Apertus 1.5: add model ([#47662](https://github.com/huggingface/transformers/pull/47662)) by [@RaphaelKreft](https://github.com/RaphaelKreft)

### WavTokenizer

WavTokenizer encodes 24 kHz mono audio into discrete tokens using a single codebook, at 40 or 75 tokens per second depending on the checkpoint, and reconstructs audio from those tokens. It is available as `WavTokenizerModel` (encode + decode) and `WavTokenizerEncoderModel` (encode only), with speech, music/audio and unified checkpoints. The 40-token-per-second variant is the audio tokenizer of Apertus 1.5.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/wavtokenizer) | [Paper](https://huggingface.co/papers/2408.16532)

- Added as part of Apertus 1.5 ([#47662](https://github.com/huggingface/transformers/pull/47662)) by [@RaphaelKreft](https://github.com/RaphaelKreft)

### Dory

Dory is a looped (latent-recurrent) language model from NVIDIA. It uses a normalized-GPT architecture with interleaved sliding-window and full attention layers. A shared block of layers is applied repeatedly, so the amount of compute spent per token can be adjusted at inference time by changing the loop count on the same checkpoint.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/dory)

- Add Dory model support ([#50099](https://github.com/huggingface/transformers/pull/50099)) by [@shan18](https://github.com/shan18)

### HY4-VL

HY4-VL (Hunyuan V4 Vision-Language) combines the HYV4 mixture-of-experts text backbone with a vision encoder for image-text and video-text generation. It supports dynamic-resolution visual inputs and uses multimodal rotary position embeddings (mRoPE) for temporal and spatial positions.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/hy_v4_vl)

- Add HY4-VL ([#50877](https://github.com/huggingface/transformers/pull/50877)) by [@vasqu](https://github.com/vasqu)

### Omnilingual ASR

Omnilingual ASR is Meta FAIR's suite of speech-recognition models covering more than 1,600 languages. Each model pairs a Wav2Vec2-style audio encoder with one of two heads: a CTC head (`OmniASRForCTC`) for fast non-autoregressive decoding, or an audio-language-model head (`OmniASRForConditionalGeneration`) that projects audio into a Llama decoder and optionally accepts a language code (e.g. `"eng_Latn"`) f
