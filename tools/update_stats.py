"""Update the Google Scholar citation and h-index tiles.

Usage: python3 tools/update_stats.py CITATIONS HINDEX "15 November 2026"
Rewrites STATS / STATS_NOTE in tools/content.py; then run gen.py and validate.py.
Prints "unchanged" if the numbers and date already match.
"""
import re, sys
cites, h, date = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
p = "tools/content.py"; s = open(p).read()
new = re.sub(r'\("[^"]*", "Citations"\)', f'("{cites:,}", "Citations")', s, count=1)
new = re.sub(r'\("\d+", "h-index"\)', f'("{h}", "h-index")', new, count=1)
new = re.sub(r"Citations and h-index from Google Scholar, [^.]*\.", f"Citations and h-index from Google Scholar, {date}.", new, count=1)
if new == s: print("unchanged"); sys.exit(0)
open(p, "w").write(new); print(f"updated: {cites:,} citations, h-index {h}, {date}")
