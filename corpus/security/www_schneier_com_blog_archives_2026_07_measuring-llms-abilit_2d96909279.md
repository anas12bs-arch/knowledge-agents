---
title: "[schneier] Measuring LLMs’ Ability to Perform Cryptanalysis"
url: "https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html"
source: "security"
category: "security"
tags: ["security", "cybersecurity", "infosec", "schneier"]
date: "2026-07-29T04:27:42Z"
metadata:
  {}
---

# [schneier] Measuring LLMs’ Ability to Perform Cryptanalysis

> Source: security | Category: security | 2026-07-29T04:27:42Z

Measuring LLMs’ Ability to Perform Cryptanalysis

There&#8217;s new benchmark measuring AI&#8217;s ability to perform mathematical cryptanalysis. Anthropic&#8217;s frontier model actually found new attacks. 
 The benchmark: &#8220; CryptanalysisBench: Can LLMs do Cryptanalysis? &#8221; The idea is to benchmark the ability of LLMs to discover new mathematical cryptanalytic attacks against a series of historical algorithms. 
   Abstract:  Cryptanalysis&#8212;the task of finding attacks against cryptographic schemes&#8212;its at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest. Cryptanalysis represents both a clean testbed for frontier reasoning (as practical attacks can be automatically verified) and a domain with unusually high stakes, since the primitives under study underpin our digital security. In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes. We introduce CryptanalysisBench, 191 tasks across six families of cryptographic primitives (block ciphers, hash functions, etc.) drawn primarily from four NIST standardization competitions. Our benchmark consists of three tiers: (i) primitives with known practical breaks; (ii) primitives with no known practical break, evaluated both at full strength and as scaled-down variants; and (iii) a challenge set of production primitives at the frontier of cryptanalysis. Five frontier models (Claude Opus 4.8, Sonnet 5, Mythos 5, GPT-5.5, and the open-weights GLM-5.2) break 65%­86% of Tier 1 schemes, 6­12 Tier-2 schemes at full strength, and 24­61 across all scaled-down variants. Beyond deriving known results, models produce novel cryptanalysis, such as a key-recovery attack that exploits a design flaw in the SpoC AEAD and an error in KINDI’s published CCA-security proof, both to the best of our knowledge not previously known...
