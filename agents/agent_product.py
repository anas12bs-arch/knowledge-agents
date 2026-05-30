"""
AGENTE 6 — Product + Startups → corpus/product/
  · Product Hunt (homepage RSS)
  · Indie Hackers RSS
  · Y Combinator blog
  · TechCrunch startups
  · First Round Review
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

FEEDS = {
    "indie-hackers":    "https://www.indiehackers.com/feed.xml",
    "yc-blog":          "https://www.ycombinator.com/blog/feed/",
    "techcrunch-startups": "https://techcrunch.com/category/startups/feed/",
    "first-round":      "https://review.firstround.com/feed.xml",
    "product-hunt":     "https://www.producthunt.com/feed",
}

HEADERS = {"User-Agent": "KnowledgeBot/1.0 (RSS reader)"}


def _parse_rss(name: str, url: str) -> int:
    saved = 0
    try:
        resp = httpx.get(url, timeout=15, follow_redirects=True, headers=HEADERS)
        if resp.status_code != 200:
            print(f"  {name}: HTTP {resp.status_code}")
            return 0
        root = ET.fromstring(resp.text)
        for item in root.findall(".//item")[:8]:
            title = (item.findtext("title") or "").strip()
            link  = (item.findtext("link") or "").strip()
            desc  = re.sub(r"<[^>]+>", " ", item.findtext("description") or "")[:2000].strip()
            if title and link:
                p = save(
                    title=f"[{name}] {title}",
                    content=f"{title}\n\n{desc}",
                    url=link,
                    source="product",
                    category="business",
                    tags=["product", "startup", "saas", "growth", name],
                )
                if p:
                    saved += 1
    except Exception as e:
        print(f"  {name}: {e}")
    return saved


def run():
    print("=== AGENT PRODUCT ===")
    total = 0
    for name, url in FEEDS.items():
        n = _parse_rss(name, url)
        print(f"  {name}: {n} new")
        total += n
        time.sleep(0.3)
    print(f"✅ Product: {total} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
