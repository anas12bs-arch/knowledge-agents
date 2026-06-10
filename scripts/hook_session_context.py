"""
SessionStart hook — inyecta el estado de la base de conocimiento al
arrancar cada sesión de Claude Code. Lo que imprime a stdout se añade
al contexto del modelo. Stdlib puro, rápido (<1s), salida acotada.
"""
from __future__ import annotations
import json
import time
from pathlib import Path

KA = Path(__file__).resolve().parent.parent
GRAPH = KA / "graphify-out" / "graph.json"
LEARN = KA / "corpus" / "learn"

STALE_HOURS = 48


def main() -> None:
    lines = ["[KNOWLEDGE BASE — estado al iniciar sesión]"]

    if GRAPH.exists():
        age_h = (time.time() - GRAPH.stat().st_mtime) / 3600
        try:
            manifest = json.loads((GRAPH.parent / "manifest.json").read_text())
            n_docs = len(manifest) if isinstance(manifest, (list, dict)) else "?"
        except Exception:
            n_docs = "?"
        lines.append(
            f"- Grafo: graphify-out/graph.json ({n_docs} docs en manifest, "
            f"actualizado hace {age_h:.0f}h)"
        )
        if age_h > STALE_HOURS:
            lines.append(
                f"- ⚠️ GRAFO DESACTUALIZADO (> {STALE_HOURS}h). Ejecuta: "
                "cd knowledge-agents && python3 query.py --pull"
            )
    else:
        lines.append("- ⚠️ No existe graph.json. Ejecuta: python3 query.py --pull")

    # Los .md de corpus/learn/ son efímeros (el CI los archiva tras ingerirlos);
    # la fuente persistente de aprendizajes es enrichment_cache.json.
    titles: list[str] = []
    try:
        cache = json.loads(
            (KA / "graphify-out" / "enrichment_cache.json").read_text())
        titles = [str(v.get("title", ""))[:90] for v in cache.values()
                  if "corpus/learn/" in str(v.get("file", ""))]
    except Exception:
        pass
    if LEARN.exists():  # pendientes aún no ingeridos
        for f in sorted(LEARN.glob("*.md"), key=lambda p: p.stat().st_mtime,
                        reverse=True):
            titles.insert(0, f.stem)
    if titles:
        lines.append(f"- Aprendizajes en la base ({len(titles)}), últimos 5:")
        for t in titles[:5]:
            lines.append(f"    · {t}")

    lines.append(
        "- REGLA: antes de buscar con grep/find o asumir contexto del "
        "proyecto, consulta primero el grafo: `graphify query \"<pregunta>\"` "
        "(en knowledge-agents/) o `python3 query.py \"<pregunta>\"`."
    )
    lines.append(
        "- REGLA: cada error resuelto, insight del usuario o patrón nuevo se "
        "captura SIN preguntar: cd knowledge-agents && python3 -m core.learn "
        "\"...\" --type <error|insight|pattern|optimization|lesson>"
    )
    print("\n".join(lines))


if __name__ == "__main__":
    main()
