---
title: "huggingface/transformers v5.22.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.22.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-10-29T15:35:54Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.22.0"
---

# huggingface/transformers v5.22.0 released

> Source: github-releases | Category: changelog | 2026-10-29T15:35:54Z

## huggingface/transformers — v5.22.0

## New Models

### Mistral Large 4 (Le Chonk)

<img width="1329" height="780" alt="image" src="https://github.com/user-attachments/assets/1cff9ca7-19e3-4622-8db6-fb1cfa842579" />

Mistral Large 4 is Mistral's largest and most capable model to date: a 1 trillion-parameter natively multimodal Mixture-of-Experts model with 49 billion active parameters per token (52 billion including embeddings and output layers), trained from scratch on 3,800 NVIDIA Grace Blackwell GPUs in Mistral's own datacenters in Europe.

Mistral Large 4 unifies instruction following, reasoning, coding, and agentic workflows in a single set of weights. While a generalist model, it shows especially good performance on workloads such as cybersecurity, finance, and law, and it surpasses frontier closed models on visual grounding. It is natively fluent in 160+ languages, including every official language of the European Union.

#### Key Features

Mistral Large 4 includes the following architectural choices:

- **~1T total / ~52B active parameters**: granular Mixture-of-Experts with 128 routed experts (4 active per token) and 1 shared expert.
- **1M context length**, for long-context workloads.
- **Multimodal input**: accepts text and image input, with text output. Pixtral-style vision encoder trained to handle variable image sizes and aspect ratios.
- **Instruct and Reasoning functionalities** with function calls, reasoning effort configurable per request.

Mistral Large 4 offers the following capabilities:

- **Reasoning Mode**: three reasoning efforts — `low`, `medium`, `high` (default) — so the same model can answer a quick chat reply or work through a complex agentic run.
- **Vision**: analyzes images, charts, technical drawings, and documents, with state-of-the-art visual grounding among open weights.
- **Multilingual**: natively fluent in 160+ languages, including all official languages of the European Union.
- **System Prompt**: strong adherence and support for system prompts.
- **Agentic**: native function calling, JSON output, and strict JSON schema enforcement.
- **Cybersecurity**: state of the art among open-weight models for security work, while refusing malicious requests.
- **Large Context Window**: supports a 1M context window.

The model is released under the [**Mistral Ecosystem Open-Weight License**](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/LICENSE): a modified version of the MIT license, for both commercial and non-commercial use — operating a Model-as-a-Service business requires a separate commercial license with Mistral.

#### Recommended Settings

- **Reasoning Effort**:
  - `'low'` / `'medium'` / `'high'` — default is `'high'`.
  - Use `reasoning_effort="high"` for complex prompts and agentic usage, `'low'` for fast chat replies and `'medium'` for day to day usage.
- **Sampling**: for all reasoning efforts, we recommend the following sampling parameters:
  - `temperature=1.0`
  - `top_p=0.95`
- **System Prompt**: define a clear environment and use case, including guidance on how to effectively leverage tools in agentic systems.
- **Tools**: keep the set of tools well-defined and limit their number to the minimum required for the use case.
- **Context**: the checkpoint supports a 1M context window.

## Breaking changes

* 🚨 Separate EP logic into its own file (#49679) by @3outeille

## Quantization

FP8 quantized models can now be used for adapter training (such as LoRA with PEFT). Backward passes were added to the dense and grouped FP8 matmuls, and `is_trainable` is now `True`. Backward also dequantizes experts in chunks and skips autograd at inference, which cuts peak memory in the MoE layer backward from about 28.9 GiB to 2.8 GiB at 8k tokens. Separately, the AMD CI image now install


* FP8 backward: chunked expert dequant, skip autograd.Function at inference (#50117) by @ArthurZucker in [#50117]
* Train adapters on top of FP8 weights (#50031) by @qgallouedec
