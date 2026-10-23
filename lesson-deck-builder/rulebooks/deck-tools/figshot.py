# figshot.py DECK SLIDE OUT.png [W H scale selector index] — screenshot one element (default the first .lf) of a fully built slide   (deck-tools 1.5)
import sys, os, asyncio
from playwright.async_api import async_playwright
deck, k, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 1280; H = int(sys.argv[5]) if len(sys.argv) > 5 else 800
sc = float(sys.argv[6]) if len(sys.argv) > 6 else 2
sel = sys.argv[7] if len(sys.argv) > 7 else '.lf'
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(viewport={'width': W, 'height': H}, device_scale_factor=sc)
        pg = await ctx.new_page(); css = open('fonts/local.css').read()
        async def f(r): await r.fulfill(status=200, content_type='text/css', body=css)
        await pg.route('**/fonts.googleapis.com/**', f); await pg.route('**/fonts.gstatic.com/**', lambda r: r.abort())
        await pg.goto('file://' + os.path.abspath(deck)); await pg.wait_for_timeout(1200)
        await pg.evaluate(f'go({k-1}, true)'); await pg.wait_for_timeout(2600)
        idx = int(sys.argv[8]) if len(sys.argv) > 8 else 0
        el = pg.locator(f'section.slide.active {sel}').nth(idx)
        await el.screenshot(path=out); await b.close()
asyncio.run(main())
