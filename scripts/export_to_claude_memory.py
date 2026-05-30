"""
Exporta corpus/ → ~/.claude/memory/knowledge-graph.md
Formato que memory_import_claude puede ingestar con embeddings ONNX.

Uso:
  python scripts/export_to_claude_memory.py
  python scripts/export_to_claude_memory.py --max 500
"""
from __future__ import annotations
import argparse
import pathlib
import sys
import re
from datetime import datetime

CORPUS_DIR   = pathlib.Path(__file__).parent.parent / "corpus"
MEMORY_DIR   = pathlib.Path.home() / ".claude" / "memory"
OUTPUT_FILE  = MEMORY_DIR / "knowledge-graph.md"


def parse_md(path: pathlib.Path) -> dict:
    """Extrae frontmatter YAML + body de un archivo markdown del corpus."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    meta = {}
    body = text

    # Parsear frontmatter ---
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            fm = text[3:end].strip()
            body = text[end+3:].strip()
            for line in fm.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"')

    return {
        "title":    meta.get("title", path.stem),
        "source":   meta.get("source", path.parent.name),
        "url":      meta.get("url", ""),
        "tags":     meta.get("tags", "").strip("[]"),
        "body":     body[:1200].strip(),   # primeros 1200 chars del contenido
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max",  type=int, default=1000, help="Max docs a exportar")
    parser.add_argument("--pull", action="store_true",   help="git pull antes de exportar")
    args = parser.parse_args()

    if args.pull:
        import subprocess
        subprocess.run(["git", "pull", "--ff-only"], cwd=CORPUS_DIR.parent)

    if not CORPUS_DIR.exists():
        print(f"❌ corpus/ no existe en {CORPUS_DIR}")
        sys.exit(1)

    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    # Recoger todos los .md del corpus
    files = sorted(CORPUS_DIR.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    files = files[:args.max]

    print(f"📚 Exportando {len(files)} docs → {OUTPUT_FILE}")

    lines = [
        "# Knowledge Graph — PrimeBot Enterprise Intelligence",
        f"_Generado: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')} | {len(files)} documentos_",
        "",
    ]

    # Agrupar por source (categoría)
    by_source: dict[str, list] = {}
    for fp in files:
        doc = parse_md(fp)
        src = doc["source"]
        by_source.setdefault(src, []).append(doc)

    for src, docs in sorted(by_source.items()):
        lines.append(f"## {src.upper()} ({len(docs)} docs)")
        lines.append("")
        for doc in docs:
            title = doc["title"].replace("[", "").replace("]", "")
            lines.append(f"### {title}")
            if doc["url"]:
                lines.append(f"_Source: {doc['url']}_")
            if doc["tags"]:
                lines.append(f"_Tags: {doc['tags']}_")
            if doc["body"]:
                lines.append("")
                lines.append(doc["body"])
            lines.append("")

    content = "\n".join(lines)
    OUTPUT_FILE.write_text(content, encoding="utf-8")

    size_kb = OUTPUT_FILE.stat().st_size // 1024
    print(f"✅ Escrito: {OUTPUT_FILE} ({size_kb} KB, {len(docs)} docs)")
    print(f"   Categorías: {', '.join(sorted(by_source.keys()))}")
    print(f"   Ahora ejecuta en Claude: memory_import_claude con namespace='knowledge-graph'")


if __name__ == "__main__":
    main()
