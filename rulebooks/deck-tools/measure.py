# measure.py DECK W H slides,comma,list — elements that stick out sideways on each listed slide   (deck-tools 1.2)
# Exit code: 0 nothing sticks out · 1 something sticks out · 2 could not run (engine globals missing or bad slide number).
import sys, os, asyncio
from playwright.async_api import async_playwright
deck = sys.argv[1]; W = int(sys.argv[2]); H = int(sys.argv[3]); ks = [int(x) for x in sys.argv[4].split(',')]
ENGINE = "typeof slides!=='undefined'&&slides.length>0&&typeof go==='function'"
RC = 0
async def main():
    global RC
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(viewport={'width': W, 'height': H}, has_touch=True, is_mobile=True); pg = await ctx.new_page()
        if os.path.exists('fonts/local.css'):
            css = open('fonts/local.css').read()
            async def f(r): await r.fulfill(status=200, content_type='text/css', body=css)
            await pg.route('**/fonts.googleapis.com/**', f); await pg.route('**/fonts.gstatic.com/**', lambda r: r.abort())
        else: print('note: fonts/local.css missing (run setup_tools.sh); measuring with fallback fonts')
        await pg.goto('file://' + os.path.abspath(deck)); await pg.wait_for_timeout(1200)
        if not await pg.evaluate(ENGINE):
            print('COULD NOT CHECK: the engine globals (slides, go) are missing; the skill engine changed.'); RC = 2; await b.close(); return
        n = await pg.evaluate('slides.length')
        for k in ks:
            if not 1 <= k <= n: print(f'COULD NOT CHECK slide {k}: the deck has {n} slides'); RC = 2; continue
            await pg.evaluate(f'go({k-1},true)'); await pg.wait_for_timeout(1500)
            r = await pg.evaluate('''(k)=>{const s=slides[k];const w=s.clientWidth;const out=[];s.querySelectorAll('*').forEach(e=>{const r=e.getBoundingClientRect();if(r.right>w+2&&r.width>0)out.push(e.tagName+'.'+(e.className.baseVal!==undefined?e.className.baseVal:e.className)+' '+Math.round(r.right)+' '+(e.textContent||'').trim().slice(0,30));});return out.slice(0,6);}''', k - 1)
            print(k, r or 'nothing sticks out')
            if r and RC == 0: RC = 1
        await b.close()
asyncio.run(main()); sys.exit(RC)
