"""Generate the static site for taochen.org.  Usage: python3 gen.py OUTDIR"""
import os, re, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from data import PROGRAMS, PUBS, FT50, UTD24, NATURE_INDEX
from papers_extra import EXTRA, DRNTU_ABSTRACTS
from content import *  # page content

OUT = sys.argv[1]
SITE = "https://taochen.org"
UPDATED_ISO = "2026-11-14"
UPDATED = "14 November 2026"
NAME = "Tao (Jonas) Chen"
E = lambda s: html.escape(str(s), quote=True)

NAV = [("/", "Home"), ("/papers.html", "Research"), ("/teaching/", "Teaching"), ("/service/", "Service"),
       ("/awards/", "Awards"), ("/talks/", "Keynotes and Seminars"), ("/media/", "Media")]

# ---------- helpers ----------
SMALL = set("a an and as at but by for from in into nor of on or per the to via vs with".split())
def titlecase(t):
    out, first = [], True
    for w in re.split(r"(\s+)", t):
        if w.isspace() or not w:
            out.append(w); continue
        def cap(part, first):
            if any(c.isupper() for c in part[1:]) or not part[:1].isalpha():
                return part
            if not first and part.lower() in SMALL:
                return part.lower()
            return part[:1].upper() + part[1:]
        parts = re.split(r"([-‐–])", w)
        w2 = "".join(p if p in "-‐–" else cap(p, first and i == 0) for i, p in enumerate(parts))
        out.append(w2)
        first = w.endswith(":") or w.endswith("?")
    return "".join(out)

ABBR = {"Nature Climate Change":"ncc","Journal of Financial and Quantitative Analysis":"jfqa","World Development":"wd",
        "Journal of Financial Economics":"jfe","Accounting & Finance":"af","Management Science":"ms","PLOS ONE":"plos-one",
        "Journal of Corporate Finance":"jcf","Economics Letters":"el","Journal of Advertising":"ja","Journal of Banking & Finance":"jbf",
        "Journal of Management Information Systems":"jmis","Strategic Management Journal":"smj","Journal of Empirical Finance":"jef",
        "Review of Finance":"rof","Journal of Risk and Insurance":"jri"}
STOP = SMALL | {"does","do","how","what","evidence","s"}
for p in PUBS:
    p["display"] = titlecase(p["title"]).replace("‐", "-")
    words = [w for w in re.findall(r"[a-z0-9]+", p["title"].lower().replace("'", "").replace("u.s.", "us")) if w not in STOP]
    p["slug"] = "-".join(words[:4]) + f"-{ABBR[p['journal']]}-{p['year']}"
    p["first_family"] = p["authors"][0].split()[-1]
assert len({p["slug"] for p in PUBS}) == len(PUBS)
for p in PUBS:
    x = EXTRA[p["doi"]]
    p.update(one=x["one"], summary=x["summary"], pdf=x["pdf"], pdf_label=x.get("pdf_label", ""), pdf_note=x.get("pdf_note", ""))
    p["finding"] = p["one"]
    if not p["abstract"]: p["abstract"] = DRNTU_ABSTRACTS.get(p["doi"], "")
PUBS.sort(key=lambda p: (-p["year"], -p["month"]))

def cite_line(p):
    s = f"{p['journal']} {p['vol']}"
    if p["issue"]: s += f"({p['issue']})"
    return s + f": {p['pages']}"

def authors_html(a):
    names = [("<span class=\"me\">" + E(n) + "</span>") if n == "Tao Chen" else E(n) for n in a]
    if len(names) == 1: return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]

def bibtex(p):
    key = re.sub(r"[^a-z]", "", p["first_family"].lower()) + str(p["year"]) + re.findall(r"[a-z]+", p["slug"])[0]
    f = [("title", "{" + p["title"] + "}"), ("author", " and ".join(p["authors"])), ("journal", p["journal"].replace("&", "\\&")),
         ("year", p["year"]), ("volume", p["vol"])]
    if p["issue"]: f.append(("number", p["issue"]))
    f += [("pages", p["pages"].replace("–", "--")), ("doi", p["doi"])]
    return "@article{" + key + ",\n" + ",\n".join(f"  {k} = {{{v}}}" for k, v in f) + "\n}"

def nav(active):
    items = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{E(t)}</a></li>' for h, t in NAV)
    return f'<nav aria-label="Main"><ul>{items}</ul></nav>'

def page(path, title, body, desc, active=None, head_extra="", jsonld=None, page_title=None):
    full_title = f"{title} | {NAME}" if title != NAME else f"{NAME} | Nanyang Business School"
    url = SITE + path
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, indent=1)}</script>' if jsonld else ""
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(full_title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
{head_extra}{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
<div class="wrap">
<p class="site-name"><a href="/">{E(NAME)}</a></p>
{nav(active)}
</div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="site">
<div class="wrap">
<p><a href="mailto:jtchen@ntu.edu.sg">jtchen@ntu.edu.sg</a> · <a href="{SCHOLAR}">Google Scholar</a> · <a href="{SSRN}">SSRN</a> · <a href="{ORCID_URL}">ORCID</a> · <a href="{NTU_PAGE}">NTU page</a></p>
<p class="meta">Nanyang Business School, Nanyang Technological University, Singapore. Last updated {UPDATED}.</p>
</div>
</footer>
</body>
</html>
"""
    fp = os.path.join(OUT, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(doc)

PAPERS = "/papers.html"

def pdf_link(p, cls=""):
    if p["pdf"]:
        return f'<a href="{E(p["pdf"])}"{cls}>PDF<span class="vh"> of {E(p["display"])}</span></a> <span class="meta">({E(p["pdf_label"])})</span>'
    return f'<span class="meta">PDF not yet publicly available. {E(p["pdf_note"])}</span>'

def status(p):
    s = f"Published in <cite>{E(p['journal'])}</cite> {E(p['vol'])}"
    if p["issue"]: s += f"({E(p['issue'])})"
    return s + f": {E(p['pages'])}"

def pub_item(p):
    text = (p['title']+' '+' '.join(p['authors'])+' '+p['journal']+' '+str(p['year'])+' '+p['one']).lower()
    return f"""<li class="paper" data-search="{E(text)}">
<h3 class="paper-title"><a href="/research/{p['slug']}/">{E(p['display'])}</a></h3>
<p class="byline">{authors_html(p['authors'])}</p>
<p class="venue"><span class="year">{p['year']}</span> · {status(p)}</p>
<p class="finding"><span class="label">In one sentence:</span> {E(p['one'])}</p>
<p class="links"><a href="/research/{p['slug']}/">Paper page<span class="vh">: {E(p['display'])}</span></a> · {pdf_link(p)}</p>
</li>"""

# ---------- Home ----------
def home():
    # Nature Climate Change paper listed first (Jonas, 14 Nov 2026), then newest.
    recent = sorted(PUBS, key=lambda p: p["journal"] != "Nature Climate Change")[:5]
    stats = "".join(f'<div class="stat"><dt>{E(l)}</dt><dd>{E(v)}</dd></div>' for v, l in STATS)
    rec = "".join(f'<li><a href="/research/{p["slug"]}/">{E(p["display"])}</a> <span class="meta">— <cite>{E(p["journal"])}</cite>, {p["year"]}</span></li>' for p in recent)
    pos = "".join(f'<li><span class="yr">{E(y)}</span> {E(t)}</li>' for y, t in POSITIONS)
    edu = "".join(f'<li><span class="yr">{E(y)}</span> {E(t)}</li>' for y, t in EDUCATION)
    progs = "".join(f'<li><a href="{PAPERS}#{pid}">{E(name)}</a></li>' for pid, name, _ in PROGRAMS)
    body = f"""<div class="intro">
<h1>{E(NAME)}</h1>
<p class="role">Provost’s Chair Professor in Finance<br>Nanyang Business School, Nanyang Technological University, Singapore</p>
{HOME_INTRO}
<p class="contact"><a href="mailto:jtchen@ntu.edu.sg">jtchen@ntu.edu.sg</a> · ABS-06-106, 91 Nanyang Avenue, Singapore 639956</p>
<p class="contact"><a href="{SCHOLAR}">Google Scholar</a> · <a href="{SSRN}">SSRN</a> · <a href="{ORCID_URL}">ORCID</a> · <a href="{NTU_PAGE}">NTU page</a></p>
</div>
<section aria-labelledby="h-record">
<h2 id="h-record">Research record</h2>
<dl class="stats">{stats}</dl>
<p class="meta">{STATS_NOTE}</p>
</section>
<section aria-labelledby="h-programs">
<h2 id="h-programs">Research programs</h2>
<ul class="plain">{progs}</ul>
</section>
<section aria-labelledby="h-recent">
<h2 id="h-recent">Recent publications</h2>
<ul class="recent">{rec}</ul>
<p><a href="{PAPERS}">All {len(PUBS)} papers</a></p>
</section>
<div class="two">
<section aria-labelledby="h-pos"><h2 id="h-pos">Positions</h2><ul class="dated">{pos}</ul></section>
<section aria-labelledby="h-edu"><h2 id="h-edu">Education</h2><ul class="dated">{edu}</ul></section>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "dateModified": UPDATED_ISO,
          "mainEntity": PERSON}
    page("/", NAME, body, HOME_DESC, active="/", jsonld=ld)

# ---------- Papers ----------
def research():
    secs = []
    for pid, name, desc in PROGRAMS:
        ps = [p for p in PUBS if p["prog"] == pid]
        secs.append(f"""<section class="program" id="{pid}" aria-labelledby="h-{pid}">
<h2 id="h-{pid}">{E(name)} <span class="count">({len(ps)})</span></h2>
<p class="program-desc">{E(desc)}</p>
<ol class="papers">{''.join(pub_item(p) for p in ps)}</ol>
</section>""")
    toc = " · ".join(f'<a href="#{pid}">{E(n)}</a>' for pid, n, _ in PROGRAMS)
    body = f"""<h1>Research papers</h1>
<p>{len(PUBS)} published articles, grouped into three research programs and listed newest first within each. Each entry links to a paper page with a summary and citation, and to a freely available PDF where one exists.</p>
<p class="toc">{toc}</p>
<div class="search" hidden>
<label for="q">Search papers</label>
<input id="q" type="search" placeholder="Title, co-author, journal, year or topic" autocomplete="off">
<p id="q-status" class="meta" aria-live="polite"></p>
</div>
{''.join(secs)}
<p class="meta">Citation counts: <a href="{SCHOLAR}">Google Scholar</a>. Working papers: <a href="{SSRN}">SSRN</a>. All entries as BibTeX: <a href="/research/publications.bib">publications.bib</a>.</p>
<script src="/assets/js/search.js" defer></script>"""
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Research papers — " + NAME, "url": SITE + PAPERS,
          "author": {"@id": SITE + "/#person"},
          "hasPart": [{"@type": "ScholarlyArticle", "name": p["title"], "url": f"{SITE}/research/{p['slug']}/", "sameAs": "https://doi.org/" + p["doi"]} for p in PUBS]}
    page(PAPERS, "Research papers", body, f"Published research by {NAME} in sustainable finance; FinTech, AI, and finance; and investors, monitors and corporate policy.", active=PAPERS, jsonld=ld)
    # old address /research/ forwards to the papers page
    os.makedirs(os.path.join(OUT, "research"), exist_ok=True)
    open(os.path.join(OUT, "research", "index.html"), "w").write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Research papers</title><link rel="canonical" href="{SITE}{PAPERS}"><meta http-equiv="refresh" content="0; url={PAPERS}"><meta name="robots" content="noindex"></head><body><p>This page has moved to <a href="{PAPERS}">Research papers</a>.</p></body></html>\n')
    for p in PUBS:
        paper_page(p)
    open(os.path.join(OUT, "research", "publications.bib"), "w").write("\n\n".join(bibtex(p) for p in PUBS) + "\n")

def paper_page(p):
    prog = next(n for pid, n, _ in PROGRAMS if pid == p["prog"])
    meta = [f'<meta name="citation_title" content="{E(p["title"])}">']
    meta += [f'<meta name="citation_author" content="{E(a)}">' for a in p["authors"]]
    meta += [f'<meta name="citation_publication_date" content="{p["year"]}/{p["month"]:02d}">',
             f'<meta name="citation_journal_title" content="{E(p["journal"])}">',
             f'<meta name="citation_volume" content="{E(p["vol"])}">']
    if p["issue"]: meta.append(f'<meta name="citation_issue" content="{E(p["issue"])}">')
    pg = p["pages"].split("–")
    meta.append(f'<meta name="citation_firstpage" content="{E(pg[0])}">')
    if len(pg) > 1: meta.append(f'<meta name="citation_lastpage" content="{E(pg[1])}">')
    meta.append(f'<meta name="citation_doi" content="{E(p["doi"])}">')
    if p["abstract"]: meta.append(f'<meta name="citation_abstract" content="{E(p["abstract"])}">')
    if p["pdf"] and p["pdf"].startswith("/"): meta.append(f'<meta name="citation_pdf_url" content="{SITE}{p["pdf"]}">')
    ld = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "headline": p["title"][:110], "name": p["title"],
          "author": [{"@type": "Person", "name": a, **({"@id": SITE + "/#person", "url": SITE + "/"} if a == "Tao Chen" else {})} for a in p["authors"]],
          "datePublished": f"{p['year']}-{p['month']:02d}", "sameAs": "https://doi.org/" + p["doi"],
          "identifier": {"@type": "PropertyValue", "propertyID": "DOI", "value": p["doi"]},
          "isPartOf": {"@type": "PublicationVolume", "volumeNumber": p["vol"], "isPartOf": {"@type": "Periodical", "name": p["journal"]}},
          "pagination": p["pages"], "about": prog, "url": f"{SITE}/research/{p['slug']}/", "description": p["one"]}
    if p["abstract"]: ld["abstract"] = p["abstract"]
    if p["pdf"]: ld["encoding"] = {"@type": "MediaObject", "encodingFormat": "application/pdf", "contentUrl": (SITE + p["pdf"]) if p["pdf"].startswith("/") else p["pdf"]}
    ab = f'<details><summary>Abstract as published</summary><p>{E(p["abstract"])}</p></details>' if p["abstract"] else ""
    apa = f'{E(", ".join(p["authors"]))} ({p["year"]}). {E(p["title"])}. <cite>{E(p["journal"])}</cite>, {E(p["vol"])}{f"({E(p["issue"])})" if p["issue"] else ""}, {E(p["pages"])}. <a href="https://doi.org/{p["doi"]}">https://doi.org/{p["doi"]}</a>'
    back = f'<a href="{PAPERS}#{p["prog"]}">{E(prog)}</a>'
    body = f"""<p class="crumb"><a href="{PAPERS}">Research papers</a> › {back}</p>
<article>
<h1 class="paper-h1">{E(p['display'])}</h1>
<p class="byline">{authors_html(p['authors'])}</p>
<p class="venue"><span class="year">{p['year']}</span> · {status(p)} · DOI <a href="https://doi.org/{p['doi']}">{E(p['doi'])}</a></p>
<p class="pdf">{pdf_link(p)}</p>
<section aria-labelledby="h-one"><h2 id="h-one">In one sentence</h2><p>{E(p['one'])}</p></section>
<section aria-labelledby="h-sum"><h2 id="h-sum">Summary</h2><p>{E(p['summary'])}</p>{ab}</section>
<section aria-labelledby="h-cite"><h2 id="h-cite">Citation</h2>
<p class="cite">{apa}</p>
<details><summary>BibTeX</summary><pre><code>{E(bibtex(p))}</code></pre></details>
</section>
</article>
<nav class="backnav" aria-label="Back"><p>← More in {back} · <a href="{PAPERS}">All research papers</a></p></nav>"""
    page(f"/research/{p['slug']}/", p["display"], body, p["one"], active=PAPERS, head_extra="\n".join(meta) + "\n", jsonld=ld)

# ---------- Simple pages ----------
def simple(path, title, body, desc):
    page(path, title, f"<h1>{E(title)}</h1>\n{body}", desc, active=path)

def dated(rows):
    return '<ul class="dated">' + "".join(f'<li><span class="yr">{E(y)}</span> {t}</li>' for y, t in rows) + "</ul>"

def build_pages():
    simple("/teaching/", "Teaching", TEACHING_HTML(dated), f"Courses taught by {NAME} at Nanyang Business School, and doctoral advising.")
    simple("/service/", "Service", SERVICE_HTML(dated), f"Editorial, professional and university service of {NAME}.")
    simple("/awards/", "Awards", AWARDS_HTML(dated), f"Research, teaching and service awards received by {NAME}.")
    simple("/talks/", "Keynotes and Seminars", TALKS_HTML(dated), f"Keynote speeches and invited seminars given by {NAME}.")
    simple("/media/", "Media", MEDIA_HTML(dated), f"Media interviews, commentary and press coverage of research by {NAME}.")
    page("/404.html", "Page not found", '<h1>Page not found</h1><p>The page you asked for does not exist. Try the <a href="/">home page</a> or the <a href="/papers.html">list of research papers</a>.</p>', "Page not found.")

# ---------- Machine-readable files ----------
def extras():
    urls = ["/", "/papers.html", "/teaching/", "/service/", "/awards/", "/talks/", "/media/"] + [f"/research/{p['slug']}/" for p in PUBS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{UPDATED_ISO}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    lines = [f"# {NAME}", "", f"> {HOME_DESC}", "",
             "Provost's Chair Professor in Finance, Nanyang Business School, Nanyang Technological University (NTU), Singapore. Email: jtchen@ntu.edu.sg.",
             "", "## Pages", ""]
    lines += [f"- [{t}]({SITE}{h})" for h, t in NAV]
    lines += ["", "## Profiles", "", "- Google Scholar: " + SCHOLAR.replace("&amp;", "&"), f"- SSRN: {SSRN}", f"- ORCID: {ORCID_URL}", f"- NTU page: {NTU_PAGE}"]
    for pid, name, desc in PROGRAMS:
        lines += ["", f"## Publications — {name}", "", desc, ""]
        for p in [p for p in PUBS if p["prog"] == pid]:
            lines.append(f"- [{p['title']}]({SITE}/research/{p['slug']}/) — {', '.join(p['authors'])}. {p['journal']} {p['vol']}, {p['year']}. DOI {p['doi']}. In one sentence: {p['one']}" + (f" PDF: {p['pdf'] if p['pdf'].startswith('http') else SITE + p['pdf']}" if p['pdf'] else ""))
    open(os.path.join(OUT, "llms.txt"), "w").write("\n".join(lines) + "\n")
    os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
    json.dump([{k: p[k] for k in ("title", "authors", "journal", "year", "vol", "issue", "pages", "doi", "prog", "one", "summary", "pdf", "pdf_label", "abstract", "slug")} for p in PUBS],
              open(os.path.join(OUT, "data", "publications.json"), "w"), ensure_ascii=False, indent=1)

os.makedirs(OUT, exist_ok=True)
home(); research(); build_pages(); extras()
c = {"ft50": sum(p["journal"] in FT50 for p in PUBS), "utd24": sum(p["journal"] in UTD24 for p in PUBS), "ni": sum(p["journal"] in NATURE_INDEX for p in PUBS)}
print("built", len(PUBS), "papers", c)
