---
title: "docker/compose v5.6.1 released"
url: "https://github.com/docker/compose/releases/tag/v5.6.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-10-21T11:43:57Z"
metadata:
  repo: "docker/compose"
  version: "v5.6.1"
---

# docker/compose v5.6.1 released

> Source: github-releases | Category: changelog | 2026-10-21T11:43:57Z

## docker/compose — v5.6.1

update to go1.26.10
These releases include 1 security fix following the security policy:

- crypto/x509: mitigation for security concerns with a specific Certificate Authority

  We're blocking trust in a small set of intermediate certificates due to specific security concerns around their operation.

  Verify will now filter out chains which contain these intermediates, preventing them from being returned to the caller.

  We highly recommend immediately upgrading to this release.

  This is CVE-2026-111943 and Go issue https://go.dev/issue/82345.

**Full Changelog**: https://github.com/docker/compose/compare/v5.6.0...v5.6.1
