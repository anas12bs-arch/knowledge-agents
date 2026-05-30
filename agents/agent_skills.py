"""
AGENTE 3 — Skills & Competencias → corpus/skills/
  · roadmap.sh (23 roadmaps completos en markdown)
  · npm top packages — descripción + keywords
  · PyPI — librerías Python AI/web/infra
  · arxiv — papers cs.AI cs.LG cs.CL cs.CV
  · State of JS / CSS (JSON de encuestas anuales)
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import time
import httpx
from xml.etree import ElementTree as ET
from core.graphify_writer import save


# ── roadmap.sh ─────────────────────────────────────────────────────────────────

ROADMAPS = [
    "frontend", "backend", "fullstack", "devops", "ai-data-scientist",
    "mlops", "software-architect", "python", "javascript", "typescript",
    "react", "nodejs", "vue", "angular", "docker", "kubernetes",
    "postgresql", "mongodb", "system-design", "git-github",
    "cyber-security", "blockchain", "android",
]
ROADMAP_RAW = "https://raw.githubusercontent.com/kamranahmedse/developer-roadmap/master/src/data/roadmaps/{name}/content/index.md"

def fetch_roadmaps() -> int:
    saved = 0
    for name in ROADMAPS:
        try:
            r = httpx.get(ROADMAP_RAW.format(name=name), timeout=15)
            if r.status_code == 200 and len(r.text) > 100:
                p = save(
                    title=f"Roadmap: {name.replace('-',' ').title()}",
                    content=r.text[:6000],
                    url=f"https://roadmap.sh/{name}",
                    source="roadmap-sh",
                    category="skill",
                    tags=["roadmap", "skills", "learning-path", name],
                )
                if p:
                    saved += 1
        except Exception:
            pass
        time.sleep(0.2)
    return saved


# ── npm packages ───────────────────────────────────────────────────────────────

NPM_PACKAGES = [
    # frameworks
    "react", "vue", "svelte", "angular", "solid-js", "qwik",
    "next", "nuxt", "astro", "remix", "gatsby",
    # build
    "vite", "webpack", "esbuild", "rollup", "turbo", "bun",
    # language/types
    "typescript", "zod", "valibot",
    # state
    "zustand", "jotai", "redux", "@tanstack/react-query",
    # backend
    "express", "fastify", "hono", "elysia", "@trpc/server",
    # ORM/DB
    "prisma", "drizzle-orm", "kysely", "@supabase/supabase-js",
    # AI
    "openai", "@anthropic-ai/sdk", "langchain", "llamaindex",
    "@vercel/ai", "ollama", "chromadb",
    # testing
    "vitest", "jest", "playwright", "@testing-library/react",
    # styling
    "tailwindcss", "shadcn-ui", "@radix-ui/react-primitives",
    # infra
    "dotenv", "zod", "commander", "chalk",
]

def fetch_npm() -> int:
    saved = 0
    for pkg in NPM_PACKAGES:
        try:
            d = httpx.get(f"https://registry.npmjs.org/{pkg}/latest", timeout=12).json()
            desc = d.get("description", "")
            kw = d.get("keywords", [])
            readme = (d.get("readme", "") or "")[:2500]
            content = f"**{pkg}** v{d.get('version','')}\n\n{desc}\n\nKeywords: {', '.join(kw)}\n\n{readme}"
            p = save(
                title=f"npm: {pkg} v{d.get('version','')}",
                content=content,
                url=f"https://npmjs.com/package/{pkg}",
                source="npm",
                category="skill",
                tags=["npm", "javascript", "package"] + kw[:4],
                metadata={"version": d.get("version",""), "package": pkg},
            )
            if p:
                saved += 1
        except Exception:
            pass
        time.sleep(0.15)
    return saved


# ── PyPI ───────────────────────────────────────────────────────────────────────

PYPI_PACKAGES = [
    # AI / LLM
    "langchain", "openai", "anthropic", "transformers", "torch",
    "litellm", "instructor", "dspy-ai", "pydantic-ai", "crewai",
    "autogen", "llama-index", "semantic-kernel", "guidance",
    # vector DBs
    "chromadb", "pinecone-client", "qdrant-client", "weaviate-client",
    "faiss-cpu", "sentence-transformers",
    # web
    "fastapi", "starlette", "httpx", "aiohttp", "uvicorn",
    # data
    "pydantic", "sqlalchemy", "alembic", "celery", "redis",
    "pandas", "polars", "numpy", "scikit-learn",
    # devtools
    "rich", "typer", "click", "pytest", "ruff", "mypy",
]

def fetch_pypi() -> int:
    saved = 0
    for pkg in PYPI_PACKAGES:
        try:
            info = httpx.get(f"https://pypi.org/pypi/{pkg}/json", timeout=12).json().get("info", {})
            content = f"**{pkg}** v{info.get('version','')}\n\n" \
                      f"{info.get('summary','')}\n\n" \
                      f"{(info.get('description') or '')[:2500]}"
            p = save(
                title=f"PyPI: {pkg} v{info.get('version','')}",
                content=content,
                url=info.get("project_url") or f"https://pypi.org/project/{pkg}",
                source="pypi",
                category="skill",
                tags=["pypi", "python", "package", pkg],
                metadata={"version": info.get("version",""), "package": pkg},
            )
            if p:
                saved += 1
        except Exception:
            pass
        time.sleep(0.15)
    return saved


# ── arxiv papers ───────────────────────────────────────────────────────────────

ARXIV_CATS = ["cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.MA", "cs.NE"]

def fetch_arxiv() -> int:
    saved = 0
    for cat in ARXIV_CATS:
        try:
            resp = httpx.get(
                "http://export.arxiv.org/api/query",
                params={"search_query": f"cat:{cat}", "sortBy": "submittedDate",
                        "sortOrder": "descending", "max_results": 12},
                timeout=20,
            )
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            root = ET.fromstring(resp.text)
            for entry in root.findall("atom:entry", ns):
                title   = (entry.find("atom:title", ns).text or "").replace("\n", " ").strip()
                summary = (entry.find("atom:summary", ns).text or "").strip()
                link    = (entry.find("atom:id", ns).text or "").strip()
                # authors
                authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
                content = f"## {title}\n\nAuthors: {', '.join(authors[:5])}\n\n{summary}"
                p = save(
                    title=title, content=content, url=link,
                    source="arxiv",
                    category="research",
                    tags=["arxiv", "research", "paper", cat.lower().replace(".", "-")],
                )
                if p:
                    saved += 1
        except Exception as e:
            print(f"  arxiv/{cat}: {e}")
        time.sleep(0.5)
    return saved


# ── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=== AGENT SKILLS ===")
    r = fetch_roadmaps(); print(f"  Roadmaps: {r} new")
    n = fetch_npm();      print(f"  npm: {n} new")
    p = fetch_pypi();     print(f"  PyPI: {p} new")
    a = fetch_arxiv();    print(f"  arxiv: {a} new")
    print(f"✅ Skills: {r+n+p+a} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
