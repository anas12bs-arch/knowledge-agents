#!/usr/bin/env bash
# sync_knowledge.sh — Sincroniza corpus → Claude memory vectors
# Ejecutado por el scheduled task de Claude cada hora
set -euo pipefail

REPO="/Users/anasahmadouch/Desktop/PrimeBot/knowledge-agents"
PYTHON="$HOME/.primebot/kavenv/bin/python3"

# Fallback a python del sistema si el venv no está
if [ ! -f "$PYTHON" ]; then
  PYTHON="$(which python3)"
fi

echo "🔄 [$(date '+%H:%M:%S')] Knowledge sync iniciado"

# 0. Commitear aprendizajes locales ANTES de cualquier cosa, para que lleguen
#    al CI y se ingieran al grafo (si se enriquecen antes del push, el
#    archivado los movería a learn-archived/ y nunca llegarían a GitHub).
if ls "$REPO/corpus/learn/"*.md >/dev/null 2>&1; then
  git -C "$REPO" add corpus/learn/ 2>/dev/null || true
  git -C "$REPO" commit --quiet -m "learn: capturas locales $(date '+%Y-%m-%d %H:%M')" 2>/dev/null \
    && echo "📝 Aprendizajes locales commiteados" || true
fi

# 1. Pull último corpus
#    Los cachés AST locales sin trackear chocan con los que commitea el CI
#    (nombres content-addressed → mismo nombre = mismo contenido). Se apartan
#    a /tmp antes del pull en vez de borrarlos.
BACKUP="/tmp/ka-cache-backup"
git -C "$REPO" ls-files --others --exclude-standard graphify-out/cache | while read -r f; do
  mkdir -p "$BACKUP/$(dirname "$f")" && mv "$REPO/$f" "$BACKUP/$f"
done
git -C "$REPO" pull --rebase --autostash 2>&1 | tail -2 || echo "⚠️ pull falló (sigo con corpus local)"

# 1c. Push si hay commits locales pendientes (los learn de arriba)
if [ -n "$(git -C "$REPO" log origin/main..HEAD --oneline 2>/dev/null)" ]; then
  git -C "$REPO" push --quiet origin main 2>&1 && echo "⬆️ Aprendizajes subidos — el CI los ingiere al grafo" || echo "⚠️ push falló"
fi

# 1b. Enriquecer docs nuevos (keywords + summary, $0.00)
#     Antes lo hacía un launchd agent, pero TCC bloquea a launchd el acceso
#     a ~/Desktop — este task corre en contexto Claude, que sí tiene acceso.
#     ARCHIVE_AFTER_DAYS alto = el archivado de corpus lo hace SOLO el CI
#     (si se hace local quedan borrados sin commitear que rompen el pull).
(cd "$REPO" && ARCHIVE_AFTER_DAYS=36500 "$PYTHON" -m core.enrich 2>&1 | tail -2) || echo "⚠️ enrich falló (no bloqueante)"

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
