---
title: "pytorch/pytorch v2.13.0 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.13.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-07-08T18:08:45Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.13.0"
---

# pytorch/pytorch v2.13.0 released

> Source: github-releases | Category: changelog | 2026-07-08T18:08:45Z

## pytorch/pytorch — v2.13.0

# PyTorch 2.13.0 Release Notes

- [Highlights](#highlights)
- [Backwards Incompatible Changes](#backwards-incompatible-changes)
- [Deprecations](#deprecations)
- [New Features](#new-features)
- [Improvements](#improvements)
- [Bug fixes](#bug-fixes)
- [Performance](#performance)
- [Documentation](#documentation)
- [Developers](#developers)

# Highlights

<table>
  <tr><td><strong>FlexAttention</strong> lands on Apple Silicon (MPS), with up to ~12x speedup over SDPA on sparse patterns, and gains a deterministic backward path on CUDA for reproducible gradient computation.</td></tr>
  <tr><td><strong>CuTeDSL "Native DSL" backend</strong> gives Inductor a second high-performance code path (alongside Triton) for key GPU operations, with faster compilation. [Prototype]</td></tr>
  <tr><td><strong><code>nn.LinearCrossEntropyLoss</code></strong> combines the final prediction and loss computation to cut peak GPU memory by up to 4x for large-vocabulary language model training.</td></tr>
  <tr><td><strong>torchcomms</strong>, a new communications backend for PyTorch Distributed, improves fault tolerance, scalability, and debuggability for large-cluster training.</td></tr>
  <tr><td><strong>FSDP2</strong> now overlaps reduce-scatter and all-gather communications via a dedicated process group (opt-in), increasing distributed training throughput.</td></tr>
  <tr><td><strong>Python 3.15 wheel support</strong> for PyTorch on Linux via the pytorch repository index, including builds compatible with free-threaded 3.15t.</td></tr>
  <tr><td><strong>Broader platform support</strong>: ROCm gains AOTriton 0.12b with native HIP CMake, Arm adds Armv9-A <code>torch.compile</code> targeting, and Intel XPU exposes new device telemetry APIs.</td></tr>
</table>

For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.

# Tracked Regressions

### ROCm wheels break `torch.compile` on CPU in environments without a GPU

Running a `torch==2.13.0+rocm7.2` wheel in an environment where no GPU is available (`torch.cuda.is_available()` is `False`) breaks `torch.compile` on the CPU path: the first compile raises `RuntimeError: Can't detect vectorized ISA for CPU` ([#189194](https://github.com/pytorch/pytorch/issues/189194)). This is a regression from `torch==2.12.1+rocm7.2`, which compiles CPU code fine (detecting e.g. `VecAVX2`) in the same setup. The 2.13 ROCm wheel appears to rely on something present in the ROCm builder image to detect the CPU vectorized ISA, so it works when run on a ROCm image but fails on a plain CPU-only image.

Workaround: run the `+rocm` wheel on a ROCm image, or install a standard CPU/CUDA build for GPU-less environments.

# Backwards Incompatible Changes

- Stop building CPython 3.13t (free-threaded) binaries (#182951)

  Upstream `pypa/manylinux` removed CPython 3.13t (free-threaded) on 2026-05-07, because 3.13t
  was experimental and has been superseded by the now-non-experimental CPython 3.14t. As a result,
  PyTorch 2.13 no longer ships `cp313t` wheels (Linux, Triton, and related artifacts). Users on the
  free-threaded interpreter should move to Python 3.14t.

  PyTorch 2.12:
  ```bash
  # cp313t (free-threaded 3.13) wheels were available
  python3.13t -m pip install torch
  ```

  PyTorch 2.13:
  ```bash
  # Use free-threaded Python 3.14t instead
  python3.14t -m pip install torch
  ```

- Bare `PyObject` is no longer allowed in operator schemas (#184209)

  Bare `PyObject` was accidentally accepted in operator schema strings in
  PyTorch 2.12. This was undocumented and is now rejected, since `torch.compile`
  does not support arbitrary `PyObject` inputs to custom ops. If
  you parse or register a schema with a bare `PyObject` argument or return type,
  you will now get a schema parse error.

  PyTorch 2.12:
  ```python
  >>> from torch._C import parse_schema
  >>> parse_schema("foo(Py
