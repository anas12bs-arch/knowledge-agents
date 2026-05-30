"""
AGENTE 1 — Tech News → corpus/hackernews/ corpus/devto/ corpus/rss/
Fuentes gratis sin auth:
  HN API · Dev.to API · 10 RSS feeds de blogs tech
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import time
import httpx
from xml.etree import ElementTree as ET
from core.graphify_writer import save

# ── Hacker News ───────────────────────────────────────────────────────────────

def fetch_hn(limit: int = 50) -> int:
    ids = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=15).json()[:limit]
    saved = 0
    for item_id in ids:
        try:
            d = httpx.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json", timeout=10).json()
            if not d or d.get("type") != "story":
                continue
            url   = d.get("url") or f"https://news.ycombinator.com/item?id={item_id}"
            title = d.get("title", "")
            text  = d.get("text", "") or ""
            content = f"Score: {d.get('score', 0)} | Comments: {d.get('descendants', 0)}\n\n{text}"
            p = save(title=title, content=content, url=url,
                     source="hackernews", category="news",
                     tags=["hackernews", "tech-news"],
                     metadata={"score": str(d.get("score", 0))})
            if p:
                saved += 1
        except Exception:
            pass
        time.sleep(0.04)
    return saved


# ── Dev.to ────────────────────────────────────────────────────────────────────

DEVTO_TAGS = ["programming","ai","webdev","javascript","python",
              "devops","career","productivity","beginners","opensource"]

def fetch_devto() -> int:
    saved = 0
    for tag in DEVTO_TAGS:
        try:
            articles = httpx.get("https://dev.to/api/articles",
                                  params={"tag": tag, "per_page": 10, "top": 1},
                                  timeout=15).json()
            for a in articles:
                url = a.get("url", "")
                if not url:
                    continue
                content = (a.get("description") or a.get("title", "")) + \
                          f"\n\nReactions: {a.get('positive_reactions_count', 0)}"
                p = save(title=a.get("title", ""), content=content, url=url,
                         source="devto", category="news",
                         tags=["devto", tag, "tech-article"],
                         metadata={"tag": tag})
                if p:
                    saved += 1
        except Exception:
            pass
        time.sleep(0.3)
    return saved


# ── RSS feeds ─────────────────────────────────────────────────────────────────

RSS_FEEDS = {
    "github-blog":     "https://github.blog/feed/",
    "vercel-blog":     "https://vercel.com/blog/rss.xml",
    "cloudflare-blog": "https://blog.cloudflare.com/rss/",
    "openai-blog":     "https://openai.com/blog/rss/",
    "anthropic-blog":  "https://www.anthropic.com/blog.rss",
    "css-tricks":      "https://css-tricks.com/feed/",
    "smashing-mag":    "https://www.smashingmagazine.com/feed/",
    "aws-news":        "https://aws.amazon.com/about-aws/whats-new/recent/feed/",
    "netlify-blog":    "https://www.netlify.com/blog/index.xml",
    "stripe-blog":     "https://stripe.com/blog/feed.rss",
}

def fetch_rss() -> int:
    saved = 0
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for feed_name, feed_url in RSS_FEEDS.items():
        try:
            resp = httpx.get(feed_url, timeout=15, follow_redirects=True,
                             headers={"User-Agent": "Mozilla/5.0"})
            root = ET.fromstring(resp.text)
            entries = root.findall(".//item") or root.findall(".//atom:entry", ns)
            for entry in entries[:8]:
                def g(tag: str) -> str:
                    el = entry.find(tag) or entry.find(f"atom:{tag}", ns)
                    return (el.text or "").strip() if el is not None else ""
                title = g("title")
                link_el = entry.find("link") or entry.find("atom:link", ns)
                link = (link_el.text or link_el.get("href", "")).strip() if link_el is not None else ""
                desc = g("description") or g("summary") or g("content") or title
                if title and link:
                    p = save(title=title, content=desc, url=link,
                             source=feed_name, category="news",
                             tags=[feed_name, "rss", "tech-news"])
                    if p:
                        saved += 1
        except Exception:
            pass
        time.sleep(0.2)
    return saved


# ── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=== AGENT NEWS ===")
    n  = fetch_hn();    print(f"  HN: {n} new")
    d  = fetch_devto(); print(f"  Dev.to: {d} new")
    r  = fetch_rss();   print(f"  RSS: {r} new")
    print(f"✅ News: {n+d+r} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
