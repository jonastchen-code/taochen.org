"""Generate the static site for taochen.org.  Usage: python3 gen.py OUTDIR"""
import os, re, sys, json, html
sys.path.insert(0, os.path.dirname(__file__))
from data import PROGRAMS, PUBS, FT50, UTD24, NATURE_INDEX
from content import *  # page content

OUT = sys.argv[1]
SITE = "https://taochen.org"
UPDATED_ISO = "2026-11-14"
UPDATED = "14 November 2026"
NAME = "Tao (Jonas) Chen"
E = lambda s: html.escape(str(s), quote=True)

NAV = [("/", "Home"), ("/research/", "Research"), ("/teaching/", "Teaching"), ("/service/", "Service"),
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

def pub_item(p, show_prog=False):
    return f"""<li class="paper" data-search="{E((p['title']+' '+' '.join(p['authors'])+' '+p['journal']+' '+str(p['year'])+' '+p['finding']).lower())}">
<h3 class="paper-title"><a href="/research/{p['slug']}/">{E(p['display'])}</a></h3>
<p class="byline">{authors_html(p['authors'])}</p>
<p class="venue"><cite>{E(p['journal'])}</cite> {E(p['vol'])}{f"({E(p['issue'])})" if p['issue'] else ""}, {p['year']}</p>
<p class="finding">{E(p['finding'])}</p>
<p class="links"><a href="/research/{p['slug']}/">Abstract and citation</a> · <a href="https://doi.org/{p['doi']}">Publisher version <span class="vh">for {E(p['display'])}</span></a></p>
</li>"""

# ---------- Home ----------
def home():
    recent = PUBS[:5]
    stats = "".join(f'<div class="stat"><dt>{E(l)}</dt><dd>{E(v)}</dd></div>' for v, l in STATS)
    rec = "".join(f'<li><a href="/research/{p["slug"]}/">{E(p["display"])}</a> <span class="meta">— <cite>{E(p["journal"])}</cite>, {p["year"]}</span></li>' for p in recent)
    pos = "".join(f'<li><span class="yr">{E(y)}</span> {E(t)}</li>' for y, t in POSITIONS)
    edu = "".join(f'<li><span class="yr">{E(y)}</span> {E(t)}</li>' for y, t in EDUCATION)
    progs = "".join(f'<li><a href="/research/#{pid}">{E(name)}</a></li>' for pid, name, _ in PROGRAMS)
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
<p><a href="/research/">All {len(PUBS)} publications</a></p>
</section>
<div class="two">
<section aria-labelledby="h-pos"><h2 id="h-pos">Positions</h2><ul class="dated">{pos}</ul></section>
<section aria-labelledby="h-edu"><h2 id="h-edu">Education</h2><ul class="dated">{edu}</ul></section>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "dateModified": UPDATED_ISO,
          "mainEntity": PERSON}
    page("/", NAME, body, HOME_DESC, active="/", jsonld=ld)

# ---------- Research ----------
def research():
    secs = []
    for pid, name, desc in PROGRAMS:
        ps = [p for p in PUBS if p["prog"] == pid]
        secs.append(f"""<section class="program" id="{pid}" aria-labelledby="h-{pid}">
<h2 id="h-{pid}">{E(name)} <span class="count">({len(ps)})</span></h2>
<p class="program-desc">{E(desc)}</p>
<ol class="papers" reversed>{''.join(pub_item(p) for p in ps)}</ol>
</section>""")
    toc = " · ".join(f'<a href="#{pid}">{E(n)}</a>' for pid, n, _ in PROGRAMS)
    body = f"""<h1>Research</h1>
<p>{len(PUBS)} published articles, grouped into three research programs and listed newest first within each. Each title links to a page with the abstract and citation; “Publisher version” links to the article’s DOI.</p>
<p class="toc">{toc}</p>
<div class="search" hidden>
<label for="q">Search publications</label>
<input id="q" type="search" placeholder="Title, co-author, journal, year or topic" autocomplete="off">
<p id="q-status" class="meta" aria-live="polite"></p>
</div>
{''.join(secs)}
<p class="meta">Citation counts and working papers: <a href="{SCHOLAR}">Google Scholar</a>, <a href="{SSRN}">SSRN</a>. All entries as BibTeX: <a href="/research/publications.bib">publications.bib</a>.</p>
<script src="/assets/js/search.js" defer></script>"""
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Research — " + NAME, "url": SITE + "/research/",
          "author": {"@id": SITE + "/#person"},
          "hasPart": [{"@type": "ScholarlyArticle", "name": p["title"], "url": f"{SITE}/research/{p['slug']}/", "sameAs": "https://doi.org/" + p["doi"]} for p in PUBS]}
    page("/research/", "Research", body, f"Published research by {NAME} in sustainable finance; FinTech, AI, and finance; and investors, monitors and corporate policy.", active="/research/", jsonld=ld)
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
    ld = {"@context": "https://schema.org", "@type": "ScholarlyArticle", "headline": p["title"][:110], "name": p["title"],
          "author": [{"@type": "Person", "name": a, **({"@id": SITE + "/#person", "url": SITE + "/"} if a == "Tao Chen" else {})} for a in p["authors"]],
          "datePublished": f"{p['year']}-{p['month']:02d}", "sameAs": "https://doi.org/" + p["doi"],
          "identifier": {"@type": "PropertyValue", "propertyID": "DOI", "value": p["doi"]},
          "isPartOf": {"@type": "PublicationVolume", "volumeNumber": p["vol"], "isPartOf": {"@type": "Periodical", "name": p["journal"]}},
          "pagination": p["pages"], "about": prog, "url": f"{SITE}/research/{p['slug']}/"}
    if p["abstract"]: ld["abstract"] = p["abstract"]
    ab = f'<section aria-labelledby="h-ab"><h2 id="h-ab">Abstract</h2><p>{E(p["abstract"])}</p></section>' if p["abstract"] else \
         f'<section aria-labelledby="h-ab"><h2 id="h-ab">Abstract</h2><p>The abstract is available from the <a href="https://doi.org/{p["doi"]}">publisher</a>.</p></section>'
    apa = f'{", ".join(p["authors"])} ({p["year"]}). {p["title"]}. <cite>{E(p["journal"])}</cite>, {E(p["vol"])}{f"({E(p["issue"])})" if p["issue"] else ""}, {E(p["pages"])}. https://doi.org/{p["doi"]}'
    body = f"""<p class="crumb"><a href="/research/">Research</a> › <a href="/research/#{p['prog']}">{E(prog)}</a></p>
<article>
<h1 class="paper-h1">{E(p['display'])}</h1>
<p class="byline">{authors_html(p['authors'])}</p>
<p class="venue"><cite>{E(p['journal'])}</cite> {E(p['vol'])}{f"({E(p['issue'])})" if p['issue'] else ""}: {E(p['pages'])}, {p['year']}</p>
<p class="links"><a href="https://doi.org/{p['doi']}">Publisher version</a> (DOI {E(p['doi'])}) · <a href="https://scholar.google.com/scholar?q={E(html.escape(p['doi']))}">Google Scholar</a></p>
<section aria-labelledby="h-find"><h2 id="h-find">Main finding</h2><p>{E(p['finding'])}</p></section>
{ab}
<section aria-labelledby="h-cite"><h2 id="h-cite">Citation</h2>
<p class="cite">{apa}</p>
<details><summary>BibTeX</summary><pre><code>{E(bibtex(p))}</code></pre></details>
</section>
</article>"""
    page(f"/research/{p['slug']}/", p["display"], body, p["finding"], active="/research/", head_extra="\n".join(meta) + "\n", jsonld=ld)

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
    page("/404.html", "Page not found", '<h1>Page not found</h1><p>The page you asked for does not exist. Try the <a href="/">home page</a> or the <a href="/research/">list of publications</a>.</p>', "Page not found.")

# ---------- Machine-readable files ----------
def extras():
    urls = ["/", "/research/", "/teaching/", "/service/", "/awards/", "/talks/", "/media/"] + [f"/research/{p['slug']}/" for p in PUBS]
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
            lines.append(f"- [{p['title']}]({SITE}/research/{p['slug']}/) — {', '.join(p['authors'])}. {p['journal']} {p['vol']}, {p['year']}. DOI {p['doi']}. Finding: {p['finding']}")
    open(os.path.join(OUT, "llms.txt"), "w").write("\n".join(lines) + "\n")
    os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
    json.dump([{k: p[k] for k in ("title", "authors", "journal", "year", "vol", "issue", "pages", "doi", "prog", "finding", "abstract", "slug")} for p in PUBS],
              open(os.path.join(OUT, "data", "publications.json"), "w"), ensure_ascii=False, indent=1)

os.makedirs(OUT, exist_ok=True)
home(); research(); build_pages(); extras()
c = {"ft50": sum(p["journal"] in FT50 for p in PUBS), "utd24": sum(p["journal"] in UTD24 for p in PUBS), "ni": sum(p["journal"] in NATURE_INDEX for p in PUBS)}
print("built", len(PUBS), "papers", c)
