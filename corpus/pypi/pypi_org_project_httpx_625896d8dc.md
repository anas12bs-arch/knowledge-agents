---
title: "PyPI: httpx v0.28.1"
url: "https://pypi.org/project/httpx/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "httpx"]
date: "2026-05-30T14:32:07Z"
metadata:
  version: "0.28.1"
  package: "httpx"
---

# PyPI: httpx v0.28.1

> Source: pypi | Category: skill | 2026-05-30T14:32:07Z

**httpx** v0.28.1

The next generation HTTP client.

<p align="center">
  <a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/butterfly.png" alt='HTTPX'></a>
</p>

<p align="center"><strong>HTTPX</strong> <em>- A next-generation HTTP client for Python.</em></p>

<p align="center">
<a href="https://github.com/encode/httpx/actions">
    <img src="https://github.com/encode/httpx/workflows/Test%20Suite/badge.svg" alt="Test Suite">
</a>
<a href="https://pypi.org/project/httpx/">
    <img src="https://badge.fury.io/py/httpx.svg" alt="Package version">
</a>
</p>

HTTPX is a fully featured HTTP client library for Python 3. It includes **an integrated command line client**, has support for both **HTTP/1.1 and HTTP/2**, and provides both **sync and async APIs**.

---

Install HTTPX using pip:

```shell
$ pip install httpx
```

Now, let's get started:

```pycon
>>> import httpx
>>> r = httpx.get('https://www.example.org/')
>>> r
<Response [200 OK]>
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=UTF-8'
>>> r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
```

Or, using the command-line client.

```shell
$ pip install 'httpx[cli]'  # The command line client is an optional dependency.
```

Which now allows us to use HTTPX directly from the command-line...

<p align="center">
  <img width="700" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/httpx-help.png" alt='httpx --help'>
</p>

Sending a request...

<p align="center">
  <img width="700" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/httpx-request.png" alt='httpx http://httpbin.org/json'>
</p>

## Features

HTTPX builds on the well-established usability of `requests`, and gives you:

* A broadly [requests-compatible API](https://www.python-httpx.org/compatibility/).
* An integrated command-line client.
* HTTP/1.1 [and HTTP/2 support](https://www.python-httpx.org/http2/).
* Standard synchronous interface, but with [async support if you need it](https://www.python-httpx.org/async/).
* Ability to make requests directly to [WSGI applications](https://www.python-httpx.org/advanced/transports/#wsgi-transport) or [ASGI applications](https://www.python-httpx.org/advanced/transports/#asgi-transport).
* Strict timeouts everywhere.
* Fully type annotated.
* 100% test coverage.

Plus all the standard features of `requests`...

* International Domains and URLs
* Keep-Alive & Connection Pooling
* Sessions wi
