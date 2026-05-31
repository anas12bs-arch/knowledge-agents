"""
Enriquece documentos del corpus con keywords (RAKE) y resumen (TextRank/LSA).
Coste: $0.00 — todo local, sin API, sin tokens.
Procesa solo documentos nuevos (SHA256 dedup).

Uso:
  python -m core.enrich               # procesa todos los nuevos
  python -m core.enrich --force       # reprocesa todo
  python -m core.enrich --stats       # muestra estadísticas
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

# ── Rutas ─────────────────────────────────────────────────────────────────────
REPO_ROOT          = Path(__file__).parent.parent
CORPUS_DIR         = Path(os.environ.get("CORPUS_DIR", REPO_ROOT / "corpus"))
GRAPH_DIR          = REPO_ROOT / "graphify-out"
CACHE_FILE         = GRAPH_DIR / "enrichment_cache.json"
LEARN_DIR          = CORPUS_DIR / "learn"
ARCHIVE_DIR        = CORPUS_DIR / "learn-archived"
CORPUS_ARCHIVE_DIR = CORPUS_DIR.parent / "corpus-archived"

# Días tras los cuales un doc se mueve a corpus-archived/ (sus vectores siguen en cache)
ARCHIVE_AFTER_DAYS = int(os.environ.get("ARCHIVE_AFTER_DAYS", "7"))

# Fuentes que se archivan automáticamente (todo el harvesting de agentes)
AUTO_ARCHIVE_SOURCES = {
    "devto", "hackernews", "github-trending", "github-releases",
    "npm", "pypi", "hn-hiring", "youtube", "podcast",
    "vercel-blog", "ai-research",
    # Categorías de los 15 agentes
    "engineering", "design", "security", "psychology", "finance",
    "legal", "devops", "sales", "product", "business",
}


# ── Lazy imports (instalados en CI vía pip) ───────────────────────────────────
def _import_rake():
    try:
        from rake_nltk import Rake
        return Rake
    except ImportError:
        print("⚠️  rake-nltk no instalado — pip install rake-nltk", file=sys.stderr)
        return None


def _import_sumy():
    try:
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lsa import LsaSummarizer
        return PlaintextParser, Tokenizer, LsaSummarizer
    except ImportError:
        print("⚠️  sumy no instalado — pip install sumy", file=sys.stderr)
        return None, None, None


# ── Extracción ─────────────────────────────────────────────────────────────────
def extract_keywords(text: str, max_kw: int = 10) -> list[str]:
    Rake = _import_rake()
    if Rake is None:
        return _fallback_keywords(text, max_kw)
    try:
        r = Rake(min_length=1, max_length=4)
        r.extract_keywords_from_text(text[:3000])
        phrases = r.get_ranked_phrases()[:max_kw]
        return [p.strip() for p in phrases if len(p.strip()) > 2]
    except Exception:
        return _fallback_keywords(text, max_kw)


def _fallback_keywords(text: str, max_kw: int) -> list[str]:
    """Extracción de frecuencia de palabras simples (sin dependencias)."""
    words = re.findall(r"\b[a-zA-Z]{4,}\b", text.lower())
    stopwords = {
        "this", "that", "with", "from", "have", "they", "been", "more",
        "also", "some", "into", "your", "will", "when", "what", "which",
        "their", "there", "about", "would", "other", "should", "these",
        "using", "used", "based", "support", "allows", "feature", "features",
    }
    freq: dict[str, int] = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: -x[1])[:max_kw]]


def extract_summary(text: str, num_sentences: int = 3) -> str:
    PlaintextParser, Tokenizer, LsaSummarizer = _import_sumy()
    if PlaintextParser is None:
        return _fallback_summary(text, num_sentences)
    try:
        # Detectar idioma (heurístico)
        lang = "spanish" if re.search(r"\b(que|para|con|esto|como|una|los)\b", text[:200]) else "english"
        parser = PlaintextParser.from_string(text[:4000], Tokenizer(lang))
        summarizer = LsaSummarizer()
        sentences = summarizer(parser.document, num_sentences)
        result = " ".join(str(s) for s in sentences).strip()
        return result if result else _fallback_summary(text, num_sentences)
    except Exception:
        return _fallback_summary(text, num_sentences)


def _fallback_summary(text: str, num_sentences: int) -> str:
    """Primeras N oraciones del texto como resumen básico."""
    # Quitar markdown
    clean = re.sub(r"[#*`\[\]()!]", "", text)
    clean = re.sub(r"https?://\S+", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    sentences = re.split(r"(?<=[.!?])\s+", clean)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    return " ".join(sentences[:num_sentences])


# ── Strip frontmatter ─────────────────────────────────────────────────────────
def strip_frontmatter(content: str) -> tuple[dict, str]:
    """Devuelve (meta, body) separando el frontmatter YAML."""
    meta: dict = {}
    body = content
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            fm = content[3:end]
            for line in fm.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            body = content[end + 3:].strip()
    return meta, body


# ── Proceso principal ─────────────────────────────────────────────────────────
def process_corpus(force: bool = False, verbose: bool = False) -> int:
    # Cargar cache
    cache: dict = {}
    if CACHE_FILE.exists() and not force:
        try:
            cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            cache = {}

    processed = 0
    skipped   = 0
    errors    = 0

    # Excluir learn-archived/ y corpus-archived/ — ya procesados, no re-vectorizar
    md_files = [
        f for f in CORPUS_DIR.rglob("*.md")
        if "learn-archived" not in f.parts
        and "corpus-archived" not in f.parts
    ]
    print(f"📁 Escaneando {len(md_files)} docs en {CORPUS_DIR} …")

    for md_file in md_files:
        # SHA256 basado en ruta relativa estable — sin mtime para evitar duplicados
        rel_str = str(md_file.relative_to(REPO_ROOT))
        uid     = hashlib.sha256(rel_str.encode()).hexdigest()[:16]

        if uid in cache and not force:
            skipped += 1
            continue

        try:
            raw  = md_file.read_text(encoding="utf-8", errors="ignore")
            if len(raw.strip()) < 80:
                skipped += 1
                continue

            meta, body = strip_frontmatter(raw)
            # Combinar título + body para mejor extracción
            title    = meta.get("title", md_file.stem)
            full_txt = f"{title}\n\n{body}"

            keywords = extract_keywords(full_txt)
            summary  = extract_summary(body or full_txt)

            rel_path = str(md_file.relative_to(REPO_ROOT))
            cache[uid] = {
                "file":     rel_path,
                "source":   meta.get("source", md_file.parent.name),
                "title":    title[:150],
                "url":      meta.get("url", ""),
                "keywords": keywords,
                "summary":  summary[:500],
            }
            processed += 1

            if verbose:
                print(f"  ✓ {rel_path[:60]:60s}  kw={len(keywords)}")

        except Exception as e:
            errors += 1
            if verbose:
                print(f"  ✗ {md_file.name}: {e}")

    # Guardar cache
    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # Archivar aprendizajes procesados de corpus/learn/ → corpus/learn-archived/
    archived_learn = _archive_learn_files(cache)

    # Archivar docs viejos de fuentes auto-harvest → corpus-archived/
    archived_corpus = _archive_old_corpus_files(cache)

    print(f"✅ Enriquecidos: {processed} nuevos | Cached: {skipped} | Errores: {errors}")
    if archived_learn:
        print(f"📦 Archivados: {archived_learn} aprendizajes → corpus/learn-archived/")
    if archived_corpus:
        print(f"📦 Archivados: {archived_corpus} docs >{ARCHIVE_AFTER_DAYS}d → corpus-archived/")
    print(f"📊 Total en cache: {len(cache)} documentos")
    print(f"💾 Cache: {CACHE_FILE}")
    return processed


def _archive_old_corpus_files(cache: dict) -> int:
    """Mueve docs de fuentes auto-archive con >ARCHIVE_AFTER_DAYS a corpus-archived/<source>/.
    Sus vectores (keywords/summary) ya están en cache, así que no se pierde información."""
    CORPUS_ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    cutoff = time.time() - (ARCHIVE_AFTER_DAYS * 86400)

    # Paths cacheados → puedes archivar
    cached_paths = {v["file"] for v in cache.values()}
    archived = 0

    for md_file in CORPUS_DIR.rglob("*.md"):
        if any(x in md_file.parts for x in ("learn", "learn-archived", "corpus-archived")):
            continue

        source = md_file.parent.name
        if source not in AUTO_ARCHIVE_SOURCES:
            continue

        try:
            mtime = md_file.stat().st_mtime
        except FileNotFoundError:
            continue
        if mtime > cutoff:
            continue

        rel = str(md_file.relative_to(REPO_ROOT))
        if rel not in cached_paths:
            continue  # aún no vectorizado, esperar

        dest_dir = CORPUS_ARCHIVE_DIR / source
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / md_file.name
        if dest.exists():
            dest = dest_dir / f"{md_file.stem}_{md_file.stat().st_mtime_ns}{md_file.suffix}"

        try:
            md_file.rename(dest)
            archived += 1
        except Exception:
            continue

    return archived


def _archive_learn_files(cache: dict) -> int:
    """Mueve corpus/learn/*.md ya procesados → corpus/learn-archived/ para evitar duplicados."""
    if not LEARN_DIR.exists():
        return 0
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # UIDs ya en cache (incluye los recién procesados)
    cached_paths = {v["file"] for v in cache.values()}
    archived = 0

    for md_file in list(LEARN_DIR.glob("*.md")):
        rel = str(md_file.relative_to(REPO_ROOT))
        if rel in cached_paths:
            dest = ARCHIVE_DIR / md_file.name
            # Evitar colisión de nombres
            if dest.exists():
                dest = ARCHIVE_DIR / f"{md_file.stem}_{md_file.stat().st_mtime_ns}{md_file.suffix}"
            md_file.rename(dest)
            archived += 1

    return archived


def show_stats() -> None:
    if not CACHE_FILE.exists():
        print("⚠️  No hay cache aún — ejecuta primero sin --stats")
        return
    cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    by_source: dict[str, int] = {}
    for doc in cache.values():
        src = doc.get("source", "unknown")
        by_source[src] = by_source.get(src, 0) + 1

    print(f"\n📊 Enrichment cache — {len(cache)} documentos\n")
    for src, count in sorted(by_source.items(), key=lambda x: -x[1]):
        print(f"   {src:25s}  {count:>5} docs")

    # Muestra un ejemplo
    sample = next(iter(cache.values()))
    print(f"\n📄 Ejemplo:")
    print(f"   Título:   {sample.get('title','')[:80]}")
    print(f"   Keywords: {', '.join(sample.get('keywords', [])[:5])}")
    print(f"   Summary:  {sample.get('summary','')[:150]}…")


def main():
    parser = argparse.ArgumentParser(description="Enriquece corpus con keywords + resumen (local, $0)")
    parser.add_argument("--force",   action="store_true", help="Reprocesar todos los docs (ignora cache)")
    parser.add_argument("--stats",   action="store_true", help="Solo muestra estadísticas")
    parser.add_argument("--verbose", action="store_true", help="Log detallado por doc")
    args = parser.parse_args()

    if args.stats:
        show_stats()
        return

    process_corpus(force=args.force, verbose=args.verbose)


if __name__ == "__main__":
    main()
