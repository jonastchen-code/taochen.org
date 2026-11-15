"""Build the research word cloud images (Research page and Home).
Usage: python3 tools/word_cloud.py      (needs: pip install wordcloud numpy pillow)
Words come from the paper keywords in papers_extra.KEYWORDS. Method-only terms are dropped,
near-synonyms merged, and the three research programmes weighted up (Jonas's choices, 15 Nov 2026;
China kept small at his request). Shape: Robinson world-map outline, no frame line (Jonas, 15 Nov 2026). Re-run after adding papers."""
import os, sys, random
from collections import Counter
import numpy as np
from PIL import Image, ImageDraw
from wordcloud import WordCloud
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from papers_extra import KEYWORDS
ROOT = os.path.dirname(HERE); IMG = os.path.join(ROOT, "assets", "img")
FONT = os.path.join(HERE, "fonts", "SourceSerif4.ttf")

DROP = {'regression discontinuity','event study','quasi-natural experiment','new zealand','persuasion knowledge model',
 'uses and gratifications','uncanny valley','russell index reconstitution','u.s. manufacturing','alibaba','it industry','institutions'}
MERGE = {'analyst coverage':'financial analysts','forecast quality':'financial analysts','institutional ownership':'institutional investors',
 'corporate social responsibility':'ESG','esg':'ESG','tax aggressiveness':'tax avoidance','real earnings management':'earnings management',
 'ai-enabled advertising':'artificial intelligence','fintech credit':'FinTech','buy now, pay later':'FinTech','fintech':'FinTech',
 'patents':'innovation','permanent normal trade relations':'globalization','import competition':'globalization','u.s.-china trade':'globalization',
 'pollution':'environmental policy','corporate environmental policy':'environmental policy','corporate environmental performance':'environmental policy',
 'risk-taking incentives':'risk-taking','labor unions':'labor','unionization elections':'labor','minimum wages':'labor','labor market policy':'labor',
 'carbon credits':'carbon markets','voluntary carbon market':'carbon markets','china':'China','board structure':'corporate governance',
 'outside directors':'corporate governance'}
BOOST = {'sustainable finance':7,'FinTech':3,'artificial intelligence':2,'corporate governance':3,'ESG':3,'corporate finance':2}
FIXED = {'China':1}

def frequencies():
    c = Counter()
    for kws in KEYWORDS.values():
        seen = set()
        for k in kws:
            k = k.strip().lower()
            if k in DROP: continue
            k = MERGE.get(k, k)
            if k not in seen: seen.add(k); c[k] += 1
    for k, v in BOOST.items(): c[k] += v
    for k, v in FIXED.items(): c[k] = v
    return {k: v for k, v in c.items() if v > 0}

ROBINSON = [(1,0),(.9986,.062),(.9954,.124),(.99,.186),(.9822,.248),(.973,.31),(.96,.372),(.9427,.434),(.9216,.4958),
 (.8962,.5571),(.8679,.6176),(.835,.6769),(.7986,.7346),(.7597,.7903),(.7186,.8435),(.6732,.8936),(.6213,.9394),(.5722,.9761),(.5322,1)]
def outline(W, H, pad):
    cx, cy, sx, sy = W/2, H/2, W/2-pad, H/2-pad
    right = [(cx+sx*x, cy-sy*y) for x, y in reversed(ROBINSON)] + [(cx+sx*x, cy+sy*y) for x, y in ROBINSON]
    return right + [(2*cx-px, py) for px, py in reversed(right)]

THEMES = {  # big-word colour, small-word colours, outline colour
 "light": ("#1F3A5F", ["#2F5D8A", "#5C6370", "#1F3A5F", "#8A5A2B"], "#2F5D8A"),
 "dark":  ("#8FB3DE", ["#A9C4E4", "#A2A7B0", "#8FB3DE", "#D2AB82"], "#5F7FA6"),
}
def render(freq, W, H, out_w, path, theme, max_font, min_font, max_words, contour):
    big, small, line = THEMES[theme]
    pad = contour + 4
    mask = Image.new("L", (W, H), 255); ImageDraw.Draw(mask).polygon(outline(W, H, pad), fill=0)
    col = lambda word, font_size, **k: big if font_size > max_font * 0.3 else random.Random(word).choice(small)
    wc = WordCloud(width=W, height=H, mask=np.array(mask), mode="RGBA", background_color=None, font_path=FONT,
                   prefer_horizontal=0.9, relative_scaling=0.5, min_font_size=min_font, max_font_size=max_font,
                   margin=6, color_func=col, random_state=3, collocations=False, max_words=max_words,
                   contour_width=0)
    im = wc.generate_from_frequencies(freq).to_image()
    if contour: pts = outline(W, H, pad); ImageDraw.Draw(im).line(pts + pts[:1], fill=line, width=contour, joint="curve")
    im = im.resize((out_w, round(H * out_w / W)), Image.LANCZOS)
    im.quantize(32, method=Image.FASTOCTREE).save(path, optimize=True); print(path, im.size, os.path.getsize(path))

if __name__ == "__main__":
    f = frequencies()
    for t in THEMES:
        sfx = "" if t == "light" else "-dark"
        render(f, 2400, 1240, 1600, os.path.join(IMG, f"research-cloud{sfx}.png"), t, 200, 14, 200, 0)
        render(f, 1200, 620, 640, os.path.join(IMG, f"research-cloud-small{sfx}.png"), t, 150, 26, 22, 0)
