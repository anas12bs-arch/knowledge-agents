---
title: "pytorch/pytorch v2.15.0 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.15.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-10-28T19:13:39Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.15.0"
---

# pytorch/pytorch v2.15.0 released

> Source: github-releases | Category: changelog | 2026-10-28T19:13:39Z

## pytorch/pytorch — v2.15.0

# PyTorch 2.15.0 Release Notes

- [Highlights](#highlights)
- [Backwards Incompatible Changes](#backwards-incompatible-changes)
- [Deprecations](#deprecations)
- [New Features](#new-features)
- [Improvements](#improvements)
- [Bug fixes](#bug-fixes)
- [Performance](#performance)
- [Documentation](#documentation)
- [Security](#security)
- [Developers](#developers)

# Highlights

<table>
  <tr><td><strong>Rewritten NCCL backend becomes the default</strong>, with a flight recorder that dumps on hangs and <code>TORCH_DIST_USE_NCCL2=0</code> or <code>nccl-legacy</code> as rollback paths</td></tr>
  <tr><td><strong>One-sided transports for <code>torch.distributed</code></strong>, with a NIXL backend and CUDA-graph-capturable transfers</td></tr>
  <tr><td><strong>FSDP2 and pipelining gain finer memory and communication control</strong>, with fp32 for precision-sensitive parameters, CUDA-graph-captured gradient accumulation, and gradient reduction overlapped with compute</td></tr>
  <tr><td><strong>Faster 4-bit (NVFP4) LLM decoding on NVIDIA Blackwell GPUs</strong> through fewer, better-overlapped kernel launches in NVGEMM</td></tr>
  <tr><td><strong>Apple Silicon gains FP8 and faster decode</strong>, with <code>float8_e4m3fn</code> and <code>_scaled_mm</code>, a new <code>grouped_mm</code> with a decode fast path (1.32–1.34x tokens/s on MoE decode), and public <code>torch.mps.Stream</code> APIs</td></tr>
  <tr><td><strong>Broader platform support</strong> with FlyDSL kernels on AMD gfx950, Tensor Data Mover support for gfx1250 (MI450), ROCm 10.0 wheels, simpler SYCL kernel authoring and multi-GPU profiling on Intel GPUs, CUDA 13.2 as the default wheel with CUDA 13.4 alongside it, and <code>torch.compile</code> on Python 3.15</td></tr>
</table>

For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.

# Backwards Incompatible Changes

## Python Frontend

### `import torch` can no longer be re-executed in the same process, including via `importlib.reload(torch)` (#194654)

`importlib.reload(torch)` and `del sys.modules["torch"]` + re-import now raise, as does retrying `import torch` after it failed. Re-running the module body was already unsafe in exactly the same way as the retry, so the new check does not distinguish the two. Normal use is unaffected: a successful import leaves `torch` in `sys.modules` so the body never re-runs, and re-entrant imports from a backend extension during autoload still short-circuit on `sys.modules` without reaching the check.

Version 2.14:
```python
import importlib
import torch

importlib.reload(torch)
# RuntimeError: Only a single TORCH_LIBRARY can be used to register the namespace triton; ...
# (re-importing after a failed `import torch` failed with similarly misleading errors or could segfault)
```

Version 2.15:
```python
import importlib
import torch

importlib.reload(torch)
# ImportError: `torch` can only be initialized once per process, so this module cannot
# be imported again: neither via `importlib.reload(torch)`, nor by re-importing after
# a failed `import torch`.
```

### Nested tensors are no longer allowlisted for `torch.load(..., weights_only=True)` (#194380)

Nested jagged and strided nested tensors are no longer on the default `weights_only` allowlist. Loading a checkpoint that contains one with `weights_only=True` (the default) now fails with `Unsupported global: GLOBAL torch.nested._internal.nested_tensor._rebuild_njt was not an allowed global by default` (or `GLOBAL torch._utils._rebuild_nested_tensor` for strided nested tensors). To load checkpoints containing nested tensors, allow them explicitly with `torch.serialization.safe_globals` (see below), or use `weights_only=False` for trusted files.

Version 2.14:
```python
loaded = torch.load("njt.pt", weights_only=True)  # works
```

Version 2.15:
```python
from torch.nested._internal.nested_tensor import _rebuild_njt, NestedTensor
with torch.seriali
