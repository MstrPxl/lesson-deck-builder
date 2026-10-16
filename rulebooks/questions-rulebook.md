# Questions Rulebook

**Version 1.2.1 · 10 October 2026 · written against `lesson-deck-builder` v1.3 (Sketchbook: paper or six chalkboard boards) · first used on Applied OS · Chapter 1**

> **Changes in 1.2.1:** goals over procedures (§0). The goals and the user's settings are fixed. The catalogue, layout and code are tested defaults that may give way to a better method, reported on a new "Departures" line (§8).
>
> **Changes in 1.2:** Sort rows put the item above its group buttons (Appendix B). With three groups, the buttons used to stack into a column beside a long item, so the slide ran past one screen even on a laptop. Found in the 210 ISY deck 1.
>
> **Changes in 1.1:**
> - **The quiz replaces the skill's question set and answer box** whenever this file is attached (the default in `slides-rulebook.md` v1.5): QL1, QW10.
> - **Label the figure is now a proven kind (K9)**, built in Applied OS deck 2 and reused in decks 3–4. Its markup, CSS, script and walk branch are in Appendices A–D, so a new course needs no earlier deck to build it.
> - **Phone first (QL7, §6, §7):** quiz slides are checked at phone size first, with touch.
> - `slides-rulebook.md` v1.5's checker keeps whole quiz slides (`data-budget="skip"`) outside the word count, feedback included.

This file tells you how to add a **final quiz** to a lesson deck: about 10 minutes, several kinds of questions, marked on the page, with a score slide that sends the learner back to what they missed.

It is a companion file. It works next to a **main rulebook** (`slides-rulebook.md` for decks made from lecture slides, `lessons-rulebook.md` for researched lessons) or on its own. It works for any course and any subject.

It is **not a menu**. Section 3 records the question kinds already designed, written and tested, so you don't have to think them through again. Use them when they fit. When a chapter's content asks for something else, reason it through with §2 and build a new kind (§3c, §6).

---

## 0. How to use this file

- **Read order:**
  1. the main rulebook, if one is attached;
  2. this file;
  3. the deck the quiz is for (or build the deck first, then come back);
  4. an earlier deck with a quiz, if attached. Reuse its quiz code unchanged.
- **Who decides what:**

  | Question | Decided by |
  |---|---|
  | Language level, terms, glossary, style, canvas, topic bar | The main rulebook and the deck's own records |
  | Which question kinds, how many, how hard, how they look and behave | This file |
  | Anything the user says in the prompt | The user. It always wins. |

- **Goals over procedures.**
  - **Fixed:** the goals (QG1–QG5), the user's settings (§9), and the main rulebook's choices.
  - **Tested defaults:** the kinds catalogue, the layout, the code in the appendices and the numbers marked *(target)*, written for the models of their date.
  - When another way meets the goals better (a new kind, a better check, better code), use it and name it on the report's "Departures" line (§8).

- Every rule has an ID (QG2, QW3, QL4 …) so the user can point at it in feedback.
- Numbers marked *(target)* are design choices that may be tuned. They are not research findings.

**A prompt can be as short as:**

```
Add a final quiz to the attached deck, following questions-rulebook.md.
```

or, while building a deck:

```
/lesson-deck-builder
Follow slides-rulebook.md for the attached lecture, and end the deck with a final quiz following questions-rulebook.md.
```

**What to attach:** this file; the main rulebook; the deck or the lecture; optionally an earlier deck of the course that already has a quiz. Appendices A–C hold the code of every proven kind (K1–K9), so the first deck of a new course needs no earlier deck.

**What the quiz replaces.** When this file is attached, the quiz is the deck's end-of-deck check: the skill's question set ("Check yourself") and its answer box are left out. The user can bring them back (`slides-rulebook.md` §11); then QW10 applies.

---

## 1. Goals

**QG1 — Answerable from the deck alone.** A junior university student who read the deck once can answer every question. No prior knowledge, no outside facts. When an item needs a number, the stem gives it.

**QG2 — Challenging, fair, motivating.** Not silly (no answer that is obvious from the wording, no joke options). Not shackling (no trick wording, no trivia, no item that needs a detail shown once in small print). The learner should have to think, and should feel that a wrong answer was a fair miss.

**QG3 — About 10 minutes** *(target; a setting, §9)*. Time comes from the per-kind estimates in §3.

**QG4 — Covers the whole deck.** Every topic of the deck has at least one item. Core ideas get more items than side facts.

**QG5 — Marks itself and teaches.** Each item says right or wrong at once, with the reason, and shows the right answer after a miss. The score slide sends the learner back to the topics they missed.

*Why:* practice testing with feedback is one of the two most useful study techniques found in a large review [D]. Feedback that explains *why* turns a miss into learning, and spacing a test after the reading adds a retrieval benefit [D][R].

---

## 2. Choosing the question kinds (the method)

This is the reasoning used for Chapter 1. Run it again for each deck; it takes minutes, not a long debate.

**Step 1 — List what the deck teaches, by kind of knowledge.**

| Kind of knowledge | Spot it in the deck when you see… |
|---|---|
| Term ↔ meaning | `<dfn>`, the glossary, "X is called Y" |
| Sequence | builds that step through a process, numbered steps, a startup or a pipeline |
| Classification | two or three categories, a table with types, a "public / private / hybrid" split |
| Mechanism (why, what happens when) | "When … the OS …", cause and effect, a step-through |
| Misconception | the deck's challenge, the eraser, "Note:" lines, "many students think…" |
| Quantity | numbers, units, a table of sizes or times, a worked calculation |
| Comparison | duo panes, comparison tables, "A vs B" |
| Structure (parts of a whole) | a labelled figure, a layered stack, a map |
| Code or a trace | code windows, trace tables |

**Step 2 — Match each kind of knowledge to the question kinds that test it best.**

| Kind of knowledge | Best question kinds (§3) |
|---|---|
| Term ↔ meaning | Match · Fill the gap (word bank) |
| Sequence | Put in order |
| Classification | Sort into groups |
| Mechanism | Choose one (a scenario stem) · Find the mistake |
| Misconception | True or false · Find the mistake · a distractor in Choose one |
| Quantity | Work it out |
| Comparison | Sort · Choose one · Odd one out (§3b) |
| Structure | Label the figure (K9) · Match |
| Code or a trace | Predict the output (§3b) · Work it out · Put in order |

**Step 3 — Pick 6–9 kinds** *(target)* that the deck's content supports.
- Keep a kind only if the deck gives **at least 2 good items** for it. Never force a kind to complete a set.
- Add a kind from §3b, or invent one (§3c), when the content calls for it. Example: a chapter full of code wants Predict the output.
- Drop a proven kind when the chapter can't give it 2 fair items. Applied OS chapter 4 had no real sequence, so it used Work it out instead of Put in order.
- Variety matters: one kind repeated 16 times tires the learner and tests one skill.

**Step 4 — Two items per kind** *(target)*. A quick kind (True or false) may have 3; a slow kind (a long Put in order) may have 1 when time is short.

**Step 5 — Check the time** with the per-kind estimates in §3. Adjust the number of items until the total is about 10 minutes.

**Step 6 — Spread the items over the topics** (QG4). Write the plan as a short table before writing items: kind · item · topic · source slide.

---

## 3. The question-kind catalogue

### 3a. Proven kinds (built and tested in Applied OS decks 1–4)

Each has a `data-type` in the reference code (Appendix A–C). Times are per item and are estimates *(target)*.

**K1 — Choose one** (`mcq`) · about 40 s
- *Tests:* mechanism, application, comparison.
- *Write:* a short scenario stem ("Job 1 waits for the disk. What happens to the CPU?"), 4 options, one clearly best.
- *Distractors:* other parts or tools from the deck that do something nearby (a load balancer, a firewall, the VMM as wrong answers for "what does a network OS do?").
- *Pitfall:* stems that only test recall of a sentence. Ask what *happens* or *which one fits*.

**K2 — True or false** (`mcq` with 2 options) · about 20 s
- *Tests:* one misconception, judged fast.
- *Write:* one claim in quotes. Aim at a real confusion ("The cache holds more data than main memory": false; it is smaller but faster).
- *Limit:* at most 3 per quiz; a coin flip gets half right. The feedback must say *why*.

**K3 — Fill the gap with a word bank** (`gap`) · about 35 s
- *Tests:* the exact term for a described idea.
- *Write:* one sentence, one gap, a bank of 4 words. The learner **drags** a word into the gap, or **taps** it; tapping a filled gap sends the word back.
- *Distractors:* real terms from the same deck that a confused learner would pick (virtual memory vs swapping; kernel vs bootstrap).
- *Why a bank, not typing:* typing tests spelling and needs a list of accepted variants. The bank tests the idea.

**K4 — Match** (`match`) · about 50 s for 4 rows
- *Tests:* several term ↔ meaning pairs that are easy to mix up.
- *Write:* 4 rows *(target)*, each a term and a drop-down of meanings (shuffled at load). Meanings are short (≤ 8 words).
- *Pick sets that compete:* the OS's roles (kernel, resource allocator, control program, application program), or the OS's process jobs.

**K5 — Put in order** (`order`) · about 50 s for 4–5 steps
- *Tests:* a sequence the deck taught (an interrupt's handling; storage from fastest to slowest).
- *Write:* 4–5 steps, shown shuffled. The learner taps them in order; numbers appear; "Clear" restarts.
- *Avoid:* sequences whose first step is obvious from the wording ("Power on…").

**K6 — Sort into groups** (`sort`) · about 45 s for 5–6 items
- *Tests:* classification.
- *Write:* 2–3 groups, 5–6 items, each item a short phrase. Each row has one chip per group.
- *Make it think:* use examples, not the deck's exact words ("A word processor you use in the browser" → SaaS).

**K7 — Find the mistake** (`spot`) · about 35 s
- *Tests:* precise understanding; targets one misconception.
- *Write:* one or two sentences split into 4–5 tappable parts; exactly one part is wrong. The wrong part should be a believable slip (per byte instead of per block; one user instead of a set of users).
- *After a check:* the real mistake is struck through; a wrong pick is underlined in red, never struck (it was a true statement).

**K8 — Work it out** (`num`) · about 50 s
- *Tests:* using a rule or a table on numbers.
- *Write:* give every number in the stem. One step of arithmetic at most, with friendly numbers (16,384 ÷ 4,096 = 4). Answers are whole numbers; spaces and commas are ignored.
- *Feedback:* show the calculation and what it means ("This gap is why caching pays").

**K9 — Label the figure** (`label`) · about 55 s for 3–4 slots
- *Built in:* Applied OS deck 2; reused in decks 3 and 4.
- *Tests:* structure: which part sits where (layers, a memory layout, mapping pictures).
- *Write:* redraw the deck's figure **without** the labels being tested, put numbered marks (`.fq-mark`) on it, and one drop per number below it, plus a bank with one extra near-miss label (PCB among memory parts; two-level among the three models).
- *Behaviour:* drag a label onto a number's drop, or tap a drop and then a label (a tapped label fills the chosen drop, else the first empty one); tap a filled drop to send its label back. Each wrong slot shows its fix.
- *Keep:* the parts that give context (arrows, the "max / 0" ends) on the figure; only the tested names go.

### 3b. Ready to build (designed, not yet built)

Use these when the content calls for them. All of them reuse an existing type.

| Kind | Use when | How to build |
|---|---|---|
| **Odd one out** | A category with a near-miss member | `mcq`: "Which one is not volatile?" with 4 options. The stem names the category, not a negative ("Which one is nonvolatile?" is better than "Which is NOT volatile?"). |
| **Predict the output** | Code or a trace in the deck | `mcq` or `num`: show a short code block (`<pre>`), ask for the printed value or the value of a variable after the loop. |
| **What happens next** | A mechanism with clear stages | `mcq`: describe stages 1–2, ask for stage 3. |
| **Cause → effect** | Several causes with distinct effects | `match`, with causes as terms and effects as meanings. |
| **Fill the table** | A comparison table in the deck | `sort` with the table's columns as groups, or `match` per row. |
| **Two-step calculation** | A formula with a worked example | `num`, with the formula repeated in the stem. Keep it to two steps. |

### 3c. Inventing a kind

When a chapter needs a kind not listed here:
1. Name the knowledge it tests (§2, step 1) and why the listed kinds test it worse.
2. Check it against QL1–QL6 and the technical contract (§6): self-marking, tap and keyboard friendly, works on a phone.
3. Build it as a new `data-type` branch in the quiz script, using the same `finish()` and reset pattern.
4. Test it (§7) and record it in the delivery report, so it can be added to this file.

### 3d. Considered and rejected

| Kind | Why not |
|---|---|
| Open answer graded on the page | The page can't judge it. Keep open "Why…?" questions in the skill's answer box instead. |
| Typed fill-in | Tests spelling; needs a list of accepted forms; frustrating on phones. Replaced by the word bank (K3). |
| Drag-only interactions | Fail with a keyboard and are awkward on small screens. Every drag must also work by tapping. |
| Crossword, word search | Test spelling and patience, not understanding. |
| Assertion–reason items | Heavy wording at A2–B2; they test reading more than the idea. |
| "All of the above", "none of the above", NOT / EXCEPT stems | Known item-writing flaws [MCQ]. |
| "Select all that apply" | Scoring partial picks is confusing. Use Sort instead. |

---

## 4. Writing the items

**QW1 — Source-locked.** Every item comes from a slide. Record it in the `QUIZ-MAP` comment (item · kind · answer · source slide). Before building, re-read each answer against the slide text.

**QW2 — Difficulty mix.**
- At most a third of the items are pure recall. The rest ask the learner to apply, classify, order, compute or spot an error.
- No item needs a fact outside the deck (QG1). No item hinges on a detail that appears only in a hidden tap card.
- Aim for most careful readers to get about 70–85% *(target)*. A quiz that everyone aces teaches little; one that everyone fails discourages.

**QW3 — Distractors come from real confusions.** In order of preference:
1. the deck's own misconceptions (the challenge, the eraser, "Note:" lines);
2. neighbouring terms the deck teaches (swapping vs virtual memory; SaaS vs PaaS);
3. a step in the wrong place, a wrong unit, a reversed relation.

Never a joke option, never an option the deck never mentions.

**QW4 — Fair wording.**
- Follow the main rulebook's language rules (its level, sentence length, glossary terms).
- Stems are full questions or full sentences, worded positively.
- Options are similar in length and grammar; the right one is not the longest.
- One clearly best answer. No double meanings.

**QW5 — Feedback that teaches.** After the check: "Yes." or "Not quite." plus one short reason (≤ 15 words *(target)*) that states the mechanism. After a miss, show the right answer: the option is ticked, the word is outlined, the fix appears beside a row.

**QW6 — Multi-part items show their parts.** Match, Sort and Put in order show "k of n right" and mark each row. The point is all-or-nothing (the score stays honest), but the learner sees how close they were.

**QW7 — One check per item.** No retry until the learner presses "Try the quiz again" on the score slide.

**QW8 — Self-contained.** No "as on slide 9", no item that depends on another item. One item's stem must not give away another item's answer.

**QW9 — Vary answer positions.** The right option is not always in the same place. Match meanings are shuffled at load; Put in order steps are shown shuffled; word banks list the answer in different positions.

**QW10 — The quiz replaces the deck's own question set.** By default the skill's end-of-deck "Check yourself" set and its answer box are left out, and the quiz is the deck's only end check. When the user keeps them (`slides-rulebook.md` §11), the quiz tests the same ideas through different items, with no item repeated.

---

## 5. Layout (the quiz's arc)

**QL1 — Place.** At the end of the deck, right after the glossary slide "Words in this deck" (or after the answer box, when the user keeps it), as **its own topic** in the topic bar ("Final quiz").

**QL2 — Intro slide.** Title with the count ("Sixteen questions, eight kinds"), one line ("Everything you need is in this deck. Each question has one check."), and a grid of the kinds, each with a 3–6-word instruction.

**QL3 — One slide per kind.**
- A tag line: "Kind n of N · name".
- The heading is the instruction ("Tap the steps in order").
- Two items side by side (`row2`), stacked on phones.
- Items are numbered across the whole quiz (1–16), not per slide.

**QL4 — Score slide.**
- "right / total", counted live when the slide is entered.
- A one-line message by score: ≥ 85% "Excellent", ≥ 60% "Good work, revisit…", lower "A second pass will help". With items still open, it says how many.
- A grid with one cell per kind: ✓, ✗ or · for each item.
- **Revisit** buttons, one per topic with a miss. Each jumps to that topic's first slide, so each item's `data-topic` must equal a `data-sec` name.
- "Try the quiz again": resets every item (shuffling the matches again) and jumps to the first quiz slide.

**QL5 — Word budget.** If the main rulebook has a word budget, mark every quiz slide `data-budget="skip"` and report the quiz's word count separately.

**QL6 — Topic bar.** A long quiz topic squeezes short topics, so give topic blocks a minimum width on laptops (in the reference CSS). The trade-off: short topics are no longer exactly proportional.

**QL7 — Phone first** (`slides-rulebook.md` M1–M8).
- Design each quiz slide at 390 × 844 first: the two items stack, and each item should fit about one phone screen. A Label the figure item may take up to about two.
- Options, Check buttons and the retry button are at least 44 px tall; chips and group pills at least 34 px (the phone layer sets them).
- Drag areas (word banks, slots) carry `data-capture`, so a swipe there doesn't turn the page. Keep them compact: a swipe on the stem or the empty space still turns the page, and Prev/Next always work.
- The score grid becomes 2 columns on phones (in the reference CSS).

---

## 6. Technical contract

- **One `<script>`.** Append the quiz script at the end of the deck's single script, after the engine and the component code. It uses the engine's globals `slides` and `go`. Never edit the engine.
- **Own class names.** Quiz items are `.fq`, never the skill's `.q`, so the skill's quiz handler doesn't also attach to them. The quiz reuses the skill's `.opt`, `.opts`, `.verdict`, `.k-btn`, `.k-ctrls`, `.row2`, `.row4`, `.card` and `.tag` styles.
- **Markup contract** (templates in Appendix A):

  | Attribute | On | Meaning |
  |---|---|---|
  | `data-type` | `.fq` | `mcq` · `gap` · `match` · `order` · `sort` · `spot` · `num` · `label` |
  | `data-kind` | `.fq` | The kind's name, shown in the score grid ("Put in order") |
  | `data-topic` | `.fq` | The topic to revisit, exactly as in a slide's `data-sec` |
  | `data-why` | `.fq` | The feedback reason (QW5) |
  | `data-ok="1"` | `.opt`, `.fq-ch` | The right option, or the wrong part of the sentence |
  | `data-answer` | `.fq` (`gap`, `num`); each `.drop` (`label`) | The right word or number; the right label for that slot |
  | `data-key` | `.fq-row` and `.fq-choices li` (`match`) | Pairs a term with its meaning |
  | `data-n` | `.fq-it` (`order`) | The step's true position |
  | `data-groups`, `data-g` | `.fq` / `.fq-row` (`sort`) | The groups, and each row's right group |

- **Phone first.** Quiz slides follow QL7 and the main rulebook's phone layer.
- **Drag safety.** Every draggable area carries `data-capture` (the engine then ignores swipes and arrow keys there), and draggable chips have `touch-action:none`. Every drag also works by tap, and every tap target works with the keyboard (buttons, or `tabindex="0"` with Enter/Space).
- **Colours.** Only the canvas and bridge tokens (`--ink`, `--ink-soft`, `--surface`, `--marker`, `--red`, `--yellow`, `--k-card` …). Word chips are paper objects, so they use the paper palette on every board. With these tokens, the quiz follows any board or canvas change automatically. A non-Sketchbook deck needs the same token names mapped.
- **No glossary cards inside the quiz.** If the deck has a glossary script (slides-rulebook / lessons-rulebook T5b), it would turn terms in quiz stems into tap cards, and a card can give the answer away (the card for "cache" says "smaller storage", which answers a true-or-false item). Change the glossary script's slide-skip line to:

  ```js
  if(sl.contains(dl)||sl.querySelector('.fq')) return;   // no glossary cards inside a quiz
  ```

  This is the one edit to existing deck code that a quiz needs. Decks without a glossary need nothing.
- **No storage.** State lives in memory; a reload clears the quiz. Say so only if the user asks for saving.
- **Validator.** The skill's `validate.py` must pass.
- **Reuse.** A later deck copies the quiz CSS and script unchanged from the previous deck (or from Appendices B–C) and writes only new items. A new kind adds a `data-type` branch; it doesn't rewrite the others.

---

## 7. Checks before delivery

- [ ] **Answers verified:** every item checked against its source slide; `QUIZ-MAP` comment present.
- [ ] **Coverage:** every topic has an item (QG4).
- [ ] **Time:** the per-kind estimates add up to about the target (QG3).
- [ ] **Wording:** the main rulebook's language checker passes on the quiz slides, apart from term flags. A quiz uses the terms it tests without glossing them, since a gloss would give answers away.
- [ ] **Browser walk:** in a real browser, answer every item once, some right and some wrong. Then check:
  - the score is exactly right;
  - the revisit buttons jump to the right topics;
  - "Try again" resets everything;
  - there are no console errors.
- [ ] **No glossary cards on quiz slides:** `document.querySelectorAll('.fq .gl-w').length` is 0.
- [ ] **Drag test:** at least one drag with a mouse and one simulated touch drag on a phone-sized viewport (CDP `Input.dispatchTouchEvent` in Playwright with `has_touch`). The word lands, and the slide doesn't turn.
- [ ] **Look, phone first:** screenshots of every quiz slide after answering at 390 × 844, then at laptop size. Nothing overflows sideways, down to 320 px; feedback is readable; main buttons are at least 44 px tall.
- [ ] `validate.py` passes.

A Playwright test that does the browser walk is in Appendix D.

---

## 8. Delivery report (add to the main report)

```
Quiz: <n> items in <k> kinds · about <m> min · slides <a>–<b> · topic "Final quiz".
Kinds: <name × count> | …  (new kinds: <list or "none">)
Coverage: every topic ✓ (or: <topic> has no item — why).
Words: <w> (outside the word budget: data-budget="skip").
Tested: browser walk ✓ · drag (mouse, touch) ✓ · phone ✓ · validator ✓.
Departures: <defaults of this file done another way, and why, or "none">.
```

---

## 9. Settings the user can change

| Setting | Default | Options |
|---|---|---|
| Time | **About 10 minutes** | 5 (one item per kind, fewer kinds) · 15–20 (three items per kind, or more kinds) |
| Kinds | **Chosen by §2** | The user names kinds to include or exclude |
| Items per kind | **2** | 1–3 |
| Placement | **End of deck, own topic** | After each topic (mini-quizzes; then the score slide counts only the end quiz) |
| Score messages | **≥ 85% / ≥ 60%** | Any thresholds |
| Partial credit | **Off** (all-or-nothing, parts shown) | On: a Match with 3 of 4 right scores 0.75 |

---

## 10. Evidence

| Tag | Source | Supports |
|---|---|---|
| [D] | Dunlosky et al. (2013), *Psychological Science in the Public Interest* | Practice testing and spaced practice rated the most useful study techniques |
| [R] | Rosenshine (2012), *Principles of Instruction* | Frequent checks with feedback; aim for high but not perfect success |
| [MCQ] | Haladyna, Downing & Rodriguez (2002) | Multiple-choice item-writing guidelines: positive stems, plausible distractors, no "all/none of the above" |

The per-kind times, the 70–85% target and the 10-minute default are design choices from the first build, not research findings.

---

## Appendix A — Markup templates

One template per type. Copy, then replace the text. Two items per slide sit in `<div class="row2 fq-pair">`.

**Quiz slide shell**

```html
<section class="slide" data-budget="skip">            <!-- first quiz slide also gets data-sec="Final quiz" -->
  <div class="inner" style="max-width:1000px">
    <span class="tag reveal">Kind 1 of 8 · choose one</span>
    <h2 class="reveal" style="--d:.05s">Choose the best answer</h2>
    <div class="row2 fq-pair">
      <!-- two .fq items -->
    </div>
  </div>
</section>
```

**mcq** (Choose one; True or false uses `class="opts fq-tf"` with two options)

```html
<div class="fq reveal" style="--d:.1s" data-type="mcq" data-kind="Choose one" data-topic="CPUs"
     data-why="The CPU always gets another job to run.">
  <p class="stem">1 · Job 1 waits for the disk. In a multiprogramming system, what happens to the CPU?</p>
  <div class="opts fq-col">
    <button class="opt"><span class="box"></span>It waits until the disk finishes</button>
    <button class="opt" data-ok="1"><span class="box"></span>The OS switches it to another job in memory</button>
    <button class="opt"><span class="box"></span>The disk controller borrows it</button>
    <button class="opt"><span class="box"></span>It turns off to save power</button>
  </div>
  <p class="verdict"></p>
</div>
```

**gap** (word bank)

```html
<div class="fq reveal" style="--d:.1s" data-type="gap" data-kind="Fill the gap" data-topic="The OS"
     data-answer="bootstrap" data-why="The bootstrap program (BIOS) is firmware in ROM.">
  <p class="stem">5 · At power-up, the <span class="drop" data-capture tabindex="0" role="button"
     aria-label="gap: drop a word here"></span> program runs from ROM and loads the kernel.</p>
  <div class="bank" data-capture><button class="chip">kernel</button><button class="chip">bootstrap</button><button class="chip">application</button><button class="chip">service</button></div>
  <div class="k-ctrls"><button class="k-btn fq-check">Check</button></div>
  <p class="verdict"></p>
</div>
```

**match**

```html
<div class="fq reveal" style="--d:.1s" data-type="match" data-kind="Match" data-topic="Processes"
     data-why="These are the OS's process jobs.">
  <p class="stem">8 · What the OS does for processes</p>
  <div class="fq-rows">
    <div class="fq-row" data-key="a"><span class="fq-term">Synchronization</span><select></select></div>
    <div class="fq-row" data-key="b"><span class="fq-term">Communication</span><select></select></div>
    <!-- 4 rows (target) -->
  </div>
  <ul class="fq-choices" hidden>
    <li data-key="a">processes act in the right order</li>
    <li data-key="b">processes exchange data</li>
  </ul>
  <div class="k-ctrls"><button class="k-btn fq-check">Check</button></div>
  <p class="verdict"></p>
</div>
```

**order** (list the steps shuffled; `data-n` is the true position)

```html
<div class="fq reveal" style="--d:.1s" data-type="order" data-kind="Put in order" data-topic="Devices"
     data-why="Save, look up, run, return.">
  <p class="stem">9 · An interrupt arrives. What does the CPU do, first to last?</p>
  <div class="fq-items">
    <button class="fq-it" data-n="3"><span class="fq-num"></span>Run the interrupt service routine</button>
    <button class="fq-it" data-n="1"><span class="fq-num"></span>Save the address of the interrupted instruction</button>
    <button class="fq-it" data-n="4"><span class="fq-num"></span>Return to the saved address</button>
    <button class="fq-it" data-n="2"><span class="fq-num"></span>Find the routine in the interrupt vector</button>
  </div>
  <div class="k-ctrls"><button class="k-btn fq-check">Check</button><button class="k-btn fq-clear">Clear</button></div>
  <p class="verdict"></p>
</div>
```

**sort**

```html
<div class="fq reveal" style="--d:.1s" data-type="sort" data-kind="Sort" data-groups="Volatile|Nonvolatile"
     data-topic="Storage" data-why="Data in volatile storage is lost without power.">
  <p class="stem">11 · Volatile or nonvolatile?</p>
  <div class="fq-rows">
    <div class="fq-row" data-g="Volatile"><span class="fq-term">Registers</span></div>
    <div class="fq-row" data-g="Nonvolatile"><span class="fq-term">Hard disk</span></div>
    <!-- 5–6 rows -->
  </div>
  <div class="k-ctrls"><button class="k-btn fq-check">Check</button></div>
  <p class="verdict"></p>
</div>
```

**spot** (Find the mistake; exactly one part has `data-ok="1"`)

```html
<div class="fq reveal" style="--d:.1s" data-type="spot" data-kind="Find the mistake" data-topic="Devices"
     data-why="With DMA, there is one interrupt per block, not per byte.">
  <p class="stem">13 · DMA</p>
  <p class="fq-sent"><button class="fq-ch">With DMA, the device controller</button> <button class="fq-ch">moves whole blocks</button> <button class="fq-ch">from its buffer to memory,</button> <button class="fq-ch">and the CPU gets one interrupt</button> <button class="fq-ch" data-ok="1">for every byte.</button></p>
  <p class="verdict"></p>
</div>
```

**num** (Work it out)

```html
<div class="fq reveal" style="--d:.1s" data-type="num" data-kind="Work it out" data-answer="4" data-topic="Devices"
     data-why="16,384 ÷ 4,096 = 4 blocks, one interrupt each.">
  <p class="stem">15 · A device sends 16,384 bytes by DMA, in blocks of 4,096 bytes. How many interrupts does the CPU get?</p>
  <div class="k-ctrls"><input class="gap num" type="text" inputmode="numeric" aria-label="your answer" autocomplete="off"><button class="k-btn fq-check">Check</button></div>
  <p class="verdict"></p>
</div>
```

**label** (Label the figure; one `.drop` per mark, each with its own `data-answer`; one extra label in the bank)

```html
<div class="fq reveal" style="--d:.1s" data-type="label" data-kind="Label the figure" data-topic="Threads"
     data-why="Stacks at the top, then the heap, static data and code at the bottom.">
  <p class="stem">15 · One process with three threads, in memory</p>
  <div class="lf fq-fig" style="--vw:360;--vh:300;width:72%">
    <svg viewBox="0 0 360 300" aria-hidden="true"><!-- the deck's figure, redrawn without the tested labels --></svg>
    <div class="lf-layer">
      <span class="lf-pin mid fq-mark" style="--x:180;--y:66">1</span>
      <span class="lf-pin mid fq-mark" style="--x:180;--y:172">2</span>
    </div>
  </div>
  <div class="fq-slots" data-capture>
    <div class="fq-slot"><span class="fq-mark">1</span><span class="drop" data-answer="stack" tabindex="0" role="button" aria-label="slot 1: drop a label here"></span></div>
    <div class="fq-slot"><span class="fq-mark">2</span><span class="drop" data-answer="heap" tabindex="0" role="button" aria-label="slot 2: drop a label here"></span></div>
  </div>
  <div class="bank" data-capture><button class="chip">heap</button><button class="chip">PCB</button><button class="chip">stack</button></div>
  <div class="k-ctrls"><button class="k-btn fq-check">Check</button></div>
  <p class="verdict"></p>
</div>
```

**Intro and score slides**

```html
<section class="slide" data-sec="Final quiz" data-budget="skip">
  <div class="inner" style="max-width:980px">
    <span class="tag reveal">Final quiz · about 10 minutes</span>
    <h2 class="reveal" style="--d:.05s">Sixteen questions, eight kinds</h2>
    <p class="lead reveal" style="--d:.1s">Everything you need is in this deck. Each question has <b>one check</b>. Your score waits on the final slide.</p>
    <div class="row4 fq-kinds reveal" style="--d:.16s">
      <div class="card"><span class="n">1</span><p><b>Choose one</b><br>Pick the best answer.</p></div>
      <!-- one card per kind -->
    </div>
  </div>
</section>

<section class="slide" data-budget="skip" id="fq-score">
  <div class="inner" style="max-width:900px">
    <span class="tag reveal">Final quiz · your score</span>
    <h2 class="reveal" style="--d:.05s"><span id="fq-total">0</span> / <span id="fq-of">16</span></h2>
    <p class="lead reveal" style="--d:.1s" id="fq-msg">Answer the questions, then come back here.</p>
    <div class="fq-grid reveal" style="--d:.16s" id="fq-grid"></div>
    <div class="reveal" style="--d:.22s" id="fq-review"></div>
    <div class="k-ctrls reveal" style="--d:.28s"><button class="k-btn" id="fq-retry">Try the quiz again</button></div>
  </div>
</section>
```

**The QUIZ-MAP comment** (next to the deck's other records)

```html
<!-- QUIZ-MAP
quiz: slides 34-43 · 16 items · 8 kinds · about 10 min · data-budget="skip"
1  mcq   "Job 1 waits for the disk…"            -> switches to another job · slide 15
5  gap   "At power-up, the ___ program…"        -> bootstrap · slide 6
…
-->
```

---

## Appendix B — Quiz CSS (append to the deck's style block)

```css
/* ===== FINAL QUIZ (9 question kinds) — reads only canvas and bridge tokens ===== */
.fq-pair{align-items:start;gap:26px;margin-top:6px}
.fq{background:var(--surface);border:1.6px solid var(--ink-soft);border-radius:var(--wob-r,14px 22px 16px 24px/22px 14px 24px 16px);padding:14px 16px}
.fq .stem{font-weight:700;line-height:1.45}
.fq .opts.fq-col{grid-template-columns:1fr;gap:8px}
.fq .opts.fq-tf{grid-template-columns:1fr 1fr}
.fq .opt{font-size:.92rem;padding:8px 12px}
.fq .verdict{font-size:1.2rem;line-height:1.25}
.fq.locked .opt,.fq.locked .fq-it,.fq.locked .fq-ch{cursor:default}
.fq.locked .opt:hover{transform:none}
.fq-kinds{margin-top:14px}
.fq-kinds .card{padding:10px 12px} .fq-kinds .card p{font-size:.86rem;line-height:1.35}
input.gap{font:inherit;font-weight:700;color:var(--ink);background:var(--surface-2);border:none;border-bottom:2px dashed var(--yellow);
  width:9.5em;padding:0 6px;margin:0 2px;border-radius:4px 4px 0 0;outline:none}
input.gap:focus{border-bottom-style:solid;background:var(--marker)}
input.gap.num{width:8em;border:1.6px solid var(--ink-soft);border-radius:8px 12px 9px 13px;padding:4px 10px}
input.gap.ok{background:var(--marker);border-bottom:2px solid var(--yellow)}
input.gap.no{border-bottom:2px solid var(--red);text-decoration:line-through;text-decoration-color:var(--red)}
.fq-rows{display:grid;gap:7px;margin-top:10px}
.fq-row{display:grid;grid-template-columns:minmax(7.5em,auto) 1fr;gap:10px;align-items:center;font-size:.92rem;
  padding:4px 6px;border-radius:8px 12px 9px 13px;transition:background .3s ease}
.fq-term{font-weight:700}
.fq-row select{font:inherit;font-size:.88rem;color:var(--ink);background:var(--paper-2);border:1.4px solid var(--ink-soft);border-radius:8px;padding:4px 6px;min-width:0;width:100%}
.fq-row.ok{background:var(--marker)}
.fq-row.no{box-shadow:inset 3px 0 0 var(--red)}
.fq-row .fix{grid-column:1/-1;font-size:.82rem;color:var(--red);padding-inline-start:4px}
.fq[data-type="sort"] .fq-row{grid-template-columns:1fr;gap:4px;padding:3px 6px}   /* sort: the item above its group buttons */
.fq-grp{display:flex;flex-wrap:wrap;gap:6px}
.fq-grp button{font:inherit;font-size:.82rem;font-weight:700;color:var(--ink-soft);background:transparent;border:1.4px dashed var(--ink-soft);
  border-radius:999px;padding:2px 11px;cursor:pointer;transition:background .25s ease,color .25s ease}
.fq-grp button.on{color:var(--ink);background:var(--marker);border-style:solid;border-color:var(--yellow)}
.fq-items{display:grid;gap:7px;margin-top:10px}
.fq-it{display:flex;gap:10px;align-items:center;font:inherit;font-size:.92rem;text-align:start;color:var(--ink);background:var(--surface);
  border:1.6px solid var(--ink-soft);border-radius:10px 16px 12px 18px/16px 10px 18px 12px;padding:7px 12px;cursor:pointer;transition:background .25s ease}
.fq-num{flex:none;width:26px;height:26px;display:grid;place-items:center;border:1.6px dashed var(--ink-soft);border-radius:50%;
  font-family:var(--font-display);font-weight:700;font-size:1.15rem;color:var(--yellow)}
.fq-it.picked .fq-num{border-style:solid;border-color:var(--yellow)}
.fq-it.ok{background:var(--marker)}
.fq-it.no{box-shadow:inset 3px 0 0 var(--red)}
.fq-it .fix{margin-inline-start:auto;font-size:.8rem;color:var(--red);white-space:nowrap}
.fq-sent{margin-top:10px;line-height:2.1;font-size:1rem}
.fq-ch{font:inherit;color:var(--ink);background:transparent;border:none;border-bottom:2px dotted var(--ink-soft);padding:0 2px;cursor:pointer;
  border-radius:3px;transition:background .25s ease}
.fq-ch:hover{background:var(--surface)}
.fq-ch.ok{background:var(--marker);border-bottom:2px solid var(--yellow);text-decoration:line-through;text-decoration-color:var(--red)}   /* found the mistake */
.fq-ch.no{border-bottom:2px dashed var(--red)}                                                                                          /* your pick: this part was fine */
.fq-ch.ans{background:color-mix(in srgb,var(--red) 18%,transparent);border-bottom:2px solid var(--red);text-decoration:line-through;text-decoration-color:var(--red)} /* the real mistake */
.fq .k-ctrls{margin-top:10px}
.k-btn:disabled{opacity:.45;cursor:default}
.fq-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:14px}
.fq-cell{background:var(--surface);border:1.6px solid var(--ink-soft);border-radius:10px 16px 12px 18px/16px 10px 18px 12px;padding:8px 10px;font-size:.84rem}
.fq-cell b{display:block;font-size:.8rem;color:var(--ink-soft);font-weight:700}
.fq-cell .marks{font-family:var(--font-display);font-weight:700;font-size:1.35rem;letter-spacing:.06em}
.fq-cell .m-ok{color:var(--yellow)} .fq-cell .m-no{color:var(--red)} .fq-cell .m-skip{color:var(--pencil)}
#fq-review{margin-top:14px;font-size:.92rem}
/* fill the gap: word bank + drop gap */
.drop{display:inline-flex;align-items:center;justify-content:center;min-width:7.5em;min-height:1.9em;vertical-align:middle;margin:0 3px;padding:1px 4px;
  border:1.8px dashed var(--yellow);border-radius:8px 12px 9px 13px;background:var(--surface-2);cursor:pointer;transition:background .2s ease}
.drop.over{background:var(--marker);border-style:solid}
.drop.full{border-style:solid;border-color:var(--ink-soft);padding:0}
.drop.full .chip{margin:0;box-shadow:none;transform:none}
.drop.ok{background:var(--marker);border-color:var(--yellow)}
.drop.no{border-color:var(--red)} .drop.no .chip{text-decoration:line-through;text-decoration-color:var(--red)}
.bank{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;min-height:2.2em}
.chip{font:inherit;font-weight:700;font-size:.92rem;color:var(--k-card-ink);background:var(--k-card);border:1.4px solid var(--k-card-ink);
  border-radius:6px 10px 7px 11px;padding:3px 12px;cursor:grab;touch-action:none;user-select:none;-webkit-user-select:none;
  box-shadow:var(--shadow);transform:rotate(-1deg);transition:opacity .2s ease,transform .2s ease}
.chip:nth-child(even){transform:rotate(1deg)}
.chip:hover{transform:translateY(-2px) rotate(-1deg)}
.chip.lifted{opacity:.3}
.chip.ghost{position:fixed;z-index:50;pointer-events:none;cursor:grabbing;transform:rotate(-3deg) scale(1.06);opacity:.95}
.chip:disabled{cursor:default;opacity:.55}
.chip.ans{opacity:1;outline:2px solid var(--yellow);outline-offset:2px}
@media(min-width:881px){.nav .sec{min-width:80px}}   /* keeps short topics legible now the quiz topic is long */
#fq-review .k-btn{font-size:1.05rem;margin:4px 6px 0 0}
@media(max-width:880px){
  .fq-kinds{grid-template-columns:repeat(2,1fr)}
  .fq-grid{grid-template-columns:repeat(2,1fr)}
  .fq-row{grid-template-columns:1fr}
  .fq .opts.fq-tf{grid-template-columns:1fr 1fr}
}
/* label the figure (new kind, deck 2): numbered marks on the figure, one drop per number below it */
.fq-fig{margin-top:8px}
.fq-mark{display:inline-grid;place-items:center;flex:none;width:1.6em;height:1.6em;border:1.6px solid var(--yellow);border-radius:50%;
  background:var(--paper);color:var(--yellow);font-family:var(--font-display);font-weight:700;font-size:1.05rem;line-height:1}
.lf-pin.fq-mark{font-size:min(1.05rem,max(11px,calc(17 * 100cqi / var(--vw))))}
.fq-slots{display:grid;grid-template-columns:1fr 1fr;gap:6px 12px;margin-top:8px}
.fq-slot{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.fq-slot .drop{flex:1;min-width:0;margin:0}
.fq-slot .fix{flex-basis:100%;font-size:.8rem;color:var(--red);padding-inline-start:2.2em}
.drop.sel{border-style:solid;background:var(--marker)}
@media(max-width:880px){.fq-slots{grid-template-columns:1fr}}
/* figure labels with a backing (.lf-pin.chip) are not quiz word chips: undo the quiz .chip look on them */
.lf-layer .lf-pin.chip{color:var(--k-ink);background:var(--paper);font-family:var(--font-display);font-weight:600;line-height:1.02;border:none;border-radius:5px;
  padding:0 5px;cursor:auto;touch-action:auto;user-select:auto;-webkit-user-select:auto;box-shadow:none;transition:none;transform:translate(0,-50%)}
.lf-layer .lf-pin.chip.mid{transform:translate(-50%,-50%)} .lf-layer .lf-pin.chip.end{transform:translate(-100%,-50%)}
```

---

## Appendix C — Quiz script (append to the end of the deck's single script)

```js
/* ===== FINAL QUIZ — 9 question kinds, one check per question, score on the last slide ===== */
(function(){
  const qs=[...document.querySelectorAll('.fq')]; if(!qs.length) return;
  const state=qs.map(()=>null);                      // null = not answered · true · false
  const resets=[];
  const num=t=>t.replace(/[\s,]/g,'');
  const shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
  const TICK='<svg viewBox="0 0 30 30"><path class="scrib" pathLength="1" d="M4 6 L26 24 M26 6 L4 24" stroke="var(--red)" stroke-width="2.6" fill="none" stroke-linecap="round"/><path class="tick" pathLength="1" d="M5 16 L12 24 L27 4" stroke="var(--ink)" stroke-width="3" fill="none" stroke-linecap="round" filter="url(#wob)"/></svg>';

  qs.forEach((q,i)=>{
    const v=q.querySelector('.verdict'), type=q.dataset.type, chk=q.querySelector('.fq-check');
    const finish=(ok,extra)=>{
      state[i]=ok; q.classList.add('locked');
      v.textContent=(ok?'Yes. ':'Not quite. ')+(extra?extra+' ':'')+q.dataset.why; v.classList.add('show');
      q.querySelectorAll('input,select,.fq-grp button,.fq-check,.fq-clear').forEach(e=>e.disabled=true);
    };
    const unlock=()=>{
      state[i]=null; q.classList.remove('locked'); v.textContent=''; v.classList.remove('show');
      q.querySelectorAll('input,select,.fq-grp button,.fq-check,.fq-clear').forEach(e=>e.disabled=false);
      q.querySelectorAll('.ok,.no,.ans,.picked,.correct,.wrong').forEach(e=>e.classList.remove('ok','no','ans','picked','correct','wrong'));
      q.querySelectorAll('.fix').forEach(e=>e.remove());
    };

    if(type==='mcq'){
      q.querySelectorAll('.opt .box').forEach(b=>b.innerHTML=TICK);
      q.querySelectorAll('.opt').forEach(b=>b.addEventListener('click',()=>{
        if(state[i]!==null) return;
        const ok=b.dataset.ok==='1'; b.classList.add(ok?'correct':'wrong');
        if(!ok) q.querySelector('.opt[data-ok="1"]').classList.add('correct');
        finish(ok);
      }));
      resets[i]=unlock;
    }

    if(type==='gap'){
      /* word bank: drag a word into the gap, or tap it; tap a filled gap to send its word back */
      const drop=q.querySelector('.drop'), bank=q.querySelector('.bank'), chips=[...bank.querySelectorAll('.chip')];
      const order=chips.slice();
      const place=c=>{ if(state[i]!==null) return; const old=drop.querySelector('.chip'); if(old===c) return;
        if(old) bank.appendChild(old); drop.appendChild(c); drop.classList.add('full');
        order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); }); };
      const back=()=>{ if(state[i]!==null) return; const c=drop.querySelector('.chip'); if(!c) return;
        bank.appendChild(c); drop.classList.remove('full'); order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); }); };
      chips.forEach(c=>{
        let sx=0, sy=0, ghost=null, moved=false;
        c.addEventListener('pointerdown',e=>{ if(state[i]!==null||e.button>0) return;
          sx=e.clientX; sy=e.clientY; moved=false; c.setPointerCapture(e.pointerId); });
        c.addEventListener('pointermove',e=>{ if(!c.hasPointerCapture(e.pointerId)) return;
          if(!moved&&Math.hypot(e.clientX-sx,e.clientY-sy)<6) return;
          if(!moved){ moved=true; const r=c.getBoundingClientRect(); ghost=c.cloneNode(true); ghost.classList.add('ghost');
            ghost.style.width=r.width+'px'; document.body.appendChild(ghost); c.classList.add('lifted'); }
          ghost.style.left=(e.clientX-ghost.offsetWidth/2)+'px'; ghost.style.top=(e.clientY-ghost.offsetHeight/2)+'px';
          const over=document.elementFromPoint(e.clientX,e.clientY); drop.classList.toggle('over',!!over&&drop.contains(over)); });
        const end=e=>{ if(!c.hasPointerCapture(e.pointerId)) return; c.releasePointerCapture(e.pointerId);
          if(!moved) return;
          const over=document.elementFromPoint(e.clientX,e.clientY);
          ghost.remove(); ghost=null; c.classList.remove('lifted'); drop.classList.remove('over');
          if(over&&drop.contains(over)) place(c); else if(c.parentNode===drop) back();
          c.dataset.dragged='1'; setTimeout(()=>delete c.dataset.dragged,0); };
        c.addEventListener('pointerup',end); c.addEventListener('pointercancel',end);
        c.addEventListener('click',e=>{ e.stopPropagation(); if(c.dataset.dragged) return;
          if(c.parentNode===drop) back(); else place(c); });
      });
      drop.addEventListener('click',back);
      drop.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); back(); } });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        const c=drop.querySelector('.chip');
        if(!c){ v.textContent='Drag a word into the gap first.'; v.classList.add('show'); return; }
        const ok=c.textContent.trim()===q.dataset.answer; drop.classList.add(ok?'ok':'no');
        if(!ok) chips.find(x=>x.textContent.trim()===q.dataset.answer).classList.add('ans');
        q.querySelectorAll('.chip').forEach(x=>x.disabled=true);
        finish(ok, ok?'':'Answer: '+q.dataset.answer+'.'); });
      resets[i]=()=>{ unlock(); q.querySelectorAll('.chip').forEach(x=>x.disabled=false);
        const c=drop.querySelector('.chip'); if(c) bank.appendChild(c); drop.classList.remove('full');
        order.forEach(x=>bank.appendChild(x)); };
    }

    if(type==='num'){
      const inp=q.querySelector('input.gap');
      const run=()=>{ if(state[i]!==null||!inp.value.trim()) return;
        const ok=num(inp.value)===q.dataset.answer; inp.classList.add(ok?'ok':'no'); finish(ok); };
      chk.addEventListener('click',run);
      inp.addEventListener('keydown',e=>{ if(e.key==='Enter'){ e.preventDefault(); run(); } });
      resets[i]=()=>{ unlock(); inp.value=''; };
    }

    if(type==='match'){
      const choices=[...q.querySelectorAll('.fq-choices li')].map(li=>({k:li.dataset.key,t:li.textContent}));
      const rows=[...q.querySelectorAll('.fq-row')];
      const fill=()=>{ const order=shuffle(choices.slice());
        rows.forEach(r=>{ const s=r.querySelector('select');
          s.innerHTML='<option value="">Choose…</option>'+order.map(c=>`<option value="${c.k}">${c.t}</option>`).join('');
          s.setAttribute('aria-label','meaning of '+r.querySelector('.fq-term').textContent); }); };
      fill();
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(rows.some(r=>!r.querySelector('select').value)){ v.textContent='Choose a meaning for every term first.'; v.classList.add('show'); return; }
        let good=0;
        rows.forEach(r=>{ const ok=r.querySelector('select').value===r.dataset.key; r.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+choices.find(c=>c.k===r.dataset.key).t; r.appendChild(f);} });
        finish(good===rows.length, good===rows.length?'':good+' of '+rows.length+' right.'); });
      resets[i]=()=>{ unlock(); fill(); };
    }

    if(type==='sort'){
      const groups=q.dataset.groups.split('|'), rows=[...q.querySelectorAll('.fq-row')];
      rows.forEach(r=>{ const g=document.createElement('div'); g.className='fq-grp';
        groups.forEach(name=>{ const b=document.createElement('button'); b.type='button'; b.textContent=name; b.dataset.g=name;
          b.addEventListener('click',()=>{ if(state[i]!==null) return; g.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b)); });
          g.appendChild(b); });
        r.appendChild(g); });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(rows.some(r=>!r.querySelector('.fq-grp .on'))){ v.textContent='Put every item in a group first.'; v.classList.add('show'); return; }
        let good=0;
        rows.forEach(r=>{ const ok=r.querySelector('.fq-grp .on').dataset.g===r.dataset.g; r.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+r.dataset.g; r.appendChild(f);} });
        finish(good===rows.length, good===rows.length?'':good+' of '+rows.length+' right.'); });
      resets[i]=()=>{ unlock(); q.querySelectorAll('.fq-grp .on').forEach(b=>b.classList.remove('on')); };
    }

    if(type==='order'){
      const items=[...q.querySelectorAll('.fq-it')], picked=[];
      const paint=()=>items.forEach(it=>{ const p=picked.indexOf(it); it.querySelector('.fq-num').textContent=p<0?'':p+1; it.classList.toggle('picked',p>=0); });
      items.forEach(it=>it.addEventListener('click',()=>{ if(state[i]!==null) return;
        const p=picked.indexOf(it); if(p>=0) picked.splice(p,1); else picked.push(it); paint(); }));
      q.querySelector('.fq-clear').addEventListener('click',()=>{ if(state[i]!==null) return; picked.length=0; paint(); });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        if(picked.length<items.length){ v.textContent='Tap every step first ('+picked.length+' of '+items.length+').'; v.classList.add('show'); return; }
        let good=0;
        picked.forEach((it,k)=>{ const ok=+it.dataset.n===k+1; it.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='should be '+it.dataset.n; it.appendChild(f);} });
        finish(good===items.length, good===items.length?'':good+' of '+items.length+' in place.'); });
      resets[i]=()=>{ unlock(); picked.length=0; paint(); };
    }

    if(type==='spot'){
      q.querySelectorAll('.fq-ch').forEach(c=>c.addEventListener('click',()=>{ if(state[i]!==null) return;
        const ok=c.dataset.ok==='1'; c.classList.add(ok?'ok':'no');
        if(!ok) q.querySelector('.fq-ch[data-ok="1"]').classList.add('ans');
        finish(ok); }));
      resets[i]=unlock;
    }

    if(type==='label'){
      /* label the figure (new kind, deck 2): one drop per numbered slot. Drag a label onto a slot, or tap a slot and then a label
         (a tapped label fills the chosen slot, else the first empty one); tap a filled slot to send its label back. */
      const drops=[...q.querySelectorAll('.drop')], bank=q.querySelector('.bank'), chips=[...bank.querySelectorAll('.chip')];
      const order=chips.slice(); let sel=null;
      const tidy=()=>order.forEach(x=>{ if(x.parentNode===bank) bank.appendChild(x); });
      const mark=d=>{ sel=d; drops.forEach(x=>x.classList.toggle('sel',x===d)); };
      const back=d=>{ if(state[i]!==null) return; const c=d.querySelector('.chip'); if(!c) return;
        bank.appendChild(c); d.classList.remove('full'); tidy(); };
      const put=(c,d)=>{ if(state[i]!==null) return; const old=d.querySelector('.chip'); if(old===c) return;
        const from=c.parentNode.classList.contains('drop')?c.parentNode:null;
        if(old) bank.appendChild(old);
        d.appendChild(c); d.classList.add('full'); if(from) from.classList.remove('full'); tidy();
        mark(drops.find(x=>!x.querySelector('.chip'))||null); };
      const target=()=>(sel&&!sel.querySelector('.chip'))?sel:(drops.find(x=>!x.querySelector('.chip'))||sel);
      chips.forEach(c=>{
        let sx=0, sy=0, ghost=null, moved=false, hot=null;
        c.addEventListener('pointerdown',e=>{ if(state[i]!==null||e.button>0) return;
          sx=e.clientX; sy=e.clientY; moved=false; c.setPointerCapture(e.pointerId); });
        c.addEventListener('pointermove',e=>{ if(!c.hasPointerCapture(e.pointerId)) return;
          if(!moved&&Math.hypot(e.clientX-sx,e.clientY-sy)<6) return;
          if(!moved){ moved=true; const r=c.getBoundingClientRect(); ghost=c.cloneNode(true); ghost.classList.add('ghost');
            ghost.style.width=r.width+'px'; document.body.appendChild(ghost); c.classList.add('lifted'); }
          ghost.style.left=(e.clientX-ghost.offsetWidth/2)+'px'; ghost.style.top=(e.clientY-ghost.offsetHeight/2)+'px';
          const over=document.elementFromPoint(e.clientX,e.clientY); hot=over&&drops.find(d=>d.contains(over))||null;
          drops.forEach(d=>d.classList.toggle('over',d===hot)); });
        const end=e=>{ if(!c.hasPointerCapture(e.pointerId)) return; c.releasePointerCapture(e.pointerId);
          if(!moved) return;
          const over=document.elementFromPoint(e.clientX,e.clientY), d=over&&drops.find(x=>x.contains(over));
          ghost.remove(); ghost=null; c.classList.remove('lifted'); drops.forEach(x=>x.classList.remove('over'));
          if(d) put(c,d); else if(c.parentNode.classList.contains('drop')) back(c.parentNode);
          c.dataset.dragged='1'; setTimeout(()=>delete c.dataset.dragged,0); };
        c.addEventListener('pointerup',end); c.addEventListener('pointercancel',end);
        c.addEventListener('click',e=>{ e.stopPropagation(); if(c.dataset.dragged||state[i]!==null) return;
          if(c.parentNode.classList.contains('drop')){ const d=c.parentNode; back(d); mark(d); }
          else{ const t=target(); if(t) put(c,t); } });
      });
      drops.forEach(d=>{
        const tap=()=>{ if(state[i]!==null) return; if(d.querySelector('.chip')) back(d); mark(d); };
        d.addEventListener('click',tap);
        d.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); tap(); } });
      });
      chk.addEventListener('click',()=>{ if(state[i]!==null) return;
        const open=drops.filter(d=>!d.querySelector('.chip')).length;
        if(open){ v.textContent='Put a label on every number first ('+(drops.length-open)+' of '+drops.length+').'; v.classList.add('show'); return; }
        let good=0;
        drops.forEach(d=>{ const ok=d.querySelector('.chip').textContent.trim()===d.dataset.answer; d.classList.add(ok?'ok':'no'); if(ok) good++;
          else{ const f=document.createElement('span'); f.className='fix'; f.textContent='→ '+d.dataset.answer; d.parentNode.appendChild(f);} });
        mark(null); chips.forEach(x=>x.disabled=true);
        finish(good===drops.length, good===drops.length?'':good+' of '+drops.length+' right.'); });
      resets[i]=()=>{ unlock(); chips.forEach(x=>x.disabled=false);
        drops.forEach(d=>{ const c=d.querySelector('.chip'); if(c) bank.appendChild(c); d.classList.remove('full','over'); });
        order.forEach(x=>bank.appendChild(x)); mark(null); };
    }
  });

  /* score slide */
  const sc=document.getElementById('fq-score'); if(!sc) return;
  const of=document.getElementById('fq-of'); if(of) of.textContent=qs.length;
  const tot=document.getElementById('fq-total'), msg=document.getElementById('fq-msg'),
        grid=document.getElementById('fq-grid'), rev=document.getElementById('fq-review');
  const topicStart=name=>slides.findIndex(s=>s.dataset.sec===name);
  function score(){
    const right=state.filter(x=>x===true).length, open=state.filter(x=>x===null).length;
    tot.textContent=right;
    msg.textContent= open===qs.length ? 'Answer the questions, then come back here.'
      : open ? `${open} question${open>1?'s':''} still open. The score counts answered questions only.`
      : right>=Math.ceil(.85*qs.length) ? 'Excellent. You own this chapter.'
      : right>=Math.ceil(.6*qs.length) ? 'Good work. Revisit the topics below, then try again.'
      : 'A second pass will help. Start with the topics below.';
    const kinds=[...new Set(qs.map(q=>q.dataset.kind||'Questions'))];      // grid: one cell per kind, in order of appearance
    grid.innerHTML=kinds.map((k,n)=>{
      const m=qs.map((q,j)=>[q,j]).filter(([q])=>(q.dataset.kind||'Questions')===k)
        .map(([,j])=>state[j]===true?'<span class="m-ok">✓</span>':state[j]===false?'<span class="m-no">✗</span>':'<span class="m-skip">·</span>').join(' ');
      return `<div class="fq-cell"><b>${n+1} · ${k}</b><span class="marks">${m}</span></div>`; }).join('');
    const miss=[...new Set(qs.filter((q,j)=>state[j]===false).map(q=>q.dataset.topic))];
    rev.innerHTML=miss.length?'<span class="soft">Revisit:</span> ':'';
    miss.forEach(t=>{ const b=document.createElement('button'); b.className='k-btn'; b.textContent=t;
      b.addEventListener('click',()=>{ const k=topicStart(t); if(k>=0) go(k); }); rev.appendChild(b); });
  }
  sc.addEventListener('slideenter',score); score();
  document.getElementById('fq-retry').addEventListener('click',()=>{
    resets.forEach(r=>r&&r()); score(); go(slides.indexOf(qs[0].closest('.slide'))); });
})();
```

---

## Appendix D — Browser walk (Playwright)

Run it after building, at laptop size and again with a 390 × 844 viewport. It answers every item: the first item of each kind right and the second wrong, except where noted. Then it checks the score and the reset, and screenshots each quiz slide. Adapt the slide indexes and the expected score to the deck.

```python
"""quiz_walk.py - answers every .fq item in a deck (questions-rulebook.md §7).
Usage: python quiz_walk.py deck.html [outdir]
Answers items alternately right / wrong, from each item's own answer data, then checks
the score slide, the reset, console errors, and screenshots every quiz slide."""
import asyncio, os, sys
from playwright.async_api import async_playwright

DECK = os.path.abspath(sys.argv[1]); OUT = sys.argv[2] if len(sys.argv) > 2 else "quiz-shots"
os.makedirs(OUT, exist_ok=True)

async def answer(pg, q, right):
    t = await q.get_attribute("data-type")
    if t == "mcq":
        await q.locator('.opt[data-ok="1"]' if right else '.opt:not([data-ok="1"])').first.click()
    elif t == "spot":
        await q.locator('.fq-ch[data-ok="1"]' if right else '.fq-ch:not([data-ok="1"])').first.click()
    elif t == "gap":
        ans = await q.get_attribute("data-answer")
        chips = q.locator(".chip")
        for j in range(await chips.count()):
            w = (await chips.nth(j).inner_text()).strip()
            if (w == ans) == right: await chips.nth(j).click(); break
        await q.locator(".fq-check").click()
    elif t == "num":
        ans = await q.get_attribute("data-answer")
        await q.locator("input").fill(ans if right else str(int(ans) + 1)); await q.locator(".fq-check").click()
    elif t == "match":
        rows = q.locator(".fq-row"); n = await rows.count()
        keys = [await rows.nth(r).get_attribute("data-key") for r in range(n)]
        for r in range(n):
            k = keys[r] if right else keys[(r + 1) % n]
            await rows.nth(r).locator("select").select_option(k)
        await q.locator(".fq-check").click()
    elif t == "sort":
        rows = q.locator(".fq-row"); groups = (await q.get_attribute("data-groups")).split("|")
        for r in range(await rows.count()):
            g = await rows.nth(r).get_attribute("data-g")
            if not right and r == 0: g = next(x for x in groups if x != g)
            await rows.nth(r).locator(f'.fq-grp button[data-g="{g}"]').click()
        await q.locator(".fq-check").click()
    elif t == "order":
        items = q.locator(".fq-it"); n = await items.count()
        ns = [int(await items.nth(j).get_attribute("data-n")) for j in range(n)]
        seq = sorted(range(n), key=lambda j: ns[j])
        if not right: seq[0], seq[1] = seq[1], seq[0]
        for j in seq: await items.nth(j).click()
        await q.locator(".fq-check").click()
    elif t == "label":
        drops = q.locator(".drop"); n = await drops.count()
        ans = [await drops.nth(d).get_attribute("data-answer") for d in range(n)]
        if not right: ans[0], ans[1] = ans[1], ans[0]
        for d in range(n):
            await drops.nth(d).click()
            await q.locator(".bank .chip", has_text=ans[d]).first.click()
        await q.locator(".fq-check").click()
    else:
        print("  ! unknown data-type", t); return None
    return right

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1280, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "Failed to load resource" not in m.text else None)  # ignore blocked fonts
        await pg.goto("file://" + DECK); await pg.wait_for_timeout(600)
        slide_ids = await pg.evaluate("[...new Set([...document.querySelectorAll('.fq')].map(q=>slides.indexOf(q.closest('.slide'))))]")
        expected = 0; n = 0
        for k in slide_ids:
            await pg.evaluate(f"go({k},true)"); await pg.wait_for_timeout(1200)
            qs = pg.locator("section.slide.active .fq")
            for j in range(await qs.count()):
                right = (n % 2 == 0); n += 1
                if await answer(pg, qs.nth(j), right): expected += 1
            await pg.wait_for_timeout(700); await pg.screenshot(path=f"{OUT}/quiz-{k+1}.png")
        score_k = await pg.evaluate("slides.indexOf(document.getElementById('fq-score'))")
        await pg.evaluate(f"go({score_k},true)"); await pg.wait_for_timeout(1200)
        await pg.screenshot(path=f"{OUT}/quiz-score.png")
        got = int(await pg.text_content("#fq-total"))
        print(f"items {n} · expected score {expected} · shown {got} · {'OK' if got == expected else 'MISMATCH'}")
        print("message:", await pg.text_content("#fq-msg"))
        print("revisit:", await pg.evaluate("[...document.querySelectorAll('#fq-review .k-btn')].map(b=>b.textContent)"))
        await pg.click("#fq-retry"); await pg.wait_for_timeout(400)
        print("after reset: score", await pg.text_content("#fq-total"), "· on slide", await pg.evaluate("idx") + 1)
        ov = await pg.evaluate("slides.map((s,k)=>[k+1,s.scrollWidth>s.clientWidth+2]).filter(x=>x[1]).map(x=>x[0])")
        print("sideways overflow on slides:", ov or "none")
        print("console errors:", errs or "none")
        await b.close()

asyncio.run(main())
```

---

## Appendix E — Worked example: Applied OS · Chapter 1

The first quiz built with this file, kept here so later decks can see the level aimed for.

| # | Kind | Item | Answer | Why it is a fair challenge |
|---|---|---|---|---|
| 1 | Choose one | Job 1 waits for the disk; what happens to the CPU? | The OS switches it to another job | Applies multiprogramming to a scenario; distractors are the "CPU idles" belief and a confusion with the controller |
| 2 | Choose one | What does a network OS do? | Lets systems exchange messages, like one system | Distractors are other "manager" tools in the deck (VMM, load balancer, firewall) |
| 3 | True or false | "The cache holds more data than main memory." | False | Targets size vs speed |
| 4 | True or false | "Each thread has its own program counter." | True | A true item, so "false" isn't a safe guess |
| 5 | Fill the gap | At power-up, the ___ program runs from ROM… | bootstrap | The bank holds kernel, a near-miss |
| 6 | Fill the gap | Moving a process out to disk and back is ___ | swapping | The bank holds virtual memory, the closest confusion |
| 7 | Match | Kernel / resource allocator / control program / application program | — | Four roles that students mix up |
| 8 | Match | Synchronization / communication / deadlock handling / suspend and resume | — | Meanings are close; needs real understanding |
| 9 | Put in order | Interrupt handling, 4 steps | save → look up → run → return | The deck's step-through |
| 10 | Put in order | Registers, cache, main memory, SSD, tapes | fastest → slowest | The hierarchy, shown shuffled |
| 11 | Sort | 6 storage types: volatile or not | — | Applies the volatile line in the pyramid |
| 12 | Sort | 5 services: IaaS, PaaS or SaaS | — | Uses new examples, not the deck's words |
| 13 | Find the mistake | DMA sentence, "for every byte" | per block | The deck's key DMA fact |
| 14 | Find the mistake | User ID sentence, "group ID covers one single user" | a set of users | A believable slip |
| 15 | Work it out | 16,384 bytes in 4,096-byte blocks | 4 interrupts | One division with friendly numbers |
| 16 | Work it out | 5,000,000 ns vs 250 ns | 20,000 | Shows why caching matters |
