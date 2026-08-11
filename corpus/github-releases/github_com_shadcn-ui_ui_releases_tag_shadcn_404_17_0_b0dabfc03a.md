---
title: "shadcn-ui/ui shadcn@4.17.0 released"
url: "https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.17.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "ui"]
date: "2026-08-11T21:09:15Z"
metadata:
  repo: "shadcn-ui/ui"
  version: "shadcn@4.17.0"
---

# shadcn-ui/ui shadcn@4.17.0 released

> Source: github-releases | Category: changelog | 2026-08-11T21:09:15Z

## shadcn-ui/ui — shadcn@4.17.0

### Minor Changes

- [#10453](https://github.com/shadcn-ui/ui/pull/10453) [`deda4df80fb350230b2fce2b575e769a90cae076`](https://github.com/shadcn-ui/ui/commit/deda4df80fb350230b2fce2b575e769a90cae076) Thanks [@nbouvrette](https://github.com/nbouvrette)! - Add SOCKS4/SOCKS5 proxy support to the registry HTTP stack via `ALL_PROXY=socks5://...` (the curl convention), backed by the `socks` package.

  Proxy selection now goes through a `createProxyDispatcher(env)` factory that checks `ALL_PROXY` / `all_proxy` for a `socks*://` URL before falling back to the existing HTTP/HTTPS handling. `ALL_PROXY` with a non-SOCKS scheme is ignored here — `HTTP_PROXY` / `HTTPS_PROXY` remain the way to configure those. Existing `HTTPS_PROXY` / `HTTP_PROXY` / `NO_PROXY` handling via `undici.EnvHttpProxyAgent` is unchanged.
