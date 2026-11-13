---
title: "huggingface/transformers v5.23.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.23.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-11-13T15:32:17Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.23.0"
---

# huggingface/transformers v5.23.0 released

> Source: github-releases | Category: changelog | 2026-11-13T15:32:17Z

## huggingface/transformers — v5.23.0

# Release v5.23.0


## New Model additions

### Inkling2

<img width="1200" height="675" alt="image" src="https://github.com/user-attachments/assets/9115e142-1be3-4f79-a51d-ea0e5c25b152" />

Inkling 2 Small is a multimodal model from Thinking Machines Lab that accepts text and image inputs and generates text outputs, and it is intended for use in English and other languages and across multiple coding languages. Its language backbone has 48 mixture-of-experts decoder layers, each routing tokens to 8 of 384 experts, for 594B total and 17B active parameters. It keeps the Inkling decoder (learned relative attention, short causal convolutions, mixture-of-experts layers) and adds block attention residuals, gated attention with a learned sink, and dynamic key/value convolutions. Images are encoded by a Perception Encoder-based vision transformer and projected into the language model embeddings, one embedding per 40x40 pixel patch.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/inkling2) | [Blog Post](https://thinkingmachines.ai/news/inkling-2-small/)
* Add inkling2 (#50682) by @guarin in [#50682](https://github.com/huggingface/transformers/pull/50682)

### JEV

JEV is a decision head that scores single-token labels with a linear layer at the last token of the prompt, soft-capped like the logits of a language model head. `JevForDecision` is the model of the checkpoint and its head, and it reads the head files shipped next to the weights (`head.safetensors` and `judge_config.json` for JEV). The same head is also used by GEV and reads the 255 answer codes of pplx-decider and d3, and it can be run through the experimental `decision` pipeline or directly with `decide`.

**Note:** JEV and the decision pipeline are currently experimental. Their APIs, configuration, and behavior may change as development continues. They should be used with caution in production environments.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/jev)
* Add Jev + decision core (#50054) by @ArthurZucker in [#50054](https://github.com/huggingface/transformers/pull/50054)

### LFM3

<img width="732" height="815" alt="image" src="https://github.com/user-attachments/assets/5a67fe26-2cee-4bbf-bc51-65e8f843b756" />

LFM3 is the third generation of Liquid Foundation Models from Liquid AI. Like LFM2, it is a hybrid architecture that combines gated short convolutions with grouped-query attention, with the attention layers split between full-attention and sliding-window layers. The attention layers apply RMSNorm to the query and key heads and gate their output with a per-head sigmoid. Every layer applies a sandwich norm to the operator and feed-forward outputs before the residual addition.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/lfm3)
* [Model] LFM3 Family: LFM3-Text (#50322) by @paulpak58 in [#50322](https://github.com/huggingface/transformers/pull/50322)

### Dots 3 Note Preview

Dots 3 Note Preview is a mixture-of-experts causal language model that accepts native text, image, video, and audio inputs. It uses a shared vision encoder for images and videos and a Whisper-style audio encoder, and both encoders project their outputs into the language model's hidden space before autoregressive text generation. BF16 and FP8 inference are supported.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/dots3_note)
* Add dots3-note Preview model support (#47844) by @miraclezqc in [#47844](https://github.com/huggingface/transformers/pull/47844)

### LFM3-VL

LFM3-VL is a vision-language model family from Liquid AI, built on the LFM3 language model. It takes images and videos at their native resolution together with text. It combines a hybrid vision encoder (a linear patchifier, gated depthwise 2D convolution layers, and bidirectional grouped-query attention layers with 2D rotary embedding
