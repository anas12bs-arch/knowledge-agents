---
title: "gin-gonic/gin ⭐88586"
url: "https://github.com/gin-gonic/gin"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "go", "framework", "gin", "go", "middleware"]
date: "2026-06-02T22:13:48Z"
metadata:
  stars: "88586"
  language: "Go"
---

# gin-gonic/gin ⭐88586

> Source: github-trending | Category: tool | 2026-06-02T22:13:48Z

**gin-gonic/gin** — ⭐ 88586

Language: Go | Topics: framework, gin, go, middleware, performance, router

Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

# Gin Web Framework

<img align="right" width="159px" src="https://raw.githubusercontent.com/gin-gonic/logo/master/color.png">

[![Build Status](https://github.com/gin-gonic/gin/actions/workflows/gin.yml/badge.svg?branch=master)](https://github.com/gin-gonic/gin/actions/workflows/gin.yml)
[![Trivy Security Scan](https://github.com/gin-gonic/gin/actions/workflows/trivy-scan.yml/badge.svg)](https://github.com/gin-gonic/gin/actions/workflows/trivy-scan.yml)
[![codecov](https://codecov.io/gh/gin-gonic/gin/branch/master/graph/badge.svg)](https://codecov.io/gh/gin-gonic/gin)
[![Go Report Card](https://goreportcard.com/badge/github.com/gin-gonic/gin)](https://goreportcard.com/report/github.com/gin-gonic/gin)
[![Go Reference](https://pkg.go.dev/badge/github.com/gin-gonic/gin?status.svg)](https://pkg.go.dev/github.com/gin-gonic/gin?tab=doc)
[![Sourcegraph](https://sourcegraph.com/github.com/gin-gonic/gin/-/badge.svg)](https://sourcegraph.com/github.com/gin-gonic/gin?badge)
[![Open Source Helpers](https://www.codetriage.com/gin-gonic/gin/badges/users.svg)](https://www.codetriage.com/gin-gonic/gin)
[![Release](https://img.shields.io/github/release/gin-gonic/gin.svg?style=flat-square)](https://github.com/gin-gonic/gin/releases)

## 📰 Gin 1.12.0 is now available!

We're excited to announce the release of **[Gin 1.12.0](https://gin-gonic.com/en/blog/news/gin-1-12-0-release-announcement/)**! This release brings new features, performance improvements, and important bug fixes. Check out the [release announcement](https://gin-gonic.com/en/blog/news/gin-1-12-0-release-announcement/) on our official blog for the full details.

---

Gin is a high-performance HTTP web framework written in [Go](https://go.dev/). It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to [httprouter](https://github.com/julienschmidt/httprouter). Gin is designed for building REST APIs, web applications, and microservices where speed and developer productivity are essential.

**Why choose Gin?**

Gin combines the simplicity of Express.js-style routing with Go's performance characteristics, making it ideal for:

- Building high-throughput REST APIs
- Developing microservices that need to handle many concurrent requests
- Creating web applications that require fast response times
- Prototyping web services quickly with minimal boilerplate

**Gin's key features:**

- **Zero allocation router** - Extremely memory-efficient routing with no heap allocations
- **High performance** - Benchmarks show superior speed compared to other Go web frameworks
- **Middleware support** - Extensible middleware system for authentication, logging, CORS, etc.
- **Crash-free** - Built-in recovery middleware prevents panics from crashing your server
- **JSON validation** - Automatic request/response JSON binding and validation
- **Route grouping** - Organize related routes and apply common middleware
- **Error management** - Centralized error handling and logging
- **B
