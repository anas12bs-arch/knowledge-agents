---
title: "sherlock-project/sherlock ⭐84234"
url: "https://github.com/sherlock-project/sherlock"
source: "github-trending"
category: "tool"
tags: ["github", "trending", "cli", "cli", "cti", "cybersecurity", "forensics"]
date: "2026-05-30T14:30:49Z"
metadata:
  stars: "84234"
  language: "Python"
---

# sherlock-project/sherlock ⭐84234

> Source: github-trending | Category: tool | 2026-05-30T14:30:49Z

**sherlock-project/sherlock** — ⭐ 84234

Language: Python | Topics: cli, cti, cybersecurity, forensics, hacktoberfest, information-gathering

Hunt down social media accounts by username across social networks

<p align="center">
  <br>
  <a href="https://sherlock-project.github.io/" target="_blank"><img src="images/sherlock-logo.png" alt="sherlock"/></a>
  <br>
  <span>Hunt down social media accounts by username across <a href="https://sherlockproject.xyz/sites">400+ social networks</a></span>
  <br>
</p>

<p align="center">
  <a href="https://sherlockproject.xyz/installation">Installation</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="https://sherlockproject.xyz/usage">Usage</a>
  &nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;
  <a href="https://sherlockproject.xyz/contribute">Contributing</a>
</p>

<p align="center">
<img width="70%" height="70%" src="images/demo.png" alt="demo"/>
</p>


## Installation

<p align="center">
  <a href="https://www.osint.industries/" target="_blank"><img src="images/banner.jpg" alt="OSINT Industries"/></a>
</p>

> [!WARNING]  
> Packages for ParrotOS and Ubuntu 24.04, maintained by a third party, appear to be __broken__.  
> Users of these systems should defer to [`uv`](https://docs.astral.sh/uv/)/`pipx`/`pip` or Docker.

| Method | Notes |
| - | - |
| `pipx install sherlock-project` | `pip` or [`uv`](https://docs.astral.sh/uv/) may be used in place of `pipx` |
| `docker run -it --rm sherlock/sherlock` |
| `dnf install sherlock-project` | |

Community-maintained packages are available for Debian (>= 13), Ubuntu (>= 22.10), Homebrew, Kali, and BlackArch. These packages are not directly supported or maintained by the Sherlock Project.

See all alternative installation methods [here](https://sherlockproject.xyz/installation).

## General usage

To search for only one user:
```bash
sherlock user123
```

To search for more than one user:
```bash
sherlock user1 user2 user3
```

Accounts found will be stored in an individual text file with the corresponding username (e.g ```user123.txt```).

```console
$ sherlock --help
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT] [--output OUTPUT] [--csv] [--xlsx] [--site SITE_NAME] [--proxy PROXY_URL] [--dump-response]
                [--json JSON_FILE] [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color] [--browse] [--local] [--nsfw] [--txt] [--ignore-exclusions]
                USERNAMES [USERNAMES ...]

Sherlock: Find Usernames Across Social Networks (Version 0.16.0)

positional arguments:
  USERNAMES             One or more usernames to check with social networks. Check similar usernames using {?} (replace to '_', '-', '.').

options:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT
                        If using multiple usernames, the output of the results will be saved to this folder.
  --output OUTPUT, -o OUTPUT
                        If using single username, the output of the result will be saved to this file.
  --csv
