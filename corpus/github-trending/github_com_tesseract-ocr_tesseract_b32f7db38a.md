---
title: "tesseract-ocr/tesseract ⭐74447"
url: "https://github.com/tesseract-ocr/tesseract"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "machine-learning", "hacktoberfest", "lstm", "machine-learning", "ocr"]
date: "2026-06-02T13:00:05Z"
metadata:
  stars: "74447"
  language: "C++"
---

# tesseract-ocr/tesseract ⭐74447

> Source: github-trending | Category: tool | 2026-06-02T13:00:05Z

**tesseract-ocr/tesseract** — ⭐ 74447

Language: C++ | Topics: hacktoberfest, lstm, machine-learning, ocr, ocr-engine, tesseract

Tesseract Open Source OCR Engine (main repository)

# Tesseract OCR

[![Coverity Scan Build Status](https://scan.coverity.com/projects/tesseract-ocr/badge.svg)](https://scan.coverity.com/projects/tesseract-ocr)
[![CodeQL](https://github.com/tesseract-ocr/tesseract/workflows/CodeQL/badge.svg)](https://github.com/tesseract-ocr/tesseract/security/code-scanning)
[![OSS-Fuzz](https://img.shields.io/badge/oss--fuzz-fuzzing-brightgreen)](https://issues.oss-fuzz.com/issues?q=is:open%20title:tesseract-ocr)
\
[![GitHub license](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/LICENSE)
[![Downloads](https://img.shields.io/badge/download-all%20releases-brightgreen.svg)](https://github.com/tesseract-ocr/tesseract/releases/)

## Table of Contents

* [Tesseract OCR](#tesseract-ocr)
  * [About](#about)
  * [Brief history](#brief-history)
  * [Installing Tesseract](#installing-tesseract)
  * [Running Tesseract](#running-tesseract)
  * [For developers](#for-developers)
  * [Support](#support)
  * [License](#license)
  * [Dependencies](#dependencies)
  * [Latest Version of README](#latest-version-of-readme)

## About

This package contains an **OCR engine** - `libtesseract` and a **command line program** - `tesseract`.

Tesseract 4 adds a new neural net (LSTM) based [OCR engine](https://en.wikipedia.org/wiki/Optical_character_recognition) which is focused on line recognition, but also still supports the legacy Tesseract OCR engine of Tesseract 3 which works by recognizing character patterns. Compatibility with Tesseract 3 is enabled by using the Legacy OCR Engine mode (--oem 0).
It also needs [traineddata](https://tesseract-ocr.github.io/tessdoc/Data-Files.html) files which support the legacy engine, for example those from the [tessdata](https://github.com/tesseract-ocr/tessdata) repository.

Stefan Weil is the current lead developer. Ray Smith was the lead developer until 2017. The maintainer is Zdenko Podobny. For a list of contributors see [AUTHORS](https://github.com/tesseract-ocr/tesseract/blob/main/AUTHORS)
and GitHub's log of [contributors](https://github.com/tesseract-ocr/tesseract/graphs/contributors).

Tesseract has **unicode (UTF-8) support**, and can **recognize [more than 100 languages](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html)** "out of the box".

Tesseract supports **[various image formats](https://tesseract-ocr.github.io/tessdoc/InputFormats)** including PNG, JPEG and TIFF.

Tesseract supports **various output formats**: plain text, hOCR (HTML), PDF, invisible-text-only PDF, TSV, ALTO and PAGE.

You should note that in many cases, in order to get better OCR results, you'll need to **[improve the quality](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) of the image** you are giving Tesseract.

This project **does not include a GUI application**. If you need one, please see the [3rdParty](https://tesseract-ocr.github.io/tessdoc/User-Projects-%E2%80%93-3rdParty.html) documentation.
