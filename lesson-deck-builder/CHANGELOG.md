# Changelog

## v1.2 — research session, 2026-10-06

**Use cases (new system)**
- `references/use-cases.md`: 19 teaching jobs, each explained once with examples and "spot it when"
  signals (usable as a lecture-slide classifier), plus a generated reverse index: the components that
  suit each job, best fit first. One vocabulary with style-system §5's eight categories.
- Every component in `components.md` (§1–§31 and the skeletons §32a–g) carries a ranked
  **Suggested for** list — suggestions, not obligations.
- `scripts/use_cases.py` keeps lists and catalogue in sync (`--write` regenerates the index).
- The Arabic font pairing has no list: it is always on, not chosen.

**Engine v2** (template + every exemplar)
- Builds: `data-build="0..n"` reveal one press at a time before the page turns; back un-builds and
  arrives fully built; `data-builds="n"` declares steps for widgets; `build` and `slideenter` events.
- Capture guard: the engine ignores keys and swipes inside `[data-capture]` (scrubbers, drag figures).

**New components** (`components.md`)
- All families: §22 labels on the figure · §23 linked figure · §24 anchored gloss (anchor positioning) ·
  §25 builds · §26 magic board (view transitions) · §27 reactive sentence.
- Sketchbook kit (paper + chalkboard): §28 ink marks · §29 eraser · §30 sketch chart · §31 live element.
- Shared controls and the **bridge tokens** (`style-system.md §9`) let one copy of §22–§31 work in
  every family.

**Style system**
- Law 1: native overlay recipe. Law 3 ruling: a figure label is not an actor. Law 4: line boil is the
  one sanctioned exception (Sketchbook, one `.live` per slide).
- Sketchbook: Arabic = Playpen Sans Arabic 800 always + IBM Plex Sans Arabic (closes the open item for
  this family); third pen (ochre / chalk-yellow).
- Nocturne gains one accent (violet `#B9A6FF`) used only as the third linked/series color.

**Validator**: engine v2, bridge tokens, `.reveal`+`data-build` clash, scrubbers without
`data-capture`, Sketchbook notes (one `.live` per slide, Playpen 800, chalk mask).

**Housekeeping**: the duplicated §17 heading in components.md is now §32.

**Not adopted**: reduced-motion contract (finding 13), by choice.

## v1.2.1 — 2026-10-07

- Removed the chalkboard chalk grain (research finding 10, "Chalk has teeth") everywhere it was
  applied: the `--chalk-mask` token and rule in style-system §7, the chalkboard exemplar's mask on
  headings, the pre-ship checklist item, and the validator note. Chalkboard text renders clean, as
  before v1.2.

## v1.3 — Sketchbook only, chalkboard boards — 2026-10-09

(Section numbers in the entries above this one follow the v1.2 numbering of `style-system.md`:
v1.2 §5 → v1.3 §3, §6 → §4, §7 → §5, §8 → §6, §9 → §7.)

**One style, two canvases**
- Sketchbook is the only style family. Playroom, Nocturne, Terra and Classic are retired as looks: their
  sample decks (`playroom*.html`, `nocturne.html`, `terra*.html`), the Classic themes (Warm Paper, Cool
  Mist, Dawn Clay, Slate Quiet) and the Classic font pairings are removed.
- The style gate becomes the **canvas gate** (SKILL.md §1b, style-system §4): paper (bright) or
  chalkboard, and on the chalkboard one of **six boards** — Slate re-inked (default; replaces the old
  `#2B322D` slate), Midnight blue, Olive gold, Dusk indigo, Deep teal, Red graphite. Each board is darker
  (OKLCH L ≈ .23) and calmer than the v1.2 slate, with warm off-white chalk, three medium-saturation pens,
  a solid dust highlight and body text ≈ APCA Lc 80. Tuning rules are recorded in style-system §5.
- The canvas is one attribute pair on `<html>` (`data-canvas`, `data-board`). The template carries every
  token block, the bridge tokens and pen washes for both canvases, and arrowheads/patterns that follow the
  canvas through CSS variables. Tape stays paper-coloured on every board.

**Template** — rebuilt in Sketchbook (Arabic default: Playpen Sans Arabic 800 + IBM Plex Sans Arabic;
English: Caveat + Karla). Components §1–§21 are re-skinned (wobbly ink/chalk frames, pen badges,
hand-drawn ticks) and read `--k-a/b/c` + `--wash-a/b/c` instead of the Classic accents. Engine v2 is
unchanged.

**Preserved component guidance** — the retired families' mechanics are ported to the Sketchbook skin, with
working code in `components.md §32` generated from the new exemplar `sketchbook-kit.html`:
- lab widget (chips + gauge in two modes — decay, and signal-vs-noise `mode:'appear'`; fixed-budget
  lamp), detail tray, numbered
  gloss footnotes, duo panes (final-geometry);
- new: §32h token journey (builds-driven, mirrors in RTL), §32i pointer spotlight cover, §32j smudge panels
  (blur, not glow), §32k skins stepper with per-skin annotations, §32l key passage frame;
- §32a is now a real stepper skeleton: per-state `|`-lists in `data-o` / `data-sw` / `data-tf` / `data-txt` /
  `data-w` (fades, moving actors, counters, reveals) — §32k is the same skeleton with skins;
- every §32 script works per container, so a component can be used on several slides of one deck.
The drawing vocabularies (blocks and flows, light and energy, objects that enact the principle, section
cues, key passages, attention-gated depth) are kept in style-system §2. Law 2 now bans reusing an
exemplar's subject or content, not its mechanics.

**Exemplars** — `sketchbook-chalkboard.html` moves to the board tokens (default Slate re-inked); its
top-bar dots preview paper and all six boards. `sketchbook.html` declares `data-canvas="paper"`.

**Sketch chart** (§30) — its fill patterns are renamed `skc-hatch` / `skc-cross` / `skc-dots` so they
never collide with the template's figure fills (`p-hatch`, `p-dots`).

**Validator** — checks `data-canvas` / `data-board`: an unknown board, a board without its token block, or
a chalkboard deck without chalkboard tokens are errors; a missing canvas is a note; fonts from retired
families are noted.

**Use cases** — §32 lists extended; reverse index regenerated (`scripts/use_cases.py --write`).

**Decks built before v1.3** keep working: they carry their own tokens. A course that copies its shell from
an earlier deck keeps that deck's colours until the shell's tokens are replaced.

## v1.4 — one-line requests, bundled rulebooks, English level — 2026-10-23

**Routing (SKILL.md step 0b).** "use /lesson-deck-builder to explain the attached file" is a complete request. An attached
lecture or document (PDF or PPTX) takes the **lecture route** (`rulebooks/slides-rulebook.md`, ending with the final quiz of
`rulebooks/questions-rulebook.md`); a teaching request without one takes the **lesson route** (`rulebooks/lessons-rulebook.md`);
pitches and showcases keep the base workflow. The user's words beat the files.

**Bundled rulebooks and tools.** The slides, questions and lessons rulebooks, the general notes (`deck-notes-general.md`) and
`deck-tools/` now ship in `rulebooks/`. Nothing is attached but the file to explain and the previous deck.

**No Markdown back and forth.** A course's memory lives in its decks: the COURSE record (lecture route; it absorbs the retired
course notes file) or DECK-SETTINGS (lesson route); in a chat-mode series the roadmap spec and the learner notes travel as
`ROADMAP-SPEC` and `LEARNER-NOTES` comments. General lessons go on the report's "Proposed for the skill" line and change the
skill's files only in a maintenance session.

**English level (step 2b).** English decks are written at A2, B1, B2 or C1, asked once per course or journey with the canvas
(lecture route suggests B1, lesson route and presentations B2) and recorded in the deck. A level table sets words and sentence
caps (15 · 20 · 25 · 30). `plain_check.py --max-level` measures any level; at C1, common words past the CEFR-J list count as
known.

**Goals first.** A new "How to read this skill" section: goals, user choices and technical contracts are fixed; workflows,
numbers, tools, rulebook procedures and notes are tested defaults that a better method may replace (named on the report's
"Departures" line). The lessons rulebook gains the same principle.

**Versions.** slides-rulebook 2.0, questions-rulebook 1.4, lessons-rulebook 2.0 (from 1.1), deck-tools 1.7. Details in
`rulebooks/rulebooks-changelog.md`.

## v1.4.1 — ask for the missing lecture — 2026-10-23

- **A course deck without its new lecture** (SKILL.md step 0b, slides-rulebook 2.0.1): when a deck with a `COURSE` record is
  attached but no new file to explain, Claude asks for the new chapter's PDF (or PPTX) before planning or building, instead
  of falling back to the lesson route. Not when the user asks to change the attached deck itself, and not for a lesson
  journey's deck (`DECK-SETTINGS`), which needs no file.

## v1.4.2 — the lesson route is phone first — 2026-10-23

- **lessons-rulebook 2.1:** new goal G6, phone first, with the lecture route's own phone rules. The slides rulebook's §8
  "Phone first" (M1–M8), its Q7 phone checks and its phone layer and phone-variant figures (Appendix B4–B5) are required
  reading on the lesson route and apply as written, so both routes follow one set of rules. The presentation route is
  unchanged.
