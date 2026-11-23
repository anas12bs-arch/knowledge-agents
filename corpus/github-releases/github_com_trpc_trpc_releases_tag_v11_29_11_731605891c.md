---
title: "trpc/trpc v11.29.11 released"
url: "https://github.com/trpc/trpc/releases/tag/v11.29.11"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "trpc"]
date: "2026-11-23T19:35:28Z"
metadata:
  repo: "trpc/trpc"
  version: "v11.29.11"
---

# trpc/trpc v11.29.11 released

> Source: github-releases | Category: changelog | 2026-11-23T19:35:28Z

## trpc/trpc — v11.29.11

## @trpc/server

### Fixes

* fix(server): close WebSocket upgrades with an unparseable URL instead of crashing ([GHSA-wx68-jchj-87rh](https://github.com/trpc/trpc/security/advisories/GHSA-wx68-jchj-87rh)) by @KATT in https://github.com/trpc/trpc/commit/11f79856c41d012fcb430f0f34f4307c700a6528
* fix(server): stop formDataToObject from reaching built-in prototypes ([GHSA-pmm4-m3wj-qm6r](https://github.com/trpc/trpc/security/advisories/GHSA-pmm4-m3wj-qm6r)) by @KATT in https://github.com/trpc/trpc/commit/3c0b92730b7b120d9ac7833019a0df729563d514
* fix(server): give nextAppDirCaller procedures only validated input by @KATT in https://github.com/trpc/trpc/commit/811de989c45b15922f315815ed211dba33e415c6
* fix(server): only build arrays from FormData indices with no gaps by @KATT in https://github.com/trpc/trpc/commit/84adfefcd47cbc9c6cfb9ec1eaa75dc3d60ad82d

## @trpc/next

### Documentation

* docs(next): say that experimental_nextCacheLink shares results across requests by @KATT in https://github.com/trpc/trpc/pull/8155

**Full Changelog**: https://github.com/trpc/trpc/compare/v11.29.10...v11.29.11

