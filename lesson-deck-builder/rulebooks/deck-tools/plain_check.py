#!/usr/bin/env python3
"""plain_check.py - language, independence and word-ceiling checker for every route of lesson-deck-builder
(slides-rulebook 2.0, lessons-rulebook 2.0, lesson-deck-builder v1.4).

Usage:  python plain_check.py deck.html [--max-level A2|B1|B2|C1] [--max-sentence N]
                                        [--max-words 110] [--known words.txt] [--cs-grad]
                                        [--budget N] [--ceiling 2.0]
Level:  the course's English level (SKILL.md, "English level"). The sentence cap follows it unless
        --max-sentence is given: A2 15 · B1 20 · B2 25 · C1 30.
        The word list stops at B2. At C1 every listed word counts as known, and so does any other
        word at least as common as wordfreq Zipf 3.5 (needs wordfreq); rarer words are flagged.
--cs-grad: also count as known the words a computer-science graduate uses daily (lessons-rulebook L1).
Needs:  pip install wordfreq   (fallback for irregular word forms)
Word list: CEFR-J Vocabulary Profile 1.5 (Tono Laboratory, TUFS), downloaded on first run.
Original (lecture decks): read from <!-- BUDGET original=N --> in the deck, or --budget N.
Ceiling: N x --ceiling (default 2.0, slides-rulebook G5); only a deck over it is flagged.
        Without a BUDGET comment (lessons) the checker reports the deck's word count only.
        Elements marked data-budget="skip" are checked but not counted (settings §11 only).
"""
import csv, re, sys, os, argparse, urllib.request
from html.parser import HTMLParser

LIST_URL = ("https://raw.githubusercontent.com/openlanguageprofiles/"
            "olp-en-cefrj/master/cefrj-vocabulary-profile-1.5.csv")
LIST_FILE = "cefrj-vocabulary-profile-1.5.csv"
SKIP = {"script", "style", "code", "pre", "kbd", "samp", "math", "svg", "var"}
BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "div", "td", "th", "dt", "dd",
         "figcaption", "button", "label", "br", "blockquote", "aside", "section", "textarea"}
PIECES = {"lf-pin"}                  # figure labels (components §22): separate pieces, not one sentence
HIDDEN = {"gl-card"}                 # on-demand gloss cards (components §24): checked, not counted as visible
VOID = {"br", "img", "input", "hr", "meta", "link", "source", "wbr", "area", "col", "embed", "track"}
# field vocabulary a CS student already owns (L1); extend per course with --known FILE
FIELD = set("""data hardware software computer computers file files byte bytes kilobyte megabyte gigabyte
terabyte database databases compile compiled compiler code program programs programming network networks
internet online app apps laptop laptops keyboard mouse printer monitor screen server servers website
browser browsers download upload digital chip chips wireless click user users password email""".split())
# --cs-grad: words a computer-science graduate owns (lessons-rulebook L1)
CS_GRAD = set("""algorithm algorithms function functions variable variables loop loops array arrays string strings integer integers
boolean input inputs output outputs debug debugging install installed update updates version versions folder folders
smartphone smartphones pixel pixels binary bit bits processor processors interface interfaces parallel sequential
reboot startup cloud dataset datasets repository repositories script scripts terminal petabyte petabytes""".split())
SENTENCE_CAP = {"A2": 15, "B1": 20, "B2": 25, "C1": 30}
C1_ZIPF = 3.5   # C1 (design choice): an off-list word at least this common (wordfreq Zipf) counts as known
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-\.]*")
BACKREF = re.compile(r"\b(as (we|you) (saw|learned|learnt|discussed|said|explained|mentioned)"
                     r"|as (mentioned|discussed|explained|shown) (before|earlier|above)"
                     r"|(mentioned|discussed|explained|defined|shown) (earlier|before|above|previously)"
                     r"|recall (that|from|the)|remember (that|from)|aforementioned|(?<!of )the above"
                     r"|(earlier|previous|last|next) (slide|section|part|lesson|page)"
                     r"|see (above|below|slide))\b", re.I)
MCQ_FLAGS = re.compile(r"\b((?i:all of the above|none of the above)|NOT|EXCEPT)\b")
CAPS_OK = {"NOT", "EXCEPT", "ALL", "NO", "OR", "AND", "I", "A", "OK"}
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ed|\w+en)\b", re.I)


class Deck(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides, self.stack, self.skip, self.hide, self.tmpl, self.unc = [], [], 0, 0, 0, 0
        self.in_dfn = self.in_slide = False
        self.gloss, self.in_gl, self.in_dt = [], False, False

    def _nl(self):
        self.slides[-1]["hid" if self.hide else "text"] += "\n"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        if tag == "section" and "slide" in cls:
            self.slides.append({"text": "", "hid": "", "cnt": "", "dfn": [], "for": set(), "forms": set(),
                                "sec": a.get("data-sec")})
            u = int(a.get("data-budget") == "skip")     # a whole slide outside the budget (the final quiz)
            self.stack, self.skip, self.hide, self.tmpl, self.unc, self.in_slide = [("section", 0, 0, 0, 0, u)], 0, 0, 0, u, True
            return
        if not self.in_slide:
            return
        skip = int(tag in SKIP or "formal" in cls)      # .formal = exact slide wording, not checked
        hid = int(bool(HIDDEN & cls) or a.get("role") == "tooltip")
        tm = int(tag == "template")
        unc = int(tag in {"script", "style", "svg", "math"}     # not readable text: never counted
                  or a.get("data-budget") == "skip")            # settings §11: content excluded from the budget
        piece = int(tag in BLOCK or bool(PIECES & cls) or (tag == "b" and self.hide > 0) or self.tmpl > 0 or tm)
        if tag not in VOID:
            self.stack.append((tag, skip, hid, piece, tm, unc))
            self.skip += skip; self.hide += hid; self.tmpl += tm; self.unc += unc
        if a.get("data-for"):
            self.slides[-1]["for"].add(a["data-for"].strip().lower())
        if a.get("data-why"):                           # quiz feedback is readable text
            self.slides[-1]["hid"] += "\n" + a["data-why"] + "\n"
            if not self.unc:                            # feedback on a skipped (quiz) slide stays outside the budget too
                self.slides[-1]["cnt"] += "\n" + a["data-why"] + "\n"
        if tag == "dl" and (a.get("id") == "glossary" or "glossary" in cls):
            self.in_gl = True
        if tag == "dt" and self.in_gl:
            self.in_dt = True
            self.gloss.append({"key": a.get("data-term", ""), "text": "",
                               "forms": [f.strip() for f in (a.get("data-forms") or "").split(",") if f.strip()]})
        if tag == "dfn":
            self.in_dfn = True
            self.slides[-1]["dfn"].append("")
            for f in (a.get("data-forms") or "").split(","):
                if f.strip():
                    self.slides[-1]["forms"].add(f.strip().lower())
        if piece:
            self._nl()

    def handle_endtag(self, tag):
        if tag == "dl":
            self.in_gl = False
        if tag == "dt":
            self.in_dt = False
        if not self.in_slide or not any(e[0] == tag for e in self.stack):
            return
        while self.stack:
            t, skip, hid, piece, tm, unc = self.stack.pop()
            self.skip -= skip; self.hide -= hid; self.tmpl -= tm; self.unc -= unc
            if piece:
                self._nl()
            if t == "dfn":
                self.in_dfn = False
            if t == tag:
                break
        if not self.stack:          # the slide's own </section>
            self.in_slide = False

    def handle_data(self, data):
        if self.in_dt and self.gloss:
            self.gloss[-1]["text"] += data
        if self.in_slide and not self.unc:              # budget count: formal wording and code count too (G5)
            self.slides[-1]["cnt"] += " " + data
        if not self.in_slide or self.skip:
            return
        if self.hide:
            self.slides[-1]["hid"] += data
            return
        self.slides[-1]["text"] += data
        if self.in_dfn:
            self.slides[-1]["dfn"][-1] += data


def load_levels():
    if not os.path.exists(LIST_FILE):
        try:
            urllib.request.urlretrieve(LIST_URL, LIST_FILE)
        except Exception as e:
            sys.exit(f"Could not download the word list ({e}).\n"
                     f"Download it by hand from {LIST_URL}\nand save it next to this script as {LIST_FILE}.")
    lv = {}
    with open(LIST_FILE, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            for h in r["headword"].split("/"):
                h = h.strip().lower()
                if h and " " not in h:
                    lv[h] = min(lv.get(h, "C"), r["CEFR"])
    return lv


def lemmas(w):
    c = [w]
    for suf, rep in (("ies", "y"), ("ied", "y"), ("ier", "y"), ("iest", "y"), ("ily", "y"),
                     ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e"),
                     ("er", ""), ("er", "e"), ("est", ""), ("est", "e"), ("ly", ""), ("'s", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 2:
            stem = w[: -len(suf)] + rep
            c.append(stem)
            if rep == "" and len(stem) > 2 and stem[-1] == stem[-2]:
                c.append(stem[:-1])  # stopped -> stop
    return c


def level_of(w, lv, zipf):
    for c in lemmas(w):
        if c in lv:
            return lv[c]
    if zipf and zipf(w, "en") >= 5.0:   # very common irregular forms: went, children
        return "A2"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--max-level", default="B1", choices=["A2", "B1", "B2", "C1"])
    ap.add_argument("--max-sentence", type=int, default=None, help="default: the level's cap (A2 15, B1 20, B2 25, C1 30)")
    ap.add_argument("--max-words", type=int, default=110)
    ap.add_argument("--known", help="extra field words a student already owns, one per line")
    ap.add_argument("--budget", type=int, help="original's total words (overrides the BUDGET comment)")
    ap.add_argument("--cs-grad", action="store_true", help="also count a computer-science graduate's daily words as known")
    ap.add_argument("--ceiling", type=float, default=2.0,
                    help="word ceiling as a multiple of the original (G5; default 2.0)")
    o = ap.parse_args()
    if o.max_sentence is None:
        o.max_sentence = SENTENCE_CAP[o.max_level]
    try:
        from wordfreq import zipf_frequency as zipf
    except ImportError:
        zipf = None
        print("note: wordfreq not installed; irregular forms may be flagged")
    lv = load_levels()
    known = set(FIELD) | (CS_GRAD if o.cs_grad else set())
    if o.known:
        known |= {l.strip().lower() for l in open(o.known, encoding="utf-8") if l.strip()}
    raw = open(o.html, encoding="utf-8").read()
    m = re.search(r"<!--\s*BUDGET\s+original=(\d+)", raw)
    budget = o.budget or (int(m.group(1)) if m else None)
    # a magic board shows one state at a time: keep only the last of each run of <template>s
    raw = re.sub(r"(?:<template\b[^>]*>.*?</template>\s*)+",
                 lambda g: re.findall(r"<template\b[^>]*>.*?</template>", g.group(0), re.S)[-1], raw, flags=re.S)
    p = Deck()
    p.feed(raw)
    gl_terms = {x.strip().lower() for g in p.gloss for x in [g["key"] or g["text"], g["text"], *g["forms"]] if x.strip()}
    terms = {t.strip().lower() for s in p.slides for t in s["dfn"] if t.strip()} | gl_terms
    forms = {f for s in p.slides for f in s["forms"]}
    term_words = {w for t in terms | forms for w in re.findall(r"[a-z]+", t)}
    problems = 0
    deck_known = deck_total = deck_words = 0
    for i, s in enumerate(p.slides, 1):
        visible = re.sub(r"[ \t]+", " ", s["text"])
        text = visible + "\n" + re.sub(r"[ \t]+", " ", s["hid"])
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        sents = [x for l in lines for x in re.split(r"(?<=[.!?])\s+", l) if x.strip()]
        n_vis = len(WORD.findall(visible))
        deck_words += len(WORD.findall(s["cnt"]))
        notes = []
        if n_vis > o.max_words:
            notes.append(f"{n_vis} visible words (soft cap {o.max_words}) - split the slide or move facts into the figure")
        for x in sents:
            n = len(re.findall(r"[A-Za-z0-9]+", x))
            if n > o.max_sentence:
                notes.append(f"long sentence ({n} words): {x[:70]}...")
        known_n = total = 0
        hard, offlist, names, acr = set(), set(), set(), set()
        for x in sents:
            toks = re.findall(r"[A-Za-z][A-Za-z']*", x)
            if toks and sum(t[0].isupper() for t in toks) >= 0.6 * len(toks):
                toks = [t if t.isupper() else t.lower() for t in toks]  # Title Case heading
            for j, t in enumerate(toks):
                for part in t.split("-"):
                    if not part:
                        continue
                    if len(part) >= 2 and part.isupper():
                        if part not in CAPS_OK:
                            acr.add(part)
                        continue
                    if j > 0 and part[0].isupper():
                        names.add(part)
                        continue
                    w = part.lower().strip("'")
                    total += 1
                    if any(c in term_words or c in known for c in lemmas(w)):
                        known_n += 1
                        continue
                    L = level_of(w, lv, zipf)
                    if L and L <= o.max_level:
                        known_n += 1
                    elif L:
                        hard.add(w)
                    elif o.max_level == "C1" and zipf and zipf(w, "en") >= C1_ZIPF:
                        known_n += 1        # C1: past the B2 list, a common word counts as known
                    else:
                        offlist.add(w)
        deck_known += known_n
        deck_total += total
        cov = 100.0 * known_n / total if total else 100.0
        if total >= 50 and cov < 98:   # short slides: judge coverage at deck level
            notes.append(f"word coverage {cov:.1f}% (target >= 98%)")
        if hard:
            notes.append("above " + o.max_level + ": " + ", ".join(sorted(hard)))
        if offlist:
            notes.append("not in list (replace, define with <dfn>, or add to --known): " + ", ".join(sorted(offlist)))
        covered = {t.strip().lower() for t in s["dfn"]} | s["for"] | gl_terms   # glossary terms are glossed at runtime (T5b)
        low = text.lower()
        for t in sorted(terms - covered):
            if re.search(r"\b" + re.escape(t) + r"(s|es)?\b", low):
                notes.append(f"term '{t}' used without a gloss on this slide (add it to the glossary or a data-for gloss)")
        for a in sorted(acr):
            if not any(a.lower() in c.split() or a.lower() == c for c in covered):
                notes.append(f"acronym {a} not expanded on this slide (add it to the glossary or a data-for gloss)")
        for mm in BACKREF.finditer(text):
            notes.append(f"back-reference: '{mm.group(0)}' - restate the idea instead")
        for mm in MCQ_FLAGS.finditer(text):
            notes.append(f"question wording: '{mm.group(0)}' - avoid in questions")
        pas = len(PASSIVE.findall(text))
        if pas > 2:
            notes.append(f"{pas} possible passive forms - prefer active voice")
        if notes:
            problems += 1
            print(f"\n--- slide {i} ---")
            for n in notes:
                print("  * " + n)
        if names:
            print(f"  (slide {i} names, check they need no gloss: {', '.join(sorted(names))})")
    # topics (N1)
    sizes = []
    for s in p.slides:
        if s["sec"] is not None or not sizes:
            sizes.append([s["sec"] or "(none)", 0])
        sizes[-1][1] += 1
    print()
    if not any(s["sec"] for s in p.slides):
        print("topics: none - mark the first slide of each topic with data-sec (N1)")
        problems += 1
    else:
        print("topics: " + " | ".join(f"{n} {k}" for n, k in sizes))
        tiny = [n for n, k in sizes if k < 2]
        two = [n for n, k in sizes if k == 2]
        if tiny:
            print("  * topic with 1 slide - merge it (N1): " + ", ".join(tiny))
            problems += 1
        if two:
            print("  note: 2-slide topic, keep its label very short (N1): " + ", ".join(two))
    dc = 100.0 * deck_known / deck_total if deck_total else 100.0
    print(f"{len(p.slides)} slides, {len(terms)} defined or glossary terms, {problems} items to fix or justify")
    print(f"deck word coverage: {dc:.1f}% at {o.max_level} or below (target >= 98%)")
    if budget:
        cap = int(budget * o.ceiling)
        print(f"deck words (all readable text): {deck_words} / original {budget} "
              f"({100.0*deck_words/budget:.0f}%; ceiling {o.ceiling:g} x = {cap} words)")
        if deck_words > cap:
            print(f"  * over the word ceiling (G5) by {deck_words - cap} words - cut the deck's own "
                  "additions (W4), never a fact or its exact wording")
            problems += 1
    else:
        print(f"deck words (all readable text): {deck_words} (no BUDGET comment: no word ceiling to check)")
    if dc < 98:
        problems += 1
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
