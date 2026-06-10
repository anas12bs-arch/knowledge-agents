---
title: "huggingface/transformers v5.11.0 released"
url: "https://github.com/huggingface/transformers/releases/tag/v5.11.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "transformers"]
date: "2026-06-10T21:21:55Z"
metadata:
  repo: "huggingface/transformers"
  version: "v5.11.0"
---

# huggingface/transformers v5.11.0 released

> Source: github-releases | Category: changelog | 2026-06-10T21:21:55Z

## huggingface/transformers — v5.11.0

# Release v5.11.0


## New Model additions

### DiffusionGemma

<img width="1240" height="700" alt="image" src="https://github.com/user-attachments/assets/5081e449-6374-4076-bd96-d295c8334ca4" />

DiffusionGemma is engineered to reduce the sequential bottlenecks of standard causal language models by employing an encoder-decoder architecture specifically optimized for inference speed. During inference, DiffusionGemma leverages multi-canvas sampling, where rather than generating one token at a time, the model iteratively denoises a full block of tokens using a diffusion sampler. This block-autoregressive approach facilitates text generation at higher speeds compared to traditional sequential generation methods.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/diffusion_gemma)
* GPU go brr (#46540) by @gante in [#46540](https://github.com/huggingface/transformers/pull/46540)



### DeepSeek-V3.2

<img width="1135" height="671" alt="image" src="https://github.com/user-attachments/assets/24c9694d-eeae-402c-9a98-f7a3971dd9d0" />

DeepSeek-V3.2-Exp is an experimental model from DeepSeek-AI that introduces DeepSeek Sparse Attention (DSA), a trainable, fine-grained sparse attention mechanism designed to improve training and inference efficiency in long-context scenarios. Built on top of DeepSeek-V3.1-Terminus with a 685B-parameter Mixture-of-Experts backbone, it reduces the quadratic cost of attention over long sequences by attending only to a selected subset of past tokens while maintaining virtually identical benchmark performance. The work was extended in DeepSeek-V3.2 which pairs DSA with scalable reinforcement learning and achieves gold-medal level results on competition math and competitive programming benchmarks.

**Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v32) | [Paper](https://huggingface.co/papers/2512.02556)
* Add deepseek 3.2 exp (#41251) by @ArthurZucker in [#41251](https://github.com/huggingface/transformers/pull/41251)


## Kernels

The `KernelConfig` API was extended to support n-to-1 module fusion and parameter transformation, simplifying how custom kernels are integrated with Transformers modules. Additional fixes include resolving a dtype mismatch in the Mamba2 CUDA kernel path for NemotronH/Zamba2, adding fine-grained fp8/fp4 Triton kernel support, and correcting the FalconMamba fast-path warning to recommend `pip install kernels` instead of `mamba-ssm`.


* Extended & simplified n-to-1 kernel fusion via KernelConfig (#46339) by @michaelbenayoun in [#46339]
* Triton finegrained fp8/fp4 (#46407) by @IlyasMoutawwakil in [#46407]
* Fix dtype mismatch in NemotronH/Zamba2 Mamba2 CUDA-kernel path (`out_proj`) (#46487) by @yuekaizhang in [#46487]
* fix(falcon_mamba): recommend `pip install kernels` in fast-path warning (#46343) by @Anai-Guo in [#46343]


## Parallelization

Fixed model parallel beam search bugs in the Qwen2-VL, Qwen2.5-VL, and Qwen3-VL MoE model families, and added documentation for tensor parallelism support with continuous batching.


* [docs] tp for continuous batching (#46019) by @stevhliu in [#46019]
* revisit history parallel beam search tests to avoid unnecessary fix (#46495) by @kaixuanliu in [#46495]
* fix qwen series VL model's model parallel bug (#46316) by @kaixuanliu in [#46316]


## Bugfixes and improvements

* Fix the offsets in processing (#46525) by @zucchini-nlp in [#46525]
* Fix buggy action sha pin (#46534) by @ydshieh in [#46534]
* Fix trailing comma bug in DataCollatorForLanguageModeling example (#46527) by @JemmaUZH in [#46527]
* Fix missing Gemma4Processor._compute_audio_num_tokens (#46416) by @csantosbh in [#46416]
* Fix InternVL models (#46524) by @hmellor in [#46524]
* fix(afmoe): reduce tokens in test_compile_static_cache to avoid flaky bfloat16 drift (#46521) by @ydshieh in [#46521]
* [CB] Add a "max_requests_per_batch" parameter (#464
