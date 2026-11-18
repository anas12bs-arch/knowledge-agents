---
title: "anthropics/anthropic-sdk-python v2.10.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.10.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-11-18T00:08:19Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v2.10.0"
---

# anthropics/anthropic-sdk-python v2.10.0 released

> Source: github-releases | Category: changelog | 2026-11-18T00:08:19Z

## anthropics/anthropic-sdk-python — v2.10.0

### Features

* **api:** add beta support for the billing_policy request parameter
* **api:** add contract_spend_limit_reached error code to messages
* **api:** add error codes for linked billing refusals
* **api:** add the user_profile_billing_not_authorized error code
* **api:** add webhook events for external key failure and recovery


### Bug Fixes

* **client:** stop reporting failed aiohttp connections as timeouts
* **types:** keep deprecated model aliases and the types nested under them working


### Chores

* **api:** rename error data models, deprecating the old names
* **docs:** clarify which AWS KMS keys a workspace can use on Claude Platform on AWS
* **docs:** clarify which credential work get, update and list accept
* **docs:** clarify which uploads a plugin pin holds back
* **docs:** note that a plugin scan's reason also covers errored scans

  `content_scan.reason` on an errored scan now says why there is no verdict. It is not a security finding, so code that treats any `reason` as a concern should also check `status`.

* **internal:** don't report moved classes as breaking changes


### Documentation

* name each SDK's own types in rename deprecations
