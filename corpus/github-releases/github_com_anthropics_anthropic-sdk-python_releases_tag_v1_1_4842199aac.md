---
title: "anthropics/anthropic-sdk-python v1.14.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.14.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-10-15T05:12:00Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v1.14.0"
---

# anthropics/anthropic-sdk-python v1.14.0 released

> Source: github-releases | Category: changelog | 2026-10-15T05:12:00Z

## anthropics/anthropic-sdk-python — v1.14.0

### Features

* **api:** add execution_identity to Managed Agents agents
* **api:** add organization_type_not_supported error to spend limit lists
* **api:** add telemetry destination test endpoint
* **api:** add telemetry destinations to the Admin API
* **client:** add OpenTelemetry tracing for API calls, streaming and tool runs


### Bug Fixes

* **api:** rename telemetry destination test response model
* **client:** close dropped streams without waiting for the collector
* **streaming:** pass unknown event types through the message stream helpers
* **streaming:** stop raising "Unexpected event order" for an event before message_start


### Chores

* **docs:** correct prefill, thinking, fallback and model descriptions
* **docs:** document the scope required to assign the managed role
* **docs:** update model examples
* **internal:** narrow the tripwire test rule in the contributor guides


### Documentation

* **api:** clarify when custom tool results can be sent
* **api:** say is_enabled is always true for user spend limits
