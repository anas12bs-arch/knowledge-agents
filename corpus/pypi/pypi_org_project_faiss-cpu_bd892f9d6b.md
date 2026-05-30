---
title: "PyPI: faiss-cpu v1.14.2"
url: "https://pypi.org/project/faiss-cpu/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "faiss-cpu"]
date: "2026-05-30T14:32:06Z"
metadata:
  version: "1.14.2"
  package: "faiss-cpu"
---

# PyPI: faiss-cpu v1.14.2

> Source: pypi | Category: skill | 2026-05-30T14:32:06Z

**faiss-cpu** v1.14.2

A library for efficient similarity search and clustering of dense vectors.

# Faiss

Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. Some of the most useful algorithms are implemented on the GPU. It is developed primarily at Meta's [Fundamental AI Research](https://ai.facebook.com/) group.

## News

See [CHANGELOG.md](CHANGELOG.md) for detailed information about latest features.

## Introduction

Faiss contains several methods for similarity search. It assumes that the instances are represented as vectors and are identified by an integer, and that the vectors can be compared with L2 (Euclidean) distances or dot products. Vectors that are similar to a query vector are those that have the lowest L2 distance or the highest dot product with the query vector. It also supports cosine similarity, since this is a dot product on normalized vectors.

Some of the methods, like those based on binary vectors and compact quantization codes, solely use a compressed representation of the vectors and do not require to keep the original vectors. This generally comes at the cost of a less precise search but these methods can scale to billions of vectors in main memory on a single server. Other methods, like HNSW and NSG add an indexing structure on top of the raw vectors to make searching more efficient.

The GPU implementation can accept input from either CPU or GPU memory. On a server with GPUs, the GPU indexes can be used a drop-in replacement for the CPU indexes (e.g., replace `IndexFlatL2` with `GpuIndexFlatL2`) and copies to/from GPU memory are handled automatically. Results will be faster however if both input and output remain resident on the GPU. Both single and multi-GPU usage is supported.

## Installing

Faiss comes with precompiled libraries for Anaconda in Python, see [faiss-cpu](https://anaconda.org/pytorch/faiss-cpu), [faiss-gpu](https://anaconda.org/pytorch/faiss-gpu) and [faiss-gpu-cuvs](https://anaconda.org/pytorch/faiss-gpu-cuvs). The library is mostly implemented in C++, the only dependency is a [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) implementation. Optional GPU support is provided via CUDA or AMD ROCm, and the Python interface is also optional. The backend GPU implementations of NVIDIA [cuVS](https://github.com/rapidsai
