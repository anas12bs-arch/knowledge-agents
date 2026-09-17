---
title: "denoland/deno v2.9.7 released"
url: "https://github.com/denoland/deno/releases/tag/v2.9.7"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-09-17T10:06:13Z"
metadata:
  repo: "denoland/deno"
  version: "v2.9.7"
---

# denoland/deno v2.9.7 released

> Source: github-releases | Category: changelog | 2026-09-17T10:06:13Z

## denoland/deno — v2.9.7

### 2.9.7 / 2026.09.16

- fix(audit): honor configured CA stores (#36728)
- fix(cache): make HTTP authority paths unambiguous (#36356)
- fix(cli): accept all valid sys permission descriptors (#36753)
- fix(cli): don't duplicate passthrough args for deno deploy/sandbox (#36722)
- fix(cli): generate valid bash completions (#36736)
- fix(cli): preserve double dash before the entrypoint (#36835)
- fix(cli): restore optional-value semantics for deno bundle --sourcemap
  (#36723)
- fix(completions): keep the dash on short flags in zsh completions (#36720)
- fix(desktop): complete deferred window close and fix NAPI symbol export on
  Linux (#36718)
- fix(ext/http): extract traceparent from Deno.serve regardless of header name
  case (#36840)
- fix(ext/node): allow repeated child process signals (#36644)
- fix(ext/node): check resolved IP against net deny list in tcp_wrap bind
  (#36482)
- fix(ext/node): don't panic on prime sizes below 2 bits (#36400)
- fix(ext/node): improve node:dns error codes and lookupService/setLocalAddress
  compat (#36552)
- fix(ext/node): normalize resourceUsage maxRSS on macOS (#36784)
- fix(install): validate lockfile tarball registry paths (#36473)
- fix(lsp): resolve the newest prerelease of jsr packages that have no stable
  release (#36655)
- fix(net): check permissions for multicast membership (#36529)
- fix(node): align IncomingMessage header map prototypes (#36438)
- fix(node): preserve AsyncLocalStorage exit context (#36464)
- fix(npm): correct the pnpm lockfile import against real-world lockfiles
  (#36727)
- fix(npm): validate lockfile tarball origins (#36430)
- fix(permissions): fold unix socket paths for case-insensitive filesystems
  (#36553)
- fix(permissions): parse unix: net rules as POSIX paths (#36785)
- fix(process): clear supplementary groups before changing identity (#36433)
- fix(sqlite): refuse symlink database paths (#36357)
- fix(transpile): don't report diagnostics from bundled assets in declaration
  emit (#36716)
- fix(web): avoid flushing compression streams on every write (#36744)
- fix: add missing property desktop.app.identifier (#36774)
- fix: hash source contents for V8 code cache (#36743)
- fix: point JSON schema $id values at the maintained GitHub raw endpoint
  (#36747)
- fix: toplevel fetch/cron leak its spans (#36757)
- fix: validate --ignore-scripts package selectors (#36742)
- perf(core): drop dead module-graph retention (#36683)
- perf(core): make extension op tables const in static memory (#36696)
- perf(core): split OpCtx into shared OpCommonCtx + borrowed op declarations
  (#36693)
- perf(ext/node): Buffer hex paths via native Uint8Array toHex/setFromHex
  (#36531)
