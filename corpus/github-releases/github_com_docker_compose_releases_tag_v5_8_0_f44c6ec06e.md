---
title: "docker/compose v5.8.0 released"
url: "https://github.com/docker/compose/releases/tag/v5.8.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "compose"]
date: "2026-11-17T17:58:11Z"
metadata:
  repo: "docker/compose"
  version: "v5.8.0"
---

# docker/compose v5.8.0 released

> Source: github-releases | Category: changelog | 2026-11-17T17:58:11Z

## docker/compose — v5.8.0

## What's Changed

> ℹ️ **Scheduled jobs are now supported.** A job is a one-shot unit of work declared in the top-level `jobs:` element of your Compose file, run on demand or on a schedule. 
Scheduling needs **Docker Engine 29.10 or later with the jobs extension enabled** (it is off by default: `dockerd --extension-enable org.mobyproject.jobs.v0`). Manual jobs keep working on any engine, and projects that declare no jobs are unaffected.

```yaml
services:
  db:
    image: postgres
jobs:
  backup:
    image: backup-tool
    depends_on: [db]
    triggers:
      schedule:
        - cron: "0 3 * * *"
```

> * `docker compose up` (or `create`) registers the scheduled jobs with the engine, which fires them on its own clock; `docker compose down` removes them. On an engine without jobs support, `up` refuses a project with scheduled jobs before creating anything.
> * `docker compose run backup` triggers a job right away: its dependencies start first, its logs are streamed and its exit code is returned. On an engine without jobs support, it runs as a one-off service with a warning, as before.

### ✨ Improvements

**Jobs**
* Jobs: add support for one-shot and scheduled `jobs` by @glours in https://github.com/docker/compose/pull/14155

**Full Changelog**: https://github.com/docker/compose/compare/v5.7.2...v5.8.0

