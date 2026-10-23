#!/usr/bin/env python3
# quiz_walk_x.py DECK [OUTDIR] [--phone]  — the rulebook's quiz_walk.py, plus walk branches for quiz kinds the   (deck-tools 1.4)
# rulebook's walk does not know yet. 1.4 adds "build" (Build the answer: tap word tiles in order; tiles with
# data-n are the answer, in order). --phone runs the walk in a 390x844 touch context (has_touch, is_mobile).
# Run from the folder that holds quiz_walk.py (setup_tools.sh copies it there). Exit 2 when a patch point is missing:
# quiz_walk.py changed; update the anchors below.
import sys, os
ELSE = '    else:\n        print("  ! unknown data-type", t); return None'
EXTRA = '''    elif t == "build":
        chips = q.locator(".bank .chip"); n = await chips.count()
        ns = [await chips.nth(j).get_attribute("data-n") for j in range(n)]
        seq = sorted([j for j in range(n) if ns[j]], key=lambda j: int(ns[j]))
        if not right: seq[0], seq[1] = seq[1], seq[0]
        texts = [(await chips.nth(j).inner_text()).strip() for j in seq]
        for tx in texts: await q.locator(".bank").get_by_text(tx, exact=True).first.click()
        await q.locator(".fq-check").click()
'''
OLD = 'pg = await b.new_page(viewport={"width": 1280, "height": 800})'
NEW = ('ctx = await b.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True); '
       'pg = await ctx.new_page()')
args = [a for a in sys.argv[1:] if a != '--phone']; phone = '--phone' in sys.argv
if not args: print('usage: quiz_walk_x.py DECK [OUTDIR] [--phone]'); sys.exit(2)
if not os.path.exists('quiz_walk.py'): print('COULD NOT CHECK: quiz_walk.py not here (run setup_tools.sh first)'); sys.exit(2)
src = open('quiz_walk.py', encoding='utf-8').read()
if src.count(ELSE) != 1: print('COULD NOT CHECK: the unknown-type branch in quiz_walk.py changed; update ELSE in this file'); sys.exit(2)
src = src.replace(ELSE, EXTRA + ELSE)
if phone:
    if src.count(OLD) != 1: print('COULD NOT CHECK: the page line in quiz_walk.py changed; update OLD in this file'); sys.exit(2)
    src = src.replace(OLD, NEW)
sys.argv = ['quiz_walk.py', args[0], args[1] if len(args) > 1 else ('quiz-shots-phone' if phone else 'quiz-shots')]
exec(compile(src, 'quiz_walk_x', 'exec'), {'__name__': '__main__'})
