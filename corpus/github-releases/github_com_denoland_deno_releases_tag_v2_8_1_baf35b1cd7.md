---
title: "denoland/deno v2.8.1 released"
url: "https://github.com/denoland/deno/releases/tag/v2.8.1"
source: "github-releases"
category: "changelog"
tags: ["github", "release", "changelog", "deno"]
date: "2026-05-30T14:31:18Z"
metadata:
  repo: "denoland/deno"
  version: "v2.8.1"
---

# denoland/deno v2.8.1 released

> Source: github-releases | Category: changelog | 2026-05-30T14:31:18Z

## denoland/deno — v2.8.1

### 2.8.1 / 2026.05.27

- Revert "fix(ext/node): polyfill module.enableCompileCache and companions"
  (#34190) (#34348)
- feat(bundle): support `browser` field map in package.json (#34407)
- fix(bundle): read package.json sideEffects field (#34406)
- fix(cli): clearer error when importing .node addon via ESM (#34361)
- fix(config): don't panic when --config path can't be converted to URL (#34351)
- fix(core): allow host objects to round-trip through core.deserialize (#34380)
- fix(core): keep lazy_loaded_esm sources across concurrent loads (#34353)
- fix(ext/fetch,ext/websocket): check resolved IPs against net deny list
  (#34236)
- fix(ext/node): TLSSocket.authorized=false when client presents no cert
  (#34381)
- fix(ext/node): accept array forms of cert/key/pfx in createSecureContext
  (#34379)
- fix(ext/node): add missing node:util APIs getSystemErrorMap,
  transferableAbortSignal, transferableAbortController (#34372)
- fix(ext/node): allow omitting arguments in base64Slice (#34318)
- fix(ext/node): attach register as static on Module (#34305)
- fix(ext/node): do not throw NotFound for fs.exists (#34244)
- fix(ext/node): drop extra positional args in promisified fs.promises.*
  (#34347)
- fix(ext/node): emit 'error' event for fs.watch open failures (#34398)
- fix(ext/node): enforce minimum Miller-Rabin rounds in checkPrime (#34391)
- fix(ext/node): extract cert/key from pfx in tls SecureContext (#34383)
- fix(ext/node): prevent panic on `node:sqlite` aggregate method (#34385)
- fix(ext/node): require env permission for process.loadEnvFile (#34350)
- fix(ext/node): reset req.reusedSocket on transparent retry (#34376)
- fix(ext/node): support PKCS#12 MACs other than SHA-1 (#34342)
- fix(ext/node): tolerate non-AsyncWrap handles in _getNewAsyncId (#34413)
- fix(http): wake runtime after direct serve dispatch (#34387)
- fix(inspector): emit NodeWorker.attachedToWorker for late workers (#34377)
- fix(node/util): don't invoke Proxy traps in util.inspect (#34373)
- fix(pack): remove automatic @deno/shim-deno injection (#34411)
- fix(runtime): lazy-loaded globals should shadow on inherited [[Set]] (#34405)
- fix(task): walk ancestor node_modules/.bin in BYONM mode (#34364)
- fix(transpile): preserve newlines after multi-line block comments (#34357)
- fix(types): restore brotli in CompressionFormat for dom/webworker libs
  (#34349)
- fix(upgrade): zstd-compress bsdiff delta patches (#34354)
- fix: allow --inspect=localhost:0 to resolve hostnames (#34230)
- fix: panic in deno test --parallel (#34378)
- fix: support npm: specifiers in --preload and --import (#34346)
- perf(ext/node): reuse keep-alive timer in node:http server (#34302)
