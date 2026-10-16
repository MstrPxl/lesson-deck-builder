# Design System — Lesson-Deck-Builder (v1.3)

The house style is **Sketchbook**: a hand-drawn notebook or blackboard —
calm, legible, visual-first, never a "techy template". Its full contract
(laws, canvases, the six chalkboard boards, components' skins) lives in
`references/style-system.md`, which is authoritative. This file holds the
practical setup: aesthetic rules, fonts, direction, and the length budget.

## Table of contents
1. Aesthetic rules (non-negotiable feel)
2. Canvas setup (paper / chalkboard boards)
3. Font pairings (Arabic + Latin)
4. Direction handling (RTL vs LTR)
5. Length budget → slide count

---

## 1. Aesthetic rules

- **Paper, not white — board, not black.** The paper canvas is ivory ruled
  paper, never `#FFFFFF`; the chalkboard is a dark coloured board, never
  `#000`. Both rest the eye.
- **Ink, not black; chalk, not white.** Text is a soft dark ink on paper and a
  warm off-white chalk on the board — never `#000` or `#FFF`.
- **One dominant pen + quiet supports.** Pen a carries tags, the margin line
  and the main emphasis; pens b and c link parts of a figure. A timid,
  evenly-spread rainbow looks generic.
- **Generous whitespace.** Let slides breathe. One idea per slide.
- **Hand-made depth.** Wobbly ink frames, tape, sticky notes, long soft
  shadows — no glossy shadows, no neon, no glow, no glassmorphism, no
  gradients as surfaces.
- **No purple-gradient-on-white.** That is the canonical "AI slop" look.

---

## 2. Canvas setup

The template ships every canvas. The canvas gate (SKILL.md §1b,
`style-system.md §4`) decides one attribute pair on `<html>`:

| Choice | `<html>` attributes |
|---|---|
| Paper (bright) | `data-canvas="paper"` |
| Chalkboard · Slate re-inked (default board) | `data-canvas="chalkboard" data-board="slate-reinked"` |
| Chalkboard · Midnight blue | `data-canvas="chalkboard" data-board="midnight-blue"` |
| Chalkboard · Olive gold | `data-canvas="chalkboard" data-board="olive-gold"` |
| Chalkboard · Dusk indigo | `data-canvas="chalkboard" data-board="dusk-indigo"` |
| Chalkboard · Deep teal | `data-canvas="chalkboard" data-board="deep-teal"` |
| Chalkboard · Red graphite | `data-canvas="chalkboard" data-board="red-graphite"` |

Nothing else changes: tokens, bridge tokens, pen washes, arrowheads, dust and
light spills all follow the attributes. Preview every board with the dots in
the top bar of `assets/style-samples/sketchbook-chalkboard.html` or
`sketchbook-kit.html`.

---

## 3. Font pairings

### Arabic (RTL) — template default
```css
--font-display:"Playpen Sans Arabic", cursive;   /* weight 800, always */
--font-body:"IBM Plex Sans Arabic", sans-serif;  /* 400 body · 600 tags/eyebrows */
--font-eyebrow:"IBM Plex Sans Arabic", sans-serif;
--display-w:800;
```
```html
<link href="https://fonts.googleapis.com/css2?family=Playpen+Sans+Arabic:wght@800&family=IBM+Plex+Sans+Arabic:wght@400;600&display=swap" rel="stylesheet" />
```

### Latin (LTR)
```css
--font-display:"Caveat", cursive;
--font-body:"Karla", sans-serif;
--font-eyebrow:"Karla", sans-serif;
--display-w:700;
```
```html
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Karla:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet" />
```

**Arabic typography notes:** never apply `letter-spacing` or uppercase to
Arabic text (the template's `:lang(ar)` rules handle tags and eyebrows); keep
`line-height` generous (~1.9); keep Playpen display text at 0.95rem or larger.
Western (`0-9`) numerals read fine in modern Arabic UIs.

---

## 4. Direction handling (RTL vs LTR)

The template uses CSS **logical properties** (`margin-inline`, `inset-inline`,
`border-inline-start`, `border-end-end-radius`, …) so layout mirrors
automatically — the notebook's margin line moves to the reading-start side.
To switch language/direction, change only:

1. `<html dir="rtl" lang="ar">` → `<html dir="ltr" lang="en">` (keep the
   `data-canvas` / `data-board` attributes).
2. The font `<link>`, the three `--font-*` variables and `--display-w`
   (section 3).
3. The two nav button labels + arrow glyphs:
   - RTL: `‹ السابق` / `التالي ›`
   - LTR: `‹ Prev` / `Next ›`
4. The `.topbar .brand span` and `<title>` text.

The keyboard and swipe logic already flip based on `dir` — no JS edits needed.
In RTL, `ArrowLeft` advances (reading moves leftward); in LTR, `ArrowRight` does.

---

## 5. Length budget → slide count

A reader spends roughly **60–90 seconds** per slide. Map the requested reading
time to a slide count and stop there:

| Reading budget | Slides (incl. cover + closing) |
|----------------|--------------------------------|
| ~10 min        | 8–10                           |
| ~20 min        | 14–16                          |
| ~30 min        | 16–20                          |

Going over the budget defeats a calm deck. If the topic needs more, tighten each
slide rather than adding slides.

In **teaching decks**, the opening challenge, challenge-revisited, and question
set/answer box slides (components.md §19–21) count **inside** this budget — they
replace content slides, they are never added on top of the count.
