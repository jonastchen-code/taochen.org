# taochen.org

Academic homepage of Tao (Jonas) Chen, Nanyang Business School, NTU. Served by GitHub Pages from the `main` branch (root folder) at https://taochen.org.

## Layout

```
/                         Home (index.html)
/research/                Publications by research program, with search
/research/<paper>/        One page per article: finding, abstract, citation, BibTeX, Google Scholar citation_* tags
/research/publications.bib  All articles as BibTeX
/teaching/  /service/  /awards/  /talks/  /media/
/assets/css/style.css     Shared stylesheet (light and dark)
/assets/js/search.js      Publication search (the list works without JavaScript)
/assets/img/favicon.svg
/data/publications.json   Machine-readable publication list
/papers/                  (optional) author accepted manuscripts, if posted later
sitemap.xml  robots.txt  llms.txt  404.html  CNAME  .nojekyll
```

The pages are plain static HTML; edit them directly, or regenerate them from the publication data.

## Updating

Publication data is in `tools/data.py` and page text in `tools/content.py`. To rebuild the pages, run `python3 tools/gen.py .` from the repository root.
