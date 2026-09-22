---
title: "Show HN: InstinctFlash – Run 5B world-action models in real time on Jetson Thor"
url: "https://github.com/General-Instinct/InstinctFlash"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-09-22T18:22:39Z"
metadata:
  score: "10"
---

# Show HN: InstinctFlash – Run 5B world-action models in real time on Jetson Thor

> Source: hackernews | Category: news | 2026-09-22T18:22:39Z

Score: 10 | Comments: 0

Hey HN, Guanming here, cofounder of General Instinct. We just released InstinctFlash, a high-performance serving framework for robotics models. It’s licensed under AGPL-3.0.<p>On Jetson Thor, we see speedups about 1.2x to 7.9x from runtime optimizations alone and up to 33.78x for LingBot-VA when we combine those runtime optimizations with a distilled few-step diffusion scheduler, going from the original 25 visual &#x2F; 50 action steps to 2 &#x2F; 4 steps. Across 50 Robotwin2.0 tasks, we evaluated 1,153 episodes per configuration, LingBot-VA with InstinctFlash at 2 visual &#x2F; 4 action steps achieved a 90.5% success rate, compared with 92.1% for the baseline at 25 visual &#x2F; 50 action steps.<p>Here’s an optimized 5B world action model, running in real time on a Jetson Thor:
<a href="https:&#x2F;&#x2F;youtu.be&#x2F;nku65iyL5Fw" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;nku65iyL5Fw</a><p>InstinctFlash currently supports 8 VLA &#x2F; world-action model families, including pi0.5 and NVIDIA Cosmos Policy, across RTX 4090 &#x2F; 5090 and Jetson Thor.<p>Just give it your fine-tuned checkpoint and InstinctFlash handles the rest, exposing the accelerated model through a Python runtime or an OpenPI-compatible WebSocket server.<p>We started working on this because we kept running into the same problem while deploying robot policies, the models were getting much better, but inference was often way too slow for the control loop we actually wanted.<p>For pi0.5, mixed-precision GEMMs and CUDA graphs speed up computation and reduce launch overhead. For Cosmos, caching avoids redundant computation across diffusion steps. World-action models’ diffusion denoising step depends on the previous one which motivated our work on few-step distillation.<p>Right now, InstinctFlash contains 6 aspects of optimization.<p>- Graph: CUDA graph capture, memory planning and separating prefill from repeated execution.<p>- Cache: Reusing KV and conditioning state across diffusion steps and prediction calls.<p>- Attention: Specialized attention paths for different model architectures.<p>- Kernels: Fused operations and kernels tailored to specific backends and tensor layouts.<p>- Precision: FP8 and mixed-precision execution.<p>- Model: Few-step distillation for diffusion and action generation.<p>Teams at Samsung, Siemens, and other robotics startups have used InstinctFlash for model acceleration on VLAs, WAMs, and diffusion-based world models. Now we are opening up access to you.<p>Feel free to try it here:
<a href="https:&#x2F;&#x2F;github.com&#x2F;General-Instinct&#x2F;InstinctFlash" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;General-Instinct&#x2F;InstinctFlash</a><p>More implementation details and benchmarks:
<a href="https:&#x2F;&#x2F;general-instinct.com&#x2F;blog&#x2F;instinctflash-edge-inference">https:&#x2F;&#x2F;general-instinct.com&#x2F;blog&#x2F;instinctflash-edge-inferen...</a><p>Would love to hear your feedback!
