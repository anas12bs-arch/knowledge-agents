"""
AGENTE 8 — DevOps + Infrastructure → corpus/devops/
  · Kubernetes blog
  · Docker blog
  · HashiCorp blog
  · CNCF blog
  · DevOps.com
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

FEEDS = {
    "kubernetes":  "https://kubernetes.io/feed.xml",
    "docker":      "https://www.docker.com/blog/feed/",
    "hashicorp":   "https://www.hashicorp.com/blog/feed.xml",
    "cncf":        "https://www.cncf.io/blog/feed/",
    "devops-com":  "https://devops.com/feed/",
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
                    source="devops",
                    category="infrastructure",
                    tags=["devops", "infrastructure", "cloud", "kubernetes", name],
                )
                if p:
                    saved += 1
    except Exception as e:
        print(f"  {name}: {e}")
    return saved


def run():
    print("=== AGENT DEVOPS ===")
    total = 0
    for name, url in FEEDS.items():
        n = _parse_rss(name, url)
        print(f"  {name}: {n} new")
        total += n
        time.sleep(0.3)
    print(f"✅ DevOps: {total} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
