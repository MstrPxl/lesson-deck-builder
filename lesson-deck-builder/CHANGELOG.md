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
