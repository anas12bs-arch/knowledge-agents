---
title: "PyPI: uvicorn v0.48.0"
url: "https://pypi.org/project/uvicorn/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "uvicorn"]
date: "2026-05-30T14:32:08Z"
metadata:
  version: "0.48.0"
  package: "uvicorn"
---

# PyPI: uvicorn v0.48.0

> Source: pypi | Category: skill | 2026-05-30T14:32:08Z

**uvicorn** v0.48.0

The lightning-fast ASGI server.

<p align="center">
  <img width="320" height="320" src="https://raw.githubusercontent.com/tomchristie/uvicorn/main/docs/uvicorn.png" alt='uvicorn'>
</p>

<p align="center">
<em>An ASGI web server, for Python.</em>
</p>

---

[![Build Status](https://github.com/Kludex/uvicorn/workflows/Test%20Suite/badge.svg)](https://github.com/Kludex/uvicorn/actions)
[![Package version](https://badge.fury.io/py/uvicorn.svg)](https://pypi.python.org/pypi/uvicorn)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/uvicorn.svg?color=%2334D058)](https://pypi.org/project/uvicorn)
[![Discord](https://img.shields.io/discord/1051468649518616576?logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/RxKUF5JuHs)

---

**Documentation**: [https://uvicorn.dev](https://uvicorn.dev)

**Source Code**: [https://www.github.com/Kludex/uvicorn](https://www.github.com/Kludex/uvicorn)

---

Uvicorn is an ASGI web server implementation for Python.

Until recently Python has lacked a minimal low-level server/application interface for
async frameworks. The [ASGI specification][asgi] fills this gap, and means we're now able to
start building a common set of tooling usable across all async frameworks.

Uvicorn supports HTTP/1.1 and WebSockets.

## Quickstart

Install using `pip`:

```shell
$ pip install uvicorn
```

This will install uvicorn with minimal (pure Python) dependencies.

```shell
$ pip install 'uvicorn[standard]'
```

This will install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras".

In this context, "Cython-based" means the following:

- the event loop `uvloop` will be installed and used if possible.
- the http protocol will be handled by `httptools` if possible.

Moreover, "optional extras" means that:

- the websocket protocol will be handled by `websockets` (should you want to use `wsproto` you'd need to install it manually) if possible.
- the `--reload` flag in development mode will use `watchfiles`.
- windows users will have `colorama` installed for the colored logs.
- `python-dotenv` will be installed should you want to use the `--env-file` option.
- `PyYAML` will be installed to allow you to provide a `.yaml` file to `--log-config`, if desired.

Create an application, in `example.py`:

```python
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b
