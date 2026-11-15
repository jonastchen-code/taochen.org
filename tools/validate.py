"""Check that every paper page carries the expected metadata. Usage: python3 tools/validate.py [report.md]"""
import os, re, sys, json, html, glob
sys.path.insert(0, os.path.dirname(__file__))
from html.parser import HTMLParser
from data import PUBS
from papers_extra import EXTRA
SITE = "https://taochen.org"
U = html.unescape

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.meta = []; s.links = []; s.title = ""; s._t = False; s.ld = []; s._ld = False; s.a = []; s._a = None
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag == "meta": s.meta.append(a)
        if tag == "link": s.links.append(a)
        if tag == "title": s._t = True
        if tag == "script" and a.get("type") == "application/ld+json": s._ld = True; s.ld.append("")
        if tag == "a": s._a = [a.get("href", ""), ""]
    def handle_endtag(s, tag):
        if tag == "title": s._t = False
        if tag == "script": s._ld = False
        if tag == "a" and s._a: s.a.append(s._a); s._a = None
    def handle_data(s, d):
        if s._t: s.title += d
        if s._ld: s.ld[-1] += d
        if s._a is not None: s._a[1] += d
def parse(f):
    p = P(); p.feed(open(f).read()); return p
def m(p, key, attr="name"):
    return [x.get("content", "") for x in p.meta if x.get(attr) == key]

slug_of = {}
for f in glob.glob("research/*/index.html"):
    d = re.search(r'citation_doi" content="([^"]+)', open(f).read()).group(1)
    slug_of[U(d)] = f.split("/")[1]

rows, fails, titles = [], [], {}
for doi, x in EXTRA.items():
    pub = next(q for q in PUBS if q["doi"] == doi)
    slug = slug_of[doi]; f = f"research/{slug}/index.html"; src = open(f).read(); p = parse(f)
    url = f"{SITE}/research/{slug}/"
    exp_pdf = (SITE + x["pdf"]) if (x["pdf"] or "").startswith("/") else x["pdf"]
    ld = [json.loads(j) for j in p.ld]; art = next((j for j in ld if j.get("@type") == "ScholarlyArticle"), {})
    c = {}
    c["title"] = bool(p.title.strip()); titles.setdefault(p.title, []).append(slug)
    c["description"] = bool(m(p, "description") and m(p, "description")[0].strip())
    c["canonical"] = [l["href"] for l in p.links if l.get("rel") == "canonical"] == [url]
    c["og:title"] = bool(m(p, "og:title", "property")); c["og:description"] = bool(m(p, "og:description", "property"))
    c["og:url"] = m(p, "og:url", "property") == [url]; c["og:type"] = m(p, "og:type", "property") == ["article"]
    c["citation_title"] = [U(v) for v in m(p, "citation_title")] == [pub["title"]]
    c["citation_author"] = [U(v) for v in m(p, "citation_author")] == pub["authors"]
    c["citation_publication_date"] = m(p, "citation_publication_date") == [f"{pub['year']}/{pub['month']:02d}"]
    c["citation_journal_title"] = [U(v) for v in m(p, "citation_journal_title")] == [pub["journal"]]
    c["citation_doi"] = m(p, "citation_doi") == [doi]
    c["citation_pdf_url"] = ([U(v) for v in m(p, "citation_pdf_url")] == [exp_pdf]) if exp_pdf else (m(p, "citation_pdf_url") == [])
    c["JSON-LD ScholarlyArticle"] = bool(art)
    c["ld:name"] = art.get("name") == pub["title"]
    c["ld:authors"] = [a["name"] for a in art.get("author", [])] == pub["authors"]
    c["ld:date"] = art.get("datePublished") == f"{pub['year']}-{pub['month']:02d}"
    c["ld:url"] = art.get("url") == url
    c["ld:pdf"] = (art.get("encoding", {}).get("contentUrl") == exp_pdf) if exp_pdf else ("encoding" not in art)
    c["ld:keywords"] = len(art.get("keywords", [])) >= 3
    c["ld:abstract=summary"] = art.get("abstract") == x["summary"]
    # visible content present in raw HTML (no JavaScript needed)
    h1 = U(re.search(r'<h1 class="paper-h1">([^<]+)</h1>', src).group(1)) if 'paper-h1' in src else ""
    c["HTML: title"] = bool(h1) and h1.lower().replace("-", "‐") .replace("‐", "-") == pub["title"].lower().replace("‐", "-") and p.title.startswith(h1)
    c["HTML: authors"] = all(html.escape(a) in src for a in pub["authors"])
    c["HTML: summary"] = html.escape(x["summary"], quote=True) in src
    c["HTML: PDF link"] = (f'href="{html.escape(x["pdf"], quote=True)}"' in src) if x["pdf"] else ("PDF not yet publicly available" in src)
    c["links: program + papers page"] = any(h == f"/papers.html#{pub['prog']}" for h, _ in p.a) and any(h == "/papers.html" for h, _ in p.a)
    c["links: descriptive text"] = not any(t.strip().lower() in ("here", "click here", "link", "more") for _, t in p.a)
    # card on papers.html
    cards = re.findall(r'<li class="paper".*?</li>', open("papers.html").read(), re.S)
    card = next((k for k in cards if f'href="/research/{slug}/"' in k), "")
    c["papers.html card → page"] = bool(card) and card.count(f'href="/research/{slug}/"') == 2
    c["papers.html card → PDF"] = (f'href="{html.escape(x["pdf"], quote=True)}"' in card) if x["pdf"] else ("PDF not yet publicly available" in card)
    # four-layer sync (Jonas, 2026-11-15): 1 card sentence, 2 page summary, 3 hidden search text, 4 machine metadata
    one, summ = x["one"], x["summary"]
    c["L1 card sentence = source"] = f'<span class="label">In one sentence:</span> {html.escape(one, quote=True)}</p>' in card
    c["L1 page sentence = source"] = f'<h2 id="h-one">In one sentence</h2><p>{html.escape(one, quote=True)}</p>' in src
    c["L2 page summary = source"] = f'<h2 id="h-sum">Summary</h2><p>{html.escape(summ, quote=True)}</p>' in src
    ds = re.search(r'data-search="([^"]*)"', card)
    c["L3 search text has sentence"] = bool(ds) and U(ds.group(1)) == U(ds.group(1)) and html.escape(one.lower(), quote=True) in ds.group(1)
    c["L4 meta+og description = sentence"] = [U(v) for v in m(p, "description")] == [one] and [U(v) for v in m(p, "og:description", "property")] == [one]
    c["L4 ld:description = sentence"] = art.get("description") == one
    c["L4 citation_abstract present (published abstract, by design)"] = bool(m(p, "citation_abstract"))
    bad = [k for k, v in c.items() if not v]
    if bad: fails.append((slug, bad))
    rows.append((slug, pub["year"], "yes" if exp_pdf else "none public", len(c) - len(bad), len(c), bad))

dup = {t: s for t, s in titles.items() if len(s) > 1}
# site-wide checks
site = []
pages = [f for f in glob.glob("**/*.html", recursive=True) if f not in ("404.html", "research/index.html")]
canon = {}
for f in pages:
    p = parse(f); cs = [l["href"] for l in p.links if l.get("rel") == "canonical"]
    exp = SITE + "/" + (f[:-10] if f.endswith("index.html") else f)
    canon[f] = cs == [exp]
site.append(("Canonical URL on every page matches its address", all(canon.values()), [f for f, ok in canon.items() if not ok]))
sm = re.findall(r"<loc>([^<]+)</loc>", open("sitemap.xml").read())
smiss = [u for u in sm if not os.path.exists((u[len(SITE)+1:] or "index.html") + ("index.html" if u.endswith("/") and u != SITE + "/" else ""))]
site.append((f"sitemap.xml lists {len(sm)} URLs, all exist", not smiss, smiss))
canon_urls = {SITE + "/" + (f[:-10] if f.endswith("index.html") else f) for f in pages}
site.append(("sitemap.xml covers every canonical page", canon_urls <= set(sm), sorted(canon_urls - set(sm))))
site.append(("robots.txt allows crawling and names the sitemap", "Allow: /" in open("robots.txt").read() and "Sitemap:" in open("robots.txt").read(), []))
llms = open("llms.txt").read()
site.append(("llms.txt lists all 24 papers with summaries", llms.count("- Summary:") == len(EXTRA), []))
home = parse("index.html"); g = json.loads(home.ld[0]).get("@graph", [])
site.append(("Home page has WebSite, ProfilePage and Person JSON-LD", {"WebSite", "ProfilePage", "Person"} <= {x.get("@type") for x in g}, []))
site.append(("Paper page titles are unique", not dup, list(dup)))
internal_bad = []
for f in glob.glob("**/*.html", recursive=True):
    for h in re.findall(r'href="(/[^"#]*)', open(f).read()):
        q = h.lstrip("/"); q = os.path.join(q, "index.html") if (q == "" or q.endswith("/")) else q
        if not os.path.exists(q): internal_bad.append((f, h))
site.append(("No broken internal links", not internal_bad, internal_bad))

out = ["# Metadata validation report", "", f"Run on the built site: {len(rows)} paper pages, {len(pages)} indexable pages.", "",
       "## Paper pages", "", "| Paper page | Year | Public PDF | Checks passed | Failed |", "|---|---|---|---|---|"]
for slug, y, pdf, ok, n, bad in sorted(rows, key=lambda r: (-r[1], r[0])):
    out.append(f"| /research/{slug}/ | {y} | {pdf} | {ok}/{n} | {', '.join(bad) or '—'} |")
out += ["", "Checks on each paper page: " + ", ".join(c.keys()) + ".", "",
        "For papers with no public PDF, the check passes when the page and card say so and no citation_pdf_url or PDF entry is emitted.", "",
        "## Site-wide", "", "| Check | Result |", "|---|---|"]
for name, ok, detail in site:
    out.append(f"| {name} | {'pass' if ok else 'FAIL: ' + str(detail)[:200]} |")
rep = "\n".join(out) + "\n"
if len(sys.argv) > 1: open(sys.argv[1], "w").write(rep)
print(rep)
print("FAILURES:", fails, [s for s in site if not s[1]])
