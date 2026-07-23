---
title: "[infoq] Ink & Switch Introduces Bijou64: Canonical Variable-Length Integer Encoding for Safe Parsing"
url: "https://www.infoq.com/news/2026/07/bijou64-canonical-varint/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global"
source: "engineering"
category: "engineering"
tags: ["system-design", "architecture", "scalability", "infoq"]
date: "2026-07-23T11:25:28Z"
metadata:
  {}
---

# [infoq] Ink & Switch Introduces Bijou64: Canonical Variable-Length Integer Encoding for Safe Parsing

> Source: engineering | Category: engineering | 2026-07-23T11:25:28Z

Ink & Switch Introduces Bijou64: Canonical Variable-Length Integer Encoding for Safe Parsing

Ink & Switch published bijou64, a variable-length integer encoding where every number has exactly one byte representation, closing the canonicality bug class behind attacks on PKCS#1, JWT libraries, and Bitcoin. The design also decodes two to ten times faster than LEB128. Community ports to Elixir, Go, Perl, and Java followed, while HN commenters debated SIMD performance and residual range checks.   By Steef-Jan Wiggers
