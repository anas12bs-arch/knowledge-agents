---
title: "pytorch/pytorch v2.14.0 released"
url: "https://github.com/pytorch/pytorch/releases/tag/v2.14.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "pytorch"]
date: "2026-09-02T20:02:46Z"
metadata:
  repo: "pytorch/pytorch"
  version: "v2.14.0"
---

# pytorch/pytorch v2.14.0 released

> Source: github-releases | Category: changelog | 2026-09-02T20:02:46Z

## pytorch/pytorch — v2.14.0

# PyTorch 2.14.0 Release Notes

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
  <tr><td><strong>NVGEMM</strong> brings CuTeDSL-generated CUTLASS kernels to Inductor, with epilogue fusion, scaled and NVFP4 GEMM, and grouped-reduction epilogues autotuned alongside Triton and ATen</td></tr>
  <tr><td><strong><code>torch.switch</code></strong> generalizes <code>torch.cond</code> to multi-way branching, and <code>torch.while_loop</code> can now be captured in a CUDA graph</td></tr>
  <tr><td><strong>Declarative dynamic shapes via <code>@dynamic_spec</code></strong>, shared across <code>torch.compile</code>, <code>torch.export</code> and <code>make_fx</code></td></tr>
  <tr><td><strong>Experimental <code>torch.compile</code> support for complex-valued tensors</strong>: Opt-in support decomposes supported complex operations into real and imaginary computations, enabling compiler backends to optimize more complex-number workloads.</td></tr>
  <tr><td><strong>A new <code>nccl2</code> backend for PyTorch Distributed</strong>, ported from torchcomms, implementing the full collective contract with nonblocking communicators and eager communicator splitting</td></tr>
  <tr><td><strong>Fault tolerance becomes a first-class <code>c10d</code> concept</strong>, with in-place process-group reconfiguration, one-sided RMA windows, and a Flight Recorder that works for any backend rather than only NCCL</td></tr>
  <tr><td><strong>Apple Silicon gains native linear algebra</strong>, including Jacobi-kernel SVD, <code>eigh</code>, QR and Cholesky, alongside a five-part reduction rewrite and a further MPSGraph to Metal kernel migration</td></tr>
  <tr><td><strong>Broader platform support</strong>: ROCm 7.14 wheels are produced from the TheRock pip SDK, Intel XPU adds native graph capture, and Inductor targets Rubin (<code>sm_107</code>)</td></tr>
</table>

For more details about these highlighted features, you can look at the release blogpost. Below are the full release notes for this release.

# Backwards Incompatible Changes

## torch.nn

- `torch.nn.LinearCrossEntropyOptions` no longer accepts `acc_policy="balanced"`; use `"compact"` instead (#188283)

  The `"balanced"` policy was removed because `"compact"` provides the same weight-gradient accumulation precision with lower memory use on CUDA, already uses the equivalent scratch layout for mixed-precision inputs on other devices, and was never selected by `"auto"`. Constructing the options with `acc_policy="balanced"` now raises `ValueError: invalid acc_policy: 'balanced'; expected one of 'auto', 'accurate', 'compact'`.

  Before:

  ```python
  options = torch.nn.LinearCrossEntropyOptions(acc_policy="balanced")
  loss = torch.nn.functional.linear_cross_entropy(
      input, linear_weight, target, options=options
  )
  ```

  After:

  ```python
  options = torch.nn.LinearCrossEntropyOptions(acc_policy="compact")
  loss = torch.nn.functional.linear_cross_entropy(
      input, linear_weight, target, options=options
  )
  ```

## Autograd

- Clamp and min/max boundary subgradients now follow the selected dispatcher schema's input space (#191142)

  This affects gradients exactly at nondifferentiable bounds or ties. A scalar clamp bound is a fixed parameter, so the input gradient at equality changes from `1` to the minimum-norm subgradient `0`. A Tensor bound is part of the differentiable input space, so `clamp`, `clamp_min`, and `clamp_max` now split the gradient evenly between the input and bound at an ordinary tie instead of assigning it entirely to the input. `fmin` and `fmax` use the same even tie split, and forward-mode AD for the mi
