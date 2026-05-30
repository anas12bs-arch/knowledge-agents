"""
AGENTE 5 — Design + UX → corpus/design/
  · Smashing Magazine RSS
  · A List Apart RSS
  · CSS-Tricks RSS
  · Sidebar.io RSS
  · Nielsen Norman Group RSS
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

FEEDS = {
    "smashing-magazine": "https://www.smashingmagazine.com/feed/",
    "a-list-apart":      "https://alistapart.com/main/feed/",
    "css-tricks":        "https://css-tricks.com/feed/",
    "sidebar-io":        "https://sidebar.io/feed.xml",
    "nn-group":          "https://www.nngroup.com/feed/rss/",
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
        # RSS 2.0
        for item in root.findall(".//item")[:8]:
            title = (item.findtext("title") or "").strip()
            link  = (item.findtext("link") or "").strip()
            desc  = re.sub(r"<[^>]+>", " ", item.findtext("description") or "")[:2000].strip()
            if title and link:
                p = save(
                    title=f"[{name}] {title}",
                    content=f"{title}\n\n{desc}",
                    url=link,
                    source="design",
                    category="design",
                    tags=["design", "ux", "ui", "frontend", name],
                )
                if p:
                    saved += 1
    except Exception as e:
        print(f"  {name}: {e}")
    return saved


def run():
    print("=== AGENT DESIGN ===")
    total = 0
    for name, url in FEEDS.items():
        n = _parse_rss(name, url)
        print(f"  {name}: {n} new")
        total += n
        time.sleep(0.3)
    print(f"✅ Design: {total} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
