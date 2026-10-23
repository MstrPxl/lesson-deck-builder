"""quiz_walk.py - answers every .fq item in a deck (questions-rulebook.md §7).
Usage: python quiz_walk.py deck.html [outdir]
Answers items alternately right / wrong, from each item's own answer data, then checks
the score slide, the reset, console errors, and screenshots every quiz slide."""
import asyncio, os, sys
from playwright.async_api import async_playwright

DECK = os.path.abspath(sys.argv[1]); OUT = sys.argv[2] if len(sys.argv) > 2 else "quiz-shots"
os.makedirs(OUT, exist_ok=True)

async def answer(pg, q, right):
    t = await q.get_attribute("data-type")
    if t == "mcq":
        await q.locator('.opt[data-ok="1"]' if right else '.opt:not([data-ok="1"])').first.click()
    elif t == "spot":
        await q.locator('.fq-ch[data-ok="1"]' if right else '.fq-ch:not([data-ok="1"])').first.click()
    elif t == "gap":
        ans = await q.get_attribute("data-answer")
        chips = q.locator(".chip")
        for j in range(await chips.count()):
            w = (await chips.nth(j).inner_text()).strip()
            if (w == ans) == right: await chips.nth(j).click(); break
        await q.locator(".fq-check").click()
    elif t == "num":
        ans = await q.get_attribute("data-answer")
        await q.locator("input").fill(ans if right else str(int(ans) + 1)); await q.locator(".fq-check").click()
    elif t == "match":
        rows = q.locator(".fq-row"); n = await rows.count()
        keys = [await rows.nth(r).get_attribute("data-key") for r in range(n)]
        for r in range(n):
            k = keys[r] if right else keys[(r + 1) % n]
            await rows.nth(r).locator("select").select_option(k)
        await q.locator(".fq-check").click()
    elif t == "sort":
        rows = q.locator(".fq-row"); groups = (await q.get_attribute("data-groups")).split("|")
        for r in range(await rows.count()):
            g = await rows.nth(r).get_attribute("data-g")
            if not right and r == 0: g = next(x for x in groups if x != g)
            await rows.nth(r).locator(f'.fq-grp button[data-g="{g}"]').click()
        await q.locator(".fq-check").click()
    elif t == "order":
        items = q.locator(".fq-it"); n = await items.count()
        ns = [int(await items.nth(j).get_attribute("data-n")) for j in range(n)]
        seq = sorted(range(n), key=lambda j: ns[j])
        if not right: seq[0], seq[1] = seq[1], seq[0]
        for j in seq: await items.nth(j).click()
        await q.locator(".fq-check").click()
    elif t == "label":
        drops = q.locator(".drop"); n = await drops.count()
        ans = [await drops.nth(d).get_attribute("data-answer") for d in range(n)]
        if not right: ans[0], ans[1] = ans[1], ans[0]
        for d in range(n):
            await drops.nth(d).click()
            await q.locator(".bank .chip", has_text=ans[d]).first.click()
        await q.locator(".fq-check").click()
    else:
        print("  ! unknown data-type", t); return None
    return right

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1280, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "Failed to load resource" not in m.text else None)  # ignore blocked fonts
        await pg.goto("file://" + DECK); await pg.wait_for_timeout(600)
        slide_ids = await pg.evaluate("[...new Set([...document.querySelectorAll('.fq')].map(q=>slides.indexOf(q.closest('.slide'))))]")
        expected = 0; n = 0
        for k in slide_ids:
            await pg.evaluate(f"go({k},true)"); await pg.wait_for_timeout(1200)
            qs = pg.locator("section.slide.active .fq")
            for j in range(await qs.count()):
                right = (n % 2 == 0); n += 1
                if await answer(pg, qs.nth(j), right): expected += 1
            await pg.wait_for_timeout(700); await pg.screenshot(path=f"{OUT}/quiz-{k+1}.png")
        score_k = await pg.evaluate("slides.indexOf(document.getElementById('fq-score'))")
        await pg.evaluate(f"go({score_k},true)"); await pg.wait_for_timeout(1200)
        await pg.screenshot(path=f"{OUT}/quiz-score.png")
        got = int(await pg.text_content("#fq-total"))
        print(f"items {n} · expected score {expected} · shown {got} · {'OK' if got == expected else 'MISMATCH'}")
        print("message:", await pg.text_content("#fq-msg"))
        print("revisit:", await pg.evaluate("[...document.querySelectorAll('#fq-review .k-btn')].map(b=>b.textContent)"))
        await pg.click("#fq-retry"); await pg.wait_for_timeout(400)
        print("after reset: score", await pg.text_content("#fq-total"), "· on slide", await pg.evaluate("idx") + 1)
        ov = await pg.evaluate("slides.map((s,k)=>[k+1,s.scrollWidth>s.clientWidth+2]).filter(x=>x[1]).map(x=>x[0])")
        print("sideways overflow on slides:", ov or "none")
        print("console errors:", errs or "none")
        await b.close()

asyncio.run(main())
