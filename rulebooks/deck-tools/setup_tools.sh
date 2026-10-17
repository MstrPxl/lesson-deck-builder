#!/usr/bin/env bash
# setup_tools.sh [slides-rulebook.md] [questions-rulebook.md]   (deck-tools 1.6)
# Run once per session, from the folder that holds the rulebooks.
#  1. copies plain_check.py and quiz_walk.py from deck-tools next to the rulebooks (the rulebooks' commands expect them
#     there) and checks that deck-tools/snippets/ and the checker brief are complete. Before 1.6 they were extracted
#     from the rulebooks' appendices; since slides-rulebook 1.9 / questions-rulebook 1.3 the code ships here.
#  2. compares the rulebook versions with the ones these tools were written for (VERSION.txt)
#  3. local fonts for screenshots, wordfreq + bs4, the CEFR-J word list
# Step 1 must succeed (exit 1 if not). Step 2 only warns. Step 3 warns and carries on: the scripts still run without it.
SR=${1:-slides-rulebook.md}; QR=${2:-questions-rulebook.md}
HERE=$(cd "$(dirname "$0")" && pwd)

# ---- 1 + 2 · copy the scripts, check the snippets, compare versions
python3 - "$SR" "$QR" "$HERE" <<'PY' || exit 1
import re, sys, os, shutil
sr, qr, here = sys.argv[1:4]
vf = os.path.join(here, 'VERSION.txt')
bad = False
for book in (sr, qr):
    if not os.path.exists(book):
        print(f'ERROR: {book} not found. Run from the folder that holds the rulebooks, or pass their paths.'); bad = True
for out in ('plain_check.py', 'quiz_walk.py'):
    src = os.path.join(here, out)
    if not os.path.exists(src):
        print(f'ERROR: deck-tools/{out} is missing (an incomplete unzip, or deck-tools older than 1.6).'); bad = True; continue
    code = open(src, encoding='utf-8').read()
    try: compile(code, out, 'exec')
    except SyntaxError as e:
        print(f'ERROR: deck-tools/{out} does not compile ({e}).'); bad = True; continue
    if os.path.abspath(src) != os.path.abspath(out): shutil.copyfile(src, out)
    print(f'ok: {out} ({code.count(chr(10))} lines) copied from deck-tools')
SNIPPETS = ['topic-bar.html', 'topic-bar.css', 'topic-bar.js', 'glossary-slide.html', 'glossary.css', 'glossary.js',
            'figure-labels.css', 'phone-layer.css', 'phone-layer.js', 'phone-variant.html', 'phone-variant.css',
            'quiz-markup.html', 'quiz.css', 'quiz.js']
gone = [s for s in SNIPPETS if not os.path.exists(os.path.join(here, 'snippets', s))]
if not os.path.exists(os.path.join(here, 'checker-brief.txt')): gone.append('checker-brief.txt')
if gone: print('ERROR: missing from deck-tools: ' + ', '.join(gone)); bad = True
else: print(f'ok: {len(SNIPPETS)} snippets and the checker brief')
if bad: sys.exit(1)

def ver(book):
    m = re.search(r'\*\*Version\s+([0-9][0-9.]*)', open(book, encoding='utf-8').read()[:2000])
    return m.group(1) if m else None
want = {}
if os.path.exists(vf):
    t = open(vf, encoding='utf-8').read()
    for key in ('slides-rulebook', 'questions-rulebook'):
        m = re.search(key + r'\s+v([0-9][0-9.]*)', t)
        if m: want[key] = m.group(1)
for key, book in (('slides-rulebook', sr), ('questions-rulebook', qr)):
    have, need = ver(book), want.get(key)
    if have and need and have != need:
        print(f'WARNING: deck-tools was written for {key} v{need}; this one is v{have}.')
        print('         Run the self-test in VERSION.txt before trusting the tools; if they fail it, fix the tools, not the deck.')
    elif not have or not need:
        print(f'note: could not compare the {key} version (rulebook says {have}, VERSION.txt says {need}).')
    else:
        print(f'ok: {key} v{have} matches deck-tools')
PY

# ---- 3 · fonts, Python packages, word list (warn on failure, carry on)
mkdir -p fonts
if (cd fonts && npm init -y >/dev/null 2>&1 && npm install @fontsource/caveat @fontsource/karla --silent >/dev/null 2>&1); then
python3 - <<'PY'
import os
b = os.path.abspath('fonts/node_modules/@fontsource')
r = [f"@font-face{{font-family:'Caveat';font-weight:{w};src:url('file://{b}/caveat/files/caveat-latin-{w}-normal.woff2')}}" for w in (500, 600, 700)]
r += [f"@font-face{{font-family:'Karla';font-weight:{w};src:url('file://{b}/karla/files/karla-latin-{w}-normal.woff2')}}" for w in (400, 500, 700)]
r.append(f"@font-face{{font-family:'Karla';font-weight:400;font-style:italic;src:url('file://{b}/karla/files/karla-latin-400-italic.woff2')}}")
missing = [x for x in r if not os.path.exists(x.split("file://")[1].split("'")[0])]
if missing: print(f'WARNING: {len(missing)} font files missing (the font packages changed layout); screenshots use fallback fonts.')
else:
    open('fonts/local.css', 'w').write('\n'.join(r)); print('ok: fonts/local.css')
PY
else
  echo "WARNING: could not install the fonts; screenshots and size checks will use fallback fonts."
fi
pip install wordfreq bs4 --break-system-packages -q 2>/dev/null || pip install wordfreq bs4 -q 2>/dev/null \
  && echo "ok: wordfreq, bs4" || echo "WARNING: could not install wordfreq/bs4; build.py needs bs4, plain_check.py needs wordfreq."
if [ -s cefrj-vocabulary-profile-1.5.csv ]; then echo "ok: CEFR-J list (already here)"
elif python3 -c "import urllib.request;urllib.request.urlretrieve('https://raw.githubusercontent.com/openlanguageprofiles/olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv','cefrj-vocabulary-profile-1.5.csv')" 2>/dev/null; then echo "ok: CEFR-J list"
else echo "WARNING: could not download the CEFR-J list; plain_check.py will try again on its first run."; fi
echo "setup done (deck-tools $(head -1 "$HERE/VERSION.txt" 2>/dev/null | sed 's/^deck-tools //;s/ ·.*//'))"
