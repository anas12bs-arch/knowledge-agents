---
title: "pavlin-policar/openTSNE ⭐1622"
url: "https://github.com/pavlin-policar/openTSNE"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "embedding", "dimensionality-reduction", "embedding", "machine-learning", "tsne"]
date: "2026-09-08T04:58:48Z"
metadata:
  stars: "1622"
  language: "Python"
---

# pavlin-policar/openTSNE ⭐1622

> Source: github-trending | Category: tool | 2026-09-08T04:58:48Z

**pavlin-policar/openTSNE** — ⭐ 1622

Language: Python | Topics: dimensionality-reduction, embedding, machine-learning, tsne, visualization

Extensible, parallel implementations of t-SNE

openTSNE
========

|Build Status| |ReadTheDocs Badge| |License Badge|

openTSNE is a modular Python implementation of t-Distributed Stochasitc Neighbor Embedding (t-SNE) [1]_, a popular dimensionality-reduction algorithm for visualizing high-dimensional data sets. openTSNE incorporates the latest improvements to the t-SNE algorithm, including the ability to add new data points to existing embeddings [2]_, massive speed improvements [3]_ [4]_ [5]_, enabling t-SNE to scale to millions of data points and various tricks to improve global alignment of the resulting visualizations [6]_.

.. figure:: docs/source/images/macosko_2015.png
   :alt: Macosko 2015 mouse retina t-SNE embedding
   :align: center

   A visualization of 44,808 single cell transcriptomes obtained from the mouse retina [7]_ embedded using the multiscale kernel trick to better preserve the global aligment of the clusters.

- `Documentation <http://opentsne.readthedocs.io>`__
- `User Guide and Tutorial <https://opentsne.readthedocs.io/en/latest/tsne_algorithm.html>`__
- Examples: `basic <https://opentsne.readthedocs.io/en/latest/examples/01_simple_usage/01_simple_usage.html>`__, `advanced <https://opentsne.readthedocs.io/en/latest/examples/02_advanced_usage/02_advanced_usage.html>`__, `preserving global alignment <https://opentsne.readthedocs.io/en/latest/examples/03_preserving_global_structure/03_preserving_global_structure.html>`__, `embedding large data sets <https://opentsne.readthedocs.io/en/latest/examples/04_large_data_sets/04_large_data_sets.html>`__
- `Speed benchmarks <https://opentsne.readthedocs.io/en/latest/benchmarks.html>`__

Installation
------------

openTSNE can be installed on all `supported versions of Python <https://devguide.python.org/versions/>`_.

Conda
~~~~~

openTSNE can be easily installed from ``conda-forge`` with

::

   conda install --channel conda-forge opentsne

`Conda package <https://anaconda.org/conda-forge/opentsne>`__

PyPi
~~~~

openTSNE is also available through ``pip`` and can be installed with

::

   pip install opentsne

`PyPi package <https://pypi.org/project/openTSNE>`__

Installing from source
~~~~~~~~~~~~~~~~~~~~~~

If you wish to install openTSNE from source, please run

::

   pip install .


in the root directory to install the appropriate dependencies and compile the necessary binary files.

Please note that openTSNE requires a C/C++ compiler to be available on the system.

In order for openTSNE to utilize multiple threads, the C/C++ compiler
must support ``OpenMP``. In practice, almost all compilers
implement this with the exception of older version of ``clang`` on OSX
systems.

To squeeze the most out of openTSNE, you may also consider installing
FFTW3 prior to installation. FFTW3 implements the Fast Fourier
Transform, which is heavily used in openTSNE. If FFTW3 is not available,
openTSNE will use numpy’s implementation of the FFT, which is slightly
slower than FFTW. The difference is only noticeable with large data sets
containin
