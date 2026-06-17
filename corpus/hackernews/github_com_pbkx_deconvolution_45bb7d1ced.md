---
title: "Show HN: Deconvolution – a Rust image deconvolution and restoration crate"
url: "https://github.com/pbkx/deconvolution"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-17T20:37:17Z"
metadata:
  score: "25"
---

# Show HN: Deconvolution – a Rust image deconvolution and restoration crate

> Source: hackernews | Category: news | 2026-06-17T20:37:17Z

Score: 25 | Comments: 4

I&#x27;ve been working on deconvolution, a comprehensive Rust image deconvolution and restoration library. Deconvolution implements 28 different image deconvolution&#x2F;restoration methods which range from practical blur removal techniques to research-grade scientific imaging algorithms.<p>Features:<p>- Top-level functions use image::DynamicImage and return images<p>- Inverse filters, Wiener, Richardson-Lucy, constrained, proximal, Krylov, MLE restoration<p>- Blind Richardson-Lucy, blind maximum likelihood, parametric PSF estimation<p>- Kernel2D, Kernel3D, Transfer2D, Transfer3D, Blur2D&#x2F;Blur3D<p>- Gaussian, motion, defocus, microscopy models, support utilities, PSF&#x2F;OTF conversion<p>- Edge tapering, apodization, range normalization, NSR estimation<p>- Deterministic blur, noise, synthetic fixture generation<p>- ndarray support for 2D image arrays and 3D volume<p>this project is a WIP, of course:)
