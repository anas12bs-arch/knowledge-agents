---
title: "tar checksums its headers and never your files"
url: "https://dev.to/remdore/tar-checksums-its-headers-and-never-your-files-ed6"
source: "devto"
category: "news"
tags: ["devto", "programming", "tech-article"]
date: "2026-10-05T12:46:41Z"
metadata:
  tag: "programming"
---

# tar checksums its headers and never your files

> Source: devto | Category: news | 2026-10-05T12:46:41Z

I built a tar archive by hand from the spec. Flip a byte in a file's contents and tar extracts it with exit code 0; flip one in the header and it refuses. Plus the 8 GiB octal limit, why there is no index, and why the same files tar to different bytes.

Reactions: 7
