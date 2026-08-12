---
title: "Benchmarkée el ORM Postgres nativo de mi lenguaje contra SQLAlchemy: ~8 más rápido en reads, 5.7 menos memoria — y dónde empata"
url: "https://dev.to/martin_palopoli/benchmarkee-el-orm-postgres-nativo-de-mi-lenguaje-contra-sqlalchemy-8x-mas-rapido-en-reads-57x-39bd"
source: "devto"
category: "news"
tags: ["devto", "opensource", "tech-article"]
date: "2026-08-12T20:12:10Z"
metadata:
  tag: "opensource"
---

# Benchmarkée el ORM Postgres nativo de mi lenguaje contra SQLAlchemy: ~8 más rápido en reads, 5.7 menos memoria — y dónde empata

> Source: devto | Category: news | 2026-08-12T20:12:10Z

"Cero overhead" es la promesa más fácil de decir y la más difícil de probar. Así que el repo de Fitz trae un cabeza-a-cabeza reproducible entre dos boilerplates idénticos — mismo Postgres, mismos endpoints, mismo docker compose — uno con el ORM nativo de Fitz, otro con Python + SQLAlchemy. Acá están los números honestos (mediana de 3), por qué Fitz gana en reads, por qué empata en writes, y el bug de Nagle que alguna vez lo hizo 30% más lento que Python.

Reactions: 0
