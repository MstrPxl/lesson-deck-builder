#!/usr/bin/env python3
"""size_check.py - the rulebooks' and the general notes' sizes against their caps   (deck-tools 1.6)

Usage:  python3 deck-tools/size_check.py [FOLDER] [--sections]
Run it after every edit of a rulebook or the notes (slides-rulebook.md §0, "Size cap").
FOLDER holds the rulebooks (default: the current folder). For each file it prints the characters, about how
many tokens a run spends reading it (characters / 4), and its cap. --sections adds every "## " section's share.
It also flags what the caps exist to keep out of the rulebooks:
  - a code block longer than MAX_BLOCK_LINES lines (code belongs in deck-tools, as a file);
  - a "Changes in ..." version note (history belongs in rulebooks-changelog.md).
Exit codes: 0 all clean · 1 a cap passed or something to move out · 2 a rulebook not found.
"""
import re, sys, pathlib

# keep these in step with slides-rulebook.md §0 ("Size cap")
CAPS = {'slides-rulebook.md': 110_000, 'questions-rulebook.md': 32_000, 'deck-notes-general.md': 30_000}
REQUIRED = {'slides-rulebook.md', 'questions-rulebook.md'}   # the notes exist only once a course has started
MAX_BLOCK_LINES = 40

args = [a for a in sys.argv[1:] if not a.startswith('--')]
folder = pathlib.Path(args[0] if args else '.')
sections = '--sections' in sys.argv
problems = missing = 0

for name, cap in CAPS.items():
    path = folder / name
    if not path.exists():
        if name in REQUIRED:
            print(f'COULD NOT CHECK: {name} not in {folder.resolve()}'); missing += 1
        else:
            print(f'{name}: not here (skipped)')
        continue
    text = path.read_text(encoding='utf-8')
    n = len(text)
    state = 'ok' if n <= cap else f'OVER by {n - cap:,}'
    print(f'{name}: {n:,} chars | ~{n // 4:,} tokens | cap {cap:,} ({100 * n / cap:.0f}%) | {state}')
    if n > cap:
        problems += 1
        print('  * merge or retire something before adding more (slides-rulebook section 0, notes W11)')
    if name in REQUIRED:
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            if re.match(r'^\s*```', lines[i]):
                j = i + 1
                while j < len(lines) and not re.match(r'^\s*```\s*$', lines[j]):
                    j += 1
                if j - i - 1 > MAX_BLOCK_LINES:
                    problems += 1
                    print(f'  * a {j - i - 1}-line code block at line {i + 1}: move it to deck-tools as a file and point to it')
                i = j + 1
            else:
                i += 1
        for k, line in enumerate(lines, 1):
            if re.match(r'^>?\s*\*\*Changes in \d', line):
                problems += 1
                print(f'  * a version note at line {k}: move it to rulebooks-changelog.md (keep one "New in" line)')
    if sections:
        parts = re.split(r'(?m)^(?=## )', text)
        for p in parts:
            head = p.split('\n', 1)[0] if p.startswith('## ') else '(top of file)'
            print(f'    {len(p):>7,}  {100 * len(p) / n:4.1f}%  {head[:70]}')

if missing:
    sys.exit(2)
print('RESULT: ' + ('clean' if not problems else f'{problems} to fix'))
sys.exit(1 if problems else 0)
