---
title: "pytorch/pytorch v2.14.1 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.14.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-09-30T23:46:48Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.14.1"
---

# pytorch/pytorch v2.14.1 released

> Source: github-releases | Category: changelog | 2026-09-30T23:46:48Z

## pytorch/pytorch — v2.14.1

This release is meant to fix the following regressions and silent correctness issues:

## Silent correctness fixes
- Fix incorrect `torch.linalg.lstsq` solutions on MPS for complex batched underdetermined systems ([#196113](https://github.com/pytorch/pytorch/issues/196113)), fixed by [#196128](https://github.com/pytorch/pytorch/pull/196128)
- Fix non-orthogonal `U` and inaccurate small singular values from `torch.linalg.svd` on MPS for rank-deficient and ill-conditioned inputs ([#196112](https://github.com/pytorch/pytorch/issues/196112)), fixed by [#196139](https://github.com/pytorch/pytorch/pull/196139) and [#199063](https://github.com/pytorch/pytorch/pull/199063)
- Update the CUDA 13.2 Linux binaries to CUDA 13.2.2 ([#196351](https://github.com/pytorch/pytorch/pull/196351)). This NVIDIA update resolves two critical issues that could produce incorrect results ([CUDA 13.2.2 release notes](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html#overview)):
  - cuBLAS: `cublasLtMatmul()` could ignore tensor-wide scaling for NVFP4 matrix multiplications (introduced in CUDA 13.2 Update 1)
  - Compiler: failed thread reconvergence could leave stale or corrupted register values in kernels with nested thread divergence (present since CUDA 12.8)

## Regression fixes
- Fix `torch.linalg.svd`, `torch.linalg.svdvals` and `torch.linalg.lstsq` failing on MPS with a Metal pipeline-state error for inputs above 8192 elements ([#195937](https://github.com/pytorch/pytorch/issues/195937)), fixed by [#195949](https://github.com/pytorch/pytorch/pull/195949) and [#195950](https://github.com/pytorch/pytorch/pull/195950)
- Fix internal assert in `torch.svd(out=)` on MPS for complex inputs ([#195822](https://github.com/pytorch/pytorch/issues/195822)), fixed by [#195872](https://github.com/pytorch/pytorch/pull/195872)

