---
title: "pytorch/pytorch v2.11.0 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.11.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-05-30T14:31:30Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.11.0"
---

# pytorch/pytorch v2.11.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:30Z

## pytorch/pytorch — v2.11.0

# PyTorch 2.11.0 Release Notes
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
  <tr>
    <td>
      Added Support for <strong>Differentiable Collectives</strong> for Distributed Training
    </td>
  </tr>
  <tr>
    <td>
      <strong>FlexAttention</strong> now has a <strong>FlashAttention-4</strong> backend on <strong>Hopper</strong> and <strong>Blackwell</strong> GPUs
    </td>
  </tr>
  <tr>
    <td>
      <strong>MPS (Apple Silicon)</strong> Comprehensive Operator Expansion
    </td>
  </tr>
  <tr>
    <td>
      Added <strong>RNN/LSTM</strong> GPU Export Support
    </td>
  </tr>
  <tr>
    <td>
      Added <strong>XPU Graph</strong> Support
    </td>
  </tr>
</table>

For more details about these highlighted features, you can look at the [release blogpost](https://pytorch.org/blog/pytorch-2-11-release-blog/). Below are the full release notes for this release.

# Backwards Incompatible Changes

## Release Engineering

### Volta (SM 7.0) GPU support removed from CUDA 12.8 and 12.9 binary builds (#172598)

  Starting with PyTorch 2.11, the CUDA 12.8 and 12.9 pre-built binaries no longer include support for Volta GPUs (compute capability 7.0, e.g. V100). This change was necessary to enable updating to CuDNN 9.15.1, which is incompatible with Volta.

  Users with Volta GPUs who need CUDA 12.8+ should use the CUDA 12.6 builds, which continue to include Volta support. Alternatively, build PyTorch from source with Volta included in `TORCH_CUDA_ARCH_LIST`.

  Version 2.10:
  ```
  # CUDA 12.8 builds supported Volta (SM 7.0)
  pip install torch --index-url https://download.pytorch.org/whl/cu128
  # Works on V100
  ```

  Version 2.11:
  ```
  # CUDA 12.8 builds no longer support Volta
  # For V100 users, use CUDA 12.6 builds instead:
  pip install torch --index-url https://download.pytorch.org/whl/cu126
  ```

### PyPI wheels now ship with CUDA 13.0 instead of CUDA 12.x ([#172663](https://github.com/pytorch/pytorch/issues/172663), [announcement](https://dev-discuss.pytorch.org/t/transitioning-pypi-cuda-wheels-to-cuda-13-0-as-the-stable-release-2-11/3325))

  Starting with PyTorch 2.11, `pip install torch` on PyPI installs CUDA 13.0 wheels by default for both Linux x86_64 and Linux aarch64. Previously, PyPI wheels shipped with CUDA 12.x and only Linux x86_64 CUDA wheels were available on PyPI. Users whose systems have only CUDA 12.x drivers installed may encounter errors when running `pip install torch` without specifying an index URL.

  Additionally, CUDA 13.0 only supports Turing (SM 7.5) and newer GPU architectures on Linux x86_64. Maxwell and Pascal GPUs are no longer supported under CUDA 13.0. Users with these older GPUs should use the CUDA 12.6 builds instead.

  CUDA 12.6 and 12.8 binaries remain available via `download.pytorch.org`.

  Version 2.10:
  ```bash
  # PyPI wheel used CUDA 12.x
  pip install torch
  ```

  Version 2.11:
  ```bash
  # PyPI wheel now uses CUDA 13.0
  pip install torch

  # To get CUDA 12.8 wheels instead:
  pip install torch --index-url https://download.pytorch.org/whl/cu128

  # To get CUDA 12.6 wheels (includes Maxwell/Pascal/Volta support):
  pip install torch --index-url https://download.pytorch.org/whl/cu126
  ```

## Python Frontend

### `torch.hub.list()`, `torch.hub.load()`, and `torch.hub.help()` now default the `trust_repo` parameter to `"check"` instead of `None`. The `trust_repo=None` option has been removed. (#174101)

  Previously, passing `trust_repo=None` (or relying on the default) would silently download and run code from untrusted repositories with only a warning. Now, the d
