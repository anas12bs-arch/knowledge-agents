---
title: "huggingface/transformers v5.20.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.20.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-15T21:38:01Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.20.0"
---

# huggingface/transformers v5.20.0 released

> Source: github-releases | Category: changelog | 2026-10-15T21:38:01Z

## huggingface/transformers — v5.20.0

# Release v5.20.0


## New Model additions

### Muse Spark Open

<img width="2400" height="1296" alt="image" src="https://github.com/user-attachments/assets/bf34ea27-0edf-4ded-ba6f-905b04096126" />

Muse Spark Open is a multimodal mixture-of-experts model from Meta that takes text, images, audio, and video as input and generates text. It has 816B total parameters (42B active per token) and a context window of up to 1,048,576 tokens shared across modalities. It is trained for agentic coding tasks such as multi-file editing, debugging, and tool use. Checkpoints are available in BF16 and NVFP4 formats.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/muse_spark) | [Blog Post](http://hf.co/blog/meta-muse-spark-open)
* Add Muse Spark Open (#49644) by @guarin in [#49644](https://github.com/huggingface/transformers/pull/49644)


### Ling 3.0

Ling 3.0 Flash is a hybrid Mixture-of-Experts language model from InclusionAI. Its decoder groups five Kimi Delta Attention (KDA) layers with one Multi-head Latent Attention (MLA) layer. The MLA blocks use interleaved rotary embeddings and a head-wise output gate, and the feed-forward blocks combine routed and shared experts. It is natively supported in Transformers as `BailingHybridForCausalLM`, so it loads without `trust_remote_code=True`.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/bailing_hybrid)
* [Model] Add native Ling 3.0 Flash support (#49446) by @icavan in [#49446](https://github.com/huggingface/transformers/pull/49446)


### Kolibri1

Kolibri 1 is Aleph Alpha's mixture-of-experts reasoning model, focused on German and English. Each of its 50 layers routes every token to 6 of 384 experts using sigmoid routing, and adds one shared expert. Four sliding-window attention layers alternate with one full-attention layer, and RoPE is applied only in the sliding-window layers.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/kolibri1)
* Add Kolibri 1 (#49463) by @lucamotz in [#49463](https://github.com/huggingface/transformers/pull/49463)


### MiniCPM-V 4.7

[MiniCPM-V](https://huggingface.co/papers/2509.18154) is a series of efficient multimodal large language models developed by [OpenBMB](https://github.com/OpenBMB). Like MiniCPM-V 4.6, the MiniCPM-V 4.7 architecture pairs a SigLIP vision encoder that has a window-attention merger with a Qwen3.5 language model backbone, and supports both 4x and 16x visual downsampling modes.

The main addition over 4.6 is *canvas M-RoPE*: instead of numbering visual tokens along a single 1-D sequence, the model lays every image out on a 2-D canvas and assigns each visual token a `(temporal, height, width)` position, so slices of the same image keep their spatial relationship and video frames keep their temporal order.

* Fix more stuff (#48979) by @zucchini-nlp in [#48979](https://github.com/huggingface/transformers/pull/48979#top)


### UnlimitedOcr

UnlimitedOcr is a single 3B-parameter OCR model from Baidu with a standard 32,768-token context length. It builds on DeepSeek OCR and replaces all decoder attention layers with Reference Sliding Window Attention (R-SWA). This keeps the KV cache constant during decoding, so the model can transcribe dozens of pages in a single forward pass. It supports "gundam" mode (640x640 tiles with dynamic cropping) and "base" mode (a single 1024x1024 view), and it can output region detections with bounding boxes.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/unlimited_ocr) | [Paper](https://huggingface.co/papers/2606.23050 (the docs link only the Hugging Face papers page, "Unlock OCR Works" is not given an arXiv link, so this is the paper URL provided))
* Add Unlimited OCR (#46836) by @guarin in [#46836](https://github.com/huggingface/transformers/pull/46836)


### UltraBERT

UltraBERT is a family of bidirectional text
