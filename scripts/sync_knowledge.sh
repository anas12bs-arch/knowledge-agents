#!/usr/bin/env bash
# sync_knowledge.sh — Sincroniza corpus → Claude memory vectors
# Ejecutado por el scheduled task de Claude cada hora
set -euo pipefail

REPO="/Users/anasahmadouch/Desktop/PrimeBot/knowledge-agents"
PYTHON="/tmp/kavenv/bin/python3"

# Fallback a python del sistema si kavenv no está
if [ ! -f "$PYTHON" ]; then
  PYTHON="$(which python3)"
fi

echo "🔄 [$(date '+%H:%M:%S')] Knowledge sync iniciado"

# 1. Pull último corpus
git -C "$REPO" pull --ff-only 2>&1 | tail -2

# 2. Contar docs
TOTAL=$(find "$REPO/corpus" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
echo "📁 Corpus: $TOTAL docs"

# 3. Exportar corpus a formato memory
"$PYTHON" "$REPO/scripts/export_to_claude_memory.py" 2>&1 | tail -3

# 4. Escribir archivos individuales para import vectorial
"$PYTHON" - <<'PYEOF'
import pathlib, re

CORPUS   = pathlib.Path("/Users/anasahmadouch/Desktop/PrimeBot/knowledge-agents/corpus")
MEM_DIR  = pathlib.Path("/Users/anasahmadouch/.claude/projects/-Users-anasahmadouch-Desktop-PrimeBot/memory")
MEM_DIR.mkdir(parents=True, exist_ok=True)

for f in MEM_DIR.glob("kg-*.md"):
    f.unlink()

files = sorted(CORPUS.rglob("*.md"), key=lambda p: p.stat().st_size, reverse=True)[:80]
for i, fp in enumerate(files):
    text = fp.read_text(errors="ignore")
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"')
            body = text[end+3:].strip()
    title  = meta.get("title",  fp.stem)[:100]
    source = meta.get("source", fp.parent.name)
    url    = meta.get("url", "")
    slug   = re.sub(r"[^a-zA-Z0-9-]", "_", title)[:40]
    (MEM_DIR / f"kg-{i:03d}-{source}-{slug}.md").write_text(
        f'---\ntitle: "{title}"\nsource: "{source}"\nurl: "{url}"\n'
        f'tags: [knowledge-graph, {source}]\n---\n\n# {title}\n\n**Source:** {source}\n\n{body[:800]}'
    )

print(f"✅ {len(files)} archivos memory escritos")
PYEOF

echo "✅ Sync completado — $(date '+%Y-%m-%d %H:%M UTC')"
