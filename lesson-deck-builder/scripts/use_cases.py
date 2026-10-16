#!/usr/bin/env python3
"""
Keep components.md and use-cases.md in sync (skill maintenance — not deck validation).

Usage:
  python scripts/use_cases.py           check only; exit 1 on any problem
  python scripts/use_cases.py --write   regenerate every reverse index in use-cases.md, then check

Checks:
  - every use case named in a component's "Suggested for" list exists in use-cases.md,
    with the same headline
  - ranks inside each list run 1..n with no duplicate use case
  - every numbered component has a list; every use case is used by at least one component
  - every reverse index in use-cases.md matches the lists (run --write after editing lists)
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMP = ROOT / "references" / "components.md"
UCF = ROOT / "references" / "use-cases.md"


def parse_use_cases(text):
    return {m.group(2): m.group(1) for m in re.finditer(r"^## (.+) \(`([a-z-]+)`\)\s*$", text, re.M)}


def parse_components(text):
    comps, cur, in_list = [], None, False
    for line in text.splitlines():
        h = re.match(r"^#{2,3} (\d+[a-z]?)\. (.+?)\s*$", line)
        if h:
            cur = {"num": h.group(1), "title": h.group(2), "uc": []}
            comps.append(cur)
            in_list = False
            continue
        if cur is None:
            continue
        if line.startswith("**Suggested for**"):
            in_list = True
            continue
        if in_list:
            m = re.match(r"^(\d+)\. (.+) `([a-z-]+)`\s*$", line)
            if m:
                cur["uc"].append((int(m.group(1)), m.group(3), m.group(2)))
                continue
            in_list = False
    return comps


def natkey(num):
    m = re.match(r"(\d+)([a-z]?)", num)
    return (int(m.group(1)), m.group(2))


def index_line(uid, comps):
    rows = sorted(((r, natkey(c["num"]), c) for c in comps for (r, u, _) in c["uc"] if u == uid),
                  key=lambda x: (x[0], x[1]))
    if not rows:
        return "**Components that suit it:** none yet."
    items = [f"§{c['num']} {c['title']} (#{r})" for r, _, c in rows]
    return "**Components that suit it** (best fit first; #n = its rank in that component's list): " + " · ".join(items)


def main():
    write = "--write" in sys.argv
    comp_text, uc_text = COMP.read_text(encoding="utf-8"), UCF.read_text(encoding="utf-8")
    ucs, comps = parse_use_cases(uc_text), parse_components(comp_text)
    problems, notes = [], []

    # a pointer heading whose sub-sections (e.g. 32 → 32a, 32b…) carry the lists needs none itself
    parents = {re.match(r"\d+", c["num"]).group(0) for c in comps if re.search(r"[a-z]$", c["num"])}
    comps = [c for c in comps if c["uc"] or c["num"] not in parents]
    for c in comps:
        if not c["uc"]:
            problems.append(f"§{c['num']} {c['title']}: no Suggested-for list")
            continue
        ranks = [r for r, _, _ in c["uc"]]
        if ranks != list(range(1, len(ranks) + 1)):
            problems.append(f"§{c['num']}: ranks must run 1..n, found {ranks}")
        ids = [u for _, u, _ in c["uc"]]
        if len(ids) != len(set(ids)):
            problems.append(f"§{c['num']}: a use case is listed twice")
        for _, u, head in c["uc"]:
            if u not in ucs:
                problems.append(f"§{c['num']}: unknown use case `{u}` (define it in use-cases.md)")
            elif head != ucs[u]:
                problems.append(f"§{c['num']}: headline for `{u}` is '{head}', catalogue says '{ucs[u]}'")
    used = {u for c in comps for _, u, _ in c["uc"]}
    for u in ucs:
        if u not in used:
            notes.append(f"use case `{u}` is not suggested by any component")

    new = uc_text
    for u in ucs:
        pat = re.compile(r"(<!-- idx:" + re.escape(u) + r" -->)(.*?)(<!-- /idx -->)", re.S)
        if not pat.search(new):
            problems.append(f"use-cases.md: missing reverse-index markers for `{u}`")
            continue
        new = pat.sub(lambda m: m.group(1) + "\n" + index_line(u, comps) + "\n" + m.group(3), new)
    if write and new != uc_text:
        UCF.write_text(new, encoding="utf-8")
        print("reverse index refreshed")
    elif new != uc_text:
        problems.append("use-cases.md reverse index is out of date — run: python scripts/use_cases.py --write")

    print(f"components with lists: {sum(1 for c in comps if c['uc'])}   ·   use cases: {len(ucs)}")
    for n in notes:
        print(f"⚠ {n}")
    for p in problems:
        print(f"✗ {p}")
    print("✓ in sync." if not problems else "\nNOT in sync.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
