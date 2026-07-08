---
title: "denoland/deno v2.9.2 released"
url: "https://github.com/denoland/deno/releases/tag/v2.9.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-07-08T15:04:37Z"
metadata:
  repo: "denoland/deno"
  version: "v2.9.2"
---

# denoland/deno v2.9.2 released

> Source: github-releases | Category: changelog | 2026-07-08T15:04:37Z

## denoland/deno — v2.9.2

### 2.9.2 / 2026.07.08

- feat(desktop): autodetect React Router framework (#35557)
- feat(desktop): enable `--hmr` for Vite and Nuxt (#35851)
- feat(desktop): run HMR by framework dev server (#35722)
- feat(desktop): window opacity and transparency APIs (#35646)
- feat(desktop): wire --exclude-unused-npm through to compile (#35740)
- feat(ext/node): implement v8.setHeapSnapshotNearHeapLimit (#35694)
- feat(ext/telemetry): honor OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT (#35068)
- feat(inspector): start inspector server on SIGUSR1 (#35738)
- feat(node): implement getTestContext() in node:test (#35678)
- feat: support wildcard patterns in minimumDependencyAge.exclude (#35746)
- fix(check): don't interleave errors with "Check" lines in a workspace (#35687)
- fix(compile): bump libsui to 0.16.1 to survive eu-strip in flatpak (#35699)
- fix(compile): bump libsui to 0.16.3 to fix segfault under gVisor/Cloud Run
  (#35701)
- fix(core): don't drain microtasks in mod_evaluate_sync mid-evaluation (#35707)
- fix(coverage): count a branch-junction line as covered when either arm runs
  (#35858)
- fix(coverage): don't count V8 block-boundary gaps as branches (#35767)
- fix(coverage): don't let a trailing comment change a line's hit count (#35741)
- fix(deploy): disable config discovery and refresh the cached CLI version
  (#35754)
- fix(desktop): attribute bind calls to the registering window id (#35654)
- fix(desktop): honor desktop.backend from deno.json (#35815
- fix(desktop): pin @std/http in generated Vite SPA entrypoint + add hermetic
  compile test (#35676)
- fix(desktop): rename launcher to <app> so it self-loads the runtime (#35709)
- fix(desktop): run framework build step before bundling output (#35603)
- fix(desktop): surface compiled-app startup errors instead of exiting silently
  (#35567)
- fix(dprint): exclude `tools/lzld` submodule (#35778)
- fix(ext): throw DataCloneError when posting non-serializable values (#35604)
- fix(ext/cache): implement Cache.keys() (#35455)
- fix(ext/fetch): reject transport failures with Node's "fetch failed" shape
  (#35618)
- fix(ext/http): error non-Uint8Array response streams (#35783)
- fix(ext/http): honor explicit content-length header on HEAD responses (#35728)
- fix(ext/http): point legacy abort warning at docs.deno.com/go link (#35713)
- fix(ext/napi): add uv_cond_* polyfills for native addons (#35536)
- fix(ext/net): abort pending Deno.connect during DNS resolution (#35729)
- fix(ext/node): allow adopting inherited extra stdio TCP fds (#35805)
- fix(ext/node): don't panic when main module path has invalid percent-encoding
  (#35534)
- fix(ext/node): don't schedule a pause in inspector.waitForDebugger() (#35796)
- fix(ext/node): flush StringDecoder in cipher final() for stream ciphers
  (#35800)
- fix(ext/node): mark TLSWrap dead on teardown before tls_conn check (#35706)
- fix(ext/node): report all active resources from process.getActiveResourcesInfo
  (#35532)
- fix(ext/node): require --allow-net=unix for node:net unix sockets (#35835)
- fix(ext/node): support fd 3 pipes in spawned Deno children (#34133)
- fix(ext/signals): unregister handler when SignalStream is dropped (#35832)
- fix(ext/web): resolve pending BYOB read when teeing a byte stream that closes
  (#35828)
- fix(fmt): format Astro inline scripts as TypeScript (#35852)
- fix(fs): support pre-1970 (negative) timestamps in FsStat (#35517)
- fix(inspector): close WebSocket connections when the runtime is torn down
  (#35791)
- fix(install): don't panic on jsr specifier with a tag like @latest (#35605)
- fix(install): don't write through hardlinks when copying package files
  (#35735)
- fix(install): make setup cache packages hash deterministic (#35825)
- fix(install): resolve lifecycle script dependency bins against the hoisted
  layout (#35762)
- fix(install): support uninstalling multiple global packages (#29352)
- fix(lint): don't error on non-analyzable package exp
