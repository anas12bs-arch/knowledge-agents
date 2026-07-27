---
title: "prisma/prisma 7.9.1 released"
url: "https://github.com/prisma/prisma/releases/tag/7.9.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "prisma"]
date: "2026-07-27T16:12:40Z"
metadata:
  repo: "prisma/prisma"
  version: "7.9.1"
---

# prisma/prisma 7.9.1 released

> Source: github-releases | Category: changelog | 2026-07-27T16:12:40Z

## prisma/prisma — 7.9.1

Today, we're issuing a patch release to resolve a security advisory in a transitive dependency of Prisma CLI (via `@prisma/dev`).

This fixes https://github.com/prisma/prisma/issues/29780.

It does not actually affect `@prisma/dev` or Prisma CLI so no urgent action is required, but it is recommended to upgrade nevertheless to avoid false positives from security scanners.
