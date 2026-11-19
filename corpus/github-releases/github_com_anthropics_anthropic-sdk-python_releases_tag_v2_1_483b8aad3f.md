---
title: "anthropics/anthropic-sdk-python v2.11.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.11.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-11-19T20:55:47Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v2.11.0"
---

# anthropics/anthropic-sdk-python v2.11.0 released

> Source: github-releases | Category: changelog | 2026-11-19T20:55:47Z

## anthropics/anthropic-sdk-python — v2.11.0

### Features

* **api:** add Claude Code managed settings to the Admin API
* **api:** add the sandbox_egress_restricted error to Admin API plugin methods


### Bug Fixes

* **client:** encode spaces in query strings as %20

  The AWS SigV4 signature of a request now matches its query string when a parameter contains a space.


### Performance Improvements

* **structured outputs:** build each call's output schema from a cached raw schema


### Chores

* **docs:** explain how the input-token rate limit types differ
* **docs:** name Claude Security in the usage and cost report descriptions
* **docs:** note that a Google Cloud external key's provider and key_name can't be changed
