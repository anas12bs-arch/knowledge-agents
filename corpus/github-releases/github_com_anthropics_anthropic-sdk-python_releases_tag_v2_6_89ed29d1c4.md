---
title: "anthropics/anthropic-sdk-python v2.6.0 released"
url: "https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.6.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "anthropic-sdk-python"]
date: "2026-11-05T22:55:13Z"
metadata:
  repo: "anthropics/anthropic-sdk-python"
  version: "v2.6.0"
---

# anthropics/anthropic-sdk-python v2.6.0 released

> Source: github-releases | Category: changelog | 2026-11-05T22:55:13Z

## anthropics/anthropic-sdk-python — v2.6.0

### Features

* **api:** add error code for ramp limit errors
* **api:** add error codes for External Key validation failures
* **api:** add support for signing organization members out everywhere


### Bug Fixes

* **bedrock,vertex:** raise error-code and status exception classes on platform clients
* **bedrock:** keep a custom http_client and aws_profile on copies made with copy and with_options


### Chores

* **client:** stop recording sampling parameters on OpenTelemetry spans
* **docs:** describe the type and message of API errors
* **internal:** define the status error mapping once on the base client
* **internal:** tell contributors when a runtime type check belongs
* **tests:** remove ambient ANTHROPIC_ and AWS_ variables before the tests run


### Documentation

* **client:** describe the type, message, code and details of API errors
* **client:** list each method's errors without their descriptions
