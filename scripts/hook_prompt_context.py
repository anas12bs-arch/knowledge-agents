"""
UserPromptSubmit hook — busca en la base de conocimiento los docs más
relevantes al mensaje del usuario y los inyecta como contexto.

Usa enrichment_cache.json (título+keywords+resumen, ~3.400 docs) en vez del
graph.json de 92MB: carga en <100ms, así no añade latencia perceptible.
Para profundidad el modelo puede seguir con `graphify query`. Stdlib puro.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

KA = Path(__file__).resolve().parent.parent
CACHE = KA / "graphify-out" / "enrichment_cache.json"

MIN_PROMPT_LEN = 15
MIN_SCORE = 4
TOP_N = 3

STOPWORDS = {
    "para", "como", "esto", "esta", "este", "pero", "porque", "cuando",
    "donde", "quiero", "hacer", "puedo", "tiene", "tienen", "sobre", "todo",
    "that", "this", "with", "from", "what", "have", "make", "want", "should",
    "como", "ahora", "tambien", "más", "mas", "the", "and", "you",
}


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-záéíóúñü0-9][a-záéíóúñü0-9.\-]{3,}", text.lower())
            if w not in STOPWORDS}


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    prompt = str(data.get("prompt") or "")
    if len(prompt) < MIN_PROMPT_LEN or not CACHE.exists():
        return

    qt = tokens(prompt)
    if len(qt) < 2:
        return

    try:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    except Exception:
        return

    scored = []
    for doc in cache.values():
        title = str(doc.get("title", ""))
        score = 3 * len(qt & tokens(title))
        score += 2 * len(qt & tokens(" ".join(doc.get("keywords") or [])))
        score += len(qt & tokens(str(doc.get("summary", ""))[:400]))
        if "corpus/learn/" in str(doc.get("file", "")):
            score *= 2  # los aprendizajes propios pesan doble
        if score >= MIN_SCORE:
            scored.append((score, title, doc))
    if not scored:
        return

    scored.sort(key=lambda x: -x[0])
    lines = ["[KNOWLEDGE BASE — docs relevantes a este mensaje]"]
    for score, title, doc in scored[:TOP_N]:
        src = str(doc.get("source", ""))
        summ = re.sub(r"\s+", " ", str(doc.get("summary", "")))[:180]
        lines.append(f"· ({src}) {title[:90]} — {summ}")
    lines.append(
        'Para profundizar: cd knowledge-agents && graphify query "<pregunta>"')
    print("\n".join(lines))


if __name__ == "__main__":
    main()
