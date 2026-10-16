#!/usr/bin/env python3
"""
Validate a Lesson-Deck-Builder deck before presenting it.

Usage:  python validate.py path/to/deck.html

Checks (fast, no dependencies):
  - exactly one <html>/<body>/<script> and balanced <style> tags
  - exactly one slide carries `class="slide active"` (the first one)
  - no element has a duplicated `style="..." style="..."` attribute
  - a Google Fonts <link> is present
  - the deck engine markers are present (nav + reveal system) and the engine is v2
    (builds + data-capture guard)
  - components §22+ (--k-* tokens) have the bridge tokens defined
  - no element carries both .reveal and data-build; scrubbers carry data-capture
  - Sketchbook notes: one .live per slide, Arabic = Playpen Sans Arabic 800
  - canvas (v1.3): <html data-canvas="paper|chalkboard"> and, on the chalkboard, a
    data-board that the stylesheet actually defines; fonts from retired families
  - reports the slide count and the implied reading time

Exit code is 0 when clean, 1 when any problem is found.
"""
import re
import sys


def validate(path: str) -> int:
    try:
        html = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"✗ cannot read file: {e}")
        return 1

    problems, notes = [], []

    # strip HTML comments first so documentation that mentions tags like
    # `<html>` or `<script>` doesn't trigger false positives
    stripped = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)

    def count(t):
        return stripped.count(t)

    # structural singletons / balance
    for tag in ("<html", "</html>", "<body", "</body>", "<script", "</script>"):
        if count(tag) != 1:
            problems.append(f"expected exactly one '{tag}', found {count(tag)}")
    if count("<style") != count("</style>"):
        problems.append(f"unbalanced <style> tags: {count('<style')} open / {count('</style>')} close")

    # slides
    n_slides = len(re.findall(r'class="slide(?:\s|")', stripped))
    n_active = count('class="slide active"')
    if n_slides == 0:
        problems.append("no slides found (expected sections with class=\"slide\")")
    if n_active != 1:
        problems.append(f"exactly one slide must have class=\"slide active\"; found {n_active}")

    # duplicate style attribute on a single tag
    dups = re.findall(r"<[^>]*\bstyle=[^>]*\bstyle=", stripped)
    if dups:
        problems.append(f"{len(dups)} element(s) have a duplicated style= attribute (merge them into one)")

    # fonts + engine markers
    if "fonts.googleapis.com" not in html:
        problems.append("no Google Fonts <link> found")
    if "querySelectorAll('.slide')" not in html and "querySelectorAll(\".slide\")" not in html:
        problems.append("deck engine <script> appears to be missing or altered")
    if re.search(r'<svg[^>]*class="(?:grain|dust)"', stripped):
        problems.append("grain/dust overlay is a live full-viewport SVG filter — use the "
                        "tiled data-URI noise background (style-system.md §5, law 3); the live "
                        "filter paints a visible patch on dark canvases")
    if "isContentEditable" not in html:
        problems.append("engine lacks the editable-field guard — arrow keys will flip "
                        "slides while typing in the answer box (copy a fresh engine "
                        "from assets/template.html)")
    if "buildMax" not in html or "[data-capture]" not in html:
        problems.append("deck engine is v1 — copy the v2 engine (builds + data-capture guard) "
                        "from assets/template.html")
    if re.search(r"var\(--k-[a-z-]+", stripped) and "--k-ink:" not in stripped:
        problems.append("components read --k-* bridge tokens but none are defined — copy the "
                        "token blocks from assets/template.html (style-system.md §7)")
    for tag in re.findall(r"<[a-zA-Z][^<>]*\bdata-build=[^<>]*>", stripped):
        if re.search(r'class="[^"]*\breveal\b', tag):
            problems.append("an element has both .reveal and data-build — they fight over "
                            "opacity/transform; wrap one in the other")
            break
    for tag in re.findall(r'<[a-zA-Z][^<>]*class="[^"]*\brs-num\b[^<>]*>', stripped):
        if "data-capture" not in tag:
            problems.append("a .rs-num scrubber lacks data-capture — dragging it will turn the page")
            break
    for i, sec in enumerate(re.split(r"<section\b", stripped)[1:], 1):
        n_live = len(re.findall(r'class="(?:[^"]*\s)?live(?:\s[^"]*)?"', sec))
        if n_live > 1:
            notes.append(f"slide {i} has {n_live} .live elements — line boil is for ONE element per slide")
    if re.search(r'<html[^>]*dir="rtl"', html) and "family=Caveat" in html and "Playpen" not in html:
        notes.append("Arabic Sketchbook deck: display face should be Playpen Sans Arabic 800 "
                     "(style-system.md §4)")
    if "Playpen+Sans+Arabic" in html and "Playpen+Sans+Arabic:wght@800" not in html:
        notes.append("Playpen Sans Arabic is used at weight 800 only — load "
                     "family=Playpen+Sans+Arabic:wght@800")
    # canvas + board (v1.3)
    BOARDS = {"slate-reinked", "midnight-blue", "olive-gold", "dusk-indigo", "deep-teal", "red-graphite"}
    root = re.search(r"<html\b[^>]*>", stripped)
    root = root.group(0) if root else ""
    canvas = re.search(r'data-canvas="([^"]*)"', root)
    board = re.search(r'data-board="([^"]*)"', root)
    if not canvas:
        notes.append('no data-canvas on <html> — set data-canvas="paper" or data-canvas="chalkboard" '
                     '(+ data-board); decks built before v1.3 keep their own tokens and still work')
        if board:
            notes.append('data-board does nothing without data-canvas="chalkboard"')
    else:
        c = canvas.group(1)
        if c not in ("paper", "chalkboard"):
            problems.append(f'data-canvas="{c}" is not a canvas — use "paper" or "chalkboard"')
        if c == "paper" and board:
            notes.append("data-board is ignored on the paper canvas")
        if c == "chalkboard":
            if ':root[data-canvas="chalkboard"]' not in stripped:
                problems.append('data-canvas="chalkboard" but the stylesheet has no chalkboard tokens — the deck '
                                'would render with the paper colours; copy the token section of assets/template.html')
            elif board:
                b = board.group(1)
                if b not in BOARDS:
                    problems.append(f'data-board="{b}" is not one of the six boards: ' + ", ".join(sorted(BOARDS)))
                elif b != "slate-reinked" and f'[data-board="{b}"]' not in stripped:
                    problems.append(f'data-board="{b}" has no token block in this deck\'s stylesheet — the deck '
                                    'would silently show the default board (Slate re-inked); copy the boards from '
                                    'assets/template.html')
    retired = [f for f in ("Bricolage+Grotesque", "Figtree", "Chakra+Petch", "Fraunces", "Newsreader",
                           "El+Messiri", "Reem+Kufi") if f in html]
    if retired:
        notes.append("fonts from retired style families are loaded (" + ", ".join(retired) + ") — "
                     "Sketchbook uses Caveat + Karla / Playpen Sans Arabic 800 + IBM Plex Sans Arabic")

    if "class=\"reveal\"" not in html and "reveal" not in html:
        notes.append("no .reveal elements found — slides won't animate on enter")

    # counter fallback sanity (not fatal)
    m = re.search(r'id="total"[^>]*>(\d+)<', html)
    if m and int(m.group(1)) != n_slides:
        notes.append(f"#total fallback says {m.group(1)} but there are {n_slides} slides (the script auto-fixes this at runtime)")

    # report
    lo, hi = round(n_slides * 1.0), round(n_slides * 1.5)
    print(f"slides: {n_slides}   ·   implied reading time ≈ {lo}–{hi} min")
    if n_slides > 20:
        notes.append("more than 20 slides — likely over a 30-minute calm budget; consider tightening")

    for n in notes:
        print(f"⚠ {n}")
    if problems:
        for p in problems:
            print(f"✗ {p}")
        print("\nNOT clean — fix the above before presenting.")
        return 1
    print("✓ clean.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python validate.py path/to/deck.html")
        raise SystemExit(2)
    raise SystemExit(validate(sys.argv[1]))
