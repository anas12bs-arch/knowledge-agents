"""
AGENTE 4 — Social + Video + X/Twitter → corpus/social/
  · X/Twitter via Nitter RSS  (sin pagar API de Twitter)
  · YouTube RSS               (sin API key)
  · Reddit hot posts
  · Podcast RSS               (descripciones de episodios)
"""
from __future__ import annotations
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import re
import time
import httpx
from xml.etree import ElementTree as ET
from core.graphify_writer import save


# ── X / Twitter via Nitter RSS ────────────────────────────────────────────────
# Nitter = frontend open-source de Twitter. Sin auth, sin pagar.
# Fallback automático entre instancias si alguna cae.

NITTER_INSTANCES = [
    "https://nitter.poast.org",
    "https://nitter.privacydev.net",
    "https://lightbird.cc",
]

# Devs, creadores e instituciones tech influyentes
TWITTER_ACCOUNTS = [
    # Creadores de contenido
    "ThePrimeagen", "t3dotgg", "fireship_dev", "addyosmani", "swyx",
    "kentcdodds", "leeerob", "shadcn", "rauchg",
    # AI / research
    "karpathy", "ylecun", "sama", "AnthropicAI", "OpenAI",
    "GoogleDeepMind", "huggingface",
    # Tools / companies
    "vercel", "github", "supabase", "prisma", "tailwindcss",
    # Languages / runtimes
    "nodejs", "rustlang", "golang", "typescriptlang", "denoland",
    # Dev educators
    "cassidoo", "jlengstorf", "daKidFresh", "simonw", "jeresig",
]

def _nitter_rss(username: str) -> list[dict]:
    for base in NITTER_INSTANCES:
        try:
            resp = httpx.get(
                f"{base}/{username}/rss",
                timeout=12, follow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            if resp.status_code != 200:
                continue
            root = ET.fromstring(resp.text)
            items = []
            for item in root.findall(".//item")[:12]:
                title = (item.findtext("title") or "").strip()
                link  = (item.findtext("link") or "").strip()
                desc  = re.sub(r"<[^>]+>", " ", item.findtext("description") or "").strip()
                # normalise link to real twitter URL
                link = re.sub(r"https?://[^/]+/", "https://twitter.com/", link)
                if title and link:
                    items.append({"title": f"@{username}: {title[:120]}",
                                  "url": link, "content": desc or title})
            return items
        except Exception:
            continue
    return []

def fetch_twitter() -> int:
    saved = 0
    for account in TWITTER_ACCOUNTS:
        for item in _nitter_rss(account):
            p = save(
                title=item["title"], content=item["content"], url=item["url"],
                source="twitter", category="social",
                tags=["twitter", "social", account.lower(), "dev-opinion"],
            )
            if p:
                saved += 1
        time.sleep(0.4)
    return saved


# ── YouTube RSS (sin API key) ─────────────────────────────────────────────────

YT_CHANNELS = {
    "fireship":       "UCsBjURrPoezykLs9EqgamOA",
    "theo":           "UCbRP3c757lWg9M-U7TyEkXA",
    "primeagen":      "UC8ENHE5xdFSwx71WHd4a2jw",
    "traversy":       "UC29ju8bIPH5as8OGnQzwJyA",
    "kevin-powell":   "UCJZv4d5rbIKd4QHMPkcABCw",
    "jack-herrington": "UC6vRUjYqDuoUsYsku86Lrsw",
    "developedbyed":  "UCDyTyKGRpKaGFrLRmYWwbSQ",
    "leerob":         "UCnUYZLuoy1rq1aVMwx4aTzw",
    "codewithantonio":"UCYMkHO1cfFkKmcF_l8VnBiA",
    "syntax-fm":      "UCSIyB_I0ILZcK8EiVBJfpJg",
    "neetcode":       "UC3fONJjENbFiJALFMvzfmCQ",
}

YT_RSS = "https://www.youtube.com/feeds/videos.xml?channel_id={cid}"

def fetch_youtube() -> int:
    ns = {
        "atom":  "http://www.w3.org/2005/Atom",
        "media": "http://search.yahoo.com/mrss/",
    }
    saved = 0
    for name, cid in YT_CHANNELS.items():
        try:
            root = ET.fromstring(
                httpx.get(YT_RSS.format(cid=cid), timeout=15).text
            )
            for entry in root.findall("atom:entry", ns)[:6]:
                title    = entry.findtext("atom:title", namespaces=ns) or ""
                link_el  = entry.find("atom:link", ns)
                link     = (link_el.get("href", "") if link_el is not None else "").strip()
                mg       = entry.find("media:group", ns)
                desc     = ""
                if mg is not None:
                    de = mg.find("media:description", ns)
                    desc = (de.text or "")[:1800] if de is not None else ""
                p = save(
                    title=f"[{name}] {title}",
                    content=f"{title}\n\n{desc}",
                    url=link,
                    source="youtube",
                    category="video",
                    tags=["youtube", "video", "tutorial", name],
                )
                if p:
                    saved += 1
        except Exception as e:
            print(f"  youtube/{name}: {e}")
        time.sleep(0.3)
    return saved


# ── Reddit ─────────────────────────────────────────────────────────────────────

REDDIT_SUBS = [
    "programming", "MachineLearning", "webdev", "javascript",
    "Python", "rust", "golang", "devops", "AITools",
    "LocalLLaMA", "SideProject", "cscareerquestions", "ExperiencedDevs",
]

def fetch_reddit() -> int:
    saved = 0
    for sub in REDDIT_SUBS:
        try:
            posts = httpx.get(
                f"https://www.reddit.com/r/{sub}/hot.json",
                headers={"User-Agent": "KnowledgeBot/1.0"},
                params={"limit": 12},
                timeout=15,
            ).json().get("data", {}).get("children", [])
            for post in posts:
                p_data = post.get("data", {})
                if p_data.get("score", 0) < 30:
                    continue
                title    = p_data.get("title", "")
                selftext = p_data.get("selftext", "")[:2000]
                url      = f"https://reddit.com{p_data.get('permalink', '')}"
                content  = f"Score: {p_data.get('score',0)} | " \
                           f"r/{sub}\n\n{title}\n\n{selftext}"
                p = save(
                    title=f"r/{sub}: {title}",
                    content=content,
                    url=url,
                    source="reddit",
                    category="social",
                    tags=["reddit", sub.lower(), "discussion", "community"],
                    metadata={"subreddit": sub, "score": str(p_data.get("score", 0))},
                )
                if p:
                    saved += 1
        except Exception as e:
            print(f"  reddit/r/{sub}: {e}")
        time.sleep(0.5)
    return saved


# ── Podcast RSS ───────────────────────────────────────────────────────────────

PODCASTS = {
    "syntax-fm":          "https://feed.syntax.fm/rss",
    "changelog":          "https://changelog.com/podcast/feed",
    "js-party":           "https://changelog.com/jsparty/feed",
    "ship-it":            "https://changelog.com/shipit/feed",
    "lex-fridman":        "https://lexfridman.com/feed/podcast/",
    "software-engineering-daily": "https://softwareengineeringdaily.com/feed/podcast/",
    "tech-lead-journal":  "https://techleadjournal.dev/index.xml",
}

def fetch_podcasts() -> int:
    saved = 0
    for name, feed_url in PODCASTS.items():
        try:
            resp = httpx.get(feed_url, timeout=15, follow_redirects=True,
                             headers={"User-Agent": "Mozilla/5.0"})
            root = ET.fromstring(resp.text)
            for item in root.findall(".//item")[:5]:
                title = (item.findtext("title") or "").strip()
                link  = (item.findtext("link") or item.findtext("enclosure") or "").strip()
                desc  = re.sub(r"<[^>]+>", " ", item.findtext("description") or "")[:2000].strip()
                if title and desc:
                    p = save(
                        title=f"[{name}] {title}",
                        content=f"{title}\n\n{desc}",
                        url=link or feed_url,
                        source="podcast",
                        category="audio",
                        tags=["podcast", name, "tech-talk"],
                    )
                    if p:
                        saved += 1
        except Exception as e:
            print(f"  podcast/{name}: {e}")
        time.sleep(0.3)
    return saved


# ── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=== AGENT SOCIAL ===")
    tw = fetch_twitter();  print(f"  Twitter/X: {tw} new")
    yt = fetch_youtube();  print(f"  YouTube: {yt} new")
    rd = fetch_reddit();   print(f"  Reddit: {rd} new")
    pc = fetch_podcasts(); print(f"  Podcasts: {pc} new")
    print(f"✅ Social: {tw+yt+rd+pc} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
