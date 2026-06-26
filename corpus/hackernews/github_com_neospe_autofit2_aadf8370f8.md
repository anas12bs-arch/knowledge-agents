---
title: "Show HN: Autofit2 – End-to-end pipeline for multilingual text classification"
url: "https://github.com/neospe/autofit2"
source: "hackernews"
category: "news"
tags: ["hackernews", "tech-news"]
date: "2026-06-26T21:57:29Z"
metadata:
  score: "5"
---

# Show HN: Autofit2 – End-to-end pipeline for multilingual text classification

> Source: hackernews | Category: news | 2026-06-26T21:57:29Z

Score: 5 | Comments: 0

Hi HN, Stefan here. autofit2 is a project I have been using at my previous company and is now opensourced. It has been used extensively in automated text moderation, but can be applied to any text&#x2F;document classification task. We had success modeling offensive texts in 20+ languages (cf. github.com&#x2F;neospe&#x2F;dataload for all the datasets).<p>It&#x27;s an integrated pipeline for lightweight multilingual text classification, covering preprocessing, training, and evaluation. It implements SetFit, a few-shot learning technique that works well for low-data regimes (down to a few dozen examples), and offers high throughput on CPUs, since it&#x27;s based on Sentence Transformers. Dependencies are kept lean, but of course PyTorch itself isn&#x27;t exactly small.<p>autofit2 takes a base model and a JSON config as input, and outputs a TorchServe model archive as well as a model card. The model card includes any benchmarks you have for your task, self-consistency tests, estimated CO2 emissions of the finetune, as well as an entropy-based bias analysis. For the bias eval, small test corpora for 50 languages are included. It works best with my EAR (Entropy-based Attention Regularization) fork of Sentence Transformers.<p>Feedback is welcome.
