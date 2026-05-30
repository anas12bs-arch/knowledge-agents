"""
AGENTE 2 — GitHub Intelligence → corpus/github/
  · Repos trending por topic (7 días)
  · Release notes de 30 herramientas clave
  · HN "Who's hiring" → stack de demanda real
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import time
from datetime import datetime, timedelta
import httpx
from core.graphify_writer import save

GH_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GH_BASE  = "https://api.github.com"

def _gh(path: str, **params) -> dict | list:
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if GH_TOKEN:
        h["Authorization"] = f"Bearer {GH_TOKEN}"
    r = httpx.get(f"{GH_BASE}{path}", headers=h, params=params, timeout=20)
    r.raise_for_status()
    return r.json()


# ── Trending repos ─────────────────────────────────────────────────────────────

TOPICS = ["ai", "llm", "agent", "machine-learning", "web", "typescript",
          "python", "rust", "go", "devops", "cli", "nextjs", "react",
          "vue", "wasm", "mcp", "rag", "embedding", "vector-database"]

def fetch_trending() -> int:
    since = (datetime.utcnow() - timedelta(days=7)).strftime("%Y-%m-%d")
    saved = 0
    for topic in TOPICS:
        try:
            data = _gh("/search/repositories",
                       q=f"topic:{topic} stars:>30 pushed:>{since}",
                       sort="stars", order="desc", per_page=6)
            for repo in data.get("items", []):
                desc = repo.get("description") or ""
                # Fetch README (first 3000 chars)
                readme = ""
                try:
                    rm = httpx.get(
                        f"{GH_BASE}/repos/{repo['full_name']}/readme",
                        headers={**{"Accept": "application/vnd.github.raw"},
                                 **({} if not GH_TOKEN else {"Authorization": f"Bearer {GH_TOKEN}"})},
                        timeout=10)
                    if rm.status_code == 200:
                        readme = rm.text[:3000]
                except Exception:
                    pass

                content = f"**{repo['full_name']}** — ⭐ {repo['stargazers_count']}\n\n" \
                          f"Language: {repo.get('language','?')} | " \
                          f"Topics: {', '.join(repo.get('topics',[])[:6])}\n\n" \
                          f"{desc}\n\n{readme}"
                p = save(
                    title=f"{repo['full_name']} ⭐{repo['stargazers_count']}",
                    content=content,
                    url=repo["html_url"],
                    source="github-trending",
                    category="tool",
                    tags=["github", "trending", topic] + repo.get("topics", [])[:4],
                    metadata={"stars": str(repo["stargazers_count"]),
                              "language": repo.get("language", "")},
                )
                if p:
                    saved += 1
        except Exception as e:
            print(f"  trending/{topic}: {e}")
        time.sleep(0.5)
    return saved


# ── Release notes ──────────────────────────────────────────────────────────────

KEY_REPOS = [
    "vercel/next.js", "facebook/react", "vuejs/vue", "sveltejs/svelte",
    "vitejs/vite", "astro-build/astro", "remix-run/remix",
    "microsoft/TypeScript", "denoland/deno", "oven-sh/bun",
    "langchain-ai/langchain", "openai/openai-python",
    "anthropics/anthropic-sdk-python", "ollama/ollama",
    "supabase/supabase", "prisma/prisma", "trpc/trpc",
    "shadcn-ui/ui", "tailwindlabs/tailwindcss",
    "docker/compose", "kubernetes/kubernetes",
    "rust-lang/rust", "golang/go", "python/cpython",
    "tiangolo/fastapi", "pydantic/pydantic",
    "huggingface/transformers", "pytorch/pytorch",
    "microsoft/autogen", "crewAIInc/crewAI",
]

def fetch_releases() -> int:
    saved = 0
    for repo in KEY_REPOS:
        try:
            releases = _gh(f"/repos/{repo}/releases", per_page=2)
            for rel in releases[:2]:
                if not isinstance(rel, dict):
                    continue
                body = (rel.get("body") or "")[:4000]
                content = f"## {repo} — {rel.get('tag_name','')}\n\n{body}"
                p = save(
                    title=f"{repo} {rel.get('tag_name','')} released",
                    content=content,
                    url=rel.get("html_url", f"https://github.com/{repo}/releases"),
                    source="github-releases",
                    category="changelog",
                    tags=["github", "release", "changelog", repo.split("/")[1]],
                    metadata={"repo": repo, "version": rel.get("tag_name","")},
                )
                if p:
                    saved += 1
        except Exception as e:
            print(f"  releases/{repo}: {e}")
        time.sleep(0.25)
    return saved


# ── HN Who's Hiring → demanda real de skills ──────────────────────────────────

def fetch_hn_hiring() -> int:
    saved = 0
    try:
        submitted = httpx.get(
            "https://hacker-news.firebaseio.com/v0/user/whoishiring.json", timeout=10
        ).json().get("submitted", [])
        for post_id in submitted[:2]:
            post = httpx.get(
                f"https://hacker-news.firebaseio.com/v0/item/{post_id}.json", timeout=10
            ).json()
            if not post or "hiring" not in post.get("title", "").lower():
                continue
            for kid in (post.get("kids") or [])[:40]:
                try:
                    c = httpx.get(
                        f"https://hacker-news.firebaseio.com/v0/item/{kid}.json", timeout=8
                    ).json()
                    text = c.get("text", "") or ""
                    if len(text) > 150:
                        p = save(
                            title=f"HN Hiring ({post['title'][:60]})",
                            content=text[:3000],
                            url=f"https://news.ycombinator.com/item?id={kid}",
                            source="hn-hiring",
                            category="job-skills",
                            tags=["hiring", "tech-stack", "skills", "market-demand"],
                        )
                        if p:
                            saved += 1
                except Exception:
                    pass
                time.sleep(0.04)
    except Exception as e:
        print(f"  HN hiring: {e}")
    return saved


# ── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=== AGENT GITHUB ===")
    t = fetch_trending(); print(f"  Trending repos: {t} new")
    r = fetch_releases(); print(f"  Release notes: {r} new")
    h = fetch_hn_hiring(); print(f"  HN hiring: {h} new")
    print(f"✅ GitHub: {t+r+h} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
