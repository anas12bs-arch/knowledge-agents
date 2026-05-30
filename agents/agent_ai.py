"""
AGENTE 9 — AI / ML Research → corpus/ai-research/
  · ArXiv CS.AI (recent papers)
  · ArXiv CS.LG (machine learning)
  · OpenAI blog
  · Hugging Face blog
  · Anthropic research
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

HEADERS = {"User-Agent": "KnowledgeBot/1.0 (RSS reader)"}

ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}

ARXIV_QUERIES = {
    "cs-ai": "http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=lastUpdatedDate&max_results=10",
    "cs-lg": "http://export.arxiv.org/api/query?search_query=cat:cs.LG&sortBy=lastUpdatedDate&max_results=10",
    "cs-cl": "http://export.arxiv.org/api/query?search_query=cat:cs.CL&sortBy=lastUpdatedDate&max_results=10",
}

RSS_FEEDS = {
    "openai-blog":    "https://openai.com/blog/rss.xml",
    "hf-blog":        "https://huggingface.co/blog/feed.xml",
    "anthropic-news": "https://www.anthropic.com/feed.xml",
}


def fetch_arxiv() -> int:
    saved = 0
    for name, url in ARXIV_QUERIES.items():
        try:
            resp = httpx.get(url, timeout=20, headers=HEADERS)
            if resp.status_code != 200:
                continue
            root = ET.fromstring(resp.text)
            for entry in root.findall("atom:entry", ARXIV_NS):
                title   = (entry.findtext("atom:title", namespaces=ARXIV_NS) or "").strip()
                title   = re.sub(r"\s+", " ", title)
                summary = (entry.findtext("atom:summary", namespaces=ARXIV_NS) or "").strip()[:2000]
                link_el = entry.find("atom:id", ARXIV_NS)
                link    = (link_el.text or "").strip() if link_el is not None else ""
                authors = [a.findtext("atom:name", namespaces=ARXIV_NS) or ""
                           for a in entry.findall("atom:author", ARXIV_NS)]
                author_str = ", ".join(authors[:5])
                if title and link:
                    p = save(
                        title=f"[arxiv/{name}] {title}",
                        content=f"**Authors:** {author_str}\n\n**Abstract:** {summary}",
                        url=link,
                        source="ai-research",
                        category="research",
                        tags=["arxiv", "ai", "ml", "research", "paper", name],
                        metadata={"authors": author_str[:200]},
                    )
                    if p:
                        saved += 1
        except Exception as e:
            print(f"  arxiv/{name}: {e}")
        time.sleep(1)  # ArXiv asks for 1s between requests
    return saved


def fetch_blogs() -> int:
    saved = 0
    for name, url in RSS_FEEDS.items():
        try:
            resp = httpx.get(url, timeout=15, follow_redirects=True, headers=HEADERS)
            if resp.status_code != 200:
                print(f"  {name}: HTTP {resp.status_code}")
                continue
            root = ET.fromstring(resp.text)
            # RSS 2.0
            items = root.findall(".//item")[:6]
            if items:
                for item in items:
                    title = (item.findtext("title") or "").strip()
                    link  = (item.findtext("link") or "").strip()
                    desc  = re.sub(r"<[^>]+>", " ", item.findtext("description") or "")[:2000].strip()
                    if title and link:
                        p = save(
                            title=f"[{name}] {title}",
                            content=f"{title}\n\n{desc}",
                            url=link,
                            source="ai-research",
                            category="research",
                            tags=["ai", "ml", "blog", "industry", name],
                        )
                        if p:
                            saved += 1
            else:
                # Atom
                entries = root.findall("atom:entry", ARXIV_NS)[:6]
                for entry in entries:
                    title   = (entry.findtext("atom:title", namespaces=ARXIV_NS) or "").strip()
                    link_el = entry.find("atom:link", ARXIV_NS)
                    link    = (link_el.get("href", "") if link_el is not None else "").strip()
                    desc    = re.sub(r"<[^>]+>", " ",
                                     entry.findtext("atom:summary", namespaces=ARXIV_NS) or "")[:2000].strip()
                    if title and link:
                        p = save(
                            title=f"[{name}] {title}",
                            content=f"{title}\n\n{desc}",
                            url=link,
                            source="ai-research",
                            category="research",
                            tags=["ai", "ml", "blog", "industry", name],
                        )
                        if p:
                            saved += 1
        except Exception as e:
            print(f"  {name}: {e}")
        time.sleep(0.3)
    return saved


def run():
    print("=== AGENT AI RESEARCH ===")
    arxiv = fetch_arxiv();  print(f"  ArXiv papers: {arxiv} new")
    blogs = fetch_blogs();  print(f"  AI blogs: {blogs} new")
    print(f"✅ AI Research: {arxiv + blogs} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
