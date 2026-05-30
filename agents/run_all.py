"""
Corre los 15 agentes en paralelo → escribe corpus/ → ejecuta graphify.
Usado por GitHub Actions y localmente.

Uso:
  python run_all.py                  # todos los agentes
  python run_all.py --only news      # solo uno
  python run_all.py --skip-graphify  # solo recolectar, no rebuildar grafo
"""
from __future__ import annotations
import sys, os, argparse, subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

AGENTS = {
    # Core Tech (4)
    "news":         "agent_news",
    "github":       "agent_github",
    "skills":       "agent_skills",
    "social":       "agent_social",
    # Design + Product (2)
    "design":       "agent_design",
    "product":      "agent_product",
    # Engineering + Infra (2)
    "engineering":  "agent_engineering",
    "devops":       "agent_devops",
    # AI + Security (2)
    "ai":           "agent_ai",
    "security":     "agent_security",
    # Business + Sales (3)
    "sales":        "agent_sales",
    "business":     "agent_business",
    "psychology":   "agent_psychology",
    # Legal + Finance (2)
    "legal":        "agent_legal",
    "finance":      "agent_finance",
}

def run_agent(module_name: str) -> str:
    import importlib
    os.chdir(os.path.dirname(__file__))
    mod = importlib.import_module(module_name)
    mod.run()
    return module_name


def build_graph(corpus_dir: str) -> None:
    """Llama a `graphify update` para reconstruir el grafo (AST-only, sin LLM)."""
    graphify_bin = os.environ.get("GRAPHIFY_BIN", "graphify")
    root = os.path.dirname(corpus_dir) if corpus_dir.endswith("corpus") else corpus_dir
    print(f"\n🔨 Building knowledge graph from {root} (no LLM) …")
    result = subprocess.run(
        [graphify_bin, "update", root, "--no-cluster"],
        capture_output=False,
        timeout=600,
    )
    if result.returncode != 0:
        print("⚠️  graphify exited with non-zero code — graph may be partial")
    else:
        print("✅ Knowledge graph updated")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="+", choices=list(AGENTS.keys()))
    parser.add_argument("--skip-graphify", action="store_true",
                        help="Don't rebuild the graph (just collect markdown)")
    parser.add_argument("--corpus-dir", default=None,
                        help="Override corpus directory path")
    args = parser.parse_args()

    corpus_dir = args.corpus_dir or str(
        (os.path.dirname(os.path.dirname(__file__)) + "/corpus")
    )

    to_run  = args.only or list(AGENTS.keys())
    modules = [AGENTS[a] for a in to_run]

    print(f"🚀 Running {len(modules)} agents in parallel: {', '.join(to_run)}")

    with ThreadPoolExecutor(max_workers=15) as pool:
        futures = {pool.submit(run_agent, m): m for m in modules}
        for fut in as_completed(futures):
            m = futures[fut]
            try:
                fut.result()
            except Exception as e:
                print(f"❌ {m} failed: {e}")

    # Print corpus stats
    from core.graphify_writer import count_corpus
    counts = count_corpus()
    total = sum(counts.values())
    print(f"\n📁 Corpus: {total} total markdown files")
    for src, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"   {src:25s} {n:>5} files")

    if not args.skip_graphify:
        build_graph(corpus_dir)


if __name__ == "__main__":
    main()
