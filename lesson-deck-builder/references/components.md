# Components — Lesson-Deck-Builder

A copy-paste library of slide building blocks. Every block reads the template's
tokens, so it follows the canvas and board set on `<html>` and the fonts of the
deck's language.
Each `<section class="slide">` is one slide; the first slide must keep
`class="slide active"`. Wrap text/figures you want animated in `class="reveal"`
and stagger them with inline `style="--d:.2s"` (delay grows ~0.06–0.08s each).

**Golden rule for visuals:** put an illustration on every slide that earns one.
Use **HTML/CSS** for anything containing text (window mockups, chat, cards) so
RTL Arabic renders correctly. Use **SVG only for shapes and icons** — never put
Arabic text inside `<svg>` (it breaks shaping/direction).

**Suggested use cases (v1.2).** Every component below lists the teaching jobs it fits, **best fit
first — suggestions, not obligations.** The same use case appears under many components on purpose;
each one is explained once, with examples, in `use-cases.md`, whose reverse index answers the
builder's real question: *which components fit this job?* Vary components across a deck — a first-
ranked fit is the usual choice, not the required one.

**One style, two canvases (v1.3).** Every component renders in Sketchbook, on paper and on every
chalkboard board. §1–§21 read the template's canvas tokens (`--ink`, `--line`, `--paper`) and the pen
tokens (`--k-a` · `--k-b` · `--k-c` and their washes `--wash-a/b/c`); §22–§31 read only the **bridge
tokens** (`style-system.md §7`); §32 reads the bridge tokens plus a few canvas and shape tokens. The template
defines all of them for both canvases. §32 holds
the mechanics ported from the retired style families, redrawn in chalk — working code in
`assets/style-samples/sketchbook-kit.html`.

## Table of contents
1. Cover slide
2. Closing slide
3. Section head + feature cards (the "map")
4. Two-column: text + figure
5. Point list
6. Aside / callout
7. Window mockup + chat
8. Source rows (search result)
9. Bar chart (data / artifact)
10. Linked cards (timeline / memory)
11. Step card (process / "skill")
12. Tri-grid (three parallel ideas)
13. Tiles (labelled list with icons)
14. Comparison tiers (with meters)
15. Flow recap (pills + arrows)
16. Code window
17. Icon set (drop-in 24×24 strokes)
18. Roadmap / learning-path (current + completed steps marked)
19. Opening challenge (commit before teaching)
20. Challenge revisited (close the loop)
21. Question set + copyable answer box (the adaptive loop)
22. Labels on the figure — paper + chalkboard
23. Linked figure (same color, same thing) — paper + chalkboard
24. Anchored gloss (define it where it stands) — paper + chalkboard
25. Builds (engine v2 — one idea per press) — paper + chalkboard · engine
26. Magic board (marks that move between states) — paper + chalkboard
27. Reactive sentence (a number you can drag) — paper + chalkboard
28. Ink marks (hand-drawn annotations in order) — Sketchbook (paper + chalkboard)
29. Eraser (write, erase, rewrite) — Sketchbook (paper + chalkboard)
30. Sketch chart (Sketchbook skin for §9) — Sketchbook (paper + chalkboard)
31. Live element (line boil) — Sketchbook (paper + chalkboard)
32. Skeletons and ported mechanics (stepper skeleton, lab, note stack, tray, footnotes, duo panes, quiz,
    token journey, spotlight cover, smudge panels, skins stepper, key passage frame)

---

## 1. Cover slide
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. State the one big idea `state-thesis`
2. Show where we are going `orient`

```html
<section class="slide active">
  <div class="inner cover">
    <svg class="spark reveal" style="--d:.05s" viewBox="0 0 120 120" aria-hidden="true">
      <g stroke="var(--k-a)" stroke-width="3.4" stroke-linecap="round"><line x1="60" y1="14" x2="60" y2="106"/><line x1="14" y1="60" x2="106" y2="60"/><line x1="27" y1="27" x2="93" y2="93"/><line x1="93" y1="27" x2="27" y2="93"/></g>
      <circle cx="60" cy="60" r="10" fill="var(--paper)" stroke="var(--ink)" stroke-width="2.4"/>
    </svg>
    <span class="eyebrow reveal" style="--d:.12s"><span class="dot"></span> تمهيد ميسّر</span>
    <h1 class="reveal" style="--d:.2s">العنوان الرئيسي<br/>في سطرين</h1>
    <p class="lead reveal" style="--d:.3s">جملة واحدة تَعِد القارئ بما سيخرج به.</p>
    <div class="hint reveal" style="--d:.42s">للتنقّل: <kbd>←</kbd> <kbd>→</kbd> أو الأزرار · القراءة أقلّ من نصف ساعة</div>
  </div>
</section>
```

## 2. Closing slide
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Recap and connect `recap`
2. State the one big idea `state-thesis`
3. Show where we are going `orient`

```html
<section class="slide">
  <div class="inner cover">
    <svg class="spark reveal" style="--d:.05s" viewBox="0 0 120 120" aria-hidden="true">
      <g stroke="var(--k-c)" stroke-width="3.4" stroke-linecap="round"><line x1="60" y1="14" x2="60" y2="106"/><line x1="14" y1="60" x2="106" y2="60"/><line x1="27" y1="27" x2="93" y2="93"/><line x1="93" y1="27" x2="27" y2="93"/></g>
      <circle cx="60" cy="60" r="10" fill="var(--paper)" stroke="var(--ink)" stroke-width="2.4"/>
    </svg>
    <span class="eyebrow reveal" style="--d:.12s"><span class="dot"></span> خاتمة</span>
    <h1 class="reveal" style="--d:.2s">الخلاصة في سطر</h1>
    <p class="lead reveal" style="--d:.3s">جملة ختامية تلخّص الرسالة وتدعو لخطوة بسيطة.</p>
  </div>
</section>
```

## 3. Section head + feature cards (the "map")
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show where we are going `orient`
2. Present parallel ideas of equal weight `list-parallel`
3. Recap and connect `recap`

Use early to preview what's coming, or anywhere you list parallel items.
`c3` = three columns, `c2` = two.
```html
<section class="slide">
  <div class="inner">
    <div class="head">
      <span class="eyebrow reveal"><span class="dot"></span> نظرة عامة</span>
      <h2 class="reveal" style="--d:.08s">عنوان القسم</h2>
      <p class="lead reveal" style="--d:.16s">جملة تمهّد للبطاقات أدناه.</p>
    </div>
    <div class="cards c3">
      <div class="card reveal" style="--d:.2s"><div class="ico">{ICON}</div><h3>عنوان</h3><p>وصف من سطر إلى سطرين.</p></div>
      <div class="card reveal" style="--d:.26s"><div class="ico clay">{ICON}</div><h3>عنوان</h3><p>وصف.</p></div>
      <div class="card reveal" style="--d:.32s"><div class="ico blue">{ICON}</div><h3>عنوان</h3><p>وصف.</p></div>
    </div>
  </div>
</section>
```
Icon background variants (pen washes): default and `gold` (pen c), `clay` (pen a), `blue` (pen b).

## 4. Two-column: text + figure
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Define a new term `define-term`
3. Name the parts of a thing `label-parts`
4. Show numbers and evidence `show-quantity`

`.grid2` puts text first; `.grid2.rev` puts the figure first.
```html
<section class="slide">
  <div class="inner">
    <div class="grid2">
      <div class="col-text">
        <span class="eyebrow reveal"><span class="dot"></span> قسم</span>
        <h2 class="reveal" style="--d:.08s">عنوان الشريحة</h2>
        <p class="lead reveal" style="--d:.16s">فقرة هادئة تشرح الفكرة.</p>
        <!-- optional: point list here -->
      </div>
      <div class="fig reveal" style="--d:.2s">
        <div class="num">٠١</div>
        <!-- drop any figure/mockup here -->
      </div>
    </div>
  </div>
</section>
```

## 5. Point list
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Recap and connect `recap`
3. Walk through a procedure `follow-procedure`

```html
<ul class="points">
  <li class="reveal" style="--d:.24s"><span class="tick"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></span> نقطة موجزة.</li>
  <li class="reveal" style="--d:.3s"><span class="tick"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></span> نقطة أخرى.</li>
</ul>
```

## 6. Aside / callout
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Correct a misconception `correct-misconception`
2. Define a new term `define-term`
3. State the one big idea `state-thesis`

```html
<div class="aside reveal" style="--d:.38s"><b>لافتة:</b> معلومة جانبية أو تعريف مختصر لمصطلح ورد للتوّ.</div>
```

## 7. Window mockup + chat
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show a tool or interface in use `demo-interface`
2. Tell a history or story in order `tell-story`
3. Walk through code `walk-code`

A browser/app frame. Put any UI text in HTML (not SVG).
```html
<div class="win">
  <div class="bar">
    <div class="dots"><i style="background:#d98b78"></i><i style="background:#dcc06a"></i><i style="background:#8bb088"></i></div>
    <div class="pill">عنوان النافذة</div>
  </div>
  <div class="body">
    <div class="chat">
      <div class="bubble user"><div class="who">أنت</div>رسالة المستخدم.</div>
      <div class="bubble bot"><div class="who">المساعد</div>الردّ.</div>
    </div>
  </div>
</div>
```

## 8. Source rows (search result look)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show a tool or interface in use `demo-interface`
2. Show numbers and evidence `show-quantity`
3. Present parallel ideas of equal weight `list-parallel`

```html
<div class="src">
  <div class="row reveal" style="--d:.3s"><span class="fav" style="background:var(--k-a)"></span><span class="ln" style="width:70%"></span></div>
  <div class="row reveal" style="--d:.36s"><span class="fav" style="background:var(--k-b)"></span><span class="ln" style="width:55%"></span></div>
  <div class="row reveal" style="--d:.42s"><span class="fav" style="background:var(--k-c)"></span><span class="ln" style="width:62%"></span></div>
</div>
```

## 9. Bar chart (data / generated artifact)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show numbers and evidence `show-quantity`
2. Compare options side by side `compare-options`

```html
<div class="barchart">
  <div class="b" style="height:45%"></div>
  <div class="b" style="height:70%; background:var(--k-c)"></div>
  <div class="b" style="height:58%"></div>
  <div class="b" style="height:88%; background:var(--k-b)"></div>
  <div class="b" style="height:66%"></div>
</div>
```

## 10. Linked cards (timeline / progression)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Tell a history or story in order `tell-story`
2. Walk through a procedure `follow-procedure`
3. Show how something works inside `explain-mechanism`

Stack rows joined by a dashed connector.
```html
<div style="display:grid; gap:12px;">
  <div style="display:flex; align-items:center; gap:12px;">
    <div style="width:40px;height:40px;border-radius:12px;background:var(--wash-a);display:grid;place-items:center;color:var(--k-a);">{ICON}</div>
    <div style="flex:1"><div style="height:9px;width:70%;background:var(--line);border-radius:5px;margin-bottom:6px"></div><div style="height:9px;width:45%;background:var(--line);border-radius:5px"></div></div>
  </div>
  <div style="margin-inline-start:20px; height:18px; border-inline-start:2px dashed var(--k-c);"></div>
  <div style="display:flex; align-items:center; gap:12px;">
    <div style="width:40px;height:40px;border-radius:12px;background:var(--wash-c);display:grid;place-items:center;color:var(--k-c);">{ICON}</div>
    <div style="flex:1"><div style="height:9px;width:55%;background:var(--line);border-radius:5px"></div></div>
  </div>
</div>
```

## 11. Step card (process / reusable "recipe")
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Walk through a procedure `follow-procedure`
2. Walk through code `walk-code`
3. Recap and connect `recap`

```html
<div class="stepcard">
  <div class="tag">قالب · خطوات</div>
  <div class="title">اسم العملية</div>
  <div class="step"><span class="n">1</span> الخطوة الأولى.</div>
  <div class="step"><span class="n">2</span> الخطوة الثانية.</div>
  <div class="step"><span class="n">3</span> الخطوة الثالثة.</div>
</div>
```

## 12. Tri-grid (three parallel ideas, centered)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Compare options side by side `compare-options`
3. State the one big idea `state-thesis`

```html
<div class="trigrid">
  <div class="rc reveal" style="--d:.24s"><div class="ico">{ICON}</div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin-bottom:6px">عنوان</h3><small>وصف قصير.</small></div>
  <div class="rc reveal" style="--d:.32s"><div class="ico clay">{ICON}</div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin-bottom:6px">عنوان</h3><small>وصف.</small></div>
  <div class="rc reveal" style="--d:.4s"><div class="ico gold">{ICON}</div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin-bottom:6px">عنوان</h3><small>وصف.</small></div>
</div>
```

## 13. Tiles (labelled list with icons, 2 columns)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Name the parts of a thing `label-parts`
3. Show where we are going `orient`

```html
<div class="tiles">
  <div class="tile reveal" style="--d:.22s"><div class="ico blue">{ICON}</div><div class="tx"><h4>عنوان</h4><p>وصف من سطر.</p></div></div>
  <div class="tile reveal" style="--d:.3s"><div class="ico">{ICON}</div><div class="tx"><h4>عنوان</h4><p>وصف.</p></div></div>
</div>
```

## 14. Comparison tiers (with meters)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Compare options side by side `compare-options`
2. Show numbers and evidence `show-quantity`

For comparing options/levels. Badge classes: `t-a` `t-b` `t-c`.
```html
<div style="display:grid; gap:14px;">
  <div class="tier reveal" style="--d:.24s">
    <div class="badge t-a">الأول</div>
    <p>وصف الخيار.</p>
    <div><span class="meter-label">المقياس</span><div class="meter"><span class="on"></span><span class="on"></span><span class="on"></span><span class="on"></span><span class="on"></span></div></div>
  </div>
  <div class="tier reveal" style="--d:.32s">
    <div class="badge t-b">الثاني</div>
    <p>وصف.</p>
    <div><span class="meter-label">المقياس</span><div class="meter"><span class="on"></span><span class="on"></span><span class="on"></span><span></span><span></span></div></div>
  </div>
</div>
```

## 15. Flow recap (pills + arrows)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Recap and connect `recap`
2. Walk through a procedure `follow-procedure`
3. Show how something works inside `explain-mechanism`

RTL arrow glyph is `‹` (points left = forward). For LTR use `›`.
```html
<div class="flow reveal" style="--d:.3s">
  <span class="pill">مرحلة ١</span><span class="arrow">‹</span>
  <span class="pill">مرحلة ٢</span><span class="arrow">‹</span>
  <span class="pill">مرحلة ٣</span>
</div>
```

## 16. Code window (dark, for code/tech topics)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Walk through code `walk-code`
2. Show a tool or interface in use `demo-interface`
3. Show one state turning into another `show-transformation`

```html
<div class="win code">
  <div class="bar"><div class="dots"><i style="background:#d98b78"></i><i style="background:#dcc06a"></i><i style="background:#8bb088"></i></div><div class="pill" style="background:#3a3f37;border-color:#4a4f44;color:#b6bbab;">terminal</div></div>
  <div class="body" style="padding:18px;">
    <div class="codeline"><span class="ln" style="width:18px;background:#7d9a86"></span><span class="ln" style="width:120px;background:#b6bbab"></span></div>
    <div class="codeline" style="padding-inline-start:18px"><span class="ln" style="width:60px;background:#cdaa6a"></span><span class="ln" style="width:90px;background:#8a9080"></span></div>
    <div style="margin-top:12px;display:flex;align-items:center;gap:8px;direction:ltr;"><span style="color:#8bb088;font-weight:600">›</span><span style="height:10px;width:160px;background:#5b6b52;border-radius:5px"></span><span style="width:8px;height:16px;background:#8bb088;border-radius:2px;animation:blink 1s steps(1) infinite"></span></div>
  </div>
</div>
```

---

## 17. Icon set (drop-in 24×24 strokes)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Show where we are going `orient`
3. Name the parts of a thing `label-parts`

Replace each `{ICON}` placeholder with one of these. They inherit color from
their container (`currentColor`). Wrap in the container that sets size/color
(`.ico`, `.tick`, etc.).

```html
<!-- check    --> <svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg>
<!-- search   --> <svg class="ic" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="16" y1="16" x2="21" y2="21"/></svg>
<!-- doc      --> <svg class="ic" viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6z"/><polyline points="14 3 14 7 18 7"/></svg>
<!-- chat     --> <svg class="ic" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
<!-- grid     --> <svg class="ic" viewBox="0 0 24 24"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></svg>
<!-- clock    --> <svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><polyline points="12 8 12 12 15 14"/></svg>
<!-- code     --> <svg class="ic" viewBox="0 0 24 24"><polyline points="9 7 4 12 9 17"/><polyline points="15 7 20 12 15 17"/></svg>
<!-- monitor  --> <svg class="ic" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
<!-- mobile   --> <svg class="ic" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><line x1="3" y1="8" x2="21" y2="8"/><line x1="9" y1="21" x2="15" y2="21"/></svg>
<!-- globe    --> <svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c4 4 4 14 0 18M12 3c-4 4-4 14 0 18"/></svg>
<!-- chart    --> <svg class="ic" viewBox="0 0 24 24"><polyline points="4 12 9 12 11 8 13 16 15 12 20 12"/></svg>
<!-- moon     --> <svg class="ic" viewBox="0 0 24 24"><path d="M17 18a5 5 0 1 1-3-9 7 7 0 1 0 3 9z"/></svg>
<!-- spark    --> <svg class="ic" viewBox="0 0 24 24"><line x1="12" y1="3" x2="12" y2="21"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="5.5" y1="5.5" x2="18.5" y2="18.5"/><line x1="18.5" y1="5.5" x2="5.5" y2="18.5"/></svg>
<!-- briefcase--> <svg class="ic" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
<!-- pen      --> <svg class="ic" viewBox="0 0 24 24"><path d="M4 20l4-1 10-10-3-3L5 16z"/><line x1="14" y1="6" x2="17" y2="9"/></svg>
<!-- arrow    --> <svg class="ic" viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="11 6 5 12 11 18"/></svg>
```

---

## 18. Roadmap / learning-path (current + completed steps marked)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show where we are going `orient`
2. Recap and connect `recap`
3. Tell a history or story in order `tell-story`

The spine of a standalone roadmap deck, and the "map" slide inside each roadmap
lesson. Mark the active step with the pen-a border + wash treatment shown below.
Keep every label in HTML (never SVG). List all steps in the roadmap deck; in a
lesson's map slide, show the full path, move the `· الآن` / `· now` marker to
the current step, and mark every finished step as **completed** — swap its
number box for a check and add `· تم` / `· done` to its label:
```html
<!-- a COMPLETED step: check instead of number -->
<div style="display:flex; align-items:center; gap:12px;">
  <div style="width:34px;height:34px;flex:none;border-radius:10px;background:var(--wash-a);display:grid;place-items:center;color:var(--k-a);"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></div>
  <div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0">مقدمة والصورة الكبيرة <span style="color:var(--k-a);font-size:.78rem;font-weight:600">· تم</span></h3><p style="margin:2px 0 0;font-size:.9rem;opacity:.72">أُنجزت في الدرس السابق.</p></div>
</div>
```
When the path itself changed since the previous lesson, flag it on the roadmap
slide. Two causes exist, each with its label — research-driven freshness
updates (`· مُحدَّث` / `· updated`) and additions the reader explicitly
approved via a proposal:
```html
<span style="color:var(--k-c);font-size:.78rem;font-weight:600">· أُضيف بطلبك</span>
```
(LTR: `· added at your request`.) Steps are never inserted, skipped, or
reshaped from answers alone. Progress must be visible at a glance: done →
check, now → pen-a border, later → plain number, changed → flagged label.
```html
<div style="display:grid; gap:10px; max-width:640px; margin-inline:auto;">
  <!-- a step (done or upcoming) -->
  <div style="display:flex; align-items:center; gap:12px;">
    <div style="width:34px;height:34px;flex:none;border-radius:10px;background:var(--wash-a);display:grid;place-items:center;color:var(--k-a);font-weight:700;">١</div>
    <div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0">مقدمة والصورة الكبيرة</h3><p style="margin:2px 0 0;font-size:.9rem;opacity:.72">ما هذا المجال، ولماذا يستحقّ التعلّم.</p></div>
  </div>
  <div style="margin-inline-start:16px;height:14px;border-inline-start:2px dashed var(--line);"></div>
  <!-- the CURRENT step: pen-a border + wash -->
  <div style="display:flex; align-items:center; gap:12px; background:var(--wash-a); border:1px solid var(--k-a); border-radius:14px; padding:10px 12px;">
    <div style="width:34px;height:34px;flex:none;border-radius:10px;background:var(--k-a);display:grid;place-items:center;color:var(--paper);font-weight:700;">٢</div>
    <div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0">الأساسيات <span style="color:var(--k-a);font-size:.78rem;font-weight:600">· الآن</span></h3><p style="margin:2px 0 0;font-size:.9rem;opacity:.72">وصف الخطوة الحالية.</p></div>
  </div>
  <div style="margin-inline-start:16px;height:14px;border-inline-start:2px dashed var(--line);"></div>
  <!-- a later step -->
  <div style="display:flex; align-items:center; gap:12px;">
    <div style="width:34px;height:34px;flex:none;border-radius:10px;background:var(--wash-c);display:grid;place-items:center;color:var(--k-c);font-weight:700;">٣</div>
    <div><h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin:0">التطبيق العملي</h3><p style="margin:2px 0 0;font-size:.9rem;opacity:.72">مشاريع صغيرة تُرسّخ ما سبق.</p></div>
  </div>
</div>
```
For LTR use Latin numerals (1, 2, 3), English labels, and `· now`; the layout
mirrors automatically. Muted text uses `opacity:.72` rather than a color var, so
it stays safe on both canvases and every board.

---

## 19. Opening challenge (commit before teaching)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Predict first, then verify `predict-first`
2. Correct a misconception `correct-misconception`
3. Let the reader push a variable `build-intuition`

**Teaching decks only.** Goes immediately after the cover, before any teaching.
Poses a real problem the deck's core idea solves and makes the reader **commit
to an answer** — tapping an option highlights it (inline handler only; the deck
must keep exactly ONE `<script>` tag, so never add another). Calibrate the
options to *attemptable-but-uncertain*. The closing line promises the return.
```html
<section class="slide">
  <div class="inner">
    <div class="head">
      <span class="eyebrow reveal"><span class="dot"></span> تحدّي البداية</span>
      <h2 class="reveal" style="--d:.08s">سؤال قبل أن نبدأ</h2>
      <p class="lead reveal" style="--d:.16s">نصّ المسألة الواقعية التي يحلّها هذا الدرس. اختر إجابة الآن — لا تقلق إن لم تكن متأكدًا.</p>
    </div>
    <div class="cards c3" onclick="if(event.target.closest('.card')){for(const c of this.children){c.style.borderColor='';c.style.background=''}const p=event.target.closest('.card');p.style.borderColor='var(--k-a)';p.style.background='var(--wash-a)'}">
      <div class="card reveal" style="--d:.22s;cursor:pointer"><h3>أ</h3><p>الخيار الأول.</p></div>
      <div class="card reveal" style="--d:.28s;cursor:pointer"><h3>ب</h3><p>الخيار الثاني.</p></div>
      <div class="card reveal" style="--d:.34s;cursor:pointer"><h3>ج</h3><p>الخيار الثالث.</p></div>
    </div>
    <div class="aside reveal" style="--d:.44s"><b>التزم بإجابتك.</b> سنعود إلى هذا السؤال نفسه في نهاية الدرس — وستحكم بنفسك.</div>
  </div>
</section>
```
For LTR swap the letters (A/B/C) and translate the copy. The tap-highlight is
decoration: the commitment works even if the reader only chooses mentally, so
never gate anything on the click.

## 20. Challenge revisited (close the loop)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Predict first, then verify `predict-first`
2. Correct a misconception `correct-misconception`
3. Recap and connect `recap`

**Mandatory in every teaching deck**, placed after the last concept and before
the recap. It restates the **exact same** problem from §19 — never a similar
one — and resolves it with the ideas just taught, making the before/after
explicit.
```html
<section class="slide">
  <div class="inner">
    <div class="head">
      <span class="eyebrow reveal"><span class="dot"></span> عودة إلى التحدّي</span>
      <h2 class="reveal" style="--d:.08s">السؤال نفسه — بأدواتك الجديدة</h2>
      <p class="lead reveal" style="--d:.16s">نصّ المسألة كما ورد في البداية، حرفيًا.</p>
    </div>
    <ul class="points">
      <li class="reveal" style="--d:.24s"><span class="tick"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></span> الخطوة الأولى في الحلّ، مبنية على مفهوم من الدرس.</li>
      <li class="reveal" style="--d:.3s"><span class="tick"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></span> الخطوة الثانية — ولماذا تنجح (الآلية، لا الوصف).</li>
      <li class="reveal" style="--d:.36s"><span class="tick"><svg class="ic" viewBox="0 0 24 24"><polyline points="5 12 10 17 19 7"/></svg></span> الإجابة الصحيحة، وسبب استبعاد البدائل.</li>
    </ul>
    <div class="aside reveal" style="--d:.46s"><b>لاحظ الفرق:</b> في الشريحة الثانية كان هذا تخمينًا — الآن صار استدلالًا. هذا هو مكسب الدرس.</div>
  </div>
</section>
```

## 21. Question set + copyable answer box (the adaptive loop)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Check understanding `check-recall`
2. Predict first, then verify `predict-first`

**Teaching decks only.** The question slide(s) use the normal card/list
components; mark transfer questions with the stretch badge. The final page is
the answer box: a pre-filled `<textarea>` the reader completes, selects all,
copies, and pastes back into the chat — the next lesson reads it to adapt.
No storage APIs, no extra scripts: the textarea holds its state in memory only.

Stretch badge (place beside a question's title):
```html
<span style="font-size:.7rem;font-weight:700;color:var(--k-c);background:var(--wash-c);border:1px solid var(--k-c);border-radius:999px;padding:2px 8px;vertical-align:middle;">stretch</span>
```

Answer-box slide:
```html
<section class="slide">
  <div class="inner">
    <div class="head">
      <span class="eyebrow reveal"><span class="dot"></span> صندوق الإجابات</span>
      <h2 class="reveal" style="--d:.08s">أجب، ثم انسخ والصق في المحادثة</h2>
      <p class="lead reveal" style="--d:.16s">اكتب إجاباتك داخل الصندوق، ثم حدّد النصّ كاملًا وانسخه وألصقه في المحادثة — الدرس التالي سيُبنى عليها.</p>
    </div>
    <div class="win reveal" style="--d:.24s">
      <div class="bar"><div class="dots"><i style="background:#d98b78"></i><i style="background:#dcc06a"></i><i style="background:#8bb088"></i></div><div class="pill">answers.txt</div></div>
      <div class="body" style="padding:14px;">
<textarea dir="auto" spellcheck="false" style="width:100%;min-height:240px;border:1px solid var(--line);border-radius:12px;background:var(--paper);color:var(--ink);font-family:var(--font-body);font-size:.95rem;line-height:1.7;padding:14px;resize:vertical;">LESSON: عنوان الدرس
STEP: 2 / 7 (موقع الدرس في الخريطة)
Q1 (اختيار): نصّ السؤال؟ [أ/ب/ج] — إجابتي: 
Q2 (اختيار): نصّ السؤال؟ [أ/ب/ج] — إجابتي: 
Q3 [stretch] (مفتوح): نصّ سؤال يتجاوز ما دُرّس بخطوة — إجابتي: 
Q4 (مفتوح): نصّ السؤال — إجابتي: 
</textarea>
      </div>
    </div>
    <div class="aside reveal" style="--d:.36s"><b>ملاحظة:</b> الأسئلة الموسومة <b>[stretch]</b> صُمّمت لتكون أبعد بخطوة — الخطأ فيها متوقّع ومفيد، وسيُعاد اختبارها في الدرس القادم.</div>
  </div>
</section>
```
Keep the `[stretch]` tags **inside the textarea text** — they must survive the
copy-paste so the next session can tell a designed miss from a genuine gap.
When a roadmap proposal is pending (see SKILL.md — persistent gaps only), add
one line to the template so the decision travels with the answers:
```
PROPOSAL: أرى من إجابات الدرسين الماضيين أن X يحتاج تثبيتًا — هل أضيف درسًا تحضيريًا قصيرًا إلى الخريطة في موضعه المناسب؟ [نعم/لا] — قراري:
```
(LTR: `PROPOSAL: Your last two lessons suggest X needs grounding — add a short
preparation deck to the roadmap at the right point? [yes/no] — My decision:`)

When the reader pastes the block back into chat: first update **NOTES.md**
(the cumulative notes file — see SKILL.md) and deliver it, answer each miss
with its mechanism, and act on the PROPOSAL line only if it carries an
explicit yes. The next lesson is then built from NOTES.md — re-testing misses
early in new clothing, and when a previously missed concept is now answered
correctly, saying so on the slide (`أخطأتَ فيه في الدرس الماضي — حللته الآن` /
"missed last lesson — solved now").

---

## Shared bits for §22–§32

Bridge tokens: already in `assets/template.html` (both canvases; listed in `style-system.md §7`). Controls
used by the examples below:

```css
/* shared controls for components 22–32 — Sketchbook buttons */
.k-ctrls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:12px}
.k-btn{font:inherit;font-family:var(--font-display);font-weight:700;color:var(--k-ink);background:var(--k-surface);
  border:1.6px solid var(--k-line);border-radius:12px;padding:4px 14px;cursor:pointer;transition:background .25s ease}
.k-btn:hover:not(:disabled){background:var(--k-hi)}
.k-btn:disabled{opacity:.35;cursor:default}
.k-dots{display:flex;gap:7px}
.k-dots b{width:9px;height:9px;border-radius:50%;border:1.5px solid var(--k-soft)}
.k-dots b.on{background:var(--k-a);border-color:var(--k-a)}
```

## 22. Labels on the figure
*Scope: paper + chalkboard*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Name the parts of a thing `label-parts`
2. Show how something works inside `explain-mechanism`
3. Show numbers and evidence `show-quantity`

Put each part's name ON the drawing with a short leader line instead of a numbered legend. A legend
makes the eye commute (read "3", hunt for 3, come back); a label brings the word to the part. Spatial
contiguity — words placed next to the pictures they describe — won in 22 of 22 experiments in Mayer's
research (median d 1.10), the strongest effect in his set for cutting wasted effort.

**Law 3 ruling:** a label is not an actor. Labels are static HTML text (the text rule) pinned in the
figure's own viewBox units, so they scale with the drawing; anything that MOVES stays inside the SVG.
Coordinates are physical on purpose: SVG never mirrors, so the pins don't either (correct in RTL too).

```css
/* 22 · labels on the figure — pins use the figure's own viewBox units */
.lf{position:relative;width:min(420px,100%);margin-inline:auto}
.lf > svg{display:block;width:100%;height:auto;overflow:visible}
.lf-pin{position:absolute;left:calc(var(--x) / var(--vw) * 100%);top:calc(var(--y) / var(--vh) * 100%);
  transform:translate(0,-50%);white-space:nowrap;font-family:var(--font-display);font-size:1.05rem;line-height:1.15;color:var(--k-ink)}
.lf-pin.end{transform:translate(-100%,-50%)}  /* text ends at the anchor */
.lf-pin.mid{transform:translate(-50%,-50%)}   /* text centred on the anchor */
.lf-lead{fill:none;stroke:var(--k-a);stroke-width:2;stroke-linecap:round}
```

```html
<!-- --vw/--vh = the viewBox size; --x/--y = each label's anchor point in viewBox units -->
<div class="lf" style="--vw:360;--vh:230">
  <svg viewBox="0 0 360 230" aria-hidden="true">
    <!-- the drawing, in the Sketchbook stroke vocabulary: filter="url(#wob)" -->
    <path class="lf-lead" d="M208 30 L248 24"/>   <!-- leader: from the part to the label's anchor -->
    <path class="lf-lead" d="M162 64 L118 52"/>
  </svg>
  <span class="lf-pin" style="--x:252;--y:24">first part</span>
  <span class="lf-pin end" style="--x:114;--y:52">second part</span>
</div>
```

- About six labels at most; past that, number the parts and put the key in a fixed tray (Law 1, mechanic 2).
- Leaders stay short and never cross each other or a label.
- To bring labels in one at a time, give a leader and its label the same `data-build` (§25).

## 23. Linked figure (same color, same thing)
*Scope: paper + chalkboard*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Name the parts of a thing `label-parts`
3. Define a new term `define-term`

Write each part's name in the color it has in the drawing; touching either the word or the shape lights
up both and dims the rest. Oliver Byrne's 1847 Euclid replaced letters with colored shapes so a proof could
be read straight off the picture; modern explainers (Red Blob Games) link text and diagram the same way.
Hover on mouse, tap to toggle on touch, focus for keyboard. At most three linked colors (`a`, `b`, `c`);
beyond that, use labels (§22). The words still name every part, so color is never the only signal.

```css
/* 23 · linked figure — touch a word or a shape to light both */
.lk-a{--lk:var(--k-a)} .lk-b{--lk:var(--k-b)} .lk-c{--lk:var(--k-c)}
.lk-t{color:var(--lk);font-weight:700;cursor:pointer;border-radius:4px;padding:0 .12em;
  text-decoration:underline dotted;text-underline-offset:4px;transition:background .3s ease,opacity .3s ease}
.lk-part{stroke:var(--lk);fill:var(--lk);fill-opacity:.1;transition:opacity .3s ease,fill-opacity .3s ease}
.lk-line{stroke:var(--lk);fill:none;transition:opacity .3s ease}
[data-linkbox][data-hot] [data-link]{opacity:.3}
[data-linkbox][data-hot="a"] [data-link="a"],[data-linkbox][data-hot="b"] [data-link="b"],
[data-linkbox][data-hot="c"] [data-link="c"]{opacity:1}
[data-linkbox][data-hot="a"] .lk-t[data-link="a"],[data-linkbox][data-hot="b"] .lk-t[data-link="b"],
[data-linkbox][data-hot="c"] .lk-t[data-link="c"]{background:var(--k-hi)}
[data-linkbox][data-hot="a"] .lk-part[data-link="a"],[data-linkbox][data-hot="b"] .lk-part[data-link="b"],
[data-linkbox][data-hot="c"] .lk-part[data-link="c"]{fill-opacity:.32}
```

```html
<div data-linkbox>
  <p>The <span class="lk-t lk-a" data-link="a" tabindex="0">first part</span> pushes on the
     <span class="lk-t lk-b" data-link="b" tabindex="0">second part</span>.</p>
  <svg viewBox="0 0 300 160" aria-hidden="true">
    <path class="lk-part lk-a" data-link="a" stroke-width="2.4" d="M30 40 L120 40 L120 120 L30 120 Z"/>
    <path class="lk-part lk-b" data-link="b" stroke-width="2.4" d="M150 40 L270 40 L270 120 L150 120 Z"/>
  </svg>
</div>
```

```js
// inside the deck's single <script>, after the engine
/* 23 · linked figure */
(function(){
  const hoverDev=matchMedia('(hover: hover)').matches;
  document.querySelectorAll('[data-linkbox]').forEach(box=>{
    box.querySelectorAll('[data-link]').forEach(el=>{
      const k=el.dataset.link;
      el.addEventListener('pointerenter',e=>{if(e.pointerType==='mouse')box.dataset.hot=k;});
      el.addEventListener('pointerleave',e=>{if(e.pointerType==='mouse'&&box.dataset.hot===k)delete box.dataset.hot;});
      el.addEventListener('focus',()=>{box.dataset.hot=k;});
      el.addEventListener('blur',()=>{if(box.dataset.hot===k)delete box.dataset.hot;});
      el.addEventListener('click',e=>{if(hoverDev&&e.pointerType!=='touch')return;
        if(box.dataset.hot===k)delete box.dataset.hot;else box.dataset.hot=k;});
    });
  });
})();
```

- Typical pairing: a formula or sentence above, the figure below, every term colored like its part.
- Add `lk-line` (stroke only) for parts that are lines rather than areas.

## 24. Anchored gloss (define it where it stands)
*Scope: paper + chalkboard*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Define a new term `define-term`
2. Point at what matters in a passage `highlight-passage`
3. Name the parts of a thing `label-parts`

A dotted term opens a small card pinned to the word; the card flips underneath when there is no room
above. This is Law 1's overlay mechanic made native: CSS anchor positioning places the card and the
browser handles the flip — no measuring script. Baseline since January 2026 (Chrome 125, Safari 26,
Firefox 147); older browsers fall back to "always above". The definition sits beside its word
(contiguity) and serves the skill's "define every new term" rule (pre-training).

The **nearest positioned ancestor** (usually the figure frame) is the area the card must fit in: terms
near its top flip their card below.

```css
/* 24 · anchored gloss — overlay mechanic (Law 1, #3) via anchor positioning */
.gl-t{text-decoration:underline dotted var(--k-a);text-underline-offset:5px;cursor:help;border-radius:3px;transition:background .25s ease}
.gl-t:hover,.gl-t:focus-visible{background:var(--k-hi);outline:none}
.gl-card{position:absolute;position-area:top;position-try-fallbacks:flip-block;margin:8px 0;width:max-content;max-width:240px;z-index:20;
  background:var(--k-card);color:var(--k-card-ink);border:1.5px solid var(--k-line);border-radius:10px;padding:8px 13px 10px;
  font-family:var(--font-body);font-weight:400;font-size:.84rem;line-height:1.5;text-align:start;letter-spacing:0;text-transform:none;
  box-shadow:0 14px 34px -20px rgba(0,0,0,.45);opacity:0;pointer-events:none;transition:opacity .3s ease}
.gl-card b{display:block;font-family:var(--font-display);font-size:1.12rem;line-height:1.15;margin-bottom:5px;color:var(--k-card-ink)}
.gl-t:hover + .gl-card,.gl-t:focus + .gl-card{opacity:1}
@supports not (anchor-name: --a){
  .gl-w{position:relative}
  .gl-card{bottom:calc(100% + 6px);left:50%;transform:translateX(-50%)}
}
```

```html
<!-- one anchor name per term: --g1, --g2, … (unique in the deck) -->
<span class="gl-w"><span class="gl-t" tabindex="0" style="anchor-name:--g1">term</span><span class="gl-card" role="tooltip" style="position-anchor:--g1"><b>term</b>One plain sentence that defines it.</span></span>
```

- One or two sentences per card, plain words; the card is a gloss, not a lesson.
- **Sketchbook skin** — an index card in the paper palette on both canvases (`style-system.md §5`, law 2):
  `.gl-card{border-radius:3px 7px 4px 8px;border-color:#29241B;background-image:linear-gradient(#C4553B,#C4553B);background-size:100% 1.5px;background-repeat:no-repeat;background-position:0 2.35em}`
- Numbered footnotes (§32e) use this same recipe for their positioning.

## 25. Builds (engine v2 — one idea per press)
*Scope: paper + chalkboard · engine*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Walk through a procedure `follow-procedure`
3. Name the parts of a thing `label-parts`
4. Tell a history or story in order `tell-story`
5. Recap and connect `recap`

Mark the parts of a slide with `data-build="0..n"` and the deck reveals them one press at a time before
the page turns. Segmenting — learner-paced chunks instead of one continuous unit — is one of Mayer's
principles for managing essential load (median d ≈ 0.79 across ten tests). The caption arrives with its
strokes, never after them.

**Engine behaviour (v2, in `assets/template.html`):**
- Next / Space / forward arrow / forward swipe → the next build; when none are left, the next page.
- Back → un-builds; on step 0 it goes to the previous page, which arrives **fully built**.
- Dots, Home and End arrive at step 0.
- The engine adds `.built` to every `[data-build]` ≤ the current step and `.now` to the ones equal to it,
  sets `data-step` on the slide, and fires two events on the slide: `build` (`detail.step`, `detail.of`)
  and `slideenter` (`detail.from`).
- `data-builds="n"` on a `<section class="slide">` declares steps for widgets that follow builds without
  their own `[data-build]` elements (§26 magic board, §28 ink marks, §29 eraser — `data-follow="build"`).
- `data-build="0"` = visible on arrival (the first strokes and the first caption).

```css
/* 25 · builds — the template already ships the [data-build] rules; this adds the caption stack */
.bcaps{display:grid}
.bcaps > *{grid-area:1/1}                      /* all captions share one cell: no reflow */
.bcaps > [data-build]:not(.now){opacity:0}     /* only the current step's caption shows */

/* builds inherit Sketchbook's one motion law (the template default) — no per-style variants */
```

```html
<section class="slide">
  <svg viewBox="0 0 320 230" aria-hidden="true">
    <g data-build="0"> <!-- strokes visible on arrival --> </g>
    <g data-build="1"> <!-- strokes for idea 1 (Sketchbook: give paths class="draw" to draw in) --> </g>
    <g data-build="2"> <!-- strokes for idea 2 --> </g>
  </svg>
  <div class="bcaps">
    <p data-build="0">What is already on the board.</p>
    <p data-build="1">Idea 1, in one line.</p>
    <p data-build="2">Idea 2, in one line.</p>
  </div>
</section>
```

- Never put `data-build` and `.reveal` on the same element (they fight over opacity and transform).
- Three to five builds per slide; more means the slide holds two ideas — split it.
- Component steppers with their own buttons (§32a) still exist: use builds when the keyboard should drive.

## 26. Magic board (marks that move between states)
*Scope: paper + chalkboard*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show one state turning into another `show-transformation`
2. Walk through code `walk-code`
3. Walk through a procedure `follow-procedure`
4. Compare options side by side `compare-options`

Each state of a board is a `<template>`; marks that keep the same `data-id` GLIDE to their new place
(view transitions), marks that vanish fade out, new marks fade in. When "+3" crosses the equals sign and
becomes "−3", moving the very same mark shows what happened; a cut between two pictures only shows
that something did. Same-document view transitions are Baseline (Chrome 111, Safari 18, Firefox 144);
without support the board simply swaps.

Use the `code` variant (one mark per line, `dir="ltr"`) for refactors: lines that survive slide to their
new position (the idea behind Slidev's Shiki Magic Move).

```css
/* 26 · magic board — view transitions glide the same mark between states */
.mb{display:flex;justify-content:center;align-items:baseline;flex-wrap:wrap;gap:.3em;min-height:1.5em;
  font-family:var(--font-display);font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.2;color:var(--k-ink)}
.mb .tk{display:inline-block}
.mb .tk.hot{color:var(--k-a)}
.mb.code{display:block;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.9rem;line-height:1.75;text-align:start;min-height:var(--mb-h,9em)}
.mb.code .tk{display:block;white-space:pre}
.mb-cap{text-align:center;color:var(--k-soft);min-height:3em;max-width:44ch;margin-inline:auto}
::view-transition-group(*){animation-duration:.55s;animation-timing-function:var(--k-ease)}
::view-transition-old(root),::view-transition-new(root){animation:none}
```

```html
<!-- buttons drive it; or put data-follow="build" here and data-builds="(states-1)" on the slide for keyboard steps -->
<div data-mb>
  <div class="mb" aria-live="polite"></div>
  <p class="mb-cap"></p>
  <div class="k-ctrls"><button class="k-btn" data-mb-prev>‹</button><span class="k-dots"></span><button class="k-btn" data-mb-next>next move ›</button></div>
  <template data-cap="Find x."><span data-id="two">2</span><span data-id="x">x</span><span data-id="op">+</span><span data-id="three">3</span><span data-id="eq">=</span><span data-id="rhs">11</span></template>
  <template data-cap="Take 3 from both sides: the 3 walks across and flips its sign."><span data-id="two">2</span><span data-id="x">x</span><span data-id="eq">=</span><span data-id="rhs">11</span><span data-id="op" class="hot">−</span><span data-id="three" class="hot">3</span></template>
  <template data-cap="11 − 3 is 8."><span data-id="two">2</span><span data-id="x">x</span><span data-id="eq">=</span><span data-id="rhs" class="hot">8</span></template>
</div>
```

```js
// inside the deck's single <script>, after the engine
/* 26 · magic board */
document.querySelectorAll('[data-mb]').forEach((w,wi)=>{
  const board=w.querySelector('.mb'), cap=w.querySelector('.mb-cap'), dots=w.querySelector('.k-dots'),
        pv=w.querySelector('[data-mb-prev]'), nx=w.querySelector('[data-mb-next]'),
        states=[...w.querySelectorAll('template')], slide=w.closest('.slide');
  let s=0;
  if(dots) states.forEach(()=>dots.appendChild(document.createElement('b')));
  function paint(){
    const frag=states[s].content.cloneNode(true);
    frag.querySelectorAll('[data-id]').forEach(e=>{e.classList.add('tk');e.style.viewTransitionName='mb'+wi+'-'+e.dataset.id;});
    board.replaceChildren(frag);
    if(cap) cap.textContent=states[s].dataset.cap||'';
    if(dots) [...dots.children].forEach((d,k)=>d.classList.toggle('on',k<=s));
    if(pv) pv.disabled=s===0; if(nx) nx.disabled=s===states.length-1;
  }
  function go(n){
    n=Math.max(0,Math.min(states.length-1,n)); if(n===s) return; s=n;
    if(document.startViewTransition&&slide.classList.contains('active')) document.startViewTransition(paint); else paint();
  }
  if(pv) pv.addEventListener('click',()=>go(s-1));
  if(nx) nx.addEventListener('click',()=>go(s+1));
  if(w.dataset.follow==='build') slide.addEventListener('build',e=>go(e.detail.step));
  paint();
});
```

- The example tokens are placeholders; any marks work (words, numbers, code lines, list items).
- Keep `data-id`s stable across templates; that is what makes a mark travel instead of fade.
- In follow mode the slide arrives at state 0 going forward and at the last state going back.

## 27. Reactive sentence (a number you can drag)
*Scope: paper + chalkboard*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Let the reader push a variable `build-intuition`
2. Show numbers and evidence `show-quantity`
3. Show how something works inside `explain-mechanism`
4. Compare options side by side `compare-options`

A number inside a sentence can be dragged (or focused and nudged with the arrow keys); the deck's own
small model rewrites the rest of the sentence and moves the figure. Bret Victor's reactive documents
let readers play with the author's assumptions and see the consequences. Few readers touch interactives
(about 10–15% in one widely cited newsroom count), so the **resting state must tell the story by itself**.

`data-capture` on the number is what makes the engine (v2) leave its drags and arrow keys alone. Drag
direction follows reading direction: in RTL, dragging left (or the left arrow) increases the value,
like a native RTL slider.

```css
/* 27 · reactive sentence */
.rs{min-height:var(--rs-h,4.2em)}   /* reserve the tallest wording so the figure below never moves */
.rs-num{color:var(--k-b);font-weight:700;border-bottom:2px dotted currentColor;cursor:ew-resize;touch-action:none;
  user-select:none;-webkit-user-select:none;padding:0 .2em;border-radius:4px 4px 0 0;white-space:nowrap;
  font-variant-numeric:tabular-nums;transition:background .2s ease}
.rs-num:hover,.rs-num:focus-visible,.rs-num.dragging{background:var(--k-hi);outline:none}
.rs-out{color:var(--k-a);font-weight:700;font-variant-numeric:tabular-nums}
```

```html
<p class="rs" data-rs="trip">
  Drive at <span class="rs-num" data-capture tabindex="0" role="slider" aria-label="speed in km per hour"
    data-min="20" data-max="120" data-step="10" data-value="60" data-unit=" km/h"></span>
  for two hours and you cover <span class="rs-out" data-out></span>.
</p>
```

```js
// inside the deck's single <script>, after the engine
/* 27 · reactive sentence — generic scrubber (fires a bubbling "rs-change" event) */
document.querySelectorAll('.rs-num').forEach(n=>{
  const min=+n.dataset.min, max=+n.dataset.max, st=+n.dataset.step||1, unit=n.dataset.unit||'',
        dec=(String(n.dataset.step||'1').split('.')[1]||'').length, px=+n.dataset.px||12;
  let v=null, sx=null, sv=0;
  const sign=()=>getComputedStyle(n).direction==='rtl'?-1:1;
  function set(x){
    x=+Math.min(max,Math.max(min,Math.round(x/st)*st)).toFixed(dec); if(x===v) return; v=x;
    n.textContent=x.toFixed(dec)+unit;
    n.setAttribute('aria-valuenow',x); n.setAttribute('aria-valuemin',min); n.setAttribute('aria-valuemax',max);
    n.dispatchEvent(new CustomEvent('rs-change',{bubbles:true,detail:{value:x}}));
  }
  n.addEventListener('pointerdown',e=>{sx=e.clientX;sv=v;n.setPointerCapture(e.pointerId);n.classList.add('dragging');e.preventDefault();});
  n.addEventListener('pointermove',e=>{if(sx!==null)set(sv+Math.round((e.clientX-sx)*sign()/px)*st);});
  const end=()=>{sx=null;n.classList.remove('dragging');};
  n.addEventListener('pointerup',end); n.addEventListener('pointercancel',end);
  n.addEventListener('keydown',e=>{
    const k=e.key, s=sign(), d=k==='ArrowUp'?1:k==='ArrowDown'?-1:k==='ArrowRight'?s:k==='ArrowLeft'?-s:0;
    if(d){set(v+d*st);e.preventDefault();}
    else if(k==='Home'){set(min);e.preventDefault();} else if(k==='End'){set(max);e.preventDefault();}
  });
  setTimeout(()=>set(+n.dataset.value),0);   /* after the deck's own model listeners exist */
});

/* the deck's own model — one small listener per sentence */
document.querySelectorAll('[data-rs="trip"]').forEach(p=>p.addEventListener('rs-change',e=>{
  p.querySelector('[data-out]').textContent=(e.detail.value*2)+' km';
}));
```

- Reserve the sentence's tallest wording with `--rs-h` so nothing below it moves (Law 1).
- Let the model reach the rule's edge (a plank that ends, a budget that runs out) and say so in words.

## 28. Ink marks (hand-drawn annotations in order)
*Scope: Sketchbook (paper + chalkboard)*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Point at what matters in a passage `highlight-passage`
2. Correct a misconception `correct-misconception`
3. Define a new term `define-term`
4. Walk through code `walk-code`

Six hand-drawn marks — underline, strike, box, circle, highlight, bracket — drawn one after another over
live text, the way a teacher's chalk follows the sentence. Signaling (cues that show the structure of the
essential material) helped in 24 of 28 experiments (median d 0.41); the order is part of the cue. This is
a native take on the rough-notation library (the validator allows one script), using the wobble filter.

Modes: `data-inkbox="enter"` draws every mark in `data-o` order when the slide opens;
`data-inkbox="build"` draws mark N at build step N (give the slide `data-builds="N"`).
Colors: `data-c="a|b|c|soft"` (bridge tokens). In RTL the bracket moves to the right-hand side.

```css
/* 28 · ink marks */
.inkbox{position:relative}
.inkbox .ink-text{position:relative;z-index:1}
[data-ink]{white-space:nowrap}
.ink-text[data-ink]{white-space:normal}
.ink-layer{position:absolute;inset:0;width:100%;height:100%;overflow:visible;pointer-events:none}
.ink-layer.under{z-index:0} .ink-layer.over{z-index:2}
.ink-layer path{fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1;opacity:0}
.ink-layer path.go{stroke-dashoffset:0;opacity:1;transition:stroke-dashoffset .45s var(--k-ease) var(--d,0s),opacity .01s linear var(--d,0s)}
```

```html
<div class="inkbox" data-inkbox="enter">
  <p class="ink-text" data-ink="bracket" data-o="6" data-c="soft">Most people think
    <span data-ink="strike" data-o="1" data-c="a">the wrong idea</span>, but the
    <span data-ink="underline" data-o="2" data-c="c">key word</span> changes it: the
    <span data-ink="box" data-o="3" data-c="b">named part</span> does
    <span data-ink="highlight" data-o="4">the real work</span> on
    <span data-ink="circle" data-o="5" data-c="a">both sides</span>.</p>
</div>
```

```js
// inside the deck's single <script>, after the engine
/* 28 · ink marks — native rough-notation idea; needs the #wob filter */
(function(){
  const NS='http://www.w3.org/2000/svg', COL={a:'var(--k-a)',b:'var(--k-b)',c:'var(--k-c)',soft:'var(--k-soft)'};
  const rnd=seed=>{let s=seed;return()=>(s=s*16807%2147483647)/2147483647;};
  function shapes(type,r,R,rtl){
    const j=a=>(R()-.5)*2*a, f=v=>v.toFixed(1), P=[];
    if(type==='underline'){const y=r.y+r.h-1;for(let k=0;k<2;k++)P.push(`M${f(r.x-3+j(2))} ${f(y+j(1.5))} Q${f(r.x+r.w*.5+j(6))} ${f(y+2.5+j(2))} ${f(r.x+r.w+4+j(2))} ${f(y+j(1.5))}`);}
    else if(type==='strike'){const y=r.y+r.h*.56;for(let k=0;k<2;k++)P.push(`M${f(r.x-4+j(2))} ${f(y+j(2))} Q${f(r.x+r.w*.5+j(6))} ${f(y-2+j(2))} ${f(r.x+r.w+2+j(1.5))} ${f(y+j(2))}`);}
    else if(type==='box'){const x0=r.x-6,y0=r.y-2,x1=r.x+r.w+6,y1=r.y+r.h+2;for(let k=0;k<2;k++)P.push(`M${f(x0+j(2))} ${f(y0+j(2))} L${f(x1+j(2))} ${f(y0+j(2))} L${f(x1+j(2))} ${f(y1+j(2))} L${f(x0+j(2))} ${f(y1+j(2))} L${f(x0+j(1.5))} ${f(y0-1+j(1.5))} L${f(x0+10)} ${f(y0+j(1.5))}`);}
    else if(type==='circle'){const cx=r.x+r.w/2,cy=r.y+r.h/2,rx=r.w/2+9,ry=r.h/2+7;
      for(let k=0;k<2;k++){const a0=-2.4+j(.4),N=36,s=1+k*.05;let d='';
        for(let i=0;i<=N;i++){const t=a0+i/N*Math.PI*2*1.08,w=1+.035*Math.sin(t*2+k)+j(.015);d+=(i?'L':'M')+f(cx+Math.cos(t)*rx*w*s)+' '+f(cy+Math.sin(t)*ry*w*s);}
        P.push(d);}}
    else if(type==='highlight'){const y=r.y+r.h*.55;P.push(`M${f(r.x-3)} ${f(y+j(1))} L${f(r.x+r.w+3)} ${f(y+j(1))}`);}
    else if(type==='bracket'){const s=rtl?-1:1,x=rtl?r.x+r.w+20:r.x-20,y0=r.y+6,y1=r.y+r.h-6;
      for(let k=0;k<2;k++)P.push(`M${f(x+9*s+j(1.5))} ${f(y0+j(1.5))} Q${f(x+j(1))} ${f(y0+j(1))} ${f(x+j(1.5))} ${f(y0+14)} L${f(x+j(1.5))} ${f(y1-14)} Q${f(x+j(1))} ${f(y1+j(1))} ${f(x+9*s+j(1.5))} ${f(y1+j(1.5))}`);}
    return P;
  }
  document.querySelectorAll('[data-inkbox]').forEach((box,bi)=>{
    const mk=c=>{const s=document.createElementNS(NS,'svg');s.setAttribute('class','ink-layer '+c);s.setAttribute('aria-hidden','true');return s;};
    const under=mk('under'), over=mk('over'); box.prepend(under); box.append(over);
    const slide=box.closest('.slide'), mode=box.dataset.inkbox||'enter';
    let shown=0, upTo=0, timer=null;
    const rectOf=el=>{let x=0,y=0,n=el;while(n&&n!==box){x+=n.offsetLeft;y+=n.offsetTop;n=n.offsetParent;}return{x,y,w:el.offsetWidth,h:el.offsetHeight};};
    function paint(limit,animate){
      upTo=limit; const rtl=getComputedStyle(box).direction==='rtl';
      [under,over].forEach(s=>{s.setAttribute('viewBox',`0 0 ${box.clientWidth} ${box.clientHeight}`);s.replaceChildren();});
      const marks=[...box.querySelectorAll('[data-ink]')].filter(m=>+m.dataset.o<=limit).sort((a,b)=>a.dataset.o-b.dataset.o);
      const R=rnd(4242+bi), fresh=[]; let t=0, last=-1;
      marks.forEach(m=>{
        const o=+m.dataset.o, isNew=animate&&o>shown, type=m.dataset.ink, r=rectOf(m);
        if(isNew&&last>=0&&o!==last) t+=.7;
        shapes(type,r,R,rtl).forEach((d,k)=>{
          const p=document.createElementNS(NS,'path'); p.setAttribute('d',d); p.setAttribute('pathLength','1');
          if(type==='highlight'){p.style.stroke='var(--k-hi)';p.style.strokeWidth=(r.h*.8).toFixed(1);p.style.strokeLinecap='butt';}
          else{p.style.stroke=COL[m.dataset.c||'soft'];p.style.strokeWidth=type==='bracket'?'2':'2.3';p.setAttribute('filter','url(#wob)');}
          if(isNew){p.style.setProperty('--d',(t+k*.3).toFixed(2)+'s');fresh.push(p);} else {p.style.transition='none';p.classList.add('go');}
          (type==='highlight'?under:over).appendChild(p);
        });
        if(isNew) last=o;
      });
      shown=marks.length?Math.max(...marks.map(m=>+m.dataset.o)):0;
      requestAnimationFrame(()=>requestAnimationFrame(()=>fresh.forEach(p=>p.classList.add('go'))));
    }
    if(mode==='build') slide.addEventListener('build',e=>paint(e.detail.step,slide.classList.contains('active')));
    else slide.addEventListener('slideenter',()=>{clearTimeout(timer);shown=0;paint(0,false);timer=setTimeout(()=>paint(Infinity,true),700);});
    let rt; addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(()=>paint(upTo,false),200);});
    if(document.fonts) document.fonts.ready.then(()=>paint(upTo,false));
  });
})();
```

- Keep each marked phrase short (it must not wrap); the bracket marks a whole paragraph.
- Paper: red/blue pens and the yellow marker; chalkboard: the board's three chalk pens and its dust smear.

## 29. Eraser (write, erase, rewrite)
*Scope: Sketchbook (paper + chalkboard)*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Correct a misconception `correct-misconception`
2. Show one state turning into another `show-transformation`
3. Predict first, then verify `predict-first`

A refutation in three gestures: write the wrong idea, wipe it (a smear and a faint ghost stay, like a real
board), then write the better explanation. Refutation text — naming the misconception, saying plainly
that it's wrong, then explaining — beat other texts across 44 comparisons (g = 0.41), and a 2025
pre-registered meta-analysis of 294 effects found the same advantage. Writing is a mask wipe, so it works
on live text in any font; one `:dir(rtl)` rule makes the chalk travel right to left in Arabic.

`data-beat="N"` appears at beat N (`.wo` = written on, anything else fades in); `data-erase="N"` on a line
wipes it at beat N. Drive it by its buttons, or by the keyboard: `data-follow="build"` on the eraser and
`data-builds="3"` on the slide. Paper = pencil and a graphite smudge; chalkboard = chalk and a dust smear
(canvas tokens in `style-system.md §5`).

```css
/* 29 · eraser */
.er-line{position:relative;width:fit-content}
.er [data-beat]:not(.wo){opacity:0;transition:opacity .5s ease}
.er [data-beat].on:not(.wo){opacity:1}
.wo{-webkit-mask-image:linear-gradient(90deg,#000 40%,transparent 60%);mask-image:linear-gradient(90deg,#000 40%,transparent 60%);
  -webkit-mask-size:250% 100%;mask-size:250% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;
  -webkit-mask-position:100% 0;mask-position:100% 0;transition:-webkit-mask-position 1.3s var(--k-ease),mask-position 1.3s var(--k-ease)}
.wo.on{-webkit-mask-position:0 0;mask-position:0 0}
.wo:dir(rtl){-webkit-mask-image:linear-gradient(270deg,#000 40%,transparent 60%);mask-image:linear-gradient(270deg,#000 40%,transparent 60%);-webkit-mask-position:0 0;mask-position:0 0}
.wo.on:dir(rtl){-webkit-mask-position:100% 0;mask-position:100% 0}
.er-txt{display:inline-block;transition:-webkit-mask-position 1.3s var(--k-ease),mask-position 1.3s var(--k-ease),opacity .9s var(--k-ease) .2s}
.er-line.erased .er-txt{opacity:var(--er-ghost)}
.er-smear{position:absolute;inset:-6px -16px;pointer-events:none;border-radius:40% 30% 45% 35%/50% 40% 60% 50%;
  background:repeating-linear-gradient(177deg,var(--er-streak) 0 4px,transparent 4px 9px),var(--er-wash)}
.er-stamp{position:absolute;inset-inline-end:-14px;top:-20px;font-family:var(--font-display);color:var(--k-a);font-weight:700;
  font-size:1.3rem;transform:rotate(-7deg);opacity:0;transition:opacity .4s ease .8s;white-space:nowrap}
.er-line.erased .er-stamp{opacity:1}
.er-lab{display:block;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--k-soft);margin-top:12px}
.er-lab:lang(ar){letter-spacing:0;text-transform:none;font-size:.8rem}
.er.noanim,.er.noanim *{transition:none!important}
```

```html
<div class="er" data-eraser>
  <span class="er-lab" data-beat="1">the belief</span>
  <div class="er-line" data-erase="2"><span class="er-txt wo" data-beat="1">The common wrong idea.</span><span class="er-smear wo" data-beat="2"></span><span class="er-stamp">not true</span></div>
  <span class="er-lab" data-beat="2">the refutation</span>
  <div class="er-line"><span class="er-txt wo" data-beat="2">Say plainly what is true instead.</span></div>
  <span class="er-lab" data-beat="3">the better idea</span>
  <p data-beat="3">Explain why, in one or two sentences.</p>
  <div class="k-ctrls"><button class="k-btn" data-er-next>next beat ›</button><button class="k-btn" data-er-again>again</button></div>
</div>
```

```js
// inside the deck's single <script>, after the engine
/* 29 · eraser — beats by button, or by build step (data-follow="build") */
document.querySelectorAll('[data-eraser]').forEach(er=>{
  const slide=er.closest('.slide'), follow=er.dataset.follow==='build',
        max=Math.max(...[...er.querySelectorAll('[data-beat]')].map(e=>+e.dataset.beat)),
        nx=er.querySelector('[data-er-next]'), ag=er.querySelector('[data-er-again]');
  let beat=0, t=null;
  function set(b){
    beat=Math.max(0,Math.min(max,b));
    er.querySelectorAll('[data-beat]').forEach(e=>e.classList.toggle('on',+e.dataset.beat<=beat));
    er.querySelectorAll('[data-erase]').forEach(e=>e.classList.toggle('erased',+e.dataset.erase<=beat));
    if(nx) nx.disabled=beat>=max;
  }
  function replay(delay){
    clearTimeout(t); er.classList.add('noanim'); set(0); void er.offsetWidth;
    requestAnimationFrame(()=>requestAnimationFrame(()=>{er.classList.remove('noanim');t=setTimeout(()=>set(1),delay);}));
  }
  if(follow) slide.addEventListener('build',e=>set(e.detail.step));
  else{
    if(nx) nx.addEventListener('click',()=>set(beat+1));
    if(ag) ag.addEventListener('click',()=>replay(300));
    slide.addEventListener('slideenter',()=>replay(600));
  }
  set(0);
});
```

- In follow mode, drop the buttons: the keyboard writes, erases and rewrites.
- The ghost of the erased line stays readable on purpose — the misconception is answered, not hidden.

## 30. Sketch chart (Sketchbook skin for §9)
*Scope: Sketchbook (paper + chalkboard)*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show numbers and evidence `show-quantity`
2. Compare options side by side `compare-options`

Bars filled with hachure, cross-hatch or dots and outlined with the wobble stroke look drawn rather than
printed. Sketchiness reads as "roughly" (roughViz's own advice: sketchy charts suit intent, not
precision), so **the exact value is always printed at the tip**. Labels and values stay in HTML.
In RTL the bars grow from the right (the SVG is mirrored; the text is not).

```css
/* 30 · sketch chart */
.skc{display:grid;gap:9px}
.skc-row{display:grid;grid-template-columns:minmax(7em,9.5em) 1fr 2.8em;gap:12px;align-items:center}
.skc-l{font-size:.82rem;line-height:1.2;color:var(--k-ink)}
.skc-l small{display:block;color:var(--k-soft);font-size:.68rem;margin-top:2px}
.skc-row svg{width:100%;height:30px;display:block;overflow:visible}
.skc-row svg:dir(rtl){transform:scaleX(-1)}
.skc-v{font-family:var(--font-display);font-size:1.45rem;font-weight:700;line-height:1;font-variant-numeric:tabular-nums}
.skc-ink{stroke:var(--k-b);fill:none} .skc-dot{fill:var(--k-b)}
.skc-out{fill:none;stroke:var(--k-b);stroke-width:2;stroke-linejoin:round}
.skc-fill{fill:url(#skc-hatch);opacity:0;transition:opacity .6s ease var(--d,0s)}
.slide.active .skc-fill{opacity:1}
.skc.cross .skc-fill{fill:url(#skc-cross)} .skc.dots .skc-fill{fill:url(#skc-dots)}
```

```html
<!-- once per deck, inside the hidden defs <svg> that holds #wob (own ids: the template's #p-hatch / #p-dots are the figure fills) -->
<pattern id="skc-hatch" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)"><line class="skc-ink" x1="1" y1="0" x2="1" y2="6" stroke-width="1.5"/></pattern>
<pattern id="skc-cross" patternUnits="userSpaceOnUse" width="8" height="8"><path class="skc-ink" d="M0 0 L8 8 M8 0 L0 8" stroke-width="1.1"/></pattern>
<pattern id="skc-dots" patternUnits="userSpaceOnUse" width="6" height="6"><circle class="skc-dot" cx="3" cy="3" r="1.3"/></pattern>

<!-- the chart: bar length = value / max × 290 (viewBox 300 wide); add class "cross" or "dots" to .skc for other fills -->
<div class="skc">
  <div class="skc-row"><div class="skc-l">first label<small>source or n</small></div>
    <svg viewBox="0 0 300 30" preserveAspectRatio="xMinYMid meet" aria-hidden="true"><g filter="url(#wob)">
      <path class="skc-fill" style="--d:.7s" d="M2 5 L254 5 L254 25 L2 25 Z"/>
      <path class="skc-out draw" pathLength="1" style="--d:.5s" d="M2 5 L254 5 L254 25 L2 25 Z"/></g></svg>
    <span class="skc-v">1.22</span></div>
</div>
```

- One fill style per chart; vary fill only to separate series, never for decoration.
- Bars start at zero; if the honest axis doesn't start at zero, don't use bars.

## 31. Live element (line boil)
*Scope: Sketchbook (paper + chalkboard)*

**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Let the reader push a variable `build-intuition`
3. Show where we are going `orient`

Cycling three noise seeds a few times a second makes strokes "boil", like hand-drawn animation. On exactly
ONE element per slide it says "this is the live part" — the moving piece of a mechanism, the thing to drag,
the "you are here" mark. This is the single sanctioned exception to Law 4: boil is a property of the
hand-drawn stroke, not a second easing. 4 fps is calm (default); 12 fps reads as alarm.

```html
<!-- once per deck, inside the hidden defs <svg> -->
<filter id="boil0"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="2" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="3.6"/></filter>
<filter id="boil1"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="9" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="3.6"/></filter>
<filter id="boil2"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="15" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="3.6"/></filter>

<!-- on the one live part of a figure (an SVG group, never text) -->
<g class="live" data-fps="4"> … strokes … </g>
```

```js
// inside the deck's single <script>, after the engine
/* 31 · live element — boils only while its slide is showing */
document.querySelectorAll('.live').forEach(g=>{
  const slide=g.closest('.slide'), fps=+g.dataset.fps||4; let k=0;
  g.setAttribute('filter','url(#boil0)');
  setInterval(()=>{if(!slide.classList.contains('active'))return;k=(k+1)%3;g.setAttribute('filter','url(#boil'+k+')');},1000/fps);
});
```

- One `.live` per slide (the validator warns on more); never on text the reader must read.

## 32. Skeletons and ported mechanics

Behavioral skeletons for slides that need more than a static figure. 32a, 32c and 32g are Sketchbook's own;
32b, 32d, 32e, 32f and 32h–32l are the mechanics of the **retired style families** (Playroom, Nocturne,
Terra), ported to the Sketchbook skin and tested on paper, on every board, in Arabic (RTL) and with several
instances on one deck. Working code for all of them: `assets/style-samples/sketchbook-kit.html` (the code
below is copied from it). Copy the mechanics, then draw a fresh per-topic skin (Law 2).

Rules for every §32 script:
- **Per container.** Each script loops over its containers (`.stepper`, `[data-lab]`, `.ixwrap`, `.panes`,
  `.journey`…), so a component can appear on as many slides as the deck needs. Never address a §32
  component by a global `id`.
- **Content lives in a small config object** keyed by the container's data attribute (`STEPPERS`, `LABS`,
  `LAMPS`) or in data attributes on the markup; the skeleton code itself is never edited per topic.
- **Ported means:** the behaviour is kept, the look is Sketchbook — wobbly ink/chalk frames, Caveat
  (Playpen in Arabic), pens through `--k-a/b/c`, one motion law (`--k-ease`). Springs, glows, blur-in
  entrances and whisper fades did not come along; the smudge that clears in place (§32j) is the one blur
  kept, because it is a depth mechanic, not an entrance.
- Besides the bridge tokens, §32 reads the template's canvas tokens (`--paper`, `--pencil`, `--shadow`)
  and shape tokens (`--wob-r`, `--wob-s`, `--display-w`) — all defined in `assets/template.html`.

### 32a. Steppable figure (the stepper skeleton)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Walk through a procedure `follow-procedure`
3. Tell a history or story in order `tell-story`
4. Show one state turning into another `show-transformation`
5. Walk through code `walk-code`

One skeleton for every figure that steps through states with its own buttons (use builds, §25, when the
keyboard should drive instead). The skeleton owns the state index, prev/next, the caption fade and the step
label; the scene says what changes per state through `|`-separated lists on ANY element (SVG or HTML pin):
`data-o` opacity · `data-sw` stroke width · `data-tf` CSS transform (moves an actor in viewBox units,
Law 3) · `data-txt` text (counters, readouts) · `data-w` shown from state *w* on. Pins sit in the figure's
own viewBox units (§22). Per-skin elements carry `data-skin` (§32k); a stepper without skins simply has
none. A hand-built variant (CSS keyed on the figure's own `data-step`) is in slide 3 of `sketchbook.html`.

```css
/* §32a · stepper skeleton (state index · prev/next · caption fade · per-state values) + §32k skins (ported from Terra) */
.st-fig{position:relative;container-type:inline-size}
.st-fig > svg{display:block;width:100%;height:auto;overflow:visible}
.st-pin{position:absolute;left:calc(var(--x) / var(--vw) * 100%);top:calc(var(--y) / var(--vh) * 100%);transform:translate(-50%,-50%);
  font-family:var(--font-display);font-weight:var(--display-w);font-size:min(1.25rem,max(9px,calc(19 * 100cqi / var(--vw))));white-space:nowrap;color:var(--k-soft)}
.st-el{transition:opacity .7s var(--k-ease),stroke-width .7s var(--k-ease),transform .9s var(--k-ease)}
.stepbar{display:flex;align-items:center;gap:14px;margin-top:14px;justify-content:center}
.stepbtn{font-family:var(--font-display);font-size:1.25rem;font-weight:var(--display-w);color:var(--k-ink);background:var(--k-surface);
  border:1.8px solid var(--k-ink);border-radius:50% 46% 52% 48%/48% 52% 46% 52%;width:44px;height:44px;cursor:pointer;transition:transform .2s ease,background .2s}
.stepbtn:hover:not(:disabled){transform:rotate(-4deg) scale(1.06);background:var(--k-hi)}
.stepbtn:disabled{opacity:.3;cursor:default}
.steplabel{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.2rem;color:var(--pencil);min-width:7ch;text-align:center}
.caption{font-family:var(--font-display);font-weight:var(--display-w);font-size:clamp(1.3rem,2.5vw,1.6rem);min-height:2.6em;text-align:center;margin-top:10px;transition:opacity .3s}
.skinbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:14px}
.skinbtn{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.1rem;color:var(--k-ink);background:var(--k-surface);cursor:pointer;
  border:1.6px solid var(--k-soft);border-radius:var(--wob-s);padding:2px 14px;transition:background .3s,border-color .3s}
.skinbtn.on{background:var(--k-hi);border-color:var(--k-ink)}
.skinnote{font-size:.82rem;color:var(--pencil);font-style:italic}
.stage{margin-top:14px}
```

```html
<div class="stepper" data-stepper="loop">
  <div class="sketch"><div class="st-fig" style="--vw:520;--vh:170">
    <svg viewBox="0 0 520 170" aria-hidden="true"><g filter="url(#wob)">
      <path class="s st-el" data-o="1|.25|1|.8" data-sw="3|3|5|5" d="…"/>                  <!-- fades, then thickens -->
      <g class="st-el" data-tf="translate(0px,0px)|translate(120px,-30px)|…"><circle class="s r k fr" cx="70" cy="118" r="8"/></g>  <!-- an actor that moves -->
      <path class="s y st-el" data-w="2" d="…"/>                                         <!-- appears from state 2 -->
    </g></svg>
    <span class="st-pin st-el" style="--x:20;--y:18" data-txt="reps: 0|reps: 0|reps: 1|reps: 1">reps: 0</span>
  </div></div>
  <p class="caption"></p>
  <div class="stepbar"><button class="stepbtn st-prev" aria-label="previous step">‹</button>
    <span class="steplabel"></span><button class="stepbtn st-next" aria-label="next step">›</button></div>
</div>
```

```js
/* §32a/§32k · stepper skeleton — per .stepper container; content lives in STEPPERS[data-stepper].
   The skeleton owns: state index, prev/next, caption fade, step label, skin switching, and per-state
   values read from '|'-separated lists on any element:  data-o (opacity) · data-sw (stroke width) ·
   data-tf (CSS transform) · data-txt (text) · data-w (shown from state w on). Skins own only their
   scene ([data-skin] groups or pins) and their captions. */
const STEPPERS={
  loop:{ labels:['1','2','3','4'], caps:['First state.','Second state.','Third state.','Fourth state.'] },   // example entry for components §32a (no skins)
  review:{ labels:['day 1','day 3','day 4','day 10'],
    caps:{ trace:['Day 1 — written once, in fresh chalk.','Day 3 — the line is fading; the board still holds a ghost of it.',
                  'Day 4 — the review: you trace it again, harder.','Day 10 — still clearly there. The second line fades slower.'],
           path:['Day 1 — one walk flattens a faint path.','Day 3 — the grass is growing back over it.',
                 'Day 4 — you walk it again; the footprints press it down.','Day 10 — the path holds. Walked paths stay open longer.'] } }
};
document.querySelectorAll('.stepper').forEach(box=>{
  const cfg=STEPPERS[box.dataset.stepper]; if(!cfg) return;
  const cap=box.querySelector('.caption'), label=box.querySelector('.steplabel'),
        pv=box.querySelector('.st-prev'), nx=box.querySelector('.st-next'), skinBtns=[...box.querySelectorAll('.skinbtn')];
  const n=cfg.labels.length, list=(el,a)=>el.dataset[a].split('|');
  let skin=skinBtns.length ? (skinBtns.find(b=>b.classList.contains('on'))||skinBtns[0]).dataset.skin : null, s=0;
  function render(){
    box.querySelectorAll('[data-skin]:not(.skinbtn)').forEach(el=>el.style.display=(el.dataset.skin===skin)?'':'none');
    box.querySelectorAll('[data-o],[data-sw],[data-tf],[data-txt],[data-w]').forEach(el=>{
      if(el.dataset.w!==undefined) el.style.opacity = s>=+el.dataset.w ? 1 : 0;
      if(el.dataset.o) el.style.opacity=list(el,'o')[s];
      if(el.dataset.sw) el.style.strokeWidth=list(el,'sw')[s];
      if(el.dataset.tf) el.style.transform=list(el,'tf')[s];
      if(el.dataset.txt) el.textContent=list(el,'txt')[s];
    });
    const caps=skin ? cfg.caps[skin] : cfg.caps;
    cap.style.opacity=0; setTimeout(()=>{cap.textContent=caps[s]; cap.style.opacity=1},180);
    if(label) label.textContent=cfg.labels[s];
    pv.disabled=s===0; nx.disabled=s===n-1;
  }
  pv.addEventListener('click',()=>{if(s>0){s--;render()}});
  nx.addEventListener('click',()=>{if(s<n-1){s++;render()}});
  skinBtns.forEach(b=>b.addEventListener('click',()=>{ skin=b.dataset.skin; skinBtns.forEach(x=>x.classList.toggle('on',x===b)); render(); }));
  render();
});
```
(`loop` is the plain example entry used by the HTML above; `review` is the skinned one of §32k. Replace
them with the deck's own entries: `labels` = one per state; `caps` = one caption per state, or `{skin:[…]}`
per skin.)

### 32b. Lab widget
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Let the reader push a variable `build-intuition`
2. Compare options side by side `compare-options`
3. Show numbers and evidence `show-quantity`

A slider drives a live readout + ONE verdict line that changes with the range (the verdict is the lesson;
the readout is the evidence). For a number inside a sentence, see §27. The slider ALWAYS carries
`data-capture` (arrow keys move the slider, not the page), and the resting value already shows the key
result in words — a reader who never drags loses nothing. Two proven skins:

- **Chips + gauge** (from Playroom's top-k lab) — labelled chips switch between kept/lost as the value
  moves, a hand-drawn gauge shows the share, the verdict names the zone. **Signal-vs-noise variant** (the
  original): chips *appear* one by one as the value grows, each tagged ✓ relevant or ✕ noise, and the gauge
  shows the relevant share of what is shown — for any "more is not better" idea (top-k retrieval, sample
  size vs. noise, features vs. overfitting). Same code: give the `LABS` entry `mode:'appear'` and
  `rel:[1,1,0,…]` instead of `share` (example entry `LABS.topk`); chips not yet fetched keep their place.
- **Fixed-budget lamp** (from Nocturne's focus lab) — one lamp, a beam whose width is the variable, dots
  inside the beam share a fixed light budget (each gets dimmer as more share it). The skin for any "fixed
  capacity spread over N things" idea: attention, bandwidth, CPU time, a budget.

```css
/* §32b · lab widget — a slider drives a live readout + one verdict line (skins: chips+gauge from Playroom, lamp budget from Nocturne) */
.labbox{background:var(--k-surface);border:1.8px solid var(--k-ink);border-radius:var(--wob-r);padding:20px 24px;margin-top:18px;box-shadow:var(--shadow)}
.krow{display:flex;align-items:center;gap:16px}
.krow label{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.3rem;white-space:nowrap}
.kval{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.7rem;color:var(--k-a);min-width:2.2ch;text-align:center}
.krow input[type=range]{flex:1;-webkit-appearance:none;appearance:none;height:4px;border-radius:2px;background:var(--k-soft);outline:none}
.krow input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:24px;height:24px;border-radius:50% 46% 52% 48%;
  background:var(--paper);border:2px solid var(--k-ink);cursor:grab}
.krow input[type=range]::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:var(--paper);border:2px solid var(--k-ink);cursor:grab}
.krow input[type=range]:focus-visible::-webkit-slider-thumb{background:var(--k-hi)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;min-height:76px;align-content:flex-start}
.chip{font-size:.86rem;font-weight:700;border:1.5px solid currentColor;border-radius:14px 18px 15px 19px/18px 15px 19px 14px;padding:3px 12px;
  transition:color .35s ease,background .35s ease,opacity .35s ease,transform .45s var(--k-ease)}
.chip.kept{color:var(--k-b);background:var(--wash-b)}
.chip.lost{color:var(--k-a);background:transparent;opacity:.55;text-decoration:line-through}
.chip.sig{color:var(--k-b);background:var(--wash-b)}                    /* 'appear' mode: relevant */
.chip.noise{color:var(--k-a);background:transparent}                      /* 'appear' mode: noise */
.chip.off{opacity:0;transform:scale(.6)}                                   /* 'appear' mode: not fetched yet — keeps its place */
.gauge{margin-top:12px;display:flex;align-items:center;gap:12px}
.gauge b{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.15rem;white-space:nowrap}
.gauge .track{flex:1;height:14px;border:1.6px solid var(--k-ink);border-radius:7px 9px 7px 10px;overflow:hidden}
.gauge .fillbar{height:100%;width:50%;background:var(--k-b);transition:width .5s var(--k-ease),background .4s}
.labnote{margin-top:12px;font-size:.95rem;color:var(--k-soft);min-height:2.6em}
.labnote b{color:var(--k-a)}
.cone{fill:color-mix(in srgb,var(--k-c) 16%,transparent);stroke:color-mix(in srgb,var(--k-c) 60%,transparent);stroke-width:1.4;stroke-dasharray:5 6}
.ldots circle{transition:opacity .4s ease}
```

```html
<!-- chips + gauge: content in LABS.gap (decay) — or data-lab="topk" for the signal-vs-noise mode -->
<div class="labbox" data-lab="gap">
  <div class="krow"><label>days before review</label>
    <input class="lab-in" type="range" min="1" max="14" value="3" data-capture aria-label="days before review" /><span class="kval">3</span></div>
  <div class="chips"></div>
  <div class="gauge"><b>kept</b><div class="track"><div class="fillbar"></div></div></div>
  <p class="labnote"></p>
</div>
<!-- fixed-budget lamp: content in LAMPS.session; beam and dots live in ONE svg (Law 3) -->
<div class="labbox" data-lamp="session">
  <svg viewBox="0 0 420 170" aria-hidden="true" style="display:block;width:100%;height:auto">
    <g filter="url(#wob)"><circle class="s y k fy" cx="210" cy="14" r="8"/></g>
    <polygon class="cone" points="210,20 160,165 260,165"/><g class="ldots"></g></svg>
  <div class="krow"><label>cards per session</label>
    <input class="lab-in" type="range" min="10" max="100" value="24" data-capture aria-label="cards per session" /></div>
  <p class="labnote"></p>
</div>
```

```js
/* §32b · lab widget, skin 1: chips + gauge — per [data-lab]; content lives in LABS[data-lab].
   Two modes:  'decay' (default) — share(v) returns 0..1; the first round(share×n) chips stay kept, the rest are struck;
               'appear' (signal vs noise) — chips appear one per step (the first v show), each tagged ✓/✕ by rel[i];
               the gauge shows the relevant share of what is shown.  verdict(v,share) returns the one-line verdict (HTML). */
const LABS={
  gap:{ items:['cell wall','osmosis','enzyme','mitosis','ATP','diffusion','ribosome','chlorophyll'],
        share:d=>Math.exp(-d/6.5),                                   // a teaching curve, not a fitted model
        verdict:d=> d<=2 ? 'Safe — but you are spending a review on cards that were not fading yet.'
          : d<=5 ? 'The sweet spot: enough fading that recall takes effort, enough left that it succeeds.'
          : '<b>Too late</b> for most cards — the review becomes relearning from scratch.' },
  topk:{ mode:'appear', items:['Clause 7 · late penalty','Clause 7.2 · grace period','Clause 9 · force majeure','Shipping FAQ (2019)','Office pizza policy','Old draft'],
         rel:[1,1,1,0,0,0],                                            // example entry for components §32b (signal-vs-noise)
         verdict:(k,sh)=> k<=2 ? 'Clean — but the grace-period clause is still missing.'
           : sh===1 ? 'The sweet spot: full coverage, nothing rotten yet.'
           : '<b>More is not better</b> — now the noise is crowding the answer.' }
};
document.querySelectorAll('[data-lab]').forEach(box=>{
  const cfg=LABS[box.dataset.lab]; if(!cfg) return;
  const slider=box.querySelector('.lab-in'), val=box.querySelector('.kval'), chipsEl=box.querySelector('.chips'),
        bar=box.querySelector('.fillbar'), note=box.querySelector('.labnote');
  const appear=cfg.mode==='appear';
  cfg.items.forEach((t,i)=>{const c=document.createElement('span'); c.className='chip';
    c.textContent=appear ? (cfg.rel[i]?'✓ ':'✕ ')+t : t; chipsEl.appendChild(c);});
  const chips=[...chipsEl.children];
  function render(){
    const v=+slider.value;
    let sh;
    if(appear){                                                       // signal vs noise
      const shown=Math.min(v,chips.length);
      chips.forEach((c,i)=>{c.classList.toggle('off',i>=shown); c.classList.toggle('sig',cfg.rel[i]===1); c.classList.toggle('noise',cfg.rel[i]!==1);});
      sh=shown ? cfg.rel.slice(0,shown).filter(Boolean).length/shown : 0;
    } else {                                                          // decay
      sh=cfg.share(v); const k=Math.round(sh*chips.length);
      chips.forEach((c,i)=>{c.classList.toggle('kept',i<k); c.classList.toggle('lost',i>=k);});
    }
    if(val) val.textContent=v;
    bar.style.width=Math.round(sh*100)+'%';
    bar.style.background=sh>.6?'var(--k-b)':sh>.35?'var(--k-c)':'var(--k-a)';
    note.innerHTML=cfg.verdict(v,sh);
  }
  slider.addEventListener('input',render); render();
});

/* §32b · lab widget, skin 2: fixed-budget lamp — per [data-lamp]; one light shared by everything in the beam */
const LAMPS={
  session:{ count:26, budget:46,
    verdict:n=> n<=3 ? '<b>'+n+'</b> card(s) in the light — each gets full attention.'
      : n<=8 ? '<b>'+n+'</b> cards share the lamp — workable, none at full brightness.'
      : '<b>'+n+'</b> cards, one lamp — everything touched, nothing really lit.' }
};
document.querySelectorAll('[data-lamp]').forEach(box=>{
  const cfg=LAMPS[box.dataset.lamp]; if(!cfg) return;
  const NS='http://www.w3.org/2000/svg', slider=box.querySelector('.lab-in'), cone=box.querySelector('.cone'),
        g=box.querySelector('.ldots'), note=box.querySelector('.labnote');
  const rnd=k=>{const v=Math.sin(k*12.9898)*43758.5453; return v-Math.floor(v);}, dots=[];   // deterministic scatter
  for(let i=0;i<cfg.count;i++){
    const x=40+rnd(i+1)*340, y=72+rnd(i+101)*88, c=document.createElementNS(NS,'circle');
    c.setAttribute('cx',x); c.setAttribute('cy',y); c.setAttribute('r',3); g.appendChild(c); dots.push({el:c,x,y});
  }
  function render(){
    const half=+slider.value*1.6;
    cone.setAttribute('points','210,20 '+(210-half)+',165 '+(210+half)+',165');
    const inside=dots.filter(d=>Math.abs(d.x-210) < half*((d.y-20)/145));
    const each=inside.length ? Math.min(1, cfg.budget/(inside.length*8)) : 0;            // fixed budget, shared
    dots.forEach(d=>{const on=inside.includes(d);
      d.el.style.fill=on?'var(--k-c)':'var(--pencil)'; d.el.style.opacity=on?(0.3+each*0.7).toFixed(2):'.3';
      d.el.setAttribute('r',on?(3+each*3).toFixed(1):3);});
    note.innerHTML=cfg.verdict(inside.length);
  }
  slider.addEventListener('input',render); render();
});
```

### 32c. Note stack (reserved flow)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Define a new term `define-term`
2. Show how something works inside `explain-mechanism`
3. Correct a misconception `correct-misconception`

Sketchbook's depth default — sticky notes in a reserved-height stack; hovering one unfolds its depth and
pushes its siblings, never the slide (Law 1, #1). Sticky notes are paper objects: paper palette on every
board. Exemplar: slide 2 of `sketchbook.html` / `sketchbook-chalkboard.html`.

### 32d. Detail tray (fixed)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Name the parts of a thing `label-parts`
3. Compare options side by side `compare-options`

From Playroom's pop cards. A row of index cards (paper objects — paper palette on every board); tapping a
card drops its depth into the ONE tray of its `.ixwrap`, a constant-size box that scrolls internally (Law 1,
#2). The right home for depth of any length — a long explanation never shoves the page.

```css
/* §32d · index cards → detail tray — depth of any length lands in a fixed-size, scrolling tray (ported from Playroom) */
.ixrow{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:18px;align-items:start}
.ixc{font:inherit;text-align:start;cursor:pointer;background:#FBF6EA;color:#29241B;border:1.6px solid #29241B;
  border-radius:3px 7px 4px 8px;padding:10px 14px 12px;transform:rotate(var(--r,-.6deg));
  background-image:linear-gradient(#C4553B,#C4553B);background-size:100% 1.5px;background-repeat:no-repeat;background-position:0 2.6em;
  transition:transform .4s var(--k-ease),box-shadow .4s ease}
.ixc:nth-child(2){--r:.7deg} .ixc:nth-child(3){--r:-.3deg}
.ixc h3{font-size:1.45rem;color:#29241B;margin-bottom:6px}
.ixc .tap{font-size:.8rem;color:#5E5748}
.ixc .more{display:none}
.ixc:hover,.ixc.sel{transform:rotate(0) translateY(-4px);box-shadow:var(--shadow)}
.ixc.sel{outline:2px dashed var(--k-a);outline-offset:4px}
.tray{margin-top:16px;background:var(--k-surface);border:1.8px dashed var(--k-soft);border-radius:var(--wob-s);padding:12px 18px;
  height:clamp(120px,22vh,190px);overflow-y:auto;color:var(--k-soft);font-size:.95rem}
.tray h4{font-family:var(--font-display);font-weight:var(--display-w);font-size:1.4rem;color:var(--k-ink);margin-bottom:2px}
.tray .empty{color:var(--pencil);font-style:italic}
@keyframes traynudge{0%{transform:rotate(-.5deg)}100%{transform:none}}
.tray.bump{animation:traynudge .5s var(--k-ease)}
@media(max-width:880px){.ixrow{grid-template-columns:1fr}}
```

```html
<div class="ixwrap">
  <div class="ixrow">
    <button class="ixc"><h3>Card title</h3><p class="tap">one-line teaser — tap</p>
      <div class="more">The depth: any length, <b>rich text</b> allowed.</div></button>
    <!-- … 2–4 cards … -->
  </div>
  <div class="tray"><p class="empty">Tap a card above — its depth lands here.</p></div>
</div>
```

```js
/* §32d · index cards → detail tray — each .ixwrap owns its cards and its tray */
document.querySelectorAll('.ixwrap').forEach(wrap=>{
  const tray=wrap.querySelector('.tray'), cards=[...wrap.querySelectorAll('.ixc')];
  cards.forEach(c=>c.addEventListener('click',()=>{
    cards.forEach(o=>o.classList.toggle('sel',o===c));
    tray.innerHTML='<h4></h4><p></p>';
    tray.querySelector('h4').textContent=c.querySelector('h3').textContent;
    tray.querySelector('p').innerHTML=c.querySelector('.more').innerHTML;
    tray.classList.remove('bump'); void tray.offsetWidth; tray.classList.add('bump'); tray.scrollTop=0;
  }));
});
```

### 32e. Gloss footnotes (overlay)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Define a new term `define-term`
2. Point at what matters in a passage `highlight-passage`

From Terra's "academic method": a paragraph carries the argument, numbered footnotes carry the depth
(Law 1, #3). Build it with §24's anchored gloss — add a superscript number to the dotted word and
"Footnote n" to the card; the index-card skin stays paper on every board. Kit: slide 2.

```html
<span class="gl-w"><span class="gl-t" tabindex="0" style="anchor-name:--f1">Ebbinghaus<sup>1</sup></span><span class="gl-card" role="tooltip"
  style="position-anchor:--f1"><b>Footnote 1</b>One or two plain sentences of depth.</span></span>
```
```css
.gl-t sup{font-family:var(--font-display);font-weight:var(--display-w);font-size:.7em;color:var(--k-a)}   /* + the §24 CSS */
```

### 32f. Duo panes (final-geometry)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Compare options side by side `compare-options`
2. Show one state turning into another `show-transformation`
3. Correct a misconception `correct-misconception`

From Terra's weight-shift duo. Two panes; hovering or focusing one widens it and opens its depth to a
PRE-MEASURED height, while the container's height is locked to the tallest end state — nothing on the slide
moves (Law 1, #4). Panes take `tabindex="0"` so the keyboard can lean too.

```css
/* §32f · duo panes (final-geometry) — lean into a side; it takes the room (ported from Terra) */
.panes{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;transition:grid-template-columns 1s var(--k-ease)}
.panes:has(.pane:nth-child(1):is(:hover,:focus-within)){grid-template-columns:1.7fr 1fr}
.panes:has(.pane:nth-child(2):is(:hover,:focus-within)){grid-template-columns:1fr 1.7fr}
.pane{background:var(--k-surface);border:1.8px solid var(--k-soft);border-radius:var(--wob-r);padding:18px 22px;cursor:pointer;overflow:hidden;outline:none;
  transition:border-color .5s ease}
.pane:hover,.pane:focus-within{border-color:var(--k-ink)}
.pane h3{font-size:1.6rem;display:flex;align-items:baseline;gap:10px}
.pane h3 span{font-family:var(--font-body);font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--pencil)}
.pane .big{font-family:var(--font-display);font-weight:var(--display-w);font-size:2.4rem;line-height:1.1;margin:2px 0;color:var(--k-a)}
.pane.b .big{color:var(--k-b)}
.pane p{font-size:.93rem;color:var(--k-soft)}
.pane .deep{height:0;overflow:hidden;opacity:0;transition:height 1s var(--k-ease),opacity .7s ease,margin .7s ease}
.pane .deep>div{overflow:hidden}
.pane:hover .deep,.pane:focus-within .deep{height:var(--dh,150px);opacity:1;margin-top:8px}
.panes.noanim,.panes.noanim *{transition:none!important}
.panes.m-left{grid-template-columns:1.7fr 1fr!important}
.panes.m-right{grid-template-columns:1fr 1.7fr!important}
.pane.m-open .deep{height:auto!important;opacity:1;margin-top:8px}
@media(max-width:880px){
  .panes,.panes:has(.pane:nth-child(1):is(:hover,:focus-within)),.panes:has(.pane:nth-child(2):is(:hover,:focus-within)){grid-template-columns:1fr}
  .panes.m-left,.panes.m-right{grid-template-columns:1fr!important}
}
```

```html
<div class="panes">
  <div class="pane" tabindex="0"><h3>Option A <span>short label</span></h3><div class="big">6 h × 1</div><p>One line, always visible.</p>
    <div class="deep"><div><p>The depth, visible at the destination.</p></div></div></div>
  <div class="pane b" tabindex="0"><h3>Option B <span>short label</span></h3><div class="big">1 h × 6</div><p>One line, always visible.</p>
    <div class="deep"><div><p>The depth, visible at the destination.</p></div></div></div>
</div>
```

```js
/* §32f · duo panes — final-geometry, per .panes: measure each deep block at its FINAL width (--dh),
   lock the container to the tallest end state; hover then travels straight to final geometry. */
document.querySelectorAll('.panes').forEach(panes=>{
  const ps=[...panes.querySelectorAll('.pane')];
  function measure(){
    panes.classList.add('noanim'); panes.style.height='';
    let maxH=panes.offsetHeight;
    [['m-left',0],['m-right',1]].forEach(([cls,i])=>{
      panes.classList.add(cls); ps[i].classList.add('m-open');
      ps[i].style.setProperty('--dh', ps[i].querySelector('.deep').scrollHeight+'px');
      maxH=Math.max(maxH,panes.offsetHeight);
      ps[i].classList.remove('m-open'); panes.classList.remove(cls);
    });
    panes.style.height=maxH+'px'; void panes.offsetWidth; panes.classList.remove('noanim');
  }
  measure();
  if(document.fonts&&document.fonts.ready) document.fonts.ready.then(()=>setTimeout(measure,30));
  window.addEventListener('load',()=>setTimeout(measure,30));
  let t; window.addEventListener('resize',()=>{clearTimeout(t);t=setTimeout(measure,150)});
  panes.closest('.slide').addEventListener('slideenter',()=>setTimeout(measure,30));
});
```

### 32g. Sketch quiz
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Check understanding `check-recall`
2. Predict first, then verify `predict-first`
3. Correct a misconception `correct-misconception`

One question, options as hand-drawn boxes, a verdict line; a wrong pick scribbles a red cross and reveals
the correct option with a drawn tick. (The retired families dressed the same skeleton as squashy buttons,
glowing orbs or a ledger — the skeleton is unchanged; only Sketchbook's dress remains.) Exemplar: slide 4 of
`sketchbook.html` / `sketchbook-chalkboard.html`.

### 32h. Token journey
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show how something works inside `explain-mechanism`
2. Walk through a procedure `follow-procedure`
3. Tell a history or story in order `tell-story`
4. Show one state turning into another `show-transformation`

From Playroom's pipeline stepper. One actor (a chalk dot, a glyph) travels a drawn route through 3–6 nodes,
one node per key press: the engine's builds drive it (no buttons of its own), and the §25 caption stack
shows one sentence per stop. Route, nodes and token live in ONE SVG (Law 3); node names are HTML pins (§22).
In Arabic the route mirrors (right → left) through the `:dir(rtl)` rules. The skin for any "one thing moves
through stages" idea: a request through a network, a fact through memory, a letter through the post.

```css
/* §32h · token journey — one actor travels a drawn route, one node per build (ported from Playroom's pipeline) */
.journey{position:relative;width:min(760px,100%);margin:26px auto 0;container-type:inline-size}
.journey > svg{display:block;width:100%;height:auto;overflow:visible}
.journey:dir(rtl) > svg{transform:scaleX(-1)}                      /* RTL: the route runs right → left */
.jnode{fill:var(--paper);transition:fill .4s ease}
.jnode.on{fill:color-mix(in srgb,var(--k-a) 28%,var(--paper))}
.jtok{transition:transform .8s var(--k-ease)}
.jpin{position:absolute;left:calc(var(--x) / 600 * 100%);top:calc(var(--y) / 200 * 100%);transform:translate(-50%,-50%);
  font-family:var(--font-display);font-weight:var(--display-w);font-size:min(1.3rem,max(9px,calc(20 * 100cqi / 600)));white-space:nowrap;color:var(--k-soft)}
.journey:dir(rtl) .jpin{left:calc((600 - var(--x)) / 600 * 100%)}
.bcaps{display:grid;margin-top:18px;text-align:center}
.bcaps > *{grid-area:1/1;font-family:var(--font-display);font-weight:var(--display-w);font-size:clamp(1.3rem,2.6vw,1.65rem)}
.bcaps > [data-build]:not(.now){opacity:0}
```

```html
<section class="slide" data-builds="4">
  …
  <div class="journey">
    <svg viewBox="0 0 600 200" aria-hidden="true">
      <g filter="url(#wob)">
        <path class="s soft dash" d="M60 110 C 120 70, 150 140, 180 110 S 260 70, 300 110 S 380 150, 420 110 S 500 70, 540 110"/>
        <circle class="s jnode" cx="60" cy="110" r="22"/> <circle class="s jnode" cx="180" cy="110" r="22"/>
        <circle class="s jnode" cx="300" cy="110" r="22"/> <circle class="s jnode" cx="420" cy="110" r="22"/>
        <circle class="s jnode" cx="540" cy="110" r="22"/>
      </g>
      <g class="jtok" style="transform:translate(60px,110px)"><circle r="9" class="s r k fr"/></g>
    </svg>
    <span class="jpin" style="--x:60;--y:162">stop one</span> <!-- … one pin per node … -->
  </div>
  <div class="bcaps"><p data-build="0">Caption for stop one.</p> <!-- … --> <p data-build="4">Caption for the last stop.</p></div>
</section>
```

```js
/* §32h · token journey — follows the engine's builds (no buttons of its own) */
document.querySelectorAll('.journey').forEach(box=>{
  const slide=box.closest('.slide'), tok=box.querySelector('.jtok'), nodes=[...box.querySelectorAll('.jnode')];
  function place(step){
    const n=nodes[Math.min(step,nodes.length-1)];
    tok.style.transform='translate('+n.getAttribute('cx')+'px,'+n.getAttribute('cy')+'px)';
    nodes.forEach((x,i)=>x.classList.toggle('on',i<=step));
  }
  slide.addEventListener('build',e=>place(e.detail.step));
  place(+slide.dataset.step||0);
});
```

### 32i. Pointer spotlight cover
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. State the one big idea `state-thesis`
2. Let the reader push a variable `build-intuition`

From Nocturne's cursor spotlight. A cover whose background is a field of words hidden under a
board-coloured veil; only a circle around the pointer shows through. Use it only when the thesis IS about
attention, selection or noise — then the interaction enacts the idea. The title and lead sit above the veil
and are always readable; on touch the light follows the finger. The words are the topic's own (`data-words`).

```css
/* §32i · pointer spotlight cover — words render only where the light lands (ported from Nocturne) */
.spot-field{position:absolute;inset:0;z-index:1;pointer-events:none;user-select:none}
.spot-field span{position:absolute;font-family:var(--font-display);font-weight:var(--display-w);font-size:1.2rem;color:var(--k-soft);opacity:.6;white-space:nowrap}
.spot-veil{position:absolute;inset:0;z-index:2;pointer-events:none;
  background:radial-gradient(circle 170px at var(--mx,50%) var(--my,38%), transparent 0 90px, color-mix(in srgb,var(--paper) 95%,transparent) 200px)}
.spot-cover{position:relative;z-index:3}
```

```html
<section class="slide active" data-spot>
  <div class="spot-field" aria-hidden="true" data-words="word one|word two|word three"></div>
  <div class="spot-veil"></div>
  <div class="inner cover spot-cover"> … title, lead, hint … </div>
</section>
```

```js
/* §32i · pointer spotlight cover — words come from data-words on .spot-field (deterministic scatter) */
document.querySelectorAll('[data-spot]').forEach(slide=>{
  const field=slide.querySelector('.spot-field'), veil=slide.querySelector('.spot-veil');
  const words=(field.dataset.words||'').split('|');
  for(let i=0;i<34;i++){
    const w=document.createElement('span'); w.textContent=words[i%words.length];
    w.style.left=((i*61.8)%90+3)+'%'; w.style.top=((i*38.2+7)%86+5)+'%';
    w.style.transform='rotate('+(((i*37)%24)-12)+'deg)';
    field.appendChild(w);
  }
  function move(x,y){ const r=slide.getBoundingClientRect();
    veil.style.setProperty('--mx',((x-r.left)/r.width*100)+'%'); veil.style.setProperty('--my',((y-r.top)/r.height*100)+'%'); }
  slide.addEventListener('pointermove',e=>move(e.clientX,e.clientY));
  slide.addEventListener('touchmove',e=>{const t=e.touches[0];move(t.clientX,t.clientY)},{passive:true});
});
```

### 32j. Smudge panels
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Present parallel ideas of equal weight `list-parallel`
2. Define a new term `define-term`
3. Show how something works inside `explain-mechanism`

From Nocturne's hover-gated panels. Two to four panels; each headline is always readable, its depth
paragraph sits in place as smudged chalk (a blur, not a glow) and clears under hover, keyboard focus or a
tap. The space is reserved from the start, so nothing reflows (Law 1, #1, limit case). Headlines must carry
the slide on their own: never smudge examinable content.

```css
/* §32j · smudge panels — depth sits in reserved space as smudged chalk; it clears under attention (ported from Nocturne) */
.smudge{display:grid;gap:12px;margin-top:18px}
.sm{background:var(--k-surface);border:1.6px solid var(--k-soft);border-radius:var(--wob-s);padding:12px 18px;cursor:help;
  transition:border-color .4s ease,transform .4s var(--k-ease)}
.sm h3{font-size:1.45rem;display:flex;gap:10px;align-items:center}
.sm .lamp{width:11px;height:11px;border-radius:50%;border:1.6px solid var(--pencil);flex:none;transition:background .4s,border-color .4s}
.sm p{margin-top:2px;font-size:.95rem;max-width:64ch;color:var(--k-soft);filter:blur(3.5px);opacity:.7;
  transition:filter .5s ease,opacity .5s ease}
.sm:hover,.sm:focus-visible,.sm.open{border-color:var(--k-ink);transform:translateY(-2px) rotate(-.3deg);outline:none}
.sm:hover .lamp,.sm:focus-visible .lamp,.sm.open .lamp{background:var(--k-c);border-color:var(--k-c)}
.sm:hover p,.sm:focus-visible p,.sm.open p{filter:none;opacity:1}
```

```html
<div class="smudge">
  <div class="sm" tabindex="0"><h3><span class="lamp"></span>Headline that carries the point</h3>
    <p>Depth: one or two sentences, revealed in place.</p></div>
  <!-- … -->
</div>
```

```js
/* §32j · smudge panels — tap toggles on touch (hover and focus need no script) */
document.querySelectorAll('.sm').forEach(p=>p.addEventListener('click',e=>{ if(e.pointerType!=='mouse') p.classList.toggle('open'); }));
```

### 32k. Skins stepper (one skeleton, swappable skins)
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Show one state turning into another `show-transformation`
2. Let the reader push a variable `build-intuition`
3. Tell a history or story in order `tell-story`

From Terra's folio stepper — Law 2 made visible. It IS the §32a skeleton with skin buttons: each skin's
scene (SVG groups) and its annotation pins carry `data-skin="…"` and only the active skin shows; captions
come per skin from `STEPPERS[…].caps.<skin>`. A per-skin annotation ("re-traced, harder" / "walked, so it
stays") is an HTML pin with its own text, position and `data-o` states. Offer two skins when one principle
shows up in two worlds (a fading trace and an overgrown path; a barbell and an orchard) — the reader sees
that the idea, not the picture, is the lesson. CSS and JS: §32a.

```html
<div class="stepper" data-stepper="review">
  <div class="skinbar"><button class="skinbtn on" data-skin="trace">The chalk trace</button>
    <button class="skinbtn" data-skin="path">The footpath</button>
    <span class="skinnote">same stepper, different illustration</span></div>
  <div class="sketch stage"><div class="st-fig" style="--vw:520;--vh:170">
    <svg viewBox="0 0 520 170" aria-hidden="true">
      <g data-skin="trace" filter="url(#wob)"> … <path class="s st-el" data-o="1|.25|1|.8" data-sw="3|3|5|5" d="…"/> … </g>
      <g data-skin="path" filter="url(#wob)" style="display:none"> … <g class="st-el" data-tf="translate(0px,0px)|…|translate(380px,-46px)|…">…</g> … </g>
    </svg>
    <span class="st-pin st-el" data-skin="trace" data-o="0|0|1|0" style="--x:300;--y:150;color:var(--k-a)">re-traced, harder</span>
    <span class="st-pin st-el" data-skin="path"  data-o="0|0|0|1" style="--x:400;--y:30;color:var(--k-c)">walked, so it stays</span>
  </div></div>
  <p class="caption"></p>
  <div class="stepbar"><button class="stepbtn st-prev" aria-label="previous step">‹</button>
    <span class="steplabel"></span><button class="stepbtn st-next" aria-label="next step">›</button></div>
</div>
```

### 32l. Key passage frame
**Suggested for** — best fit first; suggestions, not obligations (each use case is explained once in `use-cases.md`):
1. Point at what matters in a passage `highlight-passage`
2. State the one big idea `state-thesis`

From Terra's essay frame. A double-ruled sketch frame with a drop initial in pen a, for the ONE paragraph a
slide (or a deck) turns on — a definition the exam quotes, the thesis, a primary-source quote. Once per
slide at most; Arabic skips the drop initial (letters join). Kit: slide 9.

```css
/* §32l · key passage frame — the one paragraph that carries the argument (ported from Terra's essay frame) */
.keypara{position:relative;border:1.8px solid var(--k-ink);border-radius:var(--wob-r);padding:20px 26px;background:var(--k-surface);text-align:start}
.keypara::before{content:"";position:absolute;inset:6px;border:1px solid var(--k-soft);border-radius:var(--wob-s);opacity:.55;pointer-events:none}
.keypara p{color:var(--k-soft)}
.keypara p:first-of-type::first-letter{font-family:var(--font-display);font-weight:var(--display-w);font-size:3.1em;line-height:.8;
  float:inline-start;margin-inline-end:.08em;margin-top:.06em;color:var(--k-a)}
:lang(ar) .keypara p:first-of-type::first-letter{font:inherit;float:none;margin:0;color:inherit}   /* Arabic letters join: no drop initial */
```

```html
<div class="keypara"><p>The paragraph that carries the argument.</p></div>
```
