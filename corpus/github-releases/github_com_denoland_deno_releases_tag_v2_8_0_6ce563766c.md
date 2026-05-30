---
title: "denoland/deno v2.8.0 released"
url: "https://github.com/denoland/deno/releases/tag/v2.8.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-05-30T14:31:18Z"
metadata:
  repo: "denoland/deno"
  version: "v2.8.0"
---

# denoland/deno v2.8.0 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:18Z

## denoland/deno — v2.8.0

### 2.8.0 / 2026.05.22

Read more: http://deno.com/blog/v2.8

- feat: accept `deno audit fix` as alias for `deno audit --fix` (#34273)
- feat: add --watch flag to deno check (#34224)
- feat: add `deno bump-version` subcommand (#30562)
- feat: add `deno why` subcommand (#32908)
- feat: support workspaces in `deno bump-version` (#33689)
- feat(add/install): default to npm registry for unprefixed packages (#33246)
- feat(compile): add progress bar for deno compile (#33874)
- feat(compile): support module.registerHooks() in compiled binaries (#33853)
- feat(core): add `Deno.core.loadExtScript()` for lazy-loaded scripts (#33739)
- feat(core): add async module resolution support via ModuleResolveResponse
  (#32432)
- feat(core): support lazy_loaded_esm modules via import statements (#33873)
- feat(core): synthetic_esm extension DSL + node:worker_threads canary (#34038)
- feat(ext/fetch): emit Network.* inspector events for fetch() (#34220)
- feat(ext/node): ESM import() support for module.registerHooks() (#33763)
- feat(ext/node): add createHistogram to node:perf_hooks (#34003)
- feat(ext/node): buffer Network.* bodies for inspector body-fetch commands
  (#34201)
- feat(ext/node): convert node:url/util/zlib to synthetic_esm (#34041)
- feat(ext/node): emit Network.* inspector events for node:http (#34231)
- feat(ext/node): expose inspector.isEnabled() via process.binding('inspector')
  (#34203)
- feat(ext/node): implement Network CDP domain for inspector (#32707)
- feat(ext/node): implement NodeRuntime.notifyWhenWaitingForDisconnect (#34204)
- feat(ext/node): implement module.registerHooks() API for CommonJS (#33733)
- feat(ext/node): implement node:module SourceMap API (#32890)
- feat(ext/node): implement node:wasi (#34089)
- feat(ext/node): implement postMessageToThread cross-thread messaging (#34015)
- feat(ext/node): implement vm.SourceTextModule with microtaskMode afterEvaluate
  support (#33603)
- feat(ext/node): make Network.* CDP events fire under plain --inspect (#34270)
- feat(ext/node): restore module.registerHooks (#34081)
- feat(ext/node): support KeyObject structured clone over MessagePort (#34229)
- feat(ext/node): support NODE_EXTRA_CA_CERTS (#33148)
- feat(ext/node): support sending dgram.Socket handles over IPC (#33863)
- feat(ext/telemetry): add gRPC protocol support for OTLP exporter (#30365)
- feat(ext/web): support structured clone for Blob and File (#33827)
- feat(ext/websocket): emit Network.* inspector events for WebSocket (#34222)
- feat(install): add --os and --arch flags for cross-platform npm installs
  (#32785)
- feat(install): added --prod to skip dev deps and @types (#33248)
- feat(install): default to npm for `deno install -g` unprefixed packages
  (#34290)
- feat(npm): add `catalog:` protocol for centralized dependency versions in
  workspaces (#32947)
- feat(npm): add hoisted node_modules linker mode (#32788)
- feat(npmrc): support min-release-age (#33983)
- feat(task): prefix output lines with task name when running in parallel
  (#33805)
- feat(test): add timeout option to Deno.test() (#33815)
- feat(types): add Math.sumPrecise and Intl.Locale.prototype.variants (#34287)
- feat(unstable): Geometry Interfaces Module Level 1 (#27527)
- feat(unstable): support TC39 import defer proposal (#32360)
- feat(x): add --package/-p flag for specifying package separately from binary
  (#32855)
- feat: OffscreenCanvas (#29357)
- feat: add --package-json flag to deno add/install/remove/uninstall (#33199)
- feat: add `deno ci` subcommand (#34235)
- feat: add `deno pack` command to create npm tarballs (#32139)
- feat: add `deno transpile` subcommand (#32691)
- feat: disable "no-process-global", "no-node-globals" lint rules by default
  (#33247)
- feat: disable ops and resources sanitizers by default in deno test (#33250)
- feat: framework detection for deno compile (#33164)
- feat: implement `deno audit --fix` (#32909)
- feat: include node lib by
