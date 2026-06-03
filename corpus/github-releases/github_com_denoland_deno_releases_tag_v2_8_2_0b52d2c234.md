---
title: "denoland/deno v2.8.2 released"
url: "https://github.com/denoland/deno/releases/tag/v2.8.2"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-06-03T15:58:29Z"
metadata:
  repo: "denoland/deno"
  version: "v2.8.2"
---

# denoland/deno v2.8.2 released

> Source: github-releases | Category: changelog | 2026-06-03T15:58:29Z

## denoland/deno — v2.8.2

### 2.8.2 / 2026.06.03

- feat(compile): improve --bundle dependency resolution and add --minify
  (#34536)
- feat(compile): scope --bundle npm embed to packages actually reached (#34532)
- feat(ext/crypto): add ChaCha20-Poly1305, SHAKE, cSHAKE, TurboSHAKE, SHA-3 HMAC
  (#34417)
- feat(ext/crypto): add ML-DSA (FIPS 204) post-quantum signatures (#34448)
- feat(ext/crypto): implement ML-KEM (FIPS 203) post-quantum KEM (#34447)
- feat(ext/node): env/global proxy support for node:http and node:https (#34257)
- feat(ext/node): support DENO_SERVE_ADDRESS override in node:http servers
  (#34662)
- feat(jupyter): rewrite kernel in JS, drop zeromq/runtimelib deps (#34083)
- feat(lsp): autocomplete jsr:/npm:/node: in deno.json(c) imports (#34724)
- feat(publish): unfurl import specifiers in Wasm modules (#34549)
- feat(task): support --env-file flag (#34508)
- feat(task): support exclusion groups in task name wildcards (#34506)
- feat(unstable): add --bundle flag to `deno compile` (#34527)
- feat: bump deno_task_shell to 0.33.0 (#34642)
- fix(add): handle version tags like `@latest` in `deno add` for JSR packages
  (#32859)
- fix(add): replace panic with error when deno.json discovery fails (#34517)
- fix(bundle): skip decorator pass when module has no decorators (#34489)
- fix(bundle): use node-style CJS interop for the Deno platform (#34533)
- fix(cache): skip WAL journal mode on WSL-1 (#34499)
- fix(cache_dir): EnsureCachedStrategy must surface cached redirects (#34563)
- fix(check): make node:stream/web types alias the globals (#34606)
- fix(check): resolve npm packages without types when type checking (#34551)
- fix(cli): suppress bug-report banner on broken pipe print panics (#34552)
- fix(cli/task): run recursive workspace tasks in parallel (#34512)
- fix(compile): allow process.chdir() into the VFS (#34610)
- fix(compile): bundle workers separately under --bundle (#34531)
- fix(compile): cover CJS-deep imports under --bundle (#34534)
- fix(compile): create code cache when importing JSON or Wasm modules (#34614)
- fix(compile): detect svelte-adapter-deno build output (#34535)
- fix(compile): don't surface graph errors for --include files (#34568)
- fix(compile): embed workspace package.json files in the VFS (#34530)
- fix(compile): enable ANSI colors on Windows in compiled binaries (#34701)
- fix(compile): handle CJS and native addons in --bundle (#34529)
- fix(compile): respect npm registry sub-paths when flattening node_modules
  (#34575)
- fix(compile): support workers loaded from blob URLs (#34574)
- fix(compile): transpile TypeScript imported at runtime (#34616)
- fix(config): hook up verbatimModuleSyntax for the emit pipeline (#34495)
- fix(config): make config auto-discovery skip the same errors on every platform
  (#34558)
- fix(config): surface invalid "exports" map in linked/workspace packages
  (#34473)
- fix(config): warn instead of erroring when start dir is not a workspace member
  (#34458)
- fix(config): warn instead of erroring when workspace member dir is missing
  (#34511)
- fix(core): TLA hang on dyn import when async dep triggers lazy ESM load
  (#34469)
- fix(core): preserve WebAssembly streaming callback across new contexts
  (#34679)
- fix(crypto): correct X448 PKCS#8 handling (#34578)
- fix(doc): don't lint private-type-ref for cross-package types (#34339)
- fix(doc): handle non-ASCII doc lint diagnostics (#34626)
- fix(ext/console): degrade gracefully when getKeys throws (#24980) (#34464)
- fix(ext/fetch): implement missing Request properties (#34607)
- fix(ext/fetch): preserve static request body length (#34546)
- fix(ext/ffi): match V8 stack-arg layout in turbocall trampoline on Apple
  silicon (#34561)
- fix(ext/fs): error when copyFile source and destination are the same file
  (#34718)
- fix(ext/fs): retry without FILE_FLAG_BACKUP_SEMANTICS on Windows when driver
  rejects it (#34686)
- fix(ext/fs): surface non-UTF-8 file names from 
