---
title: "lex-premium hero rework: switched carousel cakes to transparent PNGs (clasica-nobg.png etc, removed "
type: "pattern"
tags: ["hero", "animation", "gsap", "images", "mobile", "lex-premium"]
date: "2026-05-31T08:10:08Z"
severity: "info"
---

# lex-premium hero rework: switched carousel cakes to transparent PNGs (clasica-nobg.png etc, removed 

> Type: pattern | Severity: info | 2026-05-31T08:10:08Z

**Context:** N/A
**Cause:** GSAP intro overlay locks body scroll; if rAF throttled (background tab) timeline may never complete
**Effect:** added setTimeout(4200) safety that force-finishes intro and restores body overflow regardless of rAF state

---

lex-premium hero rework: switched carousel cakes to transparent PNGs (clasica-nobg.png etc, removed beige photo bg that clashed with per-flavor color background), changed CakePhoto objectFit cover->contain + added elliptical plate drop-shadow for realistic floating. Mobile ghost headline now splits on space into two stacked lines (MUY / CREMA) at 24vw to fill screen like desktop. Added GSAP brand-reveal intro: big centered '99 Cheesecake' that separates 99 from Cheesecake then FLIPs (scale+translate measured from brandRef rect) to top-left brand position while overlay bg fades, revealing carousel.

---

*Auto-capturado por el sistema de aprendizaje continuo.*
