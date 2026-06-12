---
title: "denoland/deno v2.8.3 released"
url: "https://github.com/denoland/deno/releases/tag/v2.8.3"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-06-12T11:32:09Z"
metadata:
  repo: "denoland/deno"
  version: "v2.8.3"
---

# denoland/deno v2.8.3 released

> Source: github-releases | Category: changelog | 2026-06-12T11:32:09Z

## denoland/deno — v2.8.3

### 2.8.3 / 2026.06.11

- feat(cli): suggest DENO_TLS_CA_STORE on untrusted TLS certificate (#34756)
- feat(cli): support --env-file in dependency and registry subcommands (#34843)
- feat(compile): support watch mode (#34860)
- feat(config): support globs in links (#34849)
- feat(ext/crypto): implement SubtleCrypto.supports() static method (#34903)
- feat(ext/crypto): support ML-DSA JWK import/export (#34914)
- feat(ext/fetch): support `priority` in `RequestInit` (#34716)
- feat(ext/node): auto-instrument node:http2 with OpenTelemetry (#34510)
- feat(ext/node): notify control socket when node:http server starts serving
  (#34949)
- feat(ext/telemetry): honor OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT (#34787)
- feat(ext/telemetry): honor OTEL_SPAN_EVENT_COUNT_LIMIT (#34795)
- feat(ext/telemetry): support OTEL_TRACES_SAMPLER (#34764)
- feat(fmt): add JSON trailing comma config (#33383)
- feat(info): add localPath to npm packages in `deno info --json` (#34806)
- feat(info): support --minimum-dependency-age flag (#34762)
- feat(lsp): add "Debug" code lens for test steps (#34742)
- feat(lsp): add Deno.test ignore and only code actions (#34861)
- feat(lsp): diagnose import map files (#34864)
- feat(lsp): provide hover info for import map resolutions (#34854)
- feat(lsp): report `deno doc --lint` diagnostics (#34733)
- feat(lsp): show no-slow-types diagnostics for JSR packages (#34740)
- feat(outdated): warn about packages skipped due to registry errors (#34974)
- feat(test): forward shebang permissions into `deno test --doc` (#35052)
- feat(workspace): auto-discover external deno.json import maps (#34803)
- feat(x): add deno x --ignore-scripts (#34952)
- feat: `bump-version -c` to handle deno.json + package.json in same dir
  (#34770)
- fix(add): accept npm version ranges on the command line (#34799)
- fix(bundle): apply node-style CJS interop on all platforms (#34939)
- fix(bundle): don't panic when esbuild binary is busy or unavailable (#34845)
- fix(bundle): instantiate .wasm imports instead of emitting raw bytes (#34923)
- fix(bundle): rename sourcemap for HTML entrypoints (#34901)
- fix(bundle): respect `--check` and run the type checker (#33514)
- fix(cache): retry locked cache database instead of deleting it (#34873)
- fix(check): honor ts suppressions for unresolved imports (#34163)
- fix(check): ignore doc comment dynamic imports (#34888)
- fix(check): surface unresolved imports in .d.ts entrypoints (#34168)
- fix(check): treat .d.ts in ESM-supporting npm packages as ESM (#34613)
- fix(clean): keep cleaning when cache files are locked and report holders
  (#34946)
- fix(clean): support `deno clean --dry-run` without --except (#34846)
- fix(cli): accept allow-import for deno add (#35019)
- fix(cli): check worker's own permissions for dynamic asset imports (#34707)
- fix(cli): collect re-exported names for `deno test --doc` injection (#33511)
- fix(cli): don't let --env-file set Deno's own runtime control vars (#35032)
- fix(cli): don't suggest non-existent subcommand-flag combinations (#34810)
- fix(cli): generate type-only doc-test imports under verbatimModuleSyntax
  (#33508)
- fix(cli): include the typed name in unrecognized subcommand error (#34882)
- fix(cli): strip trailing CR from args so CRLF shebangs work (#34968)
- fix(compile): prune managed npm snapshot to graph-reachable packages (#34741)
- fix(compile): resolve bare npm imports in --bundle worker sources (#34967)
- fix(compile): run forked child's module instead of entrypoint (#34687)
- fix(compile): support fs.fstatSync on vfs (#34892)
- fix(console): %c colors with same red component as previous color (#34784)
- fix(core): don't set ERR_MODULE_NOT_FOUND code on module linking errors
  (#34800)
- fix(core): externalize lazy loaded sources (#34936)
- fix(core): silence too_many_arguments on Callable trait method (#33475)
- fix(core): use isolate_unchecked accessors for fast `&v8::Isolate` args
  (#33474)
- f
