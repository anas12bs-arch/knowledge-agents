"""
AGENTE 7 — System Design + Architecture → corpus/engineering/
  · Martin Fowler blog
  · InfoQ
  · The Pragmatic Engineer (Substack)
  · ByteByteGo
  · High Scalability
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

FEEDS = {
    "martin-fowler":      "https://martinfowler.com/feed.atom",
    "infoq":              "https://feed.infoq.com/",
    "pragmatic-engineer":  "https://newsletter.pragmaticengineer.com/feed",
    "bytebytego":          "https://blog.bytebytego.com/feed",
    "high-scalability":    "http://feeds.feedburner.com/HighScalability",
}

HEADERS = {"User-Agent": "KnowledgeBot/1.0 (RSS reader)"}

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _parse_feed(name: str, url: str) -> int:
    saved = 0
    try:
        resp = httpx.get(url, timeout=15, follow_redirects=True, headers=HEADERS)
        if resp.status_code != 200:
            print(f"  {name}: HTTP {resp.status_code}")
            return 0
        root = ET.fromstring(resp.text)

        # Try RSS 2.0 first
        items = root.findall(".//item")[:8]
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
                        source="engineering",
                        category="engineering",
                        tags=["system-design", "architecture", "scalability", name],
                    )
                    if p:
                        saved += 1
        else:
            # Try Atom
            entries = root.findall("atom:entry", ATOM_NS)[:8]
            for entry in entries:
                title   = (entry.findtext("atom:title", namespaces=ATOM_NS) or "").strip()
                link_el = entry.find("atom:link", ATOM_NS)
                link    = (link_el.get("href", "") if link_el is not None else "").strip()
                summary = entry.findtext("atom:summary", namespaces=ATOM_NS) or ""
                content_el = entry.findtext("atom:content", namespaces=ATOM_NS) or ""
                desc = re.sub(r"<[^>]+>", " ", summary or content_el)[:2000].strip()
                if title and link:
                    p = save(
                        title=f"[{name}] {title}",
                        content=f"{title}\n\n{desc}",
                        url=link,
                        source="engineering",
                        category="engineering",
                        tags=["system-design", "architecture", "scalability", name],
                    )
                    if p:
                        saved += 1
    except Exception as e:
        print(f"  {name}: {e}")
    return saved


def run():
    print("=== AGENT ENGINEERING ===")
    total = 0
    for name, url in FEEDS.items():
        n = _parse_feed(name, url)
        print(f"  {name}: {n} new")
        total += n
        time.sleep(0.3)
    print(f"✅ Engineering: {total} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
