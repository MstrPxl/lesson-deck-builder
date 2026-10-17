#!/usr/bin/env python3
# build.py OUT.html — joins build/p*.html (+ zz_comments.html), keeps #total in sync,     (deck-tools 1.2)
# and counts every readable word per slide and per topic (data-sec); quiz slides (data-budget="skip") listed apart.
# Warns when a piece of markup it relies on is missing, instead of writing a deck that only looks right.
import re, sys, glob, os
from bs4 import BeautifulSoup
END = '<!-- ================= END SLIDES ================= -->'
parts = sorted(glob.glob('build/p*.html'))
if not parts: print('ERROR: no build/p*.html files in this folder'); sys.exit(1)
html = ''.join(open(p, encoding='utf-8').read() for p in parts)
warn = []
if os.path.exists('build/zz_comments.html'):
    if END in html: html = html.replace(END, END + '\n' + open('build/zz_comments.html', encoding='utf-8').read())
    else: warn.append('the END SLIDES comment is missing, so build/zz_comments.html was NOT inserted (deck comments lost)')
soup = BeautifulSoup(html, 'html.parser')          # real elements only: comments that mention <section> or <script> don't count
n_slides = len(soup.select('section.slide'))
if not n_slides: print('ERROR: no <section class="slide"> in the parts; the skill markup changed'); sys.exit(1)
if not re.search(r'<span id="total">\d+</span>', html): warn.append('no <span id="total">N</span>: the slide total was NOT synced')
html = re.sub(r'<span id="total">\d+</span>', f'<span id="total">{n_slides}</span>', html)
open(sys.argv[1], 'w', encoding='utf-8').write(html)
for tag in ('html', 'head', 'body'):
    if len(soup.find_all(tag)) != 1: warn.append(f'<{tag}> appears {len(soup.find_all(tag))} times (expected once): check the part files')
if not soup.find_all('script'): warn.append('no <script> element: the engine is missing')
W = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-\.]*"); tot = hid = 0; secs = {}; cur = ''; skip = 0
found = soup.select('section.slide')
for i, sec in enumerate(found, 1):
    if sec.get('data-sec'): cur = sec['data-sec']
    for t in sec.find_all(['script', 'style', 'svg']): t.decompose()
    h = ' '.join(q.get('data-why', '') for q in sec.select('[data-why]'))
    v, n = len(W.findall(sec.get_text(' '))), len(W.findall(h))
    title = (sec.find(['h1', 'h2']) or sec).get_text(' ').strip()[:44]
    if sec.get('data-budget') == 'skip':
        skip += v + n; print(f'{i:>2} quiz {v+n:>4}  {title}'); continue
    tot += v; hid += n
    secs[cur] = secs.get(cur, 0) + v + n
    print(f'{i:>2} vis {v:>4} fb {n:>3}  {title}')
if not cur: warn.append('no slide has data-sec: words per topic could not be counted')
print(' | '.join(f'{k} {v}' for k, v in secs.items()))
print(f'ALL {tot+hid} (outside budget: quiz {skip})  slides {n_slides}')
for w in warn: print('WARNING:', w)
sys.exit(1 if warn else 0)
