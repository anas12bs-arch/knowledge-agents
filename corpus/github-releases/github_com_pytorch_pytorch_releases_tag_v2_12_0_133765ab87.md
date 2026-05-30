---
title: "pytorch/pytorch v2.12.0 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.12.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-05-30T14:31:30Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.12.0"
---

# pytorch/pytorch v2.12.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:30Z

## pytorch/pytorch — v2.12.0

# PyTorch 2.12.0 Release Notes

- [Highlights](#highlights)
- [Backwards Incompatible Changes](#backwards-incompatible-changes)
- [Deprecations](#deprecations)
- [New Features](#new-features)
- [Improvements](#improvements)
- [Bug fixes](#bug-fixes)
- [Performance](#performance)
- [Documentation](#documentation)
- [Developers](#developers)
- [Security](#security)

# Highlights

<table>
  <tr><td><strong>Batched linalg.eigh on CUDA</strong> is up to 100x faster due to updated cuSolver backend selection.</td></tr>
  <tr><td>New <strong>torch.accelerator.Graph</strong> API unifies graph capture and replay across CUDA, XPU, and out-of-tree backends.</td></tr>
  <tr><td><strong>torch.export.save</strong> now supports Microscaling (MX) quantization formats, enabling full export of aggressively compressed models.</td></tr>
  <tr><td><strong>Adagrad</strong> now supports <code>fused=True</code>, joining Adam, AdamW, and SGD with a single-kernel optimizer implementation.</td></tr>
  <tr><td><strong>torch.cond</strong> control flow can now be captured and replayed inside CUDA Graphs.</td></tr>
  <tr><td><strong>ROCm</strong> users gain expandable memory segments, rocSHMEM symmetric memory collectives, and FlexAttention pipelining.</td></tr>
</table>

For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.

# Backwards Incompatible Changes

## Build Frontend

- Strengthened SVE compile checks in `FindARM.cmake`, which may reject previously accepted but incorrect SVE configurations ([#176646](https://github.com/pytorch/pytorch/pull/176646))

  Source builds that enable SVE now validate the compiler configuration more strictly. If a build previously passed with an incomplete or mismatched SVE setup, it may now fail during CMake configuration instead of later in compilation. Update the compiler/toolchain flags so they accurately describe the target SVE support, or disable SVE for that build.

- Updated the minimum CUDA version required to build PyTorch from source to CUDA 12.6 ([#178925](https://github.com/pytorch/pytorch/pull/178925))

  Building PyTorch from source with CUDA versions older than 12.6 is no longer supported. Users building custom binaries should install CUDA 12.6 or newer and make sure `CUDA_HOME` points to that installation.

  Version 2.11:
  ```bash
  CUDA_HOME=/usr/local/cuda-12.4 python setup.py develop
  ```

  Version 2.12:
  ```bash
  CUDA_HOME=/usr/local/cuda-12.6 python setup.py develop
  ```

- Enforced a C++20 minimum in CMake build files ([#178662](https://github.com/pytorch/pytorch/pull/178662))

  Source builds now require a compiler and build configuration that support C++20. If you maintain custom build scripts or downstream extensions that build PyTorch from source, update the compiler and remove assumptions that PyTorch can be built as C++17.

## Distributed

- `torch.distributed.nn.functional` ops now raise `RuntimeError` under `torch.compile` ([#177342](https://github.com/pytorch/pytorch/pull/177342))

  All ops in `torch.distributed.nn.functional` (e.g., `broadcast`, `all_reduce`, `all_gather`, `reduce_scatter`, `all_to_all_single`) now raise `RuntimeError` when called inside `torch.compile`. Users should migrate to the functional collectives API in `torch.distributed._functional_collectives`.

  Version 2.11:
  ```python
  @torch.compile
  def my_func(x):
      return torch.distributed.nn.functional.all_reduce(x, op=ReduceOp.SUM)
  ```

  Version 2.12:
  ```python
  @torch.compile
  def my_func(x):
      return torch.distributed._functional_collectives.all_reduce(x, reduceOp="sum", group=group)
  ```

## TorchElastic

- `torchrun` now defaults to an OS-assigned free port for single-node training instead of port 29500 ([#175699](https://github.com/pytorch/pytorch/pull/175699))

  When running `torchrun --nproc-per-node=N script.py` without speci
