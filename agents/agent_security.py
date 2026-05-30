"""
AGENTE 10 — Cybersecurity → corpus/security/
  · Krebs on Security
  · The Hacker News (security)
  · Schneier on Security
  · Dark Reading
  · NIST NVD CVE feed
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import httpx
from xml.etree import ElementTree as ET
import re
from core.graphify_writer import save

FEEDS = {
    "krebs":         "https://krebsonsecurity.com/feed/",
    "hacker-news-sec": "https://feeds.feedburner.com/TheHackersNews",
    "schneier":      "https://www.schneier.com/feed/atom/",
    "dark-reading":  "https://www.darkreading.com/rss.xml",
    "bleeping-comp": "https://www.bleepingcomputer.com/feed/",
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
        # RSS 2.0
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
                        source="security",
                        category="security",
                        tags=["security", "cybersecurity", "infosec", name],
                    )
                    if p:
                        saved += 1
        else:
            # Atom
            for entry in root.findall("atom:entry", ATOM_NS)[:8]:
                title   = (entry.findtext("atom:title", namespaces=ATOM_NS) or "").strip()
                link_el = entry.find("atom:link", ATOM_NS)
                link    = (link_el.get("href", "") if link_el is not None else "").strip()
                desc    = re.sub(r"<[^>]+>", " ",
                                 entry.findtext("atom:summary", namespaces=ATOM_NS) or "")[:2000].strip()
                if title and link:
                    p = save(
                        title=f"[{name}] {title}",
                        content=f"{title}\n\n{desc}",
                        url=link,
                        source="security",
                        category="security",
                        tags=["security", "cybersecurity", "infosec", name],
                    )
                    if p:
                        saved += 1
    except Exception as e:
        print(f"  {name}: {e}")
    return saved


def fetch_nvd_cves() -> int:
    """Fetch recent CVEs from NVD API (no auth needed, 50/30s rate limit)."""
    saved = 0
    try:
        resp = httpx.get(
            "https://services.nvd.nist.gov/rest/json/cves/2.0",
            params={"resultsPerPage": "10"},
            timeout=20, headers=HEADERS,
        )
        if resp.status_code != 200:
            print(f"  nvd-cve: HTTP {resp.status_code}")
            return 0
        data = resp.json()
        for vuln in data.get("vulnerabilities", [])[:10]:
            cve = vuln.get("cve", {})
            cve_id = cve.get("id", "")
            descs  = cve.get("descriptions", [])
            desc_en = next((d["value"] for d in descs if d.get("lang") == "en"), "")
            metrics = cve.get("metrics", {})
            score = "N/A"
            for k in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
                if k in metrics and metrics[k]:
                    score = str(metrics[k][0].get("cvssData", {}).get("baseScore", "N/A"))
                    break
            if cve_id:
                p = save(
                    title=f"[CVE] {cve_id}",
                    content=f"**CVSS Score:** {score}\n\n{desc_en[:2000]}",
                    url=f"https://nvd.nist.gov/vuln/detail/{cve_id}",
                    source="security",
                    category="security",
                    tags=["cve", "vulnerability", "nvd", "security"],
                    metadata={"cvss_score": score},
                )
                if p:
                    saved += 1
    except Exception as e:
        print(f"  nvd-cve: {e}")
    return saved


def run():
    print("=== AGENT SECURITY ===")
    total = 0
    for name, url in FEEDS.items():
        n = _parse_feed(name, url)
        print(f"  {name}: {n} new")
        total += n
        time.sleep(0.3)
    cve = fetch_nvd_cves(); print(f"  NVD CVEs: {cve} new")
    total += cve
    print(f"✅ Security: {total} new markdown files written to corpus/")


if __name__ == "__main__":
    run()
