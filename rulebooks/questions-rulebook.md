# Questions Rulebook

**Version 1.3 · 17 October 2026 · written against `lesson-deck-builder` v1.3 (Sketchbook: paper or six chalkboard boards) · first used on Applied OS · Chapter 1**

> **New in 1.3 (structure only; no rule changed):** the code moved to `deck-tools` (Appendices A–D name each file), the version history moved to `rulebooks-changelog.md`, and this file has a size cap (§0).

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
  - **Tested defaults:** the kinds catalogue, the layout, the code in `deck-tools` (the appendices say which file) and the numbers marked *(target)*, written for the models of their date.
  - When another way meets the goals better (a new kind, a better check, better code), use it and name it on the report's "Departures" line (§8).

- Every rule has an ID (QG2, QW3, QL4 …) so the user can point at it in feedback.
- **Size cap:** this file stays under **32,000 characters**. Code stays in `deck-tools`, history in `rulebooks-changelog.md` (`slides-rulebook.md` §0 has the full rule; `deck-tools/size_check.py` checks it).
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

**What to attach:** this file; the main rulebook; the deck or the lecture; `deck-tools.zip`; optionally an earlier deck of the course that already has a quiz. `deck-tools/snippets/` holds the code of every proven kind (K1–K9): `quiz-markup.html`, `quiz.css` and `quiz.js` (Appendices A–C). So the first deck of a new course needs no earlier deck.

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
- **Markup contract** (templates in `deck-tools/snippets/quiz-markup.html`, Appendix A):

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
- **Reuse.** A later deck copies the quiz CSS and script unchanged from the previous deck (or from `deck-tools/snippets/quiz.css` and `quiz.js`) and writes only new items. A new kind adds a `data-type` branch; it doesn't rewrite the others.

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

A Playwright test that does the browser walk is `deck-tools/quiz_walk.py` (Appendix D).

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

All templates are in `deck-tools/snippets/quiz-markup.html`, one part per type. Copy a part with a script, then replace the text. Two items per slide sit in `<div class="row2 fq-pair">`.

| Part | Notes |
|---|---|
| `slide shell` | The quiz slide around the items |
| `mcq` | Choose one; True or false uses `class="opts fq-tf"` with two options |
| `gap` | Word bank |
| `match` | |
| `order` | List the steps shuffled; `data-n` is the true position |
| `sort` | |
| `spot` | Find the mistake; exactly one part has `data-ok="1"` |
| `num` | Work it out |
| `label` | Label the figure; one `.drop` per mark, each with its own `data-answer`; one extra label in the bank |
| `intro and score slides` | |

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

→ `deck-tools/snippets/quiz.css`

---

## Appendix C — Quiz script (append to the end of the deck's single script)

→ `deck-tools/snippets/quiz.js`

---

## Appendix D — Browser walk (Playwright)

Run it after building, at laptop size and again with a 390 × 844 viewport. It answers every item: the first item of each kind right and the second wrong, except where noted. Then it checks the score and the reset, and screenshots each quiz slide. Adapt the slide indexes and the expected score to the deck.

**The script:** `deck-tools/quiz_walk.py`. `setup_tools.sh` copies it next to the rulebooks; `quiz_walk_x.py` runs it with the newer kinds and `--phone`. Open it only to change it.

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
