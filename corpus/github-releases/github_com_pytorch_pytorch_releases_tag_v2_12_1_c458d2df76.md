---
title: "pytorch/pytorch v2.12.1 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.12.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-06-18T11:41:33Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.12.1"
---

# pytorch/pytorch v2.12.1 released

> Source: github-releases | Category: changelog | 2026-06-18T11:41:33Z

## pytorch/pytorch — v2.12.1

This release is meant to fix the following regressions and silent correctness issues:
## Regression fixes
- Fix nondeterministic outputs in test_batch_invariance with FLASH_ATTN on NVIDIA B200 GPUs ([#181248](https://github.com/pytorch/pytorch/issues/181248)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
- Fix illegal memory access in the Triton convolution2d_bwd_weight kernel on B100/B200 (sm100) GPUs ([#187081](https://github.com/pytorch/pytorch/issues/187081)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
- Fix fill_ on byte-dtype views with misaligned storage offset ([#186821](https://github.com/pytorch/pytorch/pull/186821))
## Releng / Build
- Drop CPython 3.13t from the binary build matrix ([#182951](https://github.com/pytorch/pytorch/pull/182951))
