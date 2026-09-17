---
title: "Hidratación isomórfica en Fitz: first paint en el server, y después WASM adopta el DOM"
url: "https://dev.to/martin_palopoli/hidratacion-isomorfica-en-fitz-first-paint-en-el-server-y-despues-wasm-adopta-el-dom-4b7m"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-09-17T14:53:11Z"
metadata:
  tag: "opensource"
---

# Hidratación isomórfica en Fitz: first paint en el server, y después WASM adopta el DOM

> Source: devto | Category: news | 2026-09-17T14:53:11Z

El mismo `.fitzv` se renderiza en el server para el first paint (funciona con JS deshabilitado), y el runtime client-WASM después ADOPTA ese DOM pintado por el server en vez de tirarlo y re-renderizar — estado restaurado desde un payload embebido, listeners cableados, sin wipe, sin flash. Un solo source, los dos extremos.

Reactions: 0
