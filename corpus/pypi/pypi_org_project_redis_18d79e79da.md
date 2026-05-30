---
title: "PyPI: redis v8.0.0"
url: "https://pypi.org/project/redis/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "redis"]
date: "2026-05-30T14:32:09Z"
metadata:
  version: "8.0.0"
  package: "redis"
---

# PyPI: redis v8.0.0

> Source: pypi | Category: skill | 2026-05-30T14:32:09Z

**redis** v8.0.0

Python client for Redis database and key-value store

# redis-py

The Python interface to the Redis key-value store.

[![CI](https://github.com/redis/redis-py/workflows/CI/badge.svg?branch=master)](https://github.com/redis/redis-py/actions?query=workflow%3ACI+branch%3Amaster)
[![docs](https://readthedocs.org/projects/redis/badge/?version=stable&style=flat)](https://redis.readthedocs.io/en/stable/)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/redis/redis-py/blob/master/LICENSE)
[![pypi](https://badge.fury.io/py/redis.svg)](https://pypi.org/project/redis/)
[![pre-release](https://img.shields.io/github/v/release/redis/redis-py?include_prereleases&label=latest-prerelease)](https://github.com/redis/redis-py/releases)
[![codecov](https://codecov.io/gh/redis/redis-py/branch/master/graph/badge.svg?token=yenl5fzxxr)](https://codecov.io/gh/redis/redis-py)

[Installation](#installation) |  [Usage](#usage) | [Advanced Topics](#advanced-topics) | [Contributing](https://github.com/redis/redis-py/blob/master/CONTRIBUTING.md)

---------------------------------------------

**Note:** redis-py 5.0 is the last version of redis-py that supports Python 3.7, as it has reached [end of life](https://devguide.python.org/versions/). redis-py 5.1 supports Python 3.8+.<br>
**Note:** redis-py 6.1.0 is the last version of redis-py that supports Python 3.8, as it has reached [end of life](https://devguide.python.org/versions/). redis-py 6.2.0 supports Python 3.9+.

---------------------------------------------

## How do I Redis?

[Learn for free at Redis University](https://redis.io/learn/university)

[Try the Redis Cloud](https://redis.io/try-free/)

[Dive in developer tutorials](https://redis.io/learn)

[Join the Redis community](https://redis.io/community/)

[Work at Redis](https://redis.io/careers/)

## Installation

Start a redis via docker (for Redis versions >= 8.0):

``` bash
docker run -p 6379:6379 -it redis:latest
```

Start a redis via docker (for Redis versions < 8.0):

``` bash
docker run -p 6379:6379 -it redis/redis-stack:latest
```
To install redis-py, simply:

``` bash
$ pip install redis
```

For faster performance, install redis with hiredis support, this provides a compiled response parser, and *for most cases* requires zero code changes.
By default, if hiredis >= 1.0 is available, redis-py will attempt to use it for response parsing.

``` bash
$ pip install "redis[hiredis]"
```

Looking for a high-level library to handle object mapping? See [redis-om-python](https://github.com
