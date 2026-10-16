# Style System — v1.3 (Sketchbook · paper and chalkboard)

This file is AUTHORITATIVE for visual style. The skill has ONE style family —
**Sketchbook** — on two canvases: **paper** (bright) and **chalkboard** (six
boards, §5). Canonical exemplar decks live in `assets/style-samples/`; study
them before building, then obey Law 2: exemplars teach the *vocabulary*, never
the *subjects*.

**Retired in v1.3:** Playroom, Nocturne, Terra and Classic are no longer
selectable looks. What they knew about *representing ideas* is kept: their
component mechanics are ported to the Sketchbook skin (`components.md §32`,
exemplar `sketchbook-kit.html`), and their drawing vocabularies live on in §2.
Never rebuild a retired look (its palettes, fonts, glow, springs) — borrow only
the mechanics and the ideas.

---

## 0 · The five laws (every deck)

**Law 1 — Depth never reflows the scene.** Hidden depth (hover/tap content)
may only appear through one of the four legal mechanics below. Whatever
expands must never move unrelated elements or re-center the slide. This set is
closed; extend it only with the user's explicit approval.

1. **Reserved flow** — expansion pushes *sibling elements of the same
   component* inside a fixed-size container; the container's outer box never
   changes. (Exemplars: the Sketchbook note stack; the smudge panels §32j are
   the limit case — the space is always reserved and only the ink clears.)
   ```css
   .stack{display:grid;gap:16px;align-content:start;height:<reserved>px}
   .item .body{max-height:0;overflow:hidden;opacity:0;transition:...}
   .item:hover .body{max-height:<cap>px;opacity:1}
   ```
2. **Fixed tray** — depth lands in a constant-size, internally scrolling
   area; content swaps, geometry never changes. Handles any text length.
   (Exemplar: index cards → detail tray, §32d.)
   ```css
   .tray{height:clamp(120px,22vh,190px);overflow-y:auto}
   ```
3. **Overlay** — depth floats above the scene, absolutely positioned, out of
   flow. Native recipe for word-anchored overlays: anchor positioning —
   `position-area: top` + `position-try-fallbacks: flip-block`, no measuring
   script (`components.md §24`; numbered footnotes are its variant, §32e).
4. **Final-geometry** — the expanding element animates straight to
   PRE-MEASURED final dimensions; text may clip mid-flight and is fully
   visible at the destination. Required whenever expansion changes an
   element's width (text re-wrap makes natural height non-monotonic).
   Recipe (exemplar: duo panes, §32f):
   - With transitions disabled, apply each end state, measure the deep
     block's height at its FINAL width → store as `--dh` on the element.
   - Lock the container's height to the tallest end state.
   - Animate `height: 0 → var(--dh)` (+ the width change) with one easing.
   - Re-measure on `document.fonts.ready`, `load`, debounced `resize`, and
     the slide's `slideenter`.

**Law 2 — Skeleton ≠ skin.** Behavioral components (stepper, lab, reveal,
check, duo, journey, spotlight) are generic skeletons: state index, prev/next,
caption fade, per-state values (`|`-lists in `data-o` / `data-sw` / `data-tf` /
`data-txt` / `data-w`), scoring. The illustration is a per-topic skin generated
fresh from a **scene brief**:
1. Choose the subject that best *embodies the mechanism being taught* (§2
   lists proven vocabularies). Never inherit an exemplar's *subject or
   content* — its topic, its drawing, its captions (no default chessboard,
   chalk trace, footpath, review cards). The mechanics themselves — a
   spotlight, a route with a token, a lamp whose beam is shared — are
   skeletons to reuse freely; what they show is drawn fresh for the topic.
2. Draw it in the Sketchbook stroke vocabulary (§1).
3. Map lesson states onto scene states.
4. Captions and annotations are per-skin (own text, own position).
The kit exemplar's skins stepper (§32k) demonstrates one skeleton driving two
skins.

**Law 3 — One coordinate system per figure.** Every actor of a figure
(pieces, tokens, marks, beams) lives inside the figure's own SVG viewBox and
moves in user units (CSS transforms in px == user units). Never float HTML
actors over an SVG scene.
**Ruling: a figure label is not an actor.** Static label text may sit in HTML
pinned in the figure's own viewBox units on its own frame (`components.md
§22`); anything that MOVES stays inside the SVG.

**Law 4 — One motion law.** Sketchbook's: draw-in strokes + slight
rotations, `cubic-bezier(.2,.7,.2,1)`, ~0.5s. Every component inherits it
through `--k-ease`, including the ported ones (springs, breathing glows and
whisper fades from the retired families are NOT ported).
**One sanctioned exception:** line boil (`components.md §31`) — one `.live`
element per slide, never on text; it is a property of the hand-drawn stroke,
not a second easing.

**Law 5 — Little text, louder message.** The always-visible layer carries one
idea in few words; everything else is depth (Law 1) or visual. The text
method adapts to the content category (§3).

**Craft rules:**
- Draw-in strokes are INVISIBLE before their animation: gate with
  `opacity:0 → 1`, not dash math alone (dash seams leave a visible notch).
- Expansions and movements are monotonic — geometry travels from current to
  final without overshoot or intermediate settling.
- Every slide fits the viewport; interactive figures never require scroll.
- Inside a text-centered cover, any max-width block (lead paragraphs, hints)
  also gets `margin-inline:auto` — text-align alone never centers the block.
- Interactive elements ALWAYS declare text color explicitly — buttons and
  inputs do not inherit; UA defaults paint them black, which paper hides by
  accident and the chalkboard exposes.
- A filtered SVG group whose box has zero width or zero height renders
  nothing: give a lone straight line a transparent `<rect fill="none">`
  partner inside the filtered group.

---

## 1 · SKETCHBOOK — hand-drawn

- **Identity:** a teacher's notebook — or blackboard — that draws itself
  while you watch.
- **Canvases:** paper (bright, default) · chalkboard (six boards) — §5.
- **Type:** Caveat 700 (display/annotations) + Karla (body).
- **Arabic type:** Playpen Sans Arabic at weight **800, always** (every Caveat
  role) + IBM Plex Sans Arabic (body; tags/eyebrows at 600, never uppercased or
  letter-spaced) — §4.
- **Pens:** three, read through the bridge tokens — pen a `--red` (`--k-a`),
  pen b `--blue` (`--k-b`), pen c `--yellow` (`--k-c`, the third pen: ochre on
  paper). On the chalkboard each board brings its own three chalks (§5).
- **Kit:** ink marks §28 · eraser §29 · sketch chart §30 · live element (line
  boil) §31 · ported mechanics §32 — all on both canvases.
- **Stroke vocabulary for skins:** wobble-filtered strokes (feTurbulence +
  feDisplacementMap, scale ≈ 2.6), uneven border-radius frames, tape strips,
  draw-in strokes (`pathLength="1"` + dashoffset + opacity gate), unicode
  glyph actors allowed. Anything sketchable in ≤ 20 strokes — boards, maps,
  timelines, stick figures, arrows-and-labels, and the vocabularies of §2.
  Complex objects become caricatures, not blueprints.
- **Motion law:** draw-in + slight rotations; `cubic-bezier(.2,.7,.2,1)`,
  ~0.5s.
- **Depth default:** reserved flow (sticky-note stack; dashed tear-line
  separates title from depth). The ported tray (§32d), smudge panels (§32j)
  and duo panes (§32f) are legal alternatives when the content fits them.
- **Don't:** perfect circles/lines, gradients as surfaces, glossy shadows,
  glow or neon (on either canvas), emoji, pure white text.

## 2 · Drawing ideas — vocabularies kept from the retired families

These are ways to *represent a mechanism*, not looks. Draw every one of them
in chalk or ink with the §1 stroke vocabulary; pick the one whose behaviour
mirrors the idea being taught.

- **Blocks and flows** (from Playroom). Model the topic as entities and
  movement: entities → rounded nodes; processes → a token travelling a drawn
  route (§32h); quantities → chip counts or a gauge (§32b); categories →
  rooms or zones of the board. If the idea cannot be drawn this way, simplify
  it until it can.
- **Light and energy** (from Nocturne). Beams, pulses, orbits, radar sweeps,
  signal paths, circuit traces, constellations, waveforms, heat maps. Choose
  the phenomenon whose physics mirrors the mechanism: decay → a fading pulse;
  feedback loop → an orbit; routing → a circuit trace; broadcast → radiating
  rings; limited capacity → one lamp shared by everything in its beam
  (§32b fixed-budget lamp). In Sketchbook these are chalk strokes and dashed
  fills — matte, never glowing.
- **Objects that enact the principle** (from Terra). Tools, plants, vessels,
  stones, hands, paths — pick the object whose growth or behaviour *enacts*
  the principle (a path that stays open when walked; a tree that bears more
  after pruning). One skeleton can drive several such skins (§32k).
- **Section cues** (from Playroom's rooms). Make the move into a new part of
  the deck *felt*: a tape label or a tab in pen a on the part's first slide,
  a fresh "page" with the part's name as the eyebrow, or a topic bar if the
  deck has one. Never by recolouring the board — the canvas stays one canvas.
- **Key passage** (from Terra's essay page). The one paragraph a slide turns
  on gets a double-ruled frame and a drop initial (§32l) — once per slide at
  most.
- **Attention-gated depth** (from Nocturne). When the lesson's thesis is
  about attention or noise, let the interaction enact it: the pointer
  spotlight (§32i) shows only what is attended to; smudge panels (§32j) clear
  where attention lands. Never hide examinable content this way — headlines
  stay readable; depth is extra.

## 3 · Content-category → representation map

| Category | Always-visible layer | Depth mechanic | Signature component |
|---|---|---|---|
| Academic / definitional | short headline + one core paragraph | note stack / overlay | notes · anchored gloss §24 · smudge panels §32j |
| Process / mechanism | one caption per state | builds or stepper states | steppable figure §32a · token journey §32h · builds §25 |
| Intuition / tradeoff | one instruction line | live readout | lab widget §32b · reactive sentence §27 |
| Comparison | two titles + one number each | final-geometry / tray | duo panes §32f · detail tray §32d |
| Narrative / history | one scene line per beat | stepper or reveal sequence | skins stepper §32k · linked cards §10 |
| Code walkthrough | one annotated line-range at a time | overlay notes on the code | code window §16 + stepper |
| Anchor / thesis | one poster statement | none | poster cover · pointer spotlight §32i |
| Check / recall | one question | verdict line | sketch quiz §32g |

This table is the coarse map. `use-cases.md` refines it into 19 teaching jobs
and, for every job, lists the components that suit it, best fit first; every
component in `components.md` carries the matching ranked **Suggested for**
list. Rankings are suggestions, not obligations.

## 4 · The canvas gate (replaces the style gate)

Before building, the canvas question is REQUIRED and follows the
**suggest-and-confirm** shape — never a silent decision, never a suggestion
without the menu:

1. **Canvas.** Lead with the best fit and a one-line reason, then offer both:
   **Paper** (bright ruled notebook) · **Chalkboard** (dark board, chalk
   pens). Suggest paper by default; suggest chalkboard when the user's context
   implies night or long screen reading, or when they have chosen it before.
2. **Board** (only when chalkboard is picked). Lead with **Slate re-inked**
   (the default) unless the user's record says otherwise, and list all six by
   name with a few-word identity (table in §5). Their pick is final.
3. Ask once per journey (or per course, when a rulebook keeps a course
   record) and record the choice; re-ask only if the user wants a change.

**Arabic pairing (both canvases):** Playpen Sans Arabic at weight **800,
always** (display, captions, labels, annotations: every Caveat role) + IBM
Plex Sans Arabic for body (tags/eyebrows at 600, never uppercased or
letter-spaced); load only
`family=Playpen+Sans+Arabic:wght@800&family=IBM+Plex+Sans+Arabic:wght@400;600`.
English decks use Caveat + Karla. Size floor at 800: keep Arabic display-face
text at **0.95rem or larger** — below that the counters of ه and ة start to
close (sooner in light chalk on the board, which reads heavier).

## 5 · Canvases and boards

**Setting the canvas is one attribute pair on `<html>`** — the template holds
every token block, and every component, bridge token and arrowhead colour
follows it:

```html
<html lang="en" dir="ltr" data-canvas="paper">                               <!-- paper -->
<html lang="en" dir="ltr" data-canvas="chalkboard" data-board="midnight-blue"> <!-- a board -->
```

`data-canvas="chalkboard"` without `data-board` gives the default board,
Slate re-inked. Never hand-edit a board's hex values inside a deck — pick a
board; a new board is a skill change (see "Adding a board").

### Paper (bright)

ivory ruled paper `#FBF6EA`, red margin line, marker-yellow highlight
`#FFE590`; ink `#29241B`, ink-soft `#5E5748`; pens red `#C4553B` · blue
`#3E6B8C` · ochre `#A8741A`; card surfaces `#FFFDF6`; warm top-right light
spill. No dust layer.

### Chalkboard — the six boards

| Board (`data-board`) | Board | Feel | Pens a · b · c | Body text Lc |
|---|---|---|---|---|
| **Slate re-inked** `slate-reinked` (default) | `#19211B` | the classic green-black slate, one step richer | rose `#FF9E8F` · chalk-blue `#98CCF6` · chalk-yellow `#F5D870` | 79.7 |
| Midnight blue `midnight-blue` | `#131D2A` | deep blue slate, the calmest hue | coral `#FEA684` · mint `#83E2BF` · butter `#FAD980` | 80.0 |
| Olive gold `olive-gold` | `#1F1E13` | dark olive-khaki, leans yellow | coral `#FDA19E` · periwinkle `#A5C9FF` · lemon `#F3E685` | 79.9 |
| Dusk indigo `dusk-indigo` | `#1A1A28` | muted blue-violet | peach `#FBA59A` · aqua `#7DDBE0` · gold `#F9DA7B` | 80.2 |
| Deep teal `deep-teal` | `#0E2224` | blue-green | apricot `#FEAA7A` · periwinkle `#B9BCF9` · sun `#F4DF79` | 79.7 |
| Red graphite `red-graphite` | `#281717` | dark charcoal with an oxblood tint | pink `#FDA9B5` · sage-teal `#88D9D1` · butter `#F6D97E` | 80.0 |

Shared by every board: chalk `#F3EFE3` (red graphite `#F4EFE3`), body text
`#DBD6C6` (red graphite `#DDD5C6`), surfaces `rgba(255,255,255,.06)`, screen-blend dust at .05, faint
yellow top-right spill (3.5%) and pen-b bottom-left spill (4.5%). The full
token rows (`--paper-2`, `--pencil`, `--line`, `--marker`) live in
`assets/template.html`; the template is the source of truth.

**Chalkboard translation laws** (paper → board):
1. **Token translation, end-to-end.** Every colour token has a board value;
   no paper hex survives on a board (and vice versa). Dark canvases eat
   saturation — pens are *lightened*, never merely kept.
2. **Physical paper objects keep the paper palette.** Sticky notes, tape,
   index cards and gloss cards remain paper-coloured with paper-dark ink on
   any board — including their hover-hint text.
3. **Grain/dust is a pre-tiled data-URI noise background** (`stitchTiles`,
   `background-repeat`), screen-blend on the board. NEVER a live
   full-viewport SVG feTurbulence element — its filter region paints a
   visible patch on dark canvases.
4. **Shadows stay shadows** (darker on the board). Matte, never luminous: no
   glow, no light halos, no text-shadow — on either canvas.
5. **Figure actor polarity stays legible:** on a board, "light" actors are
   solid chalk with a board-coloured outline; "dark" actors are board-filled
   (`--paper-2`) with a chalk outline.
6. Motion law, mechanics and skins are UNCHANGED by the canvas — the canvas
   is the only variable.
7. **No chalk grain on text.** Headings, labels and captions render solid
   (the chalk mask clipped the last letters of figure labels).

**How the boards were tuned** (and the rules any future board must meet):
- Board lightness OKLCH L ≈ 0.225–0.24, chroma 0.016–0.03 — dark enough to
  rest the eye, coloured enough that the hue reads. Pure black is never used.
- Chalk is warm off-white (`#F3EFE3`), never `#FFFFFF`: pure white on a dark
  ground blurs ("halation"), worst for astigmatic readers.
- Body text ≥ APCA Lc 75 on the board (all six reach ~80); headings ~95.
- Pens are light tones (L 0.79–0.92) at **medium** chroma (pens a and c
  ~0.10–0.13, pen b ~0.08–0.10):
  saturation is the strongest driver of arousal, and medium saturation was
  rated the most pleasant (Wilms & Oberfeld 2018); saturated mid-tones
  "vibrate" on dark grounds (Material Design dark theme guidance).
- The highlight (`--marker`) is a SOLID dust colour at L ≈ 0.45, C ≈ 0.056,
  warm hue — an alpha-blended yellow turns muddy grey on blue and violet
  boards (complementary mixing). Chalk on it stays ≥ Lc 75.
- Corner light spill ≤ 3.5%: on dark boards a stronger glow reads as a shine.
- Yellow-leaning boards stay clear of the drab dark yellow-brown of
  Pantone 448 C (`#4A412A`) — lean toward olive instead.
- The three pens of a board must stay distinguishable in a linked figure:
  pen b sits at least ~80° of hue from both others; pens a and c are closer
  (about 50–80° apart) and are told apart mainly by lightness — pen c is
  always the lightest. Check a three-colour figure on a new board.

**Adding a board** (only on the user's request): meet every rule above, then
update every place that lists the boards — `assets/template.html` (a token
block + the header comment), the token block in
`assets/style-samples/sketchbook-chalkboard.html` and its preview list, the
preview list in `sketchbook-kit.html`, `BOARDS` in `scripts/validate.py`, the
table here, `design-system.md §2`, and SKILL.md (step 1b's list and step 6's
keys) — and check every exemplar slide on it.

## 6 · Pre-ship checklist (grade every deck against this)

- [ ] Depth mechanics: every hidden-content interaction is one of the four
      legal mechanics; hovering anything moves nothing unrelated.
- [ ] No recycled subjects: every illustration was invented for this topic.
- [ ] Figures: actors inside the SVG viewBox, one coordinate system.
- [ ] Strokes invisible before their draw-in (opacity gate).
- [ ] Expansions monotonic; width-changing expansions use final-geometry.
- [ ] One motion law throughout (Sketchbook's); at most one `.live` per slide.
- [ ] Little text, louder message: visible layer ≈ one idea per element.
- [ ] Canvas honored end-to-end: `data-canvas` (and `data-board` on the
      chalkboard) set on `<html>`; no hand-edited board hexes; paper objects
      keep the paper palette; dust tiled per §5.
- [ ] Engine contract intact (one `active` slide, untouched engine v2 script,
      no storage APIs); `scripts/validate.py` passes.
- [ ] Components chosen per teaching job (`use-cases.md`); the deck does not
      use one component for every job.
- [ ] Builds step with the keyboard forward and back (arriving back fully
      built); no element has both `.reveal` and `data-build`.
- [ ] Every drag/arrow/slider widget carries `data-capture`; dragging never
      turns the page.
- [ ] Arabic uses Playpen Sans Arabic 800 + IBM Plex Sans Arabic.

## 7 · Component bridge tokens

Components §22–§31 read only these `--k-*` tokens; §1–§21 and §32 also read
the canvas tokens (`--ink`, `--paper`, `--pencil`, `--line`, `--shadow`) and the
template's shape tokens (`--wob-r`, `--wob-s`, `--display-w`). One copy of every
component's CSS works on both canvases and every board. **The template
already defines all of them**; a deck built without the template must copy
the whole token section of `assets/template.html`, not just this list.

```css
--k-ink:var(--ink); --k-soft:var(--ink-soft); --k-a:var(--red); --k-b:var(--blue); --k-c:var(--yellow);
--k-hi:var(--marker); --k-surface:var(--surface); --k-card:#FBF6EA; --k-card-ink:#29241B;   /* paper objects */
--k-line:var(--line); --k-ease:cubic-bezier(.2,.7,.2,1);
--wash-a:color-mix(in srgb,var(--k-a) 16%,transparent);   /* pen washes for chips, badges, icons */
--wash-b:color-mix(in srgb,var(--k-b) 16%,transparent);
--wash-c:color-mix(in srgb,var(--k-c) 18%,transparent);
--wob-r:14px 22px 16px 24px/22px 14px 24px 16px; --wob-s:10px 16px 12px 18px/16px 10px 18px 12px;   /* hand-drawn radii */
--display-w:700;   /* Caveat; Arabic Playpen: 800 */
/* eraser (§29): paper  --er-streak:rgba(41,36,27,.08); --er-wash:rgba(41,36,27,.04); --er-ghost:.2;
                 board  --er-streak:color-mix(in srgb,var(--ink) 10%,transparent);
                        --er-wash:color-mix(in srgb,var(--ink) 5%,transparent); --er-ghost:.14; */
```
