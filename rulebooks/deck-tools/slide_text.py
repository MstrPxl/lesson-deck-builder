#!/usr/bin/env python3
# slide_text.py DECK [OUT.txt] — every slide's readable text, as a student reads it, for the independent check   (deck-tools 1.4)
# Keeps figure labels, glossary, quiz feedback; marks exact slide wording «…» (class formal) and the deck's own
# framing [ours: …]. Leaves out HTML comments (the ledger), scripts, styles and SVG drawing code.
import sys, re
from bs4 import BeautifulSoup, Comment
if len(sys.argv) < 2: print('usage: slide_text.py DECK [OUT.txt]'); sys.exit(2)
soup = BeautifulSoup(open(sys.argv[1], encoding='utf-8').read(), 'html.parser')
for c in soup.find_all(string=lambda t: isinstance(t, Comment)): c.extract()
for w in soup.find_all('wbr'): w.unwrap()          # 1.4: a line-break hint is not a space (Student_<wbr>number)
soup = BeautifulSoup(str(soup), 'html.parser')    # re-parse so the text around a removed <wbr> joins
slides = soup.select('section.slide')
if not slides: print('COULD NOT CHECK: no section.slide in the deck'); sys.exit(2)
BLOCK = 'p,li,h1,h2,h3,h4,div,dt,dd,button,span.lf-pin,span.pill,span.chip,span.tag,td,th,figcaption'
out = []
for i, s in enumerate(slides, 1):
    for t in s.find_all(['script', 'style', 'svg']): t.decompose()
    for f in s.select('.formal'): f.insert_before('«'); f.insert_after('»')
    for o in s.select('.ours'): o.insert_before('[ours: '); o.insert_after(']')
    for b in s.select(BLOCK): b.insert_after('\n')
    for q in s.select('[data-why]'): q.append(f'\n(feedback: {q["data-why"]})\n')
    kind = 'QUIZ' if s.get('data-budget') == 'skip' else 'SLIDE'
    txt = re.sub(r'[ \t]+', ' ', s.get_text(' '))
    txt = '\n'.join(l.strip() for l in txt.splitlines() if l.strip())
    out.append(f'===== {kind} {i}' + (f' · topic: {s["data-sec"]}' if s.get('data-sec') else '') + f' =====\n{txt}\n')
text = '\n'.join(out)
if len(sys.argv) > 2: open(sys.argv[2], 'w', encoding='utf-8').write(text); print(f'{len(slides)} slides -> {sys.argv[2]}')
else: print(text)
