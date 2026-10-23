# shots.py DECK OUTDIR W H [slides,comma,list|all] [--touch]  — fully built slides, local fonts, contact sheets   (deck-tools 1.2)
# Exit code: 0 done · 1 page errors or sideways scrolling seen · 2 could not run (engine globals missing).
import sys, os, asyncio
from playwright.async_api import async_playwright
from PIL import Image
deck, out, W, H = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
only = [int(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 and sys.argv[5] not in ('all', '--touch') else None
touch = '--touch' in sys.argv
ENGINE = "typeof slides!=='undefined'&&slides.length>0&&typeof go==='function'&&typeof total!=='undefined'"
RC = 0
async def main():
    global RC
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={'width': W, 'height': H}, has_touch=touch, is_mobile=touch, device_scale_factor=1)
        pg = await ctx.new_page(); os.makedirs(out, exist_ok=True)
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        if os.path.exists('fonts/local.css'):
            css = open('fonts/local.css').read()
            async def f(r): await r.fulfill(status=200, content_type='text/css', body=css)
            await pg.route('**/fonts.googleapis.com/**', f); await pg.route('**/fonts.gstatic.com/**', lambda r: r.abort())
        else: print('note: fonts/local.css missing (run setup_tools.sh); screenshots use fallback fonts')
        await pg.goto('file://' + os.path.abspath(deck)); await pg.wait_for_timeout(1500)
        if not await pg.evaluate(ENGINE):
            print('COULD NOT CHECK: the engine globals (slides, go, total) are missing; the skill engine changed. No screenshots taken.')
            await b.close(); RC = 2; return
        files = []
        for k in range(await pg.evaluate('total')):
            if only and k + 1 not in only: continue
            await pg.evaluate(f'go({k}, true)'); await pg.wait_for_timeout(2600)
            sh, ch, sw, cw = await pg.evaluate(f'[slides[{k}].scrollHeight, slides[{k}].clientHeight, slides[{k}].scrollWidth, slides[{k}].clientWidth]')
            note = []
            if sh > ch + 2: note.append(f'tall {sh/ch:.2f}x')
            if sw > cw + 2: note.append('SIDEWAYS'); RC = RC or (1 if W < 800 else 0)
            if note: print('slide', k + 1, ', '.join(note))
            fn = f'{out}/s{k+1:02d}.png'; await pg.screenshot(path=fn); files.append(fn)
        print('errors:', errs or 'none'); RC = RC or (1 if errs else 0)
        await b.close()
    if not files: print('COULD NOT CHECK: no slides matched the list'); RC = 2; return
    # contact sheets: 2 per row (laptop) or 4 per row (phone), scaled
    per = 4 if W < 600 else 2; sc = 0.5 if W < 600 else 0.62; grp = per * (2 if W < 600 else 1)
    for i in range(0, len(files), grp):
        ims = [Image.open(f) for f in files[i:i + grp]]; w, h = int(W * sc), int(H * sc)
        rows = (len(ims) + per - 1) // per
        sheet = Image.new('RGB', (w * per + 6 * (per - 1), h * rows + 6 * (rows - 1)), 'white')
        for j, im in enumerate(ims):
            sheet.paste(im.resize((w, h)), ((j % per) * (w + 6), (j // per) * (h + 6)))
        sheet.save(f'{out}/sheet{i // grp + 1:02d}.png')
    print(f'{len(files)} screenshots and {(len(files) + grp - 1) // grp} contact sheets in {out}')
asyncio.run(main()); sys.exit(RC)
