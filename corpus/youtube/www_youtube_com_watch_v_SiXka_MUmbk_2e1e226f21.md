---
title: "[leerob] How to ship an in-browser image generator in under 50 MB"
url: "https://www.youtube.com/watch?v=SiXka_MUmbk"
source: "youtube"
category: "video"
tags: ["youtube", "video", "tutorial", "leerob"]
date: "2026-11-20T23:28:49Z"
metadata:
  {}
---

# [leerob] How to ship an in-browser image generator in under 50 MB

> Source: youtube | Category: video | 2026-11-20T23:28:49Z

How to ship an in-browser image generator in under 50 MB

I’ll show how I adapted image generation models for in-browser inference under strict constraints, from a 48 MB GAN implementation to a larger 400 MB diffusion pipeline. I’ll cover PyTorch to ONNX conversion, compatibility patches, WebGPU and WebAssembly support, and the tradeoffs required for fast, local inference in the browser.

Resources: 
Try NanoDreamer → https://goo.gle/4zxb6Ag
Try NanoDiffuser → https://goo.gle/4zv2MRx

Speaker: Utku Coban

Chapters:
0:00 - Introduction
0:19 - Main project constraints
1:32 - NanoDreamer architecture and size optimization
2:56 - Model output examples
3:20 - Training a smaller StyleGAN2
4:32 - Converting StyleGAN2 to ONNX format
6:59 - Replacing custom operations with portable ONNX ops
7:36 - In-browser inference flow and WebGPU
9:47 - Speed benchmarks across devices
10:25 - NanoDiffuser: text-conditioned diffusion
11:18 - Running generation on a microcontroller
12:19 - Demos and conclusion

See more Web AI talks →  https://goo.gle/WebAIVideos 
Subscribe to Chrome for Developers → https://goo.gle/ChromeDevs 


#WebAISummit2026


Event: Web AI Summit 2026
