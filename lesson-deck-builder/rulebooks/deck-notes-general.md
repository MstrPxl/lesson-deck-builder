# Slides → lesson deck: general notes

**Version 23 Oct 2026** · for `slides-rulebook.md` 2.0.1, `lessons-rulebook.md` 2.1, `questions-rulebook.md` 1.4, `deck-tools` 1.7, `lesson-deck-builder` v1.4 · drawn from Applied OS decks 1–4, 210 ISY decks 1–5 and DB decks 1–4.

---

## 0. How these notes work

**Three homes, three kinds of knowledge:**

| Kind | Home | Example |
|---|---|---|
| A rule, or code every deck needs | The rulebooks; their code in `deck-tools` | The topic bar, the phone layer, the quiz script |
| Experience that helps any course, but isn't a rule | **This file** | How to plan the word budget; figure pitfalls; how to check a phone |
| Facts about one course | The deck's COURSE record (lessons: DECK-SETTINGS) | Decisions, field words, the lecturer's slide habits, reusable figures, what comes next |

- **This file ships with the skill** (`rulebooks/`); nothing is attached or sent back. A course's facts travel inside its decks (slides-rulebook W11).
- **Read order:** the route's rulebooks and the skill first; then the parts of this file that help.
- **Who wins:** the user's latest instruction, then the rulebooks, then these notes. These notes don't add rules.
- **Advice for the models of their date.** The notes and the deck tools are helpers, not requirements. When you have a better method, use it and name it on the report's "Departures" line. If it proves better, it replaces the point here (W11).
- **Nothing here limits components.** Earlier decks' components and figures are examples; the skill's full catalog is always open.

**Updating:** only in a maintenance session, from the reports' "Proposed for the skill" lines: merge, don't append; a point that becomes a rule leaves this file; cap about 30,000 characters (`deck-tools/size_check.py`). The copy in the skill is the current one.

---

## 1. Where the tokens go (a typical run)

| Phase | Typical cost | How to keep it down |
|---|---|---|
| Reading rulebooks, notes, SKILL.md, `use-cases.md`, `components.md` | ~60–70K since rulebooks 1.9/1.3 (estimated; 75–90K before) | `components.md` by sections; with a shell, skip `template.html` and exemplars |
| Reading the lecture | 15–30K | Text layer first; 2×2 page tiles; re-render only figure pages (§2.3) |
| Research | 5–12K | 1–2 searches per doubt (§7). One broad research subagent once cost 141K |
| Drafting, then trimming to the ceiling | The biggest variable | Plan per-topic words before drafting (§3), so drafts land under the 2 × ceiling; each trimming pass costs ~25K |
| Screenshots | 40–60K | Contact sheets; re-shoot only changed slides (§9) |
| Checks | small | One script (§9) instead of walking by hand |
| Independent check (rulebook F1b) | 115–155K first pass, ~10–20K later | Only the text dumps; resume the same checker |

Avoidable losses: a rejected plan (always one deck per lecture), a broad research pass, a dense diagram placed by hand (§5).

---

## 2. Pipeline

### 2.1 A later deck of a course (rulebook case B)

The newest deck is the shell: everything except the slides, reused unchanged. Split it once:

```python
s = open(NEWEST).read()
B = '<!-- ================= BEGIN SLIDES ================= -->'; E = '<!-- ================= END SLIDES ================= -->'
head = s.split(B)[0] + B + '\n'; tail = E + s.split(E)[1]
import re; tail = re.sub(r'<!-- (COVERAGE-MAP|SOURCES|COURSE|BUDGET|QUIZ-MAP).*?-->\n?', '', tail, flags=re.S)
```

- Copy the COURSE record into the new deck's comments before stripping it; raise the deck number.
- Only `<title>` and the brand text in the top bar are deck-specific.
- The quiz slides go with the slides; the quiz code stays in the shell.
- Don't read the shell's slides in full: list them (heading, `data-sec`, classes used) with a short script, then print only the 3–5 whose markup you want.
- Keep the deck's new CSS in its own file; a small make script injects it before the head's `</style>` and runs `build.py`.
- The shell is a source of code, not a list of allowed components. A component no earlier deck used: take its code from `components.md`, add it to the shell, and the next deck inherits it.

### 2.2 The first deck of a course (rulebook case A)

- **Ask the canvas gate early**, right after reading the lecture, with the English level, the exam focus and any slideless agenda topics in the same round. A tappable question works. Six boards don't fit four options: list all six in the question text and offer four, with "Other" for the rest. Offer `assets/style-samples/sketchbook-chalkboard.html` as a preview file.
- **Build from the skill's `template.html`** plus `deck-tools/snippets/`. Pull every block out of the files with a script, never retype it:

```python
t = open(SKILL + '/assets/template.html').read()
head = t.split('<!-- ================= BEGIN SLIDES (fill from components.md) ================= -->')[0]
i = t.index('<script>\n  /* ---- deck engine') + len('<script>'); engine = t[i:t.index('</script>', i)]
blocks = lambda md, lang: re.findall(r"```" + lang + r"\n(.*?)```", md, re.S)
snip = lambda f: open('deck-tools/snippets/' + f, encoding='utf-8').read()   # rulebook code: snippets/README.md lists it
# components.md: the first ```js after a component's heading
```

- Set `data-canvas` and `data-board` on `<html>`, the English fonts, `--display-w:700`, and `viewport-fit=cover`.
- **Pitfalls of a template build:** `components.md` JS blocks carry the comment `// inside the deck's single <script>` (strip it, or the validator counts extra scripts); the §31 defs block holds an example `<g class="live">` (insert only the `<filter>` lines, or its interval throws forever); the quiz's base styles are missing from `quiz.css` (§11): add them.
- **Start the COURSE record's memory lines** (habits, reusable figures, next) at the end of the run.

### 2.3 Reading the slides cheaply

- `pdftotext -layout` first: the inventory source and the budget's text count (drop footer lines; they can be glued to a body line's end).
- Render at 72 dpi and tile 2×2 with PIL to see figures and highlights; re-render only figure pages at 160–220 dpi.
- **Figure words:** vector figures' labels are in the text layer (they add 0). Copied textbook figures are images: OCR misses light or tiny labels, so type the labels or cells into `audit/figures.txt` (it doubles as the checker's transcription) and count with the budget regex. Say how in the `BUDGET` comment.
- Read the text layer of every figure page: some boxes exist only there.
- Check with pypdf for speaker notes and annotations.

### 2.4 Then

Inventory with teaching jobs → per-topic budget (§3) → narrow research (§7) → slides in part files, one per topic (`p01_…` …), built and counted after **every** part → quiz (§8) → checks (§9) → report.

---

## 3. The word budget

The user's cap (rulebook 1.8, G5): deck words ≤ **2 × the source's** (text + figure words), never more; no slide-count limit. The room above 100% buys digestion (rulebook §1, "Where the extra words go"); it is a limit, not a target.

**Plan the arc at its real size first**, then the facts and their exact wording; digestion gets the rest.

| Arc piece | Typical words |
|---|---|
| Cover | 12–30 (a hint line counts) |
| Opening challenge | 55–65; keep the problem to ~25 words, because the revisited slide prints it again |
| Map | 12–30 |
| Challenge revisited | 80–100 |
| Recap ("You can now") | 30–50 |
| Glossary slide | ~5 words per entry; 20–27 entries = 100–145 |

Real arcs have run 300–460 words: 10–18% of a small lecture's ceiling, over 20% under 1,000 source words, so short lectures are the tightest. Admin and agenda pages give back only 50–200.

**Per-topic words.**

- Sum each topic's source words (text + figure words of its pages).
- Aim each topic's draft at **~1.6–1.7 ×** its source (the deck plans at ~1.8 ×; the arc takes the rest); under ~1,300 source words, ~1.5 ×. Drafts land 5–10% higher than aimed. *Untested under 1.8: replace with measured numbers.*
- Short lists of names cost near 100% of their source even at their tightest (a 2–4-word gloss each); long bullets compressed to ~70–80%, so they hold full sentences and examples most easily.
- **Exact definitions (rulebook F2) cost more, the more of the lecture is definitions.** Under v1.7 (exact wording could pass the cap) 210 ISY decks 2–5 ended at 119–213% of the source, DB decks 1–4 at 168–232%: the top of each range would now be over. Quoted words alone were 78% (DB deck 3) and 87% (deck 4: 2,708 of 3,096). A 23–29-entry glossary costs 215–230 words; 33 entries, 316.
- **Estimate the floor early:** quoted words + ~35% for their glosses + the arc + the glossary. The rest of 2 × is the room for examples; a definition-heavy lecture gets one short example per concept and no second ones. A floor over 2 ×: ask (rulebook W5).
- A per-topic line in `build.py` shows at once which topic is over.

**Over the ceiling** (rulebook W4 gives the order; re-check the ledger after each pass): the repeats that cost no ease are a lead that repeats the h2; part tags beyond topic openers; "Notice:" lines that repeat a figure; figure labels that repeat a glossary meaning; a term repeated under a heading that names it (put `<dfn>` on the heading). Also free: a key instead of a repeated word; one table instead of several slides of bullets; short F4 notes. Glossary entries shrink only while every half, qualifier and scope stays (§7).

**Count method:** W1b's regex on both sides (it splits at underscores: `Student_number` is 2 words on both sides); report the checker's number.

---

## 4. The language checker

Setup: `setup_tools.sh` (deck tools, §12) copies `plain_check.py` into your working folder and fetches its word list. Run it with the course's level (`--max-level`) and `--known known.txt`.

**Coverage wins at zero words**, best first:

1. Field words by the L1 set test, written to the COURSE record and `known.txt`. The lemmatizer doesn't reduce "-ion" or "-er" forms: list `execution`, `attackers` and the like separately.
2. `<dfn>` on slide terms that already have a visible gloss beside them, and on gloss-line head words ("Implicit: …"; a script turns every `.rd` `<b>word</b>:` into `<dfn>`; DB deck 1: 95.4% → 98.8%, deck 4: 94.1% → 97%). The cost: each becomes a term, so its later unglossed uses are flagged; put everyday heads back to `<b>` (Set, Valid, Existing, Sequence, Data type).
3. `<code>` around code names and file names; `<pre class="code">` for listings (skipped by the language check, still counted). Record, table, entity and attribute names (STUDENT, COMPANY, WORKS_FOR, Ssn) too, styled as text (`code.rn{font:inherit}`), or they are read as acronyms; wrap them in prose with a script that skips tags. Sample-data cells: values from a slide or figure get `.formal`; the deck's own sample values get `code.rn`, never `.formal` (the checker reads «» around invented or recombined values as misquotes).
4. `data-forms` long forms on acronym entries (`PC` → "program counter").
5. Plain swaps (halt → stop, resume → continue, employees → staff, persistence → many tries, assess → check).
6. An exam list kept word for word (names only, taught on the next slides): `class="formal"` on each name. The wording is protected and the checker skips it.

**The glossary script** (rulebook B2):

- It wraps the **first** match of each entry in order, so list compound terms (and long `data-forms`) before the single words they contain.
- A slide counts as the defining slide only when the `<dfn>` text equals the `<dt>` text (lower-cased); put other forms in `data-forms`.
- It skips headings, figure labels (`.lf`), the eraser (`.er`), buttons and formal text. A load-bearing term that appears only there gets no card; put it in a text line too.

**Known noise** (report, don't chase): hyphenated words split ("wi", "fi"); words glued across adjacent spans (add a space); "means", "known", "version" and irregular past forms (shown, drawn) flagged; Title-Case-looking lines and line-initial names; capitals and acronyms inside `data-why`; `<dfn>` inside `.formal` unseen; gloss flags in a recap, before a defining slide, or in the quiz (it uses the terms it tests); term names on figure pins (put `data-for="term"` on the pin); gloss lines beside quotes repeat the hard word, so coverage drops a little.

---

## 5. Figures

**Pitfalls that cost rework:**

- **Build wrappers for labels** (V2): an `.lf-layer`, absolute, `inset:0`.
- **Moving glyphs:** the template forces `svg [data-build]{transform:none}`; put the motion on a child group with a start offset.
- **Translucent fills let lines show through:** use an opaque fill on shapes that lines run into, and draw lines before the shapes they end at.
- **Overlaps:** place labels in empty bands, away from the lines that cross a figure. Expect one fix round per complex figure.
- **Nested two-column grids shrink figures** to unreadable; stack inside each half instead. Give a wide figure the wide column.
- **A CSS time axis beats an SVG one** with `preserveAspectRatio="none"` (it stretches the arrowhead).
- **New buttons inside `.nav`** inherit `.nav button`: scope them.
- **Class-name clashes:** the template's badge `.num{position:absolute}` hides the quiz's `input.gap.num` (set it `static`); a `.stack{display:grid}` helper squashes a phone-layer `table.tbl.stack` on laptops (set `table.tbl{display:table}`).
- **Gloss cards inherit `white-space:nowrap`** from a nowrap cell or label and push the slide sideways at 320 px: set `.gl-card{white-space:normal}` (`checks.py` catches it, `measure.py` doesn't). Mark exact slide labels that arrive with a build `.formal`, which the glossary skips.
- **Sample-data tables that are the lesson** keep their grid on phones: `<wbr>` after underscores in headers (not zero-width spaces), long cells wrap, .68rem under 400 px.
- **A wide table in one `.g2` column widens the whole phone grid** (sideways scroll at 320 px): set `.g2{grid-template-columns:minmax(0,1fr)}` under 881 px; stack 3-column comparison tables, the first cell as the row's heading. A `<pre>` in a `.g2` column needs `min-width:0` on its column, or it widens the laptop grid too. A 7-column figure table scrolls inside a `.tscroll` box with `data-capture`; a flex row of small sample tables needs `overflow-x:auto` + `data-capture` on each child at 320 px.
- **Code listings with per-line builds:** one `<span class="ln">` per line, joined with real newlines (`display:inline-block;min-width:100%`). A global `</span><span` → `</span> <span` substitution once put the whole listing on one line.
- **No `.tbl-wrap` around a table that stacks on phones:** the phone layer marks every `.tbl-wrap` `data-capture`, so a full-slide table would block swipes. Use a plain wrapper.

- **Variant figures from one generator** copy parts into variants whose source lacks them: check each against its own page. Facts only a drawing carries go in a "Notice:" line or the checker's figure descriptions.
- **Paper chips inside a slide:** scope their dark ink under a parent class with `!important`.

**Label sizes:** keep viewBoxes ~400–700 wide so one unit is about one pixel on a laptop.

**Phone variants of wide figures** (rulebook Appendix B5): only when an upright drawing can't work; main object top-left with its labels to its right, the second below, the link running down between them.

**A list that must stay exact (rulebook F2) beside a picture of where each item acts:** quote the list in order as a numbered list, and put only the numbers on the figure (`.fq-mark` circles), with the picture labelled `ours`. Labels that paraphrase the items fail the exact-wording check.

**Cheaper than a phone variant:** draw the figure near-square or upright from the start; nothing then needs a second drawing. A figure with 6+ labels works upright (about 400 × 440) beside its text in a `g2` on laptops; a dense diagram (DB deck 3, Figure 7.2: 32 shapes, 45 labels) fits one portrait drawing of about 505 × 735 units, shown 420 px wide on laptops. Expect one or two label-placement rounds per figure at phone width.

**Node-and-line diagrams (ER, flowcharts): generate, don't hand-place.** `deck-tools/er.py` sizes each shape from its label (14.6 units, the 11 px floor at 358 px in a ~500-unit drawing), clips lines to shape edges, draws double lines and anchors line ends at chosen points (diamond tips). Place cardinality and role labels as absolute pins. `figshot.py` screenshots one figure at 2× to check overlaps.

**A figure that repeats another with new labels** (an ER diagram redrawn with (min, max) pairs): a table of the new labels plus one small drawing of a single relationship in both notations teaches the difference; label the table `ours`. **Instance diagrams** (dots joined by lines): a table, one row per instance, said so in the caption. To read a dense line figure, render at 300 dpi and sample the darkness along each candidate segment.

---

## 6. Components and the engine

- Choose each slide's component by its teaching job from the whole catalog, and vary them.
- **What has worked:** an opening challenge on the lecture's most counter-intuitive fact, solved on the revisit with the slides' own data; builds with accumulating captions for any order of events; labels on the figure for parts; a linked figure only where one sentence names 2–3 parts; the magic board when the *same* items move; the eraser for a misconception (it follows builds on the revisit); one line-boil element; an HTML lane grid for timelines; an HTML flow (`.pipe`) for a process, with builds; small labelled sample tables beside quoted rules; quoted definitions as a term label over a small quote list, with a "word: meaning" line under it.
- **Lecture trees:** `.tree3` (210 ISY deck 3, three branches) and `.tree3.t2` with `.kidsN` for uneven branches (deck 4): HTML boxes, CSS connectors, stacked on phones; numbered marks turn it into a Label the figure item.
- **A glossary of 20+ entries:** on phones inline each entry (`dt`, `dd` inline, a block `::after` on `dd`); 23–29 entries fit in under 2 screens, 33 with line-height 1.36 and 3 px gaps; on laptops two pairs per row (`auto 1fr auto 1fr`). Drop entries used only on their own defining slide.

**Engine and validator:**

- Widgets in follow mode need `data-builds="N"` on the slide when no `[data-build]` reaches N.
- A `data-build="0"` part that sits below the fold on phones (a figure under the text) fails the touch walk: leave always-visible parts without `data-build`.
- Inline `onclick` for the challenge keeps the deck at one `<script>`.
- A magic-board variant must keep the class the board script selects; don't put captions in `data-cap` (neither counter sees them).

---

## 7. Research and the independent check

**Independent check (rulebook F1b), in practice:** inputs are `deck-tools/slide_text.py`'s dump and `pdftotext -layout` of the lecture; brief: `deck-tools/checker-brief.txt` (rulebook Appendix C). Add: a typed transcription of image-only figures, one-line descriptions of the deck's drawings (line styles, arrows), that the glossary is a gloss sheet (weakened or wrong entries only), and that Textbook/Extra lines are checked for errors only. When it disagrees with the deck about a figure, re-check your transcription against the image (DB deck 3: one "contradiction" was the transcription's slip). Passes so far: 3–5 per deck, first passes 13–41 findings. What it catches most:
- **Glossary entries** that drop half of a two-part definition, a qualifier or a modal, or a scope ("for a binary relationship"); textbook meanings stated too strongly ("partial: only some take part" for "not necessarily all"). Write them from the quote, every half kept; 11 words beat a weakened 10. Don't carry an earlier lecture's wording when this lecture defines the term again.
- **Pictures, even labelled ones, that contradict a slide** (DB deck 1: transaction arrows that bypassed the DBMS). A label doesn't excuse a contradiction.
- **Invented groupings with a count** ("five kinds of work") and headings that group bullets ("Insulation Between Programs and Data" over two bullets): quote such headings as eyebrows, label groupings `ours`.
- **Invented examples** that follow the textbook against the slide's odd wording: illustrate the slide's version, put the textbook in a Note. Examples labelled ours still fail when they show a state the slides forbid (a NULL foreign key in a column the slides' own table makes NOT NULL; two identical rows to show a NULL key) or say "does not change" for "rarely changes".
- **Challenge options:** check every wrong option against every option the slides offer (DB deck 4: "enrollments stay, linked to nobody" is what SET NULL does, so it could not be stamped "never").
- **Quote styling on things that aren't slide words** (numbered table titles, quiz distractors, true-or-false claims, a deck tag inside a quoted figure caption, a title quoted from another lecture, a rebuilt table's own headers): put `.formal` on the exact cells, never on a table that holds the deck's words.
- **A gloss word that changes meaning between slides** ("associations": instances on one slide, UML relationship types on another): say both meanings where it is glossed.
- **Definitions the deck writes itself:** a lead, map card or intro line that says what a term is counts as a definition not quoted (DB deck 2: four). Frame instead ("Before the data comes its description"), keep the quote's words, or label it `ours`.
- **Layout the text dump loses** (nested list items) is reported as weakened: state it in words.
- Swapping quiz items to close a "fact not drilled" finding only moves the gap: QG4 asks for every topic, not every fact.

**Research** (scope: rulebook W2b): **search the exact phrase** of a suspicious definition; it shows at once where it really comes from. For misconceptions, the slides' own "however" and "note" lines are often the best source.

---

## 8. The final quiz

- **Fact pool first.** Write one line per fact per topic, give each fact to one item, then check every pair of items. A true part of a Find-the-mistake sentence, a match meaning, a figure label or a rule stated in a stem can answer another item (DB deck 4: a Work-it-out stem defining CASCADE gave away a build item's RESTRICT/CASCADE choice; the fix was a different near-miss tile).
- **`data-why` with a quote that holds double quotes** breaks the attribute and cuts the feedback: write `&quot;`.
- **Label the figure:** a second item on the same picture must not show the names the first tests; on the lecture's own tree, test grouping with the branch order shuffled; never test arbitrary positions. A near-miss bank label must not look like a figure label (DB deck 1: "Concurrency Control Software" in title case read as a real label).
- **Small topics collide most:** choose the kinds per fact (one sort for the examples, one scenario, one find-the-mistake on a definition).
- **Odd one out across lists** is cheap and fair when a lecture has two parallel lists: "Three of these are other threats. Which one is a category of attacks instead?" (210 ISY deck 4).
- **Build the answer** (new, DB deck 1, type `build`): tap word tiles into an answer line, with one or two near-miss tiles. Only the slide-word tiles are `.formal`, styled like the rest. Walked by `deck-tools/quiz_walk_x.py`. True-or-false stems read "Claim: …", not quoted.
- **Tables in the stem** (count rows left after a CASCADE delete; cardinality after inserts) give database-exam items that test reading data, not recall.
- **Drop a kind** when the chapter can't give it 2 fair items (DB decks 2–3 dropped Put in order: their only order was the deck's own framing); a slow kind with one strong item may stay with one.
- **Stems that rest on a Textbook line** (a (min, max) count) make the item depend on the deck: state the rule in the stem.
- **Weight what the slides stress** (their own review questions): 2–3 items each.
- **What the independent check catches most in quizzes:** feedback stronger or weaker than the slide ("many" dropped); feedback giving one of two rules the slide offers as the only one; a gloss as an option where the deck quotes the slide word; a premise the slides don't state ("words from the requirements" that aren't in them); a label-the-figure item on the deck's own picture.
- **Match rows** whose quoted meanings fit two names need the distinguishing line; **counts** need a counting rule ("count a name again each time it appears").
- **Removing slides:** update `#total`, the ledger, the `QUIZ-MAP` range; re-run the quiz walk.

---

## 9. Checking

- **Fonts:** Google Fonts is blocked in the sandbox. `setup_tools.sh` installs Caveat and Karla locally; the scripts serve them through Playwright routing.
- **Screenshots** (`shots.py`): every slide fully built; phone at 390×844 with touch (8 per sheet), then laptop 1280×800 (re-tile 2×2). Re-shoot only changed slides.
- **`checks.py`** (about 3 minutes; use a 10-minute timeout): keyboard walk and arriving back fully built; glossary cards per slide and none in the quiz; mouse and CDP touch drags; tap-target heights; sideways overflow and slides over 1.5 screens at 390, 360, 320 and 844×390; a touch-swipe walk where every build must land above the nav.
- **`measure.py`** lists the elements that overflow sideways on a slide.
- **Quiz walk:** `deck-tools/quiz_walk_x.py DECK` at laptop size, then with `--phone` (390×844 touch). Its screenshots use fallback fonts.
- **Touch drag:** Playwright's touchscreen only taps. Use CDP `Input.dispatchTouchEvent` (start → 12 moves → end) in a context with `has_touch`.
- **Expect:** quiz slides with figures or sorts at 1.5–2 phone screens; landscape phones at 1.5–4 (accepted by M8). `measure.py` also lists tables inside scroll boxes; trust `checks.py` for page overflow.

---

## 10. Changing a finished deck

- **Recolour:** take the reference deck's head whole; re-insert the deck's extra CSS with its colours as tokens (`color-mix`). The phone layer (B4) is purely additive.

---

## 11. Proposed for the rulebooks and deck-tools (delete each point here once adopted)

- **questions-rulebook §3b → §3a:** *Odd one out* is built and tested (210 ISY deck 2, type `mcq`, stem "Four of these are X. Which one is a Y instead?").
- **questions-rulebook QW1, QW5 and K9:** items test the lecture, not the deck's own framing (no label-the-figure on an "ours" picture); feedback states slide facts at full strength; options keep the slide's words. `slides-rulebook.md` TE7 (since v1.7) already says this for slides decks.
- **`deck-tools/checker-brief.txt` (slides Appendix C):** the glossary is a gloss sheet (weakened or wrong entries only); give one-line descriptions of the deck's drawings; "Textbook:" lines are checked for errors only.
- **questions-rulebook §3a + the deck-tools quiz files:** *Build the answer* (`build`) is built and walked (DB deck 1): markup, CSS and script branch are in that deck's shell; its walk branch is in `deck-tools/quiz_walk_x.py`.
- **`deck-tools/snippets/quiz.css`:** add `input.gap.num{position:static}` and the base `.opt/.opts/.verdict/.row2/.row4` styles.
- **`deck-tools/quiz_walk.py`:** give it a phone switch and the `build` branch. Until then, `deck-tools/quiz_walk_x.py [--phone]` patches it in memory.

---

## 12. Deck tools (separate files, not pasted here)

`deck-tools/` (now **1.7**) ships beside these notes in the skill's `rulebooks/` folder. Run `bash <rulebooks>/deck-tools/setup_tools.sh` once per session from your working folder, and the scripts below from there (`python3 <rulebooks>/deck-tools/build.py …`).

Setup copies `plain_check.py` and `quiz_walk.py` into your working folder, checks that `snippets/` is complete, compares rulebook versions with `deck-tools/VERSION.txt` (a mismatch only warns), and installs local fonts, `wordfreq`, `bs4` and the CEFR-J list.

**Self-test:** `python3 deck-tools/checks.py PREVIOUS-DECK.html`. If it reports a problem or COULD NOT CHECK, fix the tool (not the deck), note it under Departures, and update `VERSION.txt` (which also lists the engine globals and class names the tools rely on).

**Exit codes** (checks, shots, measure): 0 clean · 1 problem found · 2 could not check; COULD NOT CHECK is never a pass. `build.py` exits 1 with a WARNING when it could not insert the deck comments or sync `#total`, or finds a doubled `<html>`/`<body>`.

| Script | Use |
|---|---|
| `build.py OUT.html` | Joins `build/p*.html` (+ `build/zz_comments.html`), syncs `#total`, prints words per slide and per topic, and the quiz apart |
| `shots.py DECK DIR W H [slides\|all] [--touch]` | Screenshots fully built slides with local fonts, plus contact sheets |
| `checks.py DECK` | All automated checks of §9; ends with a RESULT line |
| `measure.py DECK W H slides` | Elements that overflow sideways |
| `slide_text.py DECK [OUT.txt]` | Every slide's readable text as a student reads it («quotes», [ours: …], feedback), without the HTML comments: the independent checker's input |
| `quiz_walk_x.py DECK [DIR] [--phone]` | The rulebook's quiz walk plus newer kinds (`build`); `--phone` for 390×844 touch (`quiz_walk_phone.py` is the same) |
| `er.py` (imported) | ER diagrams: `er.build(spec)` returns one `.lf` with SVG shapes and HTML pins; needs the deck's "ER diagrams" CSS (DB deck 3) |
| `figshot.py DECK SLIDE OUT.png [W H scale sel idx]` | One element of a built slide at high scale, to check label overlaps |
| `size_check.py [FOLDER] [--sections]` | Rulebook and notes sizes against their caps; run after editing them |
| `snippets/`, `checker-brief.txt`, `plain_check.py`, `quiz_walk.py` | The rulebooks' code (`snippets/README.md` maps each file to its rule) |
