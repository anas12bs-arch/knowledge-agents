---
title: "graphify update local en knowledge-agents degrada el grafo: pierde los nodos de docs archivados (los"
type: "error"
tags: ["graphify", "knowledge-agents", "pipeline"]
date: "2026-06-10T09:25:00Z"
severity: "info"
---

# graphify update local en knowledge-agents degrada el grafo: pierde los nodos de docs archivados (los

> Type: error | Severity: info | 2026-06-10T09:25:00Z

**Context:** N/A
**Cause:** learn.sh corria graphify update . tras cada aprendizaje
**Effect:** grafo local perdio nodos de corpus/learn y bloqueaba 40 min

---

graphify update local en knowledge-agents degrada el grafo: pierde los nodos de docs archivados (los .md ya no existen local) y tarda ~40 min con 3437 archivos. El grafo autoritativo lo construye el CI; localmente solo hacer git pull (sync horario). No correr graphify update local salvo para cambios de codigo.

---

*Auto-capturado por el sistema de aprendizaje continuo.*
