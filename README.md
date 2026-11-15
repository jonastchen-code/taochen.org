# taochen.org

Academic homepage of Tao (Jonas) Chen, Nanyang Business School, NTU. Served by GitHub Pages from the `main` branch (root folder) at https://taochen.org.

## Layout

```
/                         Home (index.html)
/papers.html               Research papers by program, with search (the old /research/ address forwards here)
/research/<paper>/        One page per article: in one sentence, summary, PDF link, citation, BibTeX, Google Scholar tags
/papers/                  Open-access PDFs hosted on the site
/research/publications.bib  All articles as BibTeX
/teaching/  /service/  /awards/  /talks/  /media/
/assets/css/style.css     Shared stylesheet (light and dark)
/assets/js/search.js      Publication search (the list works without JavaScript)
/assets/img/favicon.svg
/data/publications.json   Machine-readable publication list
sitemap.xml  robots.txt  llms.txt  404.html  CNAME  .nojekyll
```

To check metadata on every paper page, run `python3 tools/validate.py`.

The pages are plain static HTML; edit them directly, or regenerate them from the publication data.

## Updating

Publication data is in `tools/data.py`, PDF links and summaries in `tools/papers_extra.py`, and page text in `tools/content.py`. To rebuild the pages, run `python3 tools/gen.py .` from the repository root.
