"""
Escribe items del agente como archivos .md en corpus/.
graphify los ingiere con `graphify ./corpus --incremental`.
No necesita embeddings externos ni Supabase — graphify lo maneja todo.
"""
from __future__ import annotations
import hashlib
import os
import re
from datetime import datetime, timezone
from pathlib import Path

# Directorio donde viven los markdowns que graphify procesa
# Prioridad: env var → abs path en GitHub Actions → local fallback
_env_corpus = os.environ.get("CORPUS_DIR")
if _env_corpus:
    CORPUS_DIR = Path(_env_corpus)
elif Path("/home/runner/work/knowledge-agents/knowledge-agents/corpus").exists():
    CORPUS_DIR = Path("/home/runner/work/knowledge-agents/knowledge-agents/corpus")
else:
    CORPUS_DIR = Path(__file__).parent.parent / "corpus"
CORPUS_DIR.mkdir(parents=True, exist_ok=True)


def _slug(url: str, max_len: int = 60) -> str:
    name = re.sub(r"https?://", "", url)
    name = re.sub(r"[^\w\-]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name[:max_len]


def _dedup_path(url: str, source: str) -> Path:
    uid = hashlib.sha256(url.encode()).hexdigest()[:10]
    slug = _slug(url)
    return CORPUS_DIR / source / f"{slug}_{uid}.md"


def save(
    title: str,
    content: str,
    url: str,
    source: str,           # 'hackernews' | 'github' | 'devto' | 'twitter' | ...
    category: str,         # 'news' | 'skill' | 'tool' | 'trend' | 'social' | 'research'
    tags: list[str] | None = None,
    metadata: dict | None = None,
) -> Path | None:
    """
    Escribe un archivo markdown con frontmatter YAML.
    Retorna el Path si fue escrito, None si ya existía (dedup).
    """
    dest = _dedup_path(url, source)
    if dest.exists():
        return None  # ya procesado, graphify tiene caché semántica también

    dest.parent.mkdir(parents=True, exist_ok=True)

    tags_yaml = ", ".join(f'"{t}"' for t in (tags or []))
    meta_lines = ""
    if metadata:
        for k, v in metadata.items():
            meta_lines += f'  {k}: "{v}"\n'

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # Escape title quotes for YAML
    title_escaped = title.replace('"', "'")
    meta_default = "  {}\n"
    md = f"""---
title: "{title_escaped}"
url: "{url}"
source: "{source}"
category: "{category}"
tags: [{tags_yaml}]
date: "{now}"
metadata:
{meta_lines if meta_lines else meta_default}---

# {title}

> Source: {source} | Category: {category} | {now}

{content}
"""
    dest.write_text(md, encoding="utf-8")
    return dest


def count_corpus() -> dict[str, int]:
    """Cuenta archivos por subcarpeta de source."""
    if not CORPUS_DIR.exists():
        return {}
    counts = {}
    for subdir in CORPUS_DIR.iterdir():
        if subdir.is_dir():
            counts[subdir.name] = len(list(subdir.glob("*.md")))
    return counts
