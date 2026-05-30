"""
Query local — busca en el knowledge graph que graphify construyó.
Después de `git pull`, el graph.json está actualizado con todo lo que
los agentes ingirieron mientras tu Mac estaba apagada.

Uso:
  python query.py "qué frameworks de AI están creciendo?"
  python query.py --stats
  python query.py --serve          # inicia MCP server (para Claude)
  graphify query "tu pregunta"     # alternativa directa con graphify CLI
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

GRAPH_JSON = Path(__file__).parent / "graphify-out" / "graph.json"
GRAPHIFY_BIN = os.environ.get("GRAPHIFY_BIN", "graphify")


def stats():
    """Muestra estadísticas del grafo actual."""
    if not GRAPH_JSON.exists():
        print("❌ No hay grafo todavía. Ejecuta: python agents/run_all.py")
        return
    g = json.loads(GRAPH_JSON.read_text())
    nodes = g.get("nodes", [])
    edges = g.get("links", g.get("edges", []))
    # Contar por categoría de source
    sources: dict[str, int] = {}
    for n in nodes:
        src = n.get("source_file", "").split("/")[0]
        sources[src] = sources.get(src, 0) + 1
    print("\n📊 Knowledge Graph Stats")
    print("─" * 50)
    print(f"  Total nodes : {len(nodes)}")
    print(f"  Total edges : {len(edges)}")
    print()
    # Corpus files
    corpus = Path(__file__).parent / "corpus"
    if corpus.exists():
        for subdir in sorted(corpus.iterdir()):
            if subdir.is_dir():
                n = len(list(subdir.glob("*.md")))
                print(f"  corpus/{subdir.name:20s} {n:>5} docs")
    print()


def serve():
    """Inicia el MCP server de graphify para que Claude lo consulte."""
    print("🚀 Starting graphify MCP server…")
    print("   Claude puede consultarlo con /graphify")
    subprocess.run([GRAPHIFY_BIN, "serve", str(GRAPH_JSON)])


def query_graph(question: str):
    """Usa graphify CLI para buscar en el grafo."""
    if not GRAPH_JSON.exists():
        print("❌ No hay grafo. Ejecuta primero: python agents/run_all.py")
        sys.exit(1)
    print(f"\n🔍 Buscando: \"{question}\"")
    subprocess.run([GRAPHIFY_BIN, "query", question, "--graph", str(GRAPH_JSON)])


def pull_latest():
    """Hace git pull para traer el grafo más reciente de GitHub Actions."""
    print("⬇️  Pulling latest knowledge graph from GitHub…")
    result = subprocess.run(["git", "pull", "--ff-only"], capture_output=True, text=True)
    print(result.stdout or result.stderr)
    stats()


def main():
    parser = argparse.ArgumentParser(
        description="Query the local knowledge graph built by graphify"
    )
    parser.add_argument("question", nargs="?", help="Pregunta a buscar en el grafo")
    parser.add_argument("--stats",  action="store_true", help="Mostrar estadísticas del grafo")
    parser.add_argument("--serve",  action="store_true", help="Iniciar MCP server para Claude")
    parser.add_argument("--pull",   action="store_true", help="git pull + mostrar stats")
    args = parser.parse_args()

    if args.pull:
        pull_latest()
    elif args.stats:
        stats()
    elif args.serve:
        serve()
    elif args.question:
        query_graph(args.question)
    else:
        parser.print_help()
        print()
        stats()


if __name__ == "__main__":
    main()
