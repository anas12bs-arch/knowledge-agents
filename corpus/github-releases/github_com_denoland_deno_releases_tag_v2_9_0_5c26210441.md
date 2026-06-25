---
title: "denoland/deno v2.9.0 released"
url: "https://github.com/denoland/deno/releases/tag/v2.9.0"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-06-25T16:01:37Z"
metadata:
  repo: "denoland/deno"
  version: "v2.9.0"
---

# denoland/deno v2.9.0 released

> Source: github-releases | Category: changelog | 2026-06-25T16:01:37Z

## denoland/deno — v2.9.0

### 2.9.0 / 2026.06.25

Read more: http://deno.com/blog/v2.9

- feat(bundle): add --declaration flag to generate rolled-up .d.ts files
  (#33838)
- feat(cli): add `deno link` and `deno unlink` subcommands (#34359)
- feat(cli): add `deno watch` subcommand (#35301)
- feat(cli): add deno list subcommand to list declared dependencies (#34972)
- feat(cli): auto-migrate pnpm-workspace.yaml on resolution failure (#34993)
- feat(cli): provide a `node` on PATH when Node.js is not installed (#34969)
- feat(compile): persist Web Storage/KV in a per-app data directory (#34618)
- feat(coverage): add configurable coverage thresholds (#35056)
- feat(desktop): --compress for self-extracting app bundles (#35420)
- feat(desktop): add Linux .deb and .rpm installer output formats (#35296)
- feat(desktop): add Windows .msi installer output format (#35378)
- feat(desktop): autodetect Vite framework (#35470)
- feat(desktop): default UI backend to webview (#35442)
- feat(ext/crypto): support remaining modern WebCrypto algorithms (#35223)
- feat(ext/http): deprecation warning for legacy request abort (#34397)
- feat(ext/net): implement Happy Eyeballs for `Deno.connect` and
  `Deno.connectTls` (#31726)
- feat(ext/node): implement node:test mock.module (#35329)
- feat(ext/node): implement node:test mock.timers (#33946)
- feat(ext/web): web locks api (#31166)
- feat(fmt): add sortNamedImports and sortNamedExports options (#33313)
- feat(fmt): infer config from .editorconfig (#34071)
- feat(fmt): use lax-css for CSS, SCSS, and Less (#35160)
- feat(fmt): use lax-markup for HTML, XML, SVG, and components (#35174)
- feat(fmt): use lax-sql for SQL formatting (#35161)
- feat(http): allow disabling serve compression (#35253)
- feat(http): disable Deno.serve automatic compression by default (#35486)
- feat(install): create node_modules for workspace members (#34970)
- feat(install): seed deno.lock from bun.lock (#35394)
- feat(install): seed deno.lock from package-lock.json (#35330)
- feat(install): seed deno.lock from pnpm-lock.yaml (#35346)
- feat(install): seed deno.lock from yarn.lock (#35350)
- feat(install): warn on package.json engines mismatch (#34225)
- feat(lockfile): auto-resolve git merge conflicts in deno.lock (#34726)
- feat(lsp): add inferred type request (#35099)
- feat(napi): implement Node-API version 10 (#35270)
- feat(node): bump reported process.version to v26.3.0 (#34747)
- feat(npm): install jsr deps into node_modules via npm-compat registry (#35029)
- feat(npm): publishing-trust ranking and no-downgrade trust policy (#34927)
- feat(runtime): add request_builder_hook for fetch token and cdn-loop headers
  (#35088)
- feat(task): add --if-present flag to deno task (#35315)
- feat(task): add --jobs/--concurrency flag to deno task (#35318)
- feat(task): input-based caching with files/output/env (#34509)
- feat(task): set npm_execpath, npm_node_execpath and npm_command for
  package.json scripts (#35317)
- feat(test): add --changed and --related flags to deno test (#35199)
- feat(test): add --shard flag to split a test run across machines (#35057)
- feat(test): add Deno.test.each for parameterized tests (#34938)
- feat(test): add retry and repeats options to Deno.test (#35053)
- feat(test): built-in snapshot testing via t.assertSnapshot (#35139)
- feat(test): show sub-millisecond test durations (#35200)
- feat(unstable): CSS module imports (with { type: "css" }) (#35093)
- feat: `deno desktop` subcommand (#33441)
- feat: `deno remove --global` as alias for `deno uninstall --global` (#35327)
- feat: add "preferPackageJson" deno.json setting (#35392)
- feat: add stable --unsafe-proto flag (#34738)
- feat: enable default minimum dependency age (#35458)
- feat: stabilize "links" field in deno.json (#34996)
- feat: stabilize bare node built-in resolution (#33316)
- feat: support `ignore` option in `Deno.watchFs` (#31582)
- feat: support navigator.userAgentData (#34743)
- fix(check): 
