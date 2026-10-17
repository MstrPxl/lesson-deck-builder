# checks.py DECK — automated deck checks (deck-tools 1.3)
# keyboard walk, glossary cards, drag tests (mouse + touch), control sizes, phone sizes, touch swipe walk.
# Every check first confirms it found what it examines; if not it prints COULD NOT CHECK instead of passing.
# Exit code: 0 all checked and clean · 1 a check found a problem · 2 something could not be checked.
import sys, os, asyncio
from playwright.async_api import async_playwright
DECK = 'file://' + os.path.abspath(sys.argv[1])
FONTS = open('fonts/local.css').read() if os.path.exists('fonts/local.css') else None
STATUS = {'problem': False, 'unchecked': []}

def unchecked(what, why):
    STATUS['unchecked'].append(what); print(f'COULD NOT CHECK {what}: {why}')
def problem(msg):
    STATUS['problem'] = True; print('PROBLEM:', msg)

ENGINE = "typeof slides!=='undefined'&&slides.length>0&&typeof go==='function'&&typeof next==='function'&&typeof idx!=='undefined'&&typeof buildStep!=='undefined'&&typeof buildMax!=='undefined'&&typeof total!=='undefined'"

async def openpg(b, w, h, touch=False):
    ctx = await b.new_context(viewport={'width': w, 'height': h}, has_touch=touch, is_mobile=touch)
    pg = await ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'Failed to load' not in m.text else None)
    if FONTS:
        async def f(r): await r.fulfill(status=200, content_type='text/css', body=FONTS)
        await pg.route('**/fonts.googleapis.com/**', f); await pg.route('**/fonts.gstatic.com/**', lambda r: r.abort())
    await pg.goto(DECK); await pg.wait_for_timeout(1200)
    return ctx, pg, errs

async def drag(pg, chip, drop, cdp=None):
    # centre both in the slide: scroll_into_view_if_needed can leave the chip under the fixed nav (deck-tools 1.3)
    await chip.evaluate("e=>e.scrollIntoView({block:'center'})"); await pg.wait_for_timeout(300)
    if not await drop.evaluate("e=>{const r=e.getBoundingClientRect();return r.top>40&&r.bottom<innerHeight-90}"):
        await drop.evaluate("e=>e.scrollIntoView({block:'center'})"); await pg.wait_for_timeout(300)
    cb = await chip.bounding_box(); db = await drop.bounding_box()
    if not cb or not db: return None
    x0, y0 = cb['x'] + cb['width'] / 2, cb['y'] + cb['height'] / 2; x1, y1 = db['x'] + db['width'] / 2, db['y'] + db['height'] / 2
    if cdp:
        await cdp.send('Input.dispatchTouchEvent', {'type': 'touchStart', 'touchPoints': [{'x': x0, 'y': y0}]})
        for i in range(1, 13):
            await cdp.send('Input.dispatchTouchEvent', {'type': 'touchMove', 'touchPoints': [{'x': x0 + (x1 - x0) * i / 12, 'y': y0 + (y1 - y0) * i / 12}]})
            await pg.wait_for_timeout(15)
        await cdp.send('Input.dispatchTouchEvent', {'type': 'touchEnd', 'touchPoints': []})
    else:
        await pg.mouse.move(x0, y0); await pg.mouse.down()
        for i in range(1, 13):
            await pg.mouse.move(x0 + (x1 - x0) * i / 12, y0 + (y1 - y0) * i / 12); await pg.wait_for_timeout(15)
        await pg.mouse.up()
    await pg.wait_for_timeout(250)
    return await drop.locator('.chip').count() == 1

async def drag_test(pg, label, cdp=None):
    # first gap item (or label item for touch): drag the chip whose text is the answer onto its drop
    for sel in (['.fq[data-type="label"]', '.fq[data-type="gap"]'] if cdp else ['.fq[data-type="gap"]', '.fq[data-type="label"]']):
        n = await pg.locator(sel).count()
        if not n: continue
        k = await pg.evaluate(f"slides.indexOf(document.querySelector('{sel}').closest('.slide'))")
        await pg.evaluate(f'go({k},true)'); await pg.wait_for_timeout(900)
        q = pg.locator(f'section.slide.active {sel}').first
        drop = q.locator('.drop').first
        ans = await drop.get_attribute('data-answer') or await q.get_attribute('data-answer')
        chip = q.locator('.bank .chip', has_text=ans).first if ans else None
        if not ans or not await chip.count():
            unchecked(label, f'{sel} found, but no chip matches its answer'); return
        ok = await drag(pg, chip, drop, cdp)
        if ok is None: unchecked(label, 'chip or drop has no size on screen'); return
        same = await pg.evaluate(f'idx==={k}')
        print(f'{label}: lands {ok} · slide unchanged {same}')
        if not (ok and same): problem(f'{label} failed')
        return
    unchecked(label, 'no gap or label quiz item in the deck')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx, pg, errs = await openpg(b, 1280, 800)
        if not await pg.evaluate(ENGINE):
            unchecked('everything', 'the engine globals (slides, go, next, idx, buildStep, buildMax, total) are missing; the skill engine changed')
            await b.close(); sys.exit(2)
        if not FONTS: print('note: fonts/local.css missing (run setup_tools.sh); layout uses fallback fonts')
        # 1 · keyboard walk
        n = 0
        while not await pg.evaluate('idx==total-1 && buildStep[idx]>=buildMax[idx]') and n < 400:
            await pg.keyboard.press('ArrowRight'); n += 1; await pg.wait_for_timeout(40)
        builds = await pg.evaluate('buildMax.reduce((a,b)=>a+b,0)'); tot = await pg.evaluate('total')
        print(f'keyboard walk: {n} presses for {tot} slides + {builds} builds')
        if n != tot - 1 + builds: problem('keyboard walk did not match slides + builds')
        k_built = await pg.evaluate("buildMax.findIndex(b=>b>0)")
        if k_built > 0:
            await pg.evaluate(f'go({k_built + 1})'); await pg.keyboard.press('ArrowLeft'); await pg.wait_for_timeout(200)
            ok = await pg.evaluate(f'idx==={k_built} && buildStep[{k_built}]===buildMax[{k_built}]')
            print('stepping back arrives fully built:', ok)
            if not ok: problem('stepping back did not arrive fully built')
        else: unchecked('stepping back into builds', 'no slide has builds')
        # 2 · glossary
        if await pg.locator('#glossary').count():
            cards = await pg.evaluate("slides.map((s,k)=>[k+1,[...s.querySelectorAll('.gl-card b')].map(b=>b.textContent)]).filter(x=>x[1].length)")
            if not cards: problem('a glossary exists but no slide got a card')
            print('glossary cards:', '; '.join(f'{k}:{",".join(v)}' for k, v in cards))
            if await pg.locator('.fq').count():
                q = await pg.evaluate("document.querySelectorAll('.fq .gl-w').length")
                print('cards on quiz items:', q)
                if q: problem('glossary cards inside quiz items')
            else: unchecked('cards on quiz items', 'no quiz items (.fq)')
        else: unchecked('glossary cards', 'no #glossary in the deck')
        # 3 · mouse drag
        await drag_test(pg, 'mouse drag')
        print('laptop errors:', errs or 'none')
        if errs: problem('page errors at laptop size')
        await ctx.close()

        # 4 · touch drag and control sizes on a phone
        ctx, pg, errs = await openpg(b, 390, 844, True)
        cdp = await ctx.new_cdp_session(pg)
        await drag_test(pg, 'touch drag', cdp)
        sizes = await pg.evaluate("""()=>{const o={};const sel={'nav prev/next':'#prev,#next','quiz options':'.opt','check buttons':'.k-btn','chips':'.chip','group pills':'.fq-grp button','topic blocks':'.nav .sec'};
          for(const [k,s] of Object.entries(sel)){const hs=[...document.querySelectorAll(s)].map(e=>{const sl=e.closest('.slide');const was=sl&&sl.classList.contains('active');if(sl)sl.classList.add('active');
            const h=e.getBoundingClientRect().height;if(sl&&!was)sl.classList.remove('active');return h}).filter(h=>h>0);o[k]=hs.length?Math.round(Math.min(...hs)):null}return o}""")
        print('smallest tap targets (px):', sizes)
        for k, need in (('nav prev/next', 44), ('quiz options', 44), ('check buttons', 44), ('chips', 24), ('group pills', 24), ('topic blocks', 24)):
            if sizes.get(k) is None: unchecked(f'tap size of {k}', 'none found')
            elif sizes[k] < need: problem(f'{k} are {sizes[k]} px, under {need}')
        await ctx.close()

        # 5 · sideways overflow and tall slides
        for (w, h) in [(390, 844), (360, 740), (320, 640), (844, 390)]:
            ctx, pg, errs = await openpg(b, w, h, True); res = []
            for k in range(await pg.evaluate('total')):
                await pg.evaluate(f'go({k},true)'); await pg.wait_for_timeout(350)
                sw, cw, sh, ch = await pg.evaluate(f'[slides[{k}].scrollWidth,slides[{k}].clientWidth,slides[{k}].scrollHeight,slides[{k}].clientHeight]')
                res.append((k + 1, sw > cw + 2, sh / ch))
            side = [k for k, s, _ in res if s]; tall = [f'{k}:{t:.2f}' for k, _, t in res if t > 1.5]
            print(f'{w}x{h}: sideways {side or "none"} · over 1.5 screens {tall or "none"}')
            if side and w < 800: problem(f'sideways scrolling at {w}px on slides {side}')
            await ctx.close()

        # 6 · touch swipe walk at 390: every build lands above the nav
        ctx, pg, errs = await openpg(b, 390, 844, True)
        if not await pg.locator('.nav').count():
            unchecked('touch walk', 'no .nav element')
        else:
            cdp = await ctx.new_cdp_session(pg); hidden = []; steps = 0
            while not await pg.evaluate('idx==total-1 && buildStep[idx]>=buildMax[idx]') and steps < 400:
                before = await pg.evaluate('[idx,buildStep[idx]]')
                for t, x in (('touchStart', 330), ('touchMove', 200), ('touchMove', 60)):
                    await cdp.send('Input.dispatchTouchEvent', {'type': t, 'touchPoints': [{'x': x, 'y': 150}]})
                await cdp.send('Input.dispatchTouchEvent', {'type': 'touchEnd', 'touchPoints': []})
                await pg.wait_for_timeout(700)
                if await pg.evaluate('[idx,buildStep[idx]]') == before: await pg.evaluate('next()'); await pg.wait_for_timeout(700)
                steps += 1
                r = await pg.evaluate('''()=>{const s=slides[idx];const now=[...s.querySelectorAll('[data-build].now')].filter(e=>e.getBoundingClientRect().height>0).pop();if(!now)return null;
                    const nav=document.querySelector('.nav').getBoundingClientRect().top;const r=now.getBoundingClientRect();return r.top<nav-4?null:[idx+1,buildStep[idx]]}''')
                if r: hidden.append(r)
            print('touch walk steps', steps, '· builds out of view (slide, step):', hidden or 'none', '· errors:', errs or 'none')
            if hidden: problem('builds landed out of view on a phone')
            if errs: problem('page errors on a phone')
        await b.close()

    print('\nRESULT:', 'problems found' if STATUS['problem'] else 'no problems found',
          '·', ('could not check: ' + ', '.join(STATUS['unchecked'])) if STATUS['unchecked'] else 'everything was checked')
    sys.exit(1 if STATUS['problem'] else 2 if STATUS['unchecked'] else 0)

asyncio.run(main())
