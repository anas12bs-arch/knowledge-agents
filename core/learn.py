"""
Captura lecciones, errores, feedback y aprendizajes → corpus/learn/.
Graphify lo ingiere automaticamente en el knowledge graph.
Cada leccion queda conectada con su contexto, causa y efecto.

Uso:
  python -m core.learn "no hacer X causa error Y" --type error --tags "fastapi,sqlalchemy"
  python -m core.learn --from-claude  (lee ultimo aprendizaje de Claude)
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path

_learn_corpus = os.environ.get("CORPUS_DIR")
if _learn_corpus:
    LEARN_DIR = Path(_learn_corpus) / "learn"
else:
    LEARN_DIR = Path(__file__).parent.parent / "corpus" / "learn"
LEARN_DIR.mkdir(parents=True, exist_ok=True)


def _fingerprint(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def save_learning(
    title: str,
    body: str,
    learn_type: str = "insight",
    tags: list[str] | None = None,
    context: str | None = None,
    cause: str | None = None,
    effect: str | None = None,
    severity: str = "info",
):
    """
    Escribe una leccion como archivo markdown → corpus/learn/.
    El proximo ciclo de graphify lo ingiere automaticamente.
    """
    fp = _fingerprint(title + body)
    dest = LEARN_DIR / f"{learn_type}_{fp}.md"
    if dest.exists():
        return False

    tags_yaml = ", ".join(f'"{t}"' for t in (tags or []))
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    md = f"""---
title: "{title}"
type: "{learn_type}"
tags: [{tags_yaml}]
date: "{now}"
severity: "{severity}"
---

# {title}

> Type: {learn_type} | Severity: {severity} | {now}

**Context:** {context or 'N/A'}
**Cause:** {cause or 'N/A'}
**Effect:** {effect or 'N/A'}

---

{body}

---

*Auto-capturado por el sistema de aprendizaje continuo.*
"""
    dest.write_text(md, encoding="utf-8")
    return True


def capture_claude_feedback():
    """
    Lee el archivo de feedback de Claude (si existe) y lo persiste.
    """
    feedback_path = Path("/tmp/claude_learn.md")
    if not feedback_path.exists():
        print("No hay feedback de Claude pendiente.")
        return
    content = feedback_path.read_text().strip()
    lines = content.split("\n")
    title = lines[0] if lines else "Claude Learning"
    body = "\n".join(lines[1:]) if len(lines) > 1 else content
    saved = save_learning(title, body, learn_type="claude-feedback", tags=["claude", "feedback"])
    if saved:
        feedback_path.unlink(missing_ok=True)
        print(f"Aprendizaje capturado: {title}")
    else:
        print("Ya existia ese aprendizaje (dedup).")


def stats():
    files = list(LEARN_DIR.glob("*.md"))
    if not files:
        print("No hay aprendizajes registrados aun.")
        return
    counts: dict[str, int] = {}
    for f in files:
        t = f.stem.split("_")[0] if "_" in f.stem else "unknown"
        counts[t] = counts.get(t, 0) + 1
    print(f"\nAprendizajes registrados: {len(files)}")
    print("-" * 40)
    for t, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {t:20s} {c:>4}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Capturar aprendizajes en el knowledge graph")
    parser.add_argument("text", nargs="?", help="Texto del aprendizaje")
    parser.add_argument("--type", default="insight", help="Tipo: error, insight, optimization, pattern, lesson")
    parser.add_argument("--tags", default="", help="Tags separados por coma")
    parser.add_argument("--context", default=None, help="Contexto donde ocurrio")
    parser.add_argument("--cause", default=None, help="Que lo causo")
    parser.add_argument("--effect", default=None, help="Que efecto tuvo")
    parser.add_argument("--severity", default="info", choices=["critical", "warning", "info", "optimization"])
    parser.add_argument("--from-claude", action="store_true", help="Capturar feedback pendiente de Claude")
    parser.add_argument("--stats", action="store_true", help="Mostrar estadisticas de aprendizajes")
    args = parser.parse_args()

    if args.stats:
        stats()
        return

    if args.from_claude:
        capture_claude_feedback()
        return

    if not args.text:
        parser.print_help()
        return

    saved = save_learning(
        title=args.text.split("\n")[0][:100],
        body=args.text,
        learn_type=args.type,
        tags=[t.strip() for t in args.tags.split(",") if t.strip()],
        context=args.context,
        cause=args.cause,
        effect=args.effect,
        severity=args.severity,
    )
    if saved:
        print(f"Aprendizaje guardado en corpus/learn/ ({args.type})")
        print("Se integrara en el knowledge graph en el proximo ciclo.")
    else:
        print("Ya existe ese aprendizaje (dedup).")


if __name__ == "__main__":
    main()
