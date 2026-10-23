# Slides Rulebook

**Version 2.0 · 23 October 2026 · written against `lesson-deck-builder` v1.4 (Sketchbook: paper, or chalkboard in six boards)**

> **New in 2.0:** this file ships inside the skill (`rulebooks/`), and the skill routes an attached lecture here by itself, so a run starts from one line ("use /lesson-deck-builder to explain the attached file"). Nothing else is attached but the previous deck, and no Markdown file goes back: the course's memory lives in the COURSE record (§0, W11). English decks can be written at A2–C1 (G2). Full history: `rulebooks-changelog.md`.

This file tells you how to turn a set of university lecture slides into one lesson-deck-builder HTML deck that a student can study **instead of** the slides:
- complete;
- **easier to digest than the slides**, in **no more than twice their words**;
- in plain English at the course's level (A2–C1; B1 unless the user picks another);
- organised in topics that each stand alone;
- taught with methods that have research behind them.

It also tells you how to keep all the decks of a course consistent, from the first lecture to the last, for any course.

---

## 0. How to use this file

- Read this whole file and the lesson-deck-builder `SKILL.md` with the references it tells you to read, **before** you plan anything. The general notes (`deck-notes-general.md`, beside this file) record experience, not rules: read the parts that help. When there is a shell (case B, "Starting a run"), the skill's `template.html` and example decks are optional.
- This file **adds to** the skill. Where §2 says so, it **overrides** the skill. Where this file says nothing, follow the skill.
- **Who wins:**
  1. The user's instructions.
  2. The course's choices in the COURSE record.
  3. This file.
  4. The general notes, which record experience, not rules.
  5. How an earlier deck happened to be built.
- **Goals over procedures.** Some parts of this file are fixed:
  - the goals (§1, G1–G6) and their precedence;
  - the user's choices, here and in the COURSE record;
  - the limits that serve the user: completeness, the word ceiling (2 × the original's words, G5), the deck shape the user picked (§11), the canvas gate.

  Everything that says *how* is a tested default, written for the models and the skill of its date: the workflow steps, the numbers marked *(target)*, the tools it names, the code in `deck-tools`, the checks.
  - If you can meet the goals better another way, do it, and name the change and its reason on the report's "Departures" line (§10).
  - A departure never trades away a goal or a choice.
  - Rules that cite evidence (§12) change only for a reason as strong as their evidence.
- Every rule has an ID (F3, L2, T5, N1 …) so the user can point at it in feedback.
- **Size cap.** Every run reads this file, so its size is a cost paid on every deck. It stays under **110,000 characters** (about 28K tokens). `questions-rulebook.md` stays under **32,000**, `lessons-rulebook.md` under **75,000**, and the general notes under about 30,000 (their own rule).
  - Code lives in `deck-tools`, and version history in `rulebooks-changelog.md`. Neither comes back into a rulebook: a new block of code becomes a file, and a new version adds one "New in" line here and its full entry to the changelog.
  - A change that would pass a cap first merges or retires something (the general notes work the same way, their §0).
  - Check with `python deck-tools/size_check.py` after every edit of a rulebook or the notes. The caps live in that script too; change both together.
- "Why" lines give the mechanism. Tags in square brackets (for example [HN]) point to the evidence table in §12.
- This file was written against **lesson-deck-builder v1.4** (engine v2, `use-cases.md`, components §1–§32). Component numbers (§22, §25 …) refer to that version's `components.md`. In v1.3 the only style is Sketchbook, on a **paper** canvas or a **chalkboard** in one of six boards (`style-system.md §5`); the bridge tokens are in `style-system.md §7`.
  - If your version of the skill renamed or replaced something named here, apply the rule to its current equivalent and mention the mismatch in the delivery report (§10).
  - The topic bar (N1), the deck glossary (T5b), the phone layer (M1–M8) and phone-variant figures (M4) are not in the skill yet. Their code is in `deck-tools/snippets/`; Appendix B says where each file goes.
- Numbers marked *(target)* are design choices, not research findings. They may be tuned. Numbers without that mark come from a standard or a study.
- **When the model or the skill gets a new version, review the procedural parts of this file.** Ask: what here has become a workaround? Test it now and then: build one deck from the goals, the user's choices and the COURSE record alone, and compare it with a normal build. Keep a procedure only where it still makes the deck better.

### Starting a run

**What the user sends.** One line, for every deck of every course, for example:

```
use /lesson-deck-builder to explain the attached file
```

with the lecture (PDF or PPTX) attached and, from the second deck of a course on, the previous deck (HTML). The skill routes here by itself (SKILL.md, step 0b). Nothing else is attached, and no Markdown file goes back to the user. Anything the user writes (a canvas, a level, an exam focus, a §11 setting, a skip) wins over everything below and is not asked again.

| Input | Where it comes from |
|---|---|
| The lecture | Attached. One deck per lecture file. |
| The course's choices and memory | The previous deck's COURSE record. No previous deck: case A. |
| The shell | The previous deck (case B), or the skill's template (case A). |
| Older decks | Not attached. Ask for one only when you need a figure or a glossary wording from it. |
| `questions-rulebook.md` | Beside this file. Its final quiz ends every deck (§2). |
| General notes (`deck-notes-general.md`) | Beside this file. Experience that isn't a rule (word budgets, figure pitfalls, checks): read the parts that help, before planning. |
| `deck-tools/` | Beside this file: the checker, the quiz walk, the checker's brief, the `snippets/` a deck pastes in, and helpers for building, screenshots and checks. Run `setup_tools.sh` once per session from your working folder. |

**Which case is this?** The attachments decide.

- **A. First deck of a course.** No earlier deck of this course is attached.
  - Ask the course questions once, in the W5 message: the **canvas gate** (canvas, then board), the **English level** (SKILL.md step 2b; suggest B1), the exam focus, and any §11 setting the slides make relevant.
  - **The canvas gate is always asked at the first deck, and nothing is built until the user answers** (W5). Use the skill's shape: suggest one canvas with a one-line reason and list both (Paper · Chalkboard); when the user picks the chalkboard, list all six boards with their few-word identities, suggested one first, and offer the skill's board preview (`assets/style-samples/sketchbook-chalkboard.html`, whose top-bar dots switch boards) as a file the user can open. Never pick on the user's behalf. Only a canvas and board named in the prompt skip the question.
  - Build from the skill's template, with the phone layer (Appendix B4). Take every code block from the skill and from `deck-tools/snippets/` with a script, never by retyping. The template's header comment contains the text `<script>`: take the engine from `<script>` followed by `/* ---- deck engine`, or the whole template lands in the deck (symptom: two `<html>`, two active slides).
  - Start the COURSE record at deck 1, its memory lines included (W11).
- **B. Later deck of a course.** The previous deck of the same course is attached: the same course appears in its COURSE record, or in its title.
  - Don't ask anything the COURSE record already answers.
  - Use the newest deck as the shell (see "Earlier decks" below).
  - Ask in W5 only what is new in this lecture.
  - Copy the COURSE record into the new deck and raise its deck number by one.
- **C. Decks of another course are attached.** Their course differs from this lecture's.
  - Settings don't carry across courses: run case A.
  - One exception: if the user picks the same canvas and board, the other course's newest deck may replace the skill's template as the shell. Its COURSE record is not copied.

Course and lecture names come from the slides' title page or headers.

**The COURSE record.** Every deck carries the course's standing choices in one HTML comment, next to the fact ledger:

```html
<!-- COURSE
course: Applied Operating Systems · slug: applied-os
deck: 2 · source: Lecture_3_ch2_OS_Structures.pdf
style: Sketchbook · canvas: chalkboard · board: slate-reinked · english level: B1
exam focus: none (every unit equally examinable)
settings changed (§11): none
standing decisions: admin slides skipped; agenda topics with no slides skipped and named in the report; final quiz, no question set or answer box; phone first
field words: none beyond the checker's built-in list
lecturer's habits: review questions on the last page; agenda slides name topics the lecture never reaches
reusable figures: deck 2 · slide 9 · the memory hierarchy (a pyramid)
next: Lecture 4, processes (from the slides' last page)
-->
```

- The record holds the **user's choices** for the course and, since 2.0, its **memory**: the lecturer's habits, the figures later decks can reuse, and what comes next (the lines a course notes file used to hold). The next deck reads it first, so keep it short. The choices win over this file's defaults (§11).
- **This file wins over how an older deck was built.** A deck made under an older version may lack a newer part, such as a glossary slide or a `BUDGET` comment. Build the new deck to this version: **add** the missing parts, but don't rewrite the code the shell already has (see "Earlier decks").
- **Decks made before v1.4 have no record.** Take what the deck shows (canvas, board, deck number), ask the rest in W5, then write the record into the new deck.
- **Records without a `board:`** (made before v1.5): the board is the `data-board` attribute on the deck's `<html>`, or Slate re-inked when the attribute is absent. Write the `board:` into the new record.
- **Records made before 2.0** have no `english level:` (it was B1) and no memory lines: write `english level: B1` and the memory lines you can fill into the new record. The course notes file is retired; if the user offers one anyway, move its facts into the record once.
- **Shells made before v1.5 have no phone layer.** Add Appendix B4 to the new deck (it adds code, it rewrites nothing), and check the phone view (Q7).
- **Courses started before v1.8** built their decks to be shorter than the slides. Their next deck follows the 2 × word ceiling (G5) unless the record's `settings changed` line or the prompt keeps the **Shorter** setting (§11). Don't ask about it in W5. Say it on the report's "Settings changed" line ("word ceiling: 2 × from this deck (v1.8)"), and write it into the new record. Notes written before v1.8 may give advice that only served the old rule (fewer slides than the source, compressing to stay under 100%). This file wins over them.
- **Field words** beyond the checker's built-in list, for any course: list them in the record, write them to a file, and pass it to the checker with `--known` (Q2). Each deck inherits the list with the record and may add to it (L1).

**Earlier decks.**
- **The shell is the newest deck**: the highest deck number in the COURSE records, or, for a deck with no record, the number in its file name.
  - Split off everything except the slides and reuse it **unchanged**: styles, shared SVG defs, engine, component code, topic bar and glossary code. Copying the code, not re-writing it from a description, is what keeps every deck of a course looking and behaving the same.
  - When several decks are attached, the newest is the shell.
- **The shell is a source of code, not a list of allowed components.**
  - Choose each slide's component from the skill's full catalog, by teaching job (W8).
  - When a component comes back, reuse its code from the shell.
  - When it is new, take its code from the skill and add it to the shell, so the next deck inherits it.
- **Older decks** are not attached. When the record's `reusable figures` line points to one you need, ask the user for that deck; don't read it in full.
- **Glossary wording:** reuse the attached deck's glossary text for terms that come back (W6), so a term reads the same in every deck of the course; pull its `dl#glossary` entries with a short script. For a term that only an older deck glossed, ask for that deck when its exact wording matters.
- **Skill files:** read `SKILL.md`, `use-cases.md` and `components.md` in every case. With a shell, the skill's `template.html` and example decks are optional.

**Naming.**
- Name the deck `<course-slug>-NN-<lecture-slug>.html`, where NN is the deck's number in the course (01, 02 …).
- Repo mode keeps its own pattern (§2).
- Older names, for example `applied-os-ch1-introduction.html`, count by the number they contain.

**Order of work:**
1. Run W1–W4.
2. Run W5 only if it has something to ask (W5 lists what counts).
3. Build the deck, check it (W9, ending with the independent check F1b), and deliver it with the §10 report.
4. Update the COURSE record (W11).

---

## 1. The six goals and how each one is measured

| Goal | What it means here | How it is checked |
|---|---|---|
| **G1 — Replace the slides** | Every piece of content in the slides (text, figures, formulas, code, examples, speaker notes) is taught in the deck, **every fact at its full strength**, and every definition in the slides' own words. The student never needs to open the slides. | Fact ledger at 100% (F1) and a clean independent check (F1b) |
| **G2 — English at the course's level** (A2–C1, default B1) | Words and sentences that a reader at that level takes in with ease; simple grammar. | `plain_check.py --max-level <level>`: ≥ 98% of running words at the level or below (field words allowed, L1); no sentence over the level's cap (SKILL.md step 2b: 15 · 20 · 25 · 30 words) |
| **G3 — Independent topics, no jargon** | Any topic (N1) can be understood without the other topics. On any slide, every term is explained, visibly or by its glossary card. "No jargon" means **no unexplained word**, not "no technical word": the course terms that exams use are still taught. | `plain_check.py` gloss, acronym and back-reference checks; cold read (Q4) |
| **G4 — The best ways to teach** | The Concept Pattern (§6) and the teaching rules TE1–TE10. | Checklist Q5 (§9) |
| **G5 — Easier to digest than the slides, in at most twice their words** | One deck per lecture. Each concept is easier to take in than on the slides: plain words even when they are longer, full sentences instead of telegraphic bullets, the "why", a concrete example for every load-bearing concept, and small steps (one idea per slide, few new terms at a time). **The word ceiling:** the deck's words are at most **2 ×** the source's, counting its text and the words inside its figures and tables. The ceiling is never passed. **Size is measured in words only:** there is no slide-count limit. | Word ceiling (W1b, Q6): `plain_check.py` reports deck words / original ≤ 200%. Digestibility (Q6): the Concept Pattern in its deck form (§6), words per slide (V5), new-term load (T4), cold read (Q4) |
| **G6 — Phone first** | Every slide reads and works well on a phone, held upright, and still as well on a laptop as before. | Phone checks M1–M8 (Q7), at 390 × 844 first, then laptop |

### Precedence when rules conflict

1. **Correctness, and the skill's technical hard rules** (untouched engine script, validator passes, no storage APIs).
2. **Completeness (G1), including exact wording (F2).** Never drop, shrink or weaken content to meet the word ceiling, a word cap, or a simplicity target. The ceiling is met by cutting the deck's own additions (W4), never the slides' facts. If the facts and their exact wording alone would pass the ceiling, stop and ask the user (W5). (For scale, under v1.7: the 210 ISY deck 2 needed 119% of the source with every definition quoted; deck 5, a short lecture of 989 words, reached 213%. Short lectures need the tightest planning, because the arc and the glossary cost about the same words in every deck.)
3. **The word ceiling (G5).** The deck's total words stay at or below **2 × the original's**. This is a hard limit: no overrun is delivered. There is no slide-count limit.
4. **Easy to digest: understandability (G2, G3, G5), on a phone as on a laptop (G6).**
5. **Teaching method (G4).**
6. **Style** (Law 5 "little text"). The skill's reading-time budget and slide counts do not apply (§2).

*Why this order:* a deck that leaves out a topic fails the student at the exam (G1). A deck that is harder to take in than the slides gives the student no reason to use it (G5). Plain language, full sentences and examples need *more* words than the slides' telegraphic bullets, and that is where the room up to 2 × goes. The ceiling keeps the deck a study tool, not a textbook: at the slower reading speed of second-language readers (about 128 words per minute [RS]), every 1,000 source words become at most about 16 minutes of reading.

These rules still apply, because they make a slide easier to read, not only shorter:
- Facts that name or describe a part move into figure labels (V13).
- Each idea is said once, in its best place (L11).
- Terms are explained once and re-used through the glossary (T5b).

### Where the extra words go (G5)

The room between the original's word count and the ceiling is spent in this order. Spend it only where it makes the deck easier to digest; never pad toward the ceiling.

1. **Plain words and full sentences.** Everyday words even when they are longer ("the program that always runs" for "resident"), small words kept (L3), and complete sentences instead of the slides' telegraphic bullets.
2. **One concrete example for every load-bearing concept** (Concept Pattern step 2), and a worked example with a practice problem for every procedure, calculation and piece of code (step 6).
3. **The "why"**: the mechanism in one or two sentences (step 5).
4. **Help where it is needed**: the visible glosses that a topic's main sentence depends on (T5), the plain reading beside every exact quote (F2), and "What you need first" background (T8).
5. **The common mistake**, named and corrected (step 7).
6. **A second example or an analogy** (T10), only for a concept that students often find hard.

Never spend it on repeats (L11), decorative stories or fun facts (V1, TE10), or content outside the slides beyond what F3 allows.

**When a plan or a draft passes the ceiling,** cut from the bottom of this list up (W4 gives the full order). Only the deck's own additions are cut: never a fact or its exact wording.

### Improve the presentation, keep the content

Lecture slides are usually not built to teach on their own: ideas arrive in a weak order, steps are skipped, figures are cluttered, and examples are thin. **The deck is not a transcription. It is a better, easier-to-digest teaching of the same content, in at most twice the words.**

| You are expected to improve | You must keep exactly |
|---|---|
| The order of ideas (W3) | Every fact and claim the slides make, at the same strength: its qualifiers and modality (L10) |
| How ideas are grouped into topics and where slides break | The meaning of every definition |
| Headings, explanations, and missing steps in a derivation or example | Formulas, notation, and code (F2, F7, F8) |
| Examples, analogies, and practice problems | The names of terms, algorithms, and laws |
| Figures: replace a weak figure with a clearer one that carries the same information (F5) | The examinable scope: nothing removed; anything added is marked (F3) |
| Visual form: turn lists into tables, flows, maps, or step-throughs (§8); turn descriptive sentences into figure labels (V13) | The slides' version when a source disagrees, taught with a visible note (F4) |
| Background the slides assume but never teach (T8) | |
| Wording: plain words and full sentences, even when they are longer than the slides' (G5, within the 2 × ceiling) | |

Every improvement must rest on research (W2b) and must not change what the student will be examined on.

---

## 2. How this rulebook changes the lesson-deck-builder workflow

| Skill step | Under this rulebook |
|---|---|
| **Deck kind** | Always a **teaching deck** (teaching arc, challenge pair), ending with the **final quiz** of `questions-rulebook.md`. |
| **Topic conversation (step 1)** | Replaced by W5, which runs only when there is something to decide. The slides already define the topic. |
| **Canvas gate (step 1b)** | Unchanged in shape: always the skill's exact question (canvas, then board on the chalkboard). Ask **once per course**, at its first deck (case A, §0), **always**, and build nothing until the user answers. Later decks read the canvas and board from the COURSE record. |
| **Language (step 2)** | Already answered: **English**, `dir="ltr" lang="en"`. Do not ask. |
| **English level (step 2b)** | Asked once per course, at its first deck, with the canvas gate (B1 suggested). Later decks read it from the COURSE record. |
| **Scope & mode (step 3)** | Not used. The slides define the scope. |
| **Intake (step 4)** | Already answered. Audience: newcomers to the subject who read English at the course's level (the COURSE record; first deck: asked, B1 suggested), often on a phone (G6). Length: the word ceiling, at most 2 × the source's words (G5, W4). |
| **Teaching arc (step 5)** | Keep it, compactly. Order: cover · opening challenge · map (the topics, named as in the topic bar) · the topics · challenge revisited · recap (with a one-line closing) · glossary slide "Words in this deck" (T5b) · **final quiz** (its own topic, `questions-rulebook.md`). **The skill's question set and answer box are left out:** the final quiz does their job (§11 brings them back). The arc costs about 250 words *(target)*; the quiz is outside the word count (`data-budget="skip"`). Inside "one idea per slide", use the Concept Pattern in its deck form (§6). |
| **Length** | **One deck per lecture file**, measured in **words only**: at most 2 × the original's words (G5), never more. There is no slide-count limit, and the skill's reading-time budget and its slides-per-minute table (`design-system.md` §5) do not apply. The slide count follows from TE1 and V5. The validator's "> 20 slides" note is expected; mention it, don't act on it. |
| **Law 5: little text** | Applies fully. The always-visible layer carries the complete plain explanation and every gloss that the slide's main sentence depends on (T5). Hover/tap depth is only for supporting-term glosses (T5, T5b) and extras ("Extra: not in your slides"). Examinable content is never hidden (F9). |
| **Visual-first** | Visuals are the main carrier of structure, sequence, comparison and change (§8), and the main way to keep slides light (V13). Every visual must explain something from the source (V1). No mood pictures. Where this file and the skill disagree about *how* a visual is built, the skill wins; this file decides *what* the visual must show. |
| **Matching slides to teaching jobs (step 5)** | Use it fully. Every inventory unit already carries its job (W2), so each slide's component comes from that job's reverse index in `use-cases.md`, varied across the deck. Use a component only where it does a job that text cannot (§8). The catalogue's advice to trim ("three load-bearing rows", "show the range that matters") decides emphasis, never deletion (F9). |
| **Navigation** | The topic bar (N1) replaces the slide dots. |
| **Phone** | Phone first (G6, M1–M8): design and check at phone size first. The skill's template stays the base; the phone layer (Appendix B4) goes on top. |
| **Per-lesson research** | Required, at the depth of W2b. |
| **Chat mode** | One deck per lecture file per reply, named as in §0. Several lecture files: one deck each, one per reply, numbered in order. |
| **Repo mode** | Save decks as `lessons/NN-<course>-<lecture-slug>.html`. The fact ledger, independent-check record, sources, budget (the original's word count) and course record live inside each deck as HTML comments. |
| **Series mode** (setting §11) | Only when the user asks for it. Then the v1.2 rules apply: 14–18 slides per deck, hard cap 20, about 8 arc slides each, a deck list confirmed in W5, one deck per reply, and TE9 series review. The word ceiling (G5) applies to the series as a whole: all its decks together stay within 2 × the lecture's words. |

---

## 3. Workflow

**W1 — Read everything.**
- Extract the text **and** render every slide page to an image and look at it. Diagrams, arrows, tables, formulas, code, colour highlights and speaker notes carry content that text extraction loses.
- Read PDFs and `.pptx` files with the best reader you have (for example, the environment's PDF or PPTX skill).
- If a page is unreadable or seems to be missing, ask the user before you continue.

**W1b — Measure the original's words (the base of the word ceiling).**
- **Text:** count the words in the slides' text layer, without repeated footer and header lines. One tested way for a PDF: `pdftotext -layout`, then drop footer lines, then count with the regex `[A-Za-z0-9][A-Za-z0-9'’\-\.]*`.
- **Figures and tables:** count the words inside them, which the text layer misses. Use OCR (`tesseract page.png - --psm 11`) on the figure and table pages, minus those pages' text-layer words, or count by hand.
- **Record it** in the deck as `<!-- BUDGET original=<text+figures> (text <a> + figures/tables <b>) -->`. The ceiling is not written down: it is always 2 × `original` (or the §11 setting's multiple), and `plain_check.py` computes it. In this file, "counts toward the budget" means: counts toward the deck's words, which are measured against the ceiling.
- *Why:* the student compares the deck with everything they would otherwise read, including the words in pictures and tables. The ch1 deck: text 1,864 + figures/tables about 295 = about 2,160, so its ceiling would be about 4,320 words.

**W2 — Build the content inventory and the fact ledger (F1).**
- Split every bullet into single facts, keeping their qualifiers, and give each an ID `p<page>.<n>`. Mark the facts that define a term (`def`) and the lists a review question asks (`list`): F2 quotes them exactly.
- Give every content unit its **teaching job** from the skill's `use-cases.md`. Use each job's "Spot it when" lines as the classifier. One source slide often holds several units with different jobs (a definition, a figure, a warning).

  `state-thesis · orient · predict-first · define-term · label-parts · highlight-passage · explain-mechanism · follow-procedure · show-transformation · build-intuition · compare-options · show-quantity · correct-misconception · tell-story · walk-code · demo-interface · list-parallel · recap · check-recall`

- Two extra tags:
  - `admin` = course logistics (dates, grading, office hours);
  - `exam` = an explicit exam hint ("this will be on the exam"), added next to the unit's job.
- Also list the **implicit prerequisites**: words, symbols and ideas the slides use without teaching them.
- Also list **agenda items with no content slides**. These go to W5.

**W2b — Research every load-bearing concept (required, scoped).**
1. **Correctness.**
   - Check each claim, definition and formula against the slides' own source first: the textbook, or the publisher's official slide set when the slides are adapted from one.
   - Then check against one other reliable source: a university course page, official documentation or a standard.
   - Search the web for a claim only when it looks wrong, out of date or unclear. Use 1–2 searches per doubt. Disagreement with the slides → F4.
2. **Best explanation.** How strong teachers and textbooks explain the concept, and which visual they use. Build your own version; never copy text or images.
3. **Misconceptions** for the 3–5 heaviest concepts *(target)*. These feed Concept Pattern step 7 and the question-set distractors. Forums are acceptable here only.
4. **Examples.** Concrete cases and real applications (steps 2 and 6).
5. **Currency.** For fast-moving topics (tools, versions, standards, sizes, prices), check whether the slides are out of date. If so → F4 note.

Record the sources in an HTML comment at the end of the deck, next to the fact ledger:

```html
<!-- SOURCES
fidelity: publisher's official slides ch.1 <URL>
DRAM vs SRAM (F4): <URL>; <URL>
misconceptions: <URL> (students think one CPU runs all programs at the same moment)
-->
```

**W3 — Order the concepts for learning.**
- Use the order that teaches best: prerequisites first, concrete before abstract, simple before complex, and the "why" before the details. This is often the slides' order, but not always.
- Record every move in the fact ledger, so a student can still find any lecture slide's content.

**W4 — Plan the deck.**
- **Topics (N1).** Group the concepts into topics that a student would revise as a unit. Aim for **3 or more slides per topic** *(target)*, never 1.
  - The arc slides form a "Start" topic (cover, challenge, map) and a "Review" topic (revisited challenge, recap, glossary). The final quiz is its own last topic, "Final quiz".
  - The map slide names the same topics as the topic bar.
- **Slides.** No slide-count target: size is measured in words. One idea per slide (TE1), each slide within V5's word range; a concept that needs more words takes more slides, never a denser slide. Admin, agenda and divider slides need no slide of their own; they become the map slide and the topic bar.
- **Words.**
  - `ceiling = original words (W1b) × 2`. This limit is never passed (G5, precedence 3).
  - Plan to **about 1.8 × or less** *(target)*, so the fixes that the checks bring (F1b, Q4) still fit under the ceiling.
  - Spend the room in the order of §1, "Where the extra words go". The ceiling is a limit, not a goal: a deck that is easy to digest at 1.3 × stays at 1.3 ×.
  - The arc costs about 250 words (the glossary is most of it: about 4–5 words per entry). The quiz is outside the word count.
- **Per slide, write down:** its job, its component, its word cap (within V5), the source units it covers, and its phone shape (M2–M4) when it differs from the laptop shape. The sum of the caps plus the arc is the planned total.
- **If the plan passes the ceiling, fix it in this order:**
  1. Move facts into figures (V13).
  2. Say things once (L11), and merge slides that teach the same idea.
  3. Cut the deck's own additions from the bottom of §1's list up: first second examples and analogies, then the common-mistake lines that aren't required, then background lines that a glossary entry can carry. Keep every concept's first example and every required worked example as long as anything else can go.
  4. Never cut or weaken a fact or its exact wording (precedence 2). If the facts and their exact wording alone pass the ceiling, stop and ask the user (W5). Never deliver a deck over the ceiling.
- **Write a draft opening challenge** (TE3).

**W5 — Confirm only what needs a decision.** Send **one** message, and only if at least one of these applies:
- the canvas gate and the English level, at the first deck of a course (case A, §0), **always**, in the skill's shape. When they are the only questions, ask them alone, and build nothing until the user answers;
- the exam focus, once per course, if not given: "Does your exam stress anything in particular? (You can skip this.)";
- a slide error that changes what would be taught (F4), when the right handling is unclear;
- agenda topics with no content slides: skip them, or add them as "Extra: not in your slides"?
- a setting (§11) the slides make relevant. Example: the first lecture with code or numeric tables raises "what counts toward the budget";
- the facts and their exact wording alone would pass the word ceiling (G5), so the deck cannot be complete under it. Say by how much, and ask how to go on. Count before asking: the deck's own additions (examples, analogies, background, the arc's extra lines) are cut first (W4), and they are usually what pushes a deck over.

Never ask what the COURSE record already answers.

Otherwise, don't stop: build the deck, and put the plan's essentials (topics, slide count, words against the ceiling) in the delivery report. At a first deck, the canvas gate and the level always stop the run once.

**W6 — Write the term sheet.** For every term:
- the plain meaning (≤ 12 words, in the simplest words that say it: A2 words in A2 and B1 courses);
- one everyday comparison, if a good one exists (T10);
- the exact formal wording or notation from the slides;
- the forms that appear (plural, verb).

The term sheet feeds the visible definitions (T3), the deck glossary (T5b) and the "Words in this deck" slide (TE8). Use the **same gloss text** for a term everywhere, and across the lectures of a course: copy it from the earlier decks' glossary when the term comes back.

**W7 — Draft every concept** with the Concept Pattern in its deck form (§6), in plain language (§4), with independence (§5). Count words after the first draft, not at the end (Q6).

**W8 — Build** the deck with the skill (engine v2, canvas and board, bridge tokens). Start from the shell when there is one (case B, §0); otherwise from the skill's template. Then:
- For each slide, take its job and choose a component from that job's reverse index in `use-cases.md`; vary components across the deck.
- Write each slide's new CSS phone first (M1), and check the phone view as you go, not only at the end.
- Add the topic bar (N1), the glossary (T5b) and the phone layer (M1–M8), all from `deck-tools/snippets/` (Appendix B says where each goes).
- Add the final quiz as the last topic, following `questions-rulebook.md`.
- Add the `FACT-LEDGER`, `INDEPENDENT-CHECK`, `SOURCES`, `BUDGET` and `COURSE` comments (F1, F1b, W2b, W1b, §0).

**W9 — Check** (§9): `validate.py`, `plain_check.py`, fact ledger, word ceiling and digestibility, cold read, visual check (phone first), checklist. Fix and re-run until clean, or until every remaining flag has a written reason.
- **After every trimming pass, re-check the ledger** against the trimmed text: trimming is where facts get weakened ("generally", "may", "highly technical" were lost this way).
- **Then the independent check (F1b),** last, on the finished deck including its quiz. Fix what it reports and send it the new text, until a pass reports nothing.

**W10 — Deliver** with the short report (§10).

**W11 — Update the COURSE record: merge, don't append.** The record is the course's memory: the next deck reads it first, and no notes file travels between runs.
- **Into the record** (facts about this course only): new decisions and settings, field words (L1), the lecturer's slide habits that change how to read the next lecture, figures a later lecture can reuse (deck · slide · what), and what the next lecture covers when the slides say. Replace what this deck proved wrong; drop details that only this deck needed.
- **Keep it short:** about 15 lines *(target)*, one line per item.
- **Lessons for every course** (a better method, a pitfall, a rule worth adding, a tool fix): don't write them into any file. List them on the report's "Proposed for the skill" line (§10). The user brings them to a maintenance session, where the rulebooks, the general notes and `deck-tools` change. Send nothing back with the deck but the deck.

---

## 4. Language rules (G2)

**L1 — Words.**
- Use the most common word that says it. A word at the course's level is fine when no simpler word says the same thing (at A2: A1–A2 words only).
- A word above the course's level is either a course term (teach it, §5), a field word, or it gets replaced (L5).
- **Field words** are the general computing words a student of the subject already owns (data, hardware, file, database, byte, network, server, laptop …). They count as known. `plain_check.py` has a built-in list; extend it per course with `--known words.txt`. A field word is not a course term: if the lecture *teaches* it, it is a term (§5).
  - **New field words.** When the checker flags a word, add it to the course's field words only if all three hold:
    1. the lecture uses it without teaching it;
    2. a first-year student of the subject knows it from everyday use (*folder*, *smartphone*, *pixel*);
    3. the exam could not ask what it means.
  - **When in doubt, it is a term.** Define it (§5). Never add a word to the field list just to pass the checker.
  - **Where they go:** the COURSE record's `field words:` line (§0), so every later deck of the course inherits them. They are never removed from the deck; the list only changes what the checker flags.
  - **Report** every word added (§10), so the user can veto it.
  - A word that would help every course in the subject may be suggested for the built-in list in `deck-tools/plain_check.py` (Appendix A). Only the user edits the rulebooks and their tools.
- Target: **at least 98% of running words known**, about one unknown word in fifty. A course term counts as known on slides where it is defined, glossed, or in the deck glossary (T5b).

*Why:* readers need about 95% known words for minimal comprehension and about 98% for adequate comprehension. Going from 95% to 98% more than halves the unknown words the reader meets [HN]. The general word list rates field words such as *data* as B2. Without the allowlist, the target would push every course to re-teach its own field vocabulary.

**L2 — Sentences.** One idea per sentence, within **the level's cap** (SKILL.md step 2b): 15 words at A2, **20 at B1**, 25 at B2, 30 at C1. Aim for the level's usual range *(target)*. Split long sentences instead of chaining them with "which", "that", "and", semicolons or colons. Splitting at a period costs no words.

*Why:* Simplified Technical English, a standard written for second-language readers of technical manuals, caps procedures at 20 words and descriptions at 25 [STE]: the B1 and B2 caps. The A2 and C1 caps are design choices.

**L3 — Grammar.**
- Present simple tense where possible.
- Active voice: "The router reads the address", not "The address is read by the router". Use passive only when the actor truly does not matter.
- Talk to the reader with "you" and "we" [M].
- Positive statements. No double negatives. Use "not" only when no positive form exists.
- No idioms (*in a nutshell → in short*). No phrasal verbs at A2–B1 (*set up → create*, *figure out → find*, *carry out → do*); from B2, common ones are fine where they are the clearest way to say it.
- No noun stacks longer than 3 words: *"packet header length field" → "the length field in the packet header"* [STE].
- Do not drop small words ("the", "a", "that") to save space. Telegraphic text is harder for second-language readers [STE]. The word ceiling (G5) leaves room for full sentences; save words with L11 and V13 instead.

**L4 — One concept, one word.** Pick one word for each concept and never switch to a synonym: "router" stays "router", never "the device", "the node" or "the box". Repeat the noun instead of "it / this / they" when the thing was named more than one sentence earlier.

*Why:* for second-language readers, repeating key content words makes text easier to process; a synonym looks like a new thing [CO][STE].

**L5 — Replace formal words.** Use the right column (at C1 it is advice: keep a formal word when it is the precise one). **Exception:** if the course uses the word as a technical term (for example *implement* in programming, *yield* in Python, *allocate* in operating systems), it is a term: teach it (§5), do not replace it.

| Instead of | Write |
|---|---|
| utilize, employ | use |
| facilitate | help, make easier |
| obtain, acquire | get |
| require | need |
| sufficient | enough |
| approximately | about |
| subsequent, subsequently | next, then, later |
| prior to | before |
| in order to | to |
| therefore, thus, hence | so |
| however | but |
| whereas | but, while |
| regarding, with respect to | about |
| determine | find, decide, work out the value of |
| consist of, comprise | is made of, has |
| demonstrate, indicate | show |
| initial | first |
| terminate | stop, end |
| commence, initiate | start |
| component | part |
| numerous | many |
| additional | more, extra |
| modify | change |
| eliminate | remove |
| perform | do |
| corresponding | matching |
| arbitrary | any |
| denote | stand for, mean |
| mechanism | way, tool |
| halt | stop |
| respectively | (split into two sentences) |
| the former / the latter | (repeat the noun) |
| via | through, by, using |
| e.g. | for example |
| i.e. | this means |
| etc. | and more (or list them all) |

**L6 — Numbers, symbols, units.**
- Write numbers as digits.
- Write a unit in full the first time it appears in each topic: "5 ms (milliseconds)". On later slides, the glossary (T5b) carries it.
- Read every symbol in words the first time it appears on each slide: "x² (x squared, which means x × x)".

**L7 — Headings.** Sentence case, plain words, **2–5 words** *(target)*. A statement or a question: "Why every packet needs an address".

**L8 — Abbreviations.** Every acronym is a term (T9). No Latin abbreviations (e.g., i.e., etc., vs., cf.).

**L9 — Questions and feedback follow L1–L8 too.**

*Why:* hard wording in a question tests English instead of the concept. Simplifying the wording of test items helps second-language readers without changing what the item measures. The effect is real but small, so treat this as hygiene, not magic [A].

**L10 — Keep the meaning exact.** A rewording keeps the claim at the same strength. These are the words that get lost; each one must survive:
- **Qualifiers:** generally, usually, often, some, most, many, nearly, increasingly, at least, at most, only, always, serious, highly.
- **Modality:** *may, might, can, could* never become *is*; *should, needs to, must, have to* never become plain statements or "think about".
- **Paired claims:** *not only … but also* never becomes *or*; *A and B* never loses B.
- **Scope:** "a specific organization" never widens to "anyone"; "include, such as" (an open list) never becomes a closed list or a ranking.
- **Attribution:** "attempts to X" never becomes "X happened".

The rest of this rule:
- Plain words must not change the claim.
- Words like *usually, typically, always, only, at most, at least* must survive simplification.
- When the plain version loses precision, keep the original sentence in a **Formal version** box (F2) and explain it in plain words next to it.

**L11 — Say it once, in its best place.** These cut words without cutting content or ease, so the room under the ceiling goes to explanations and examples (G5):
- A fact that names or describes a part goes on the figure, next to that part (V13), not in a sentence that repeats the label.
- Don't restate in prose what the figure already shows. The caption says what to *notice*.
- Number steps only in real procedures. Digits count as words; elsewhere use plain bullets.
- Tags and eyebrows only on topic-opening slides ("Part 2").
- One version of a definition, not a formal and a plain one, unless F2 requires both.
- Quiz feedback: short (the final quiz's own limit, `questions-rulebook.md` QW5). When a deck has the skill's answer box (§11), it refers to questions by number instead of repeating them.
- Don't gloss a term the slide's figure already explains.

*Why:* words that don't serve the learning goal lower learning (coherence), and words placed next to the parts they describe save search effort (spatial contiguity) [M]. Both make a slide easier to digest, and both keep the deck under its ceiling.

---

## 5. Terms and independence (G3)

**T1 — Idea first, name second.** First explain the idea in everyday words on a concrete example. Then attach the name: "This is called a `<dfn>packet</dfn>`." Never open a slide with a term the slide has not explained, unless the glossary (T5b) carries it.

*Why:* in a randomized study, students who met concepts in everyday language before the scientific terms understood more, and used the terms better, than students who got the terms first. The study was small (49 fifth-graders), but it agrees with the pre-training principle [CFA][M].

**T2 — Teach every course term the slides use.** Exams use these terms, so the student must own them. Leave a term out only if the slides never use it.

**T3 — Definition (the defining slide).** For each term, on the slide that teaches it:
1. the plain meaning in ≤ 12 words (from the term sheet);
2. a picture or diagram (often the slide's main figure);
3. one everyday comparison, if a good one exists (T10);
4. a **Formal version** with the exact course wording or notation, only when F2 requires it.

Mark the defining use with `<dfn>`. Add `data-forms` for irregular forms: `<dfn data-forms="matrices">matrix</dfn>`.

**T4 — New-term load.** At most **2 new terms per slide** *(target)*, 3 as a hard limit. At most **4 new terms before the next check question or topic boundary**.

*Why:* working memory holds about 3–5 new chunks at a time, and each new term is one chunk [WM].

**T5 — Every term is explained where it is used.** Which form depends on where the term is used and how much the slide leans on it:

| Where the term is used | How |
|---|---|
| Its defining slide | **Visible** definition (T1, T3). Never hidden. |
| Its **first use in another topic**, when that slide's main sentence makes no sense without it (**load-bearing**) | A **visible** short gloss, inline and ≤ 6 words: `the kernel <span class="gloss" data-for="kernel">(the one program always running)</span>` |
| Anywhere else | The **deck glossary card** (T5b), added automatically at the term's first use on each slide. Or a hand-made anchored gloss (components §24) for a supporting term that isn't in the glossary. |

When a deck uses on-demand glosses, the cover's hint line says so: "Tap dotted words for their meaning."

*Why:* students revise by topic: they jump in with the topic bar (N1). So a topic must stand alone, and a load-bearing term needs its meaning visible where a topic starts using it. On-demand glosses work for second-language readers: in a meta-analysis they had a medium effect on reading comprehension and a large effect on word learning [GL2]. But optional content is often never opened, so the main sentence where a topic starts using a term must not depend on one. Re-glossing every term visibly on every slide costs about 5 words per term per slide, and it fills slides with repeats the reader already knows (L11). The glossary gives every slide the meaning at about one word of cost per term, and leaves the room under the word ceiling (G5) for explanations and examples.

**T5b — The deck glossary.**
- The term sheet's cross-topic terms and every acronym go on one slide, **"Words in this deck"**, as `<dl id="glossary" class="glossary">`:

  ```html
  <dt data-forms="interrupts">interrupt</dt><dd>a signal that calls the CPU</dd>
  ```

- A small script (Appendix B) turns the first use of each glossary term on every other slide into an anchored gloss card. It skips headings, figure labels, buttons, `<dfn>` and formal text, and it skips the term's own defining slide.
- The definitions exist once, on a visible slide, so they count once toward the budget.
- The glossary slide doubles as the revision sheet (TE8).
- `plain_check.py` reads the glossary and treats its terms as glossed on every slide.
- Keep each entry ≤ 10 words, in the term sheet's wording (W6). Acronym entries give the full form first: "DMA — direct memory access: …".

**T6 — No back-references.** Never write "as we saw", "recall that", "remember that", "the previous slide", "mentioned above", "see slide 4" or "discussed earlier". Restate the needed fact in one short sentence, or rely on the glossary card. *Exception:* the challenge-revisited slide may say "your first answer", but it must restate the full problem.

**T7 — Every topic stands alone.** Never write "see Part 1" or "as in Storage". In series mode (§11), every deck also stands alone: re-teach terms in each deck.

**T8 — "What you need first."** For knowledge the slides assume but never teach:
- When one line is enough, put it in the glossary.
- When the lecture leans on the prerequisite across several topics, teach only the pieces it uses, on a "Background" slide in the Start topic (the skill's "Ground the newcomer" slide).

*Why:* knowing the names and basic meaning of the key parts before the main explanation frees attention for how the parts work together (pre-training) [M].

**T9 — Acronyms are terms.**
- At the first use in each topic, write the full form and the plain meaning, then the short form: "Internet Protocol (IP): the rules for addressing computers".
- On other slides, the glossary card carries it.
- Every acronym the deck uses goes in the glossary.

**T10 — Analogies: map them and say where they stop.**
1. Name the familiar thing.
2. Show which part matches which (a two-column table or a labelled picture).
3. Say where the comparison stops working ("Unlike a post office, a router keeps no copy of the letter").
4. Return to the real concept.

Use one analogy per concept and keep it the same through the deck. Choose comparisons any university student knows anywhere: a phone, a map, a queue, a delivery, a timetable, a recipe. Avoid comparisons that need a specific culture, sport or idiom. Use an analogy where it carries a concept that the figure alone does not, or where students often find the concept hard. It is paid from the room under the word ceiling, after the concept's own example (G5, "Where the extra words go", item 6).

*Why:* analogies help, but an unmapped analogy can plant a misconception, and the "where it breaks" step is the one most often skipped [TWA].

---

## 6. Teaching rules (G4)

### The Concept Pattern

Use this for every **load-bearing concept** (anything a student could be asked about), in this order. It is the skill's click trio (structure · mechanism · application) with research-backed steps added. Each step names its teaching job in the skill's vocabulary, so the component comes from that job's reverse index in `use-cases.md`.

The **deck form** column shows how each step appears in a deck under G5: steps may share a slide, no slide passes V5's word range, and a typical concept takes **1–3 slides** *(target)*, more for a long procedure.

| # | Step | What to write | Deck form | Why |
|---|---|---|---|---|
| 1 | **Ask** *(optional)* · `predict-first` | A one-line prediction question before teaching | Usually the deck's opening challenge covers it; add more only for a counter-intuitive concept | Trying to answer before learning improves later learning, even when the guess is wrong, as long as teaching or feedback follows [PT] |
| 2 | **Plain idea + one concrete case** · `define-term` or `build-intuition` | The idea in everyday words, shown on one specific example | **Required** for every load-bearing concept (G5): 1–3 plain sentences next to the figure that shows the case | Content first [CFA]; concrete before general [CF] |
| 3 | **Name it** · `define-term` | `<dfn>` + definition (T3) | The `<dfn>` sits in the step-2 sentence | T1 |
| 4 | **Picture** · `label-parts`, `explain-mechanism` or `compare-options` | The visual chosen by V7, with labels next to the parts (V2), colour links to the text and a "Notice:" caption (V8). For a process, a step-through (V9) | **Required.** The picture carries the facts (V13) | Words + pictures beat words alone; labels close to the parts and text–picture signals save search effort [M][SIG] |
| 5 | **Why it works** · `explain-mechanism` | The mechanism | 1–2 sentences, or one caption per build step | The skill's click trio |
| 6 | **Worked example** · `follow-procedure`, `walk-code` or `show-transformation` | Step by step, each step with a short label ("Step 2: find the column"). Then a similar problem for the student | **Required** for procedures, calculations and code; usually its own slide. Numbers go in a table, not in prose | Novices learn more from studying solved examples than from solving alone; step labels help them see the reusable steps [WE][SG] |
| 7 | **Common mistake** · `correct-misconception` | "Many students think X. This is not true, because Y. The correct idea is Z." | **Required** where a known misconception exists: one or two sentences, or the eraser on the revisited challenge | Texts that name and refute a misconception correct it better than plain explanation. Some learners drift back later, so re-test it (TE7) [RT] |
| 8 | **Check** · `check-recall` | One quick question with feedback that explains why each wrong option is wrong | In the final quiz (`questions-rulebook.md`); or at the topic's end when mid-deck checks are on (§11) | Practice testing with feedback is one of the two highest-utility study techniques [D][R] |

For a pure definition, steps 2–5 (and 8 in the final quiz) are enough.

### Teaching rules

**TE1 — Small steps.** One idea per slide. Split any slide that teaches two unrelated things; merge two slides that teach one idea [R][M].

**TE2 — Concrete, then general.** Start with a specific example, then the general rule, then the formal notation, saying in words what each symbol stands for.

*Caveat:* the evidence is strongest in mathematics; a review argues it does not fit every domain. For a pure definition, a direct definition plus an example is fine [CF].

**TE3 — The opening challenge** (skill arc, step 2) must:
- be answerable from **everyday knowledge** (no course terms);
- be written one level below the course's (A2 for A2 and B1 courses);
- ask for a **committed answer** (a tappable MCQ);
- be "attemptable but uncertain", as the skill says;
- ideally touch **several topics** of the lecture, so that the revisited challenge pulls them together.

*Why:* guessing before teaching helps [PT]. Full problem-solving-first works best when learners have enough prior knowledge to try, and a self-paced deck cannot rescue a hopeless attempt [PF]. So the challenge must be attemptable with what a newcomer already knows.

**TE4 — Mid-deck checks.** A setting (§11).
- **Off (default):** retrieval comes from the opening challenge, the revisited challenge and the final quiz.
- **On:** one question at the end of each topic, marked `data-budget="skip"` so it doesn't count toward the budget.
- Core checks should be answerable by most careful readers (about 80% *(target)*); save hard items for `[stretch]` [R].

*Why the default is off:* the final quiz already gives the deck its retrieval practice, and a check every 2–3 slides adds reading time and slides between the ideas. Retrieval practice is still one of the highest-utility techniques [D], which is why the setting exists. When it is on, the checks stay outside the word count (`data-budget="skip"`), like the final quiz.

**TE5 — "Why…?" prompt.** With the final quiz (the default), the deck has no answer box, so this is optional: when space allows, add one in the deck, a text box and a model answer the student reveals after typing, using one of the skill's legal depth mechanics (outside the budget, `data-budget="skip"`). When the answer box is on (§11), put one open "Why…?" question in it.

*Why:* prompting learners to explain why something works has a medium effect, and question-form prompts work better than multiple-choice prompts [SE].

**TE6 — Fade support across a course.** Early lectures: fully worked examples. Later lectures on the same skill: partly worked examples, then full problems.

*Why:* worked examples help novices but become redundant as expertise grows (the expertise reversal effect) [WE].

**TE7 — Question items.** The final quiz (`questions-rulebook.md`) replaces the skill's end-of-deck question set by default; its items follow the rules below too. The skill's question set (3–5 items *(target)*) comes back only when the user turns it on (§11). Each item:
- has a stem that is a full question, worded positively: no NOT / EXCEPT, no "all of the above", no "none of the above", no double negatives;
- has 3–4 options of similar length and grammar, and one clearly best answer;
- uses wrong options taken from real student mistakes (the step-7 mistakes);
- stands alone: it restates any fact it needs and never depends on another item;
- follows the language rules (L9);
- has short feedback (4–8 words, L11) that says why.

- tests the **lecture**, never the deck's own pictures or framing (F3b): a label-the-figure item on an "our picture" figure tests the deck, not the exam;
- has feedback that states slide facts at full strength (L10), in the slides' terms;
- keeps the slides' wording in its options when they quote a fact ("persistence", not a gloss of it).

Across the set:
- at least half the items ask the student to **apply or explain**, not only recall;
- the deck's main misconception is re-tested (the revisited challenge counts);
- keep the skill's 1–2 `[stretch]` items;
- when the answer box is on (§11), it lists the questions by number, plus one open "Why…?" question (TE5) [MCQ][A].

**TE8 — Recap and revision sheet.**
- Keep the skill's "you can now …" capabilities slide, with a one-line closing ("Next: …").
- The **glossary slide "Words in this deck"** (T5b) is the revision sheet.

**TE9 — Series review** (series mode only). A deck after the first may put 1–2 retrieval questions about the earlier deck on its first slides. Each question must be self-contained (it restates the facts it needs), and its feedback re-teaches the idea in one line.

*Why:* spaced retrieval is one of the highest-utility techniques [D]; self-contained wording keeps T7.

**TE10 — Examples.** Correct, specific, and close to students' daily lives. No jokes, puns or fun facts that do not serve the concept (V1).

---

## 7. Fidelity and completeness (G1)

**F1 — Fact ledger (required).** One line per single fact of the slides (W2), with its kind, the deck slide that teaches it and its status:
- `exact`: the slide's own words, quoted (F2);
- `faithful`: plain rewording, same claim at the same strength (L10);
- `weakened` or `missing`: not allowed at delivery.

Admin pages and agenda items without slides are listed as skipped. Put the ledger at the end of the deck as an HTML comment (`validate.py` strips comments):

```html
<!-- FACT-LEDGER
source: "ch2.pdf" (30 pages) · deck: 23 teaching slides + 10 quiz slides
admin (skipped): p1, p11, p21 titles · p2 topics · p3 objectives · p10 "End of" pages
p4.3 fact viruses and worms are generally non-discriminating threats -> 5 faithful ("generally")
p5.2 def  hacking also applies to exceeding one's authority          -> 5 exact
p15  list four goals (review question p19)                          -> 10 exact; quiz 4, 9
our framing (labelled): s15 map of where each domain works
background, not in the slides: glossary entries virus, worm …
totals: 82 lines · weakened 0 · missing 0
-->
```

- Ledger the qualifiers with the fact ("generally", "may"): they are what a rewrite loses.
- Moved facts keep their page ID, so a student can still find any page's content.
- *Why a ledger and not a map of slides:* a map that says "page 5 → deck slide 5" stays true after a trim removes half of page 5. A fact line does not.

**F1b — Independent check (required).** The author's own ledger misses what the author misread. Before delivery:
1. Dump the deck's slide text as a student reads it (`deck-tools/slide_text.py`: labels, glossary and quiz feedback included; HTML comments, and so the ledger, left out). Quotes show as «…», the deck's framing as [ours: …].
2. Give a separate agent, one that did not build the deck, only the PDF's text and that dump, with the brief in `deck-tools/checker-brief.txt` (Appendix C). It builds its own fact list and reports: missing, weakened, contradicted, misquoted, not exact (a definition or review list not quoted), unlabelled claims, quiz items with a wrong or arguable key or unsourced feedback.
3. Fix every finding, or write down why it stands. Send the new dump back for another pass. Stop when a pass reports nothing.
4. Record the passes in an `<!-- INDEPENDENT-CHECK -->` comment (counts per pass, final verdict), and in the report's "Standalone" line.

*Why:* on the 210 ISY deck 2 the author's ledger showed 0 weakened facts; the first independent pass found 13 weakened, 2 contradicted and 9 quiz problems. Three passes closed them all.

**F2 — Keep the exam-facing form exactly.**
- Formulas, notation, code, names of algorithms and laws, numbered procedures, and the instructor's definitions are copied exactly.
- **Quote every definition (default since 1.7, §11).** Every sentence that says what a term *is, means, applies to, involves, includes, encompasses, ensures* or *covers*, and every list a review question asks (its item names and their order), appears word for word in quote marks with `class="formal"`. The slides' slips stay inside the quote; only spacing and hyphen typos may be fixed (list them).
- **Beside each quote, its plain reading**: short "word: meaning" glosses for its hard words ("Underway: in progress. Mechanisms: tools."). The glossary script skips `.formal`, so a hard word inside a quote gets no card: the gloss line is its only help.
- Don't repeat a quoted fact in a plain sentence; the gloss line carries what the quote needs.
- The cover's hint line says it once: "“Quoted” lines are your slides' exact words."
- **When the slide's wording is already plain enough**, use it once, as is, with `<dfn>`: one version, no box.
- **When the plain wording would differ from what the exam expects**, show the exact wording in a **Formal version** box (`class="formal"`) and explain it in plain words beside it, with a short "How to read it" line.

```html
<div class="aside formal"><b>Formal version:</b> Packet switching: data is segmented
into packets which are independently routed through the network and reassembled at
the destination.</div>
<p>How to read it: <span class="formal">segmented</span> = cut into pieces.
<span class="formal">Routed</span> = sent along a path.
<span class="formal">Reassembled</span> = put back together.</p>
```

- This is the skill's `highlight-passage` job. In Sketchbook decks, the ink marks (§28) can circle and underline the load-bearing words of the formal sentence in order.
- Prefer the "How to read it" line to §24 cards on formal words: the checker reads the line but skips everything inside `.formal`.
- Do not rename the instructor's terms, even when another name is more common. You may add "also called …".

**F3 — Do not grow the syllabus.** Add only what the student needs to understand the slides (background, T8). Anything useful but not in the slides is labelled **"Extra: not in your slides"** and goes in the depth layer.

**F3b — Label the deck's own framing.** A picture, timeline, grouping, map or summary line that states a relation the slides don't (when something acts, where it sits, what causes what, which items belong together) carries a visible label on the picture itself: `<span class="ours">our picture</span>`.
- **Don't use a framing that can contradict a slide fact,** labelled or not. A before / during / after timeline of four goals put one goal "after" when the slides say its first form *stops* the attack.
- **"Notice:" lines** state only what follows from slide facts, at their strength ("Attacks cannot always be prevented. Then detection is most useful, and containment is needed.", not "detection is needed because…").
- Examples (an alert, a fingerprint reader) and glosses need no label, but the independent check lists them so you can confirm they don't mislead.

**F4 — Errors and doubts in the slides.**
- Do not silently change the slide's content. Teach the slide's version and add a visible note: "Note: many sources say X. Ask your instructor which one your exam uses."
- List every note in the report.
- Before writing any claim you are unsure about, verify it (W2b).
- Typos and wrong abbreviations ("i.e." meant as "for example") can be fixed silently, and are listed in the report.

**F5 — Figures.**
- Rebuild every figure, table and chart from the slides with the skill's components, or give its full information in the deck.
- If the original is cluttered, unclear or decorative, design a clearer one that carries the same information (§8).
- Never write "see the figure in your slides".

**F6 — Hidden content counts.** Speaker notes, slide titles, footnotes and highlighted words are content. Inventory them.

**F7 — Code.**
- Copy it exactly (same names, language and style).
- Explain each block with a step label and plain-English comments.
- When values change over time (loops, assignments, recursion), add a **trace table** showing every variable after each step.

**F8 — Math.**
- Show the formula exactly (Formal version). Add a "How to read it" line in words.
- Give a symbol table:

  | Symbol | Read as | Meaning | Unit |
  |---|---|---|---|

- Then a worked numeric example (Concept Pattern step 6), with its numbers in a table rather than in prose.

**F9 — "Trim" means emphasis, never deletion.**
- The skill's catalogue often advises showing less at once: "three load-bearing rows" of an eight-row comparison, "the range that matters" of a long code listing, "pick one claim" for a thesis slide, at most six labels on a figure. Follow that advice for **what comes first and largest**.
- Everything else the slides contain is still taught on the visible layer: in further builds (§25), in a second pane, or in a table.
- Never move examinable content into hover/tap depth, and never drop it. The word ceiling (G5) never overrides this: when only cutting content would keep the deck under it, stop and ask (W5).
- Record where each part went in the fact ledger.

---

## 8. Visual and layout rules (adds to the skill's style system)

**V1 — Every image explains.** Each illustration, icon scene or animation shows the concept or its example, never only a mood. When the skill's scene-brief procedure invents a "skin", the skin must be the concept's own example.

*Why:* interesting but irrelevant extras lower learning, and they hurt novices most, especially when the learner controls the pace, which is exactly a self-paced deck [SD][M].

**V2 — Labels next to the parts.**
- Words sit on or right beside the part of the picture they name (spatial contiguity): the skill's labels on the figure (§22), not a numbered legend.
- Every part name must be readable without opening anything. Past about six new labels, split the figure into builds (§25) or slides so that each step adds six or fewer; never hide names in a tray.
- When labels arrive with builds, put `data-build` on a wrapper layer that holds the labels, never on a label itself. The build style resets the label's position transform.
- One SVG path per arrow: a path with several subpaths gets an arrowhead only at its last end [M].

**V3 — Signalling.** One consistent look for defined terms and one for the key sentence of each slide. Add this CSS to the deck's style block (never to the engine). It reads the skill's bridge tokens (`style-system.md §7`), so paste the chosen family's bridge-token row into `:root`:

```css
dfn { font-style: normal; font-weight: 700; color: var(--k-ink);
      background: var(--k-hi); border-radius: 3px; padding: 0 .12em; }
.gloss { color: var(--k-soft); }
.formal { font-style: italic; color: var(--ink); }
.ours { display:inline-block; font-family:var(--font-body); font-style:normal; font-weight:700; font-size:.72rem;
        letter-spacing:.04em; color:var(--pencil); border:1.2px dashed var(--pencil); border-radius:999px;
        padding:0 9px; vertical-align:middle; }   /* F3b: the deck's own framing */
```

Keep the linked colours `--k-a`, `--k-b`, `--k-c` for linked figures (V8), not for terms, so a colour always means "this word = that part".

**V4 — Readable text blocks.** Lines no longer than about 70–80 characters, line height at least 1.5, left-aligned (never justified), sentence case [W].

**V5 — Visible words per slide.**
- About **50–70** *(target)*, averaging about 60; soft cap 110 (the checker's default).
- This range keeps each slide one small chunk, which is part of being easy to digest (G5). The room under the word ceiling is spent across more slides, never by packing more words onto one.
- More than that → move facts into the figure (V13), then split.
- A slide that reproduces a source table may exceed the cap. Note it in the report; don't split the table.

*Why:* second-language readers read English much more slowly than the native average of about 238 words per minute (one study measured about 128 for non-native readers), and the skill budgets 60–90 seconds per slide, which must also cover the picture [RS].

**V6 — Colour is never the only signal.** Pair it with a label, shape, position or fill pattern.

**V7 — Choose the visual by the teaching job.**
- Each slide's job (W2) points to its components in `use-cases.md`. Pick from the top of that list unless the content argues for another, and vary components across the deck.
- Two jobs the catalogue leaves to you:
  - code that changes values → a trace table (F7);
  - how several concepts relate → a map with labelled links (V10).
- **Use a component only when it does a job text cannot.** Builds for an order of events; the magic board when the *same* items move; a draggable number or lab only when a variable really varies, and with a resting state that shows the answer (V12). A component that only decorates is a V1 violation.
- A good visual replaces descriptive sentences (where things are, what connects to what, what comes next). It does not replace the "why" sentence or the labels.

*Why:* words and pictures together beat words alone, but pictures alone are not the proven condition; novices still need the words [M].

**V8 — Link the words to the picture.**
- Use the skill's linked figure (§23): each key term has the same colour in the sentence and on its part of the diagram, and touching either lights both.
- At most three linked colours; past that, use labels (§22). Words still name every part (V6).
- Use it only where one sentence names 2–3 parts of one picture.
- Add a one-line caption that says what to notice: "Notice: each packet takes its own road."

*Why:* signals that connect text and picture improve comprehension, and they help learners with low prior knowledge most, which is exactly our readers [SIG].

**V9 — Processes are step-throughs, not autoplay.**
- Show a changing process one step per key press with the skill's builds (§25): 3–5 builds per slide, each caption arriving with its strokes, one short sentence per step.
- Captions **accumulate**: each step stays visible, so the finished slide is a complete revision view.
- Use the steppable figure (§32a) when the figure needs its own buttons.
- When the same pieces move from one state to another (memory blocks, a sorted list, algebra, refactored code), use the magic board (§26) so the student sees *what* moved. Its states can follow the builds.
- In Sketchbook decks, the eraser (§29) shows a misconception being replaced; the better idea always comes last.
- Motion is used only when the change itself is what the student must learn, and always under the student's control. The skill's entrance reveals are style and are fine.

*Why:* animations beat static pictures only modestly overall, mainly when the change itself must be learned, while autoplay is transient and cannot be re-read. Learner-paced segments fix both [AN][M].

**V10 — Show how ideas connect, not just a list.**
- For the `orient` and `recap` jobs, prefer components that draw links: the flow recap (§15) with arrow labels that say how ideas connect ("causes", "is a kind of", "needs"), or the map slide (§3) with one line per card saying how it relates to the others.
- The map slide names the deck's topics (N1).

*Why:* studying ready-made concept maps beats studying text, and the benefit is larger for learners with lower domain knowledge or lower verbal ability; building or completing maps helps even more [CM].

**V11 — One visual, one job.** Each visual answers one question ("What are the parts?", "What happens first?"). If a figure tries to show everything at once, split it across slides or builds.

**V12 — Interactives are a bonus, never the lesson.** For the reactive sentence (§27) or a lab widget (§32b), the resting state must already show the key result in words and numbers. A student who never touches the control must lose nothing examinable.

*Why:* only a small share of readers touch interactive elements (the skill's own note), so anything that appears only after interaction is invisible to most students.

**V13 — Facts live on the figure.**
- When a sentence would only name a part, say where it is, or give its property ("registers: inside the CPU"), write it as a label beside that part instead.
- The prose that remains carries the mechanism, the "why" and the conditions.

*Why:* contiguity [M]. It also removes the repeated names that a separate list would need. On the ch1 storage slide, this cut about 25 words and made the levels easier to compare.

**V14 — Legible at every width.**
- Figure labels scale with their figure. Size them in the figure's own units (container query units, Appendix B), with a minimum size. Display faces like Caveat become hard to read below about 1rem on a laptop.
- Labels on patterned fills get a backing chip.
- Phone sizes are set by M4; check every slide at phone width (Q7). Internal scroll on dense slides is the engine's accepted fallback, within M3's limit.

### Phone first (G6)

These rules make the deck work well on a phone without changing it on a laptop. The code that serves them is `deck-tools/snippets/phone-layer.css` and `phone-layer.js` (Appendix B4).

**M1 — Design the phone view first; keep the laptop view.**
- Plan and check each slide at **390 × 844**, held upright, before the laptop size (1280 × 800). The phone view is the base, and the laptop gets more room for the same content, never other content.
- Write new CSS phone first: the base rule is the phone rule, and `@media (min-width:881px)` adds columns and larger sizes. The skill's template and the course shell keep their own CSS unchanged; the phone layer (Appendix B4) goes on top.
- A laptop screenshot of every slide must look as it would without the phone layer (Q7).

*Why:* a phone changes three things at once: a narrow screen, touch instead of a mouse, and browser bars and notches that take space. A slide planned at laptop size and squeezed afterwards breaks there first: figures shrink until their labels can't be read, two columns crush each other, and the nav hides behind the browser bar.

**M2 — One column, no sideways scrolling.**
- Below 881 px every multi-column layout becomes one column. Set columns with classes, never with an inline `grid-template-columns` (it beats the phone media query).
- Reading order on a phone: the slide's main sentence, then its figure, then the details. Use CSS `order` when the laptop order differs.
- Nothing makes the page scroll sideways, down to 320 px wide [WR].
- Tables with 3 or more columns turn each row into a block on phones, with the column name inside each cell (the `data-m` pattern in Appendix B4).
- A box that must stay wide (code, a long formula) scrolls inside itself, with `data-capture`, so a sideways swipe on it doesn't turn the page (B4 sets it).

**M3 — Height.** Aim for each slide to fit in about **1.5 phone screens** at 390 × 844 *(target)*, with the main sentence and the top of its figure visible without scrolling. Internal scroll is the fallback. A slide taller than 2 screens is split, or its figure gets a phone variant (M4). When a build lands below the bottom edge, the phone layer scrolls it into view.

**M4 — Readable sizes.**
- Body text at least 15 px on a phone; lead lines 16 px.
- Figure labels at least **11 px** at 390 px wide (Appendix B3 floors).
- When a figure can't hold its labels at that size, give it a phone variant instead of shrinking it: a taller layout (parts stacked), fewer labels per build, or a second viewBox shown only on phones (Appendix B5: one set of labels, two drawings, so the words count once). Labels stay on the figure (V2).

**M5 — Touch.**
- Main controls (Prev/Next, quiz options, Check buttons) are at least **44 × 44 px** [WT].
- Smaller targets (topic blocks, word chips, group pills) are at least **24 px** tall, with space between them [WT].
- Nothing needs a mouse hover: every hover effect also opens by tap or keyboard focus (gloss cards and linked figures already do).
- Every drag also works by tap (`questions-rulebook.md` §6).

**M6 — Swipes.** A sideways swipe turns the page and a vertical swipe scrolls the slide. Areas with `data-capture` (drag widgets, word banks, wide code) don't turn the page, so keep them compact, never the whole slide. Prev and Next always work.

**M7 — Browser bars and notches.** Use the visible height (`100dvh`), keep the nav above the phone's home bar (`env(safe-area-inset-bottom)`), end slide content above the nav and the topic name, and add `viewport-fit=cover` to the viewport tag (Appendix B4).

**M8 — Light and steady.** Phones are slower: one line-boil element per slide at most, no full-screen live filters (the validator checks), and respect the reader's reduced-motion setting (B4). The deck still works when the phone is turned sideways; scrolling is fine there.

### Navigation

**N1 — A topic bar instead of slide dots.**
- **What it shows:** the slide dots are replaced by a row of **rounded-corner rectangles**, one per **topic**, each with the topic's name inside.
- **Length = size:** each rectangle's length is proportional to the number of slides in its topic, so the student sees how long each topic is.
- **Only the current topic is marked.** There is no indicator of progress *inside* a topic:
  - the thin progress line is hidden;
  - the current rectangle is highlighted;
  - topics already passed get a light fill, so moving to the next topic is visible.
- **Click to jump:** clicking a rectangle goes to the topic's first slide.
- **Topics:** mark the first slide of each topic with `data-sec="Name"`. Every slide belongs to the topic last named before it.
  - 3 or more slides per topic *(target)*; 2 only with a very short name; never 1.
  - Names of 1–3 words, ≤ 24 characters (they may wrap to two lines).
  - The names match the map slide (V10).
- **Phones:** the rectangles keep their lengths but drop their text, and stay at least 24 px tall so they can be tapped (M5). The current topic's name shows just above the bar.
- **Same in every deck of a course:** later decks copy the topic bar's code from the shell unchanged (§0). Appendix B's code is for a deck that has no topic bar yet, such as the first deck of a course. In Sketchbook, it reproduces the Applied OS decks' bar exactly.
- **Build:**
  - keep the engine untouched;
  - keep the hidden dots element, because the engine writes to it;
  - add the topic bar after the engine (Appendix B).
- `plain_check.py` lists the topics and flags 1-slide topics.

*Why:* 30 or more dots read as a long to-do list, and counting slides invites watching progress instead of the content. Topic blocks show the lecture's structure, which signals its organisation [M]. Each block is also a natural revision unit that students can jump to (T5, T7). Proportional length sets honest expectations about effort. Showing no in-topic progress is a design choice to keep attention on the content; it is not a research finding.

---

## 9. Quality checks before delivery

**Q1 —** `python scripts/validate.py deck.html` (the skill's validator) passes. Its "more than 20 slides" note is expected for single-deck lectures.

**Q2 —** `python plain_check.py deck.html --max-level <the course's level>` (Appendix A) runs. Fix every flag, or list it in the report with a reason (for example: "kept *algorithm*: course term, defined on slide 4").
- Add the course's field words with `--known`.
- *If you cannot run code* (code execution is off, or the word-list download is blocked):
  - say so in the report's "Checker" line;
  - check L1, L2, T5, T6 by a careful read, and the word ceiling by a careful count, instead;
  - never report a percentage you did not measure.
  - The skill's `validate.py` needs code too; say the same for it.

**Q3 —** The fact ledger lists 100% of the slides' facts, none weakened or missing (F1), and the last independent pass reports nothing (F1b).

**Q4 — Cold read.**
- Pick 2 random topics. Read each one as a student who opened only that topic. Can it be understood without the rest?
- Then pick 3 random slides. Is every term on them explained, either visibly or by its glossary card? Does each slide's main sentence avoid depending on a hidden card?
- If not, add a visible gloss (T5) or restate the missing fact.

**Q5 — Checklist.**
- [ ] Every course term: idea first, then `<dfn>`; formal version kept where F2 requires it.
- [ ] Every definition and review-question list quoted exactly, with its plain reading beside it (F2).
- [ ] Every qualifier and modality of the slides survives (L10); the ledger was re-checked after the last trim.
- [ ] The deck's own framing is labelled, and none of it contradicts a slide fact (F3b).
- [ ] Independent check clean, passes recorded (F1b).
- [ ] Every load-bearing concept follows the Concept Pattern (deck form), with its plain idea, a concrete example, a picture and its "why" on the visible layer.
- [ ] The words above the original's count went to §1's "Where the extra words go" list, not to padding or repeats.
- [ ] Every procedure, calculation, or code block has a labelled worked example and a practice problem.
- [ ] Known misconceptions are refuted and the main one is re-tested.
- [ ] Opening challenge is attemptable from everyday knowledge and written one level below the course's (TE3).
- [ ] The final quiz follows `questions-rulebook.md` (with the question set on, §11: it follows TE7).
- [ ] No decorative visuals (V1); every component does a job text cannot (V7).
- [ ] No content dropped to fit the word ceiling (precedence 2, F9).
- [ ] Slide problems are noted in the deck and in the report (F4).
- [ ] Canvas, board and English level match the COURSE record (first deck: the user chose them). The record is present, with the deck number raised by one and its memory lines updated (§0, W11).
- [ ] Phone first: M1–M8 pass in the Q7 checks; the phone layer (Appendix B4) is present.
- [ ] Research done for every load-bearing concept; `SOURCES` comment present (W2b).
- [ ] Every slide's job is named and its component comes from `use-cases.md`; components vary across the deck.
- [ ] Every visual follows V7–V14: labels on the figure, colour-linked where useful, a "Notice:" caption, processes as builds or step-throughs.
- [ ] Nothing examinable is hidden behind hover/tap or trimmed away (F9, V12); load-bearing glosses are visible where T5 requires.
- [ ] Topic bar present; topics named as on the map slide; no 1-slide topic (N1).
- [ ] Glossary slide present; every acronym and cross-topic term is in it (T5b, T9).
- [ ] Every improvement changed presentation only: no fact, formula or term changed (§1).

**Q6 — Word ceiling and digestibility (G5).**
- **Ceiling:** deck words (all readable text: visible text, labels, tables, gloss cards, quiz feedback; the fullest state of a magic board) ≤ **2 × the original's words** (W1b). `plain_check.py` reports the deck's words, the original's and the ceiling when the deck has the `BUDGET` comment, and flags a deck over it. A deck over the ceiling is not delivered (W4).
- **No slide-count check.** The slide count is reported for information only.
- **Digestibility:** pick 3 random load-bearing concepts. Each one has its plain idea, a concrete example, a picture and its "why" on the visible layer, in full sentences (Concept Pattern, deck form). No slide passes V5's soft cap, and no slide brings more new terms than T4 allows.
- Count after the first draft, not only at the end. Cutting a finished draft back under the ceiling costs more than writing to the caps.

**Q7 — Visual check (phone first).**
- **Phone:** look at **every** slide fully built at 390 × 844 with touch turned on (Playwright `has_touch`, `is_mobile`). Then:
  - check 360 × 740, 320 × 640 and the phone turned sideways (844 × 390) for sideways scrolling: there must be none (M2);
  - list the slides taller than 1.5 screens at 390 × 844 (M3) and fix those over 2;
  - swipe through the whole deck with touch events, using Prev/Next where a drag area takes the swipe: every build must end up in view (M3, M6);
  - measure the main controls: none under 44 px tall (M5).
- **Laptop:** look at every slide fully built at about 1280 × 800. It must look as it does without the phone layer (M1).
- At both sizes, check that:
  - labels don't overlap lines or each other, and are readable (M4);
  - every arrow has its head (V2);
  - the topic bar marks the right topic.
- Step through every build once with the keyboard. Click each quiz item once.

---

## 10. Delivery report (chat, keep it short)

```
Deck: <lecture title>, covers source slides 1–<n>.
Course: <slug>, deck <NN> (case A/B/C) · shell: <file, or "skill template"> · level: <A2–C1> · record: <what changed in it>.
Canvas: <paper, or chalkboard · board> (<chosen by the user now, or from the COURSE record>).
Slides: <x> (source <y>, for information). Words: <deck> / <original> (<pct>% of the original; ceiling 200%); original = <text> text + <fig> in figures/tables. Over 100%: say in one line what the extra words went to (for example: examples, worked examples, exact quotes and their glosses, plain rewording).
Topics: <name · slides> | …
Coverage: <f>/<f> facts in the ledger (exact <e>, faithful <r>; admin skipped: <list or "none">).
Standalone: independent check <n> passes; first pass <counts>; last pass <"nothing found" or what stands, and why>.
Checker: word coverage <c>% at <the course's level>; kept flags: <word or rule — reason>.
Slide issues: <F4 notes or "none">.
Phone: checked at 390×844 (all slides), 360, 320, sideways; slides over 1.5 screens: <list or "none">; laptop unchanged ✓.
Quiz: <the questions-rulebook §8 report lines>.
Settings changed: <list or "none">.
Field words added: <list, or "none"> (L1).
Skill mismatches: <parts of this file that did not match the skill, or "none">.
Departures: <procedures of this file done another way, and why, or "none">.
Proposed for the skill: <lessons for every course (W11), or "none">.
```

---

## 11. Settings the user can change

| Setting | Default | Other options and their effect |
|---|---|---|
| English level | **B1** (asked at the first deck) | **A2 · B2 · C1:** SKILL.md step 2b sets the words and the sentence caps; the checker runs with `--max-level`. Recorded as `english level:` in the COURSE record. |
| Field vocabulary (L1) | **Built-in computing list** | **Course list:** a `words.txt` passed with `--known`. **None:** stricter; field words must be glossed. |
| Arabic support | **Off** | **On:** each definition and glossary entry adds the Arabic term in one line. In a meta-analysis, glosses in the reader's first language beat English-only glosses (g ≈ 0.33), mostly for immediate word learning and most for beginners. Cost: more words, and the deck is no longer English-only [GL]. |
| Deck shape | **One deck per lecture file** | **Series:** several decks of 14–18 slides (cap 20), each a full arc, one per reply, with TE9. Use when the user wants shorter sittings. |
| Word ceiling (G5) | **2 × the original's words**, never passed; no slide-count limit | **Tighter:** 1.5 × the original (`plain_check.py --ceiling 1.5`); fewer examples and analogies, cut from the bottom of §1's list. **Shorter:** the v1.7 rule: no more words than the original (`--ceiling 1`) and about 0.8 × its slides, paid by compressing wording and moving facts into figures. Use it only when the user asks. |
| What counts toward the budget | **Everything readable**, including copied code, formulas and tables (the original's count includes them too) | **Exclude added worked-example and trace tables:** mark them `data-budget="skip"`. They are still checked for language, and are listed in the report. |
| Mid-deck checks (TE4) | **Off** | **On:** one question at the end of each topic, marked `data-budget="skip"`. |
| Final quiz (`questions-rulebook.md`) | **On**, as the last topic | **Off:** the skill's question set and answer box come back (TE7). |
| Question set and answer box | **Off while the final quiz is on** | **On:** both come back after the glossary slide, inside the budget. |
| Canvas and board | **Asked at the first deck of a course** (never decided by Claude) | Named in the prompt: then not asked. |
| Phone first (G6) | **On** | **Off:** laptop-first, as before v1.5 (not recommended; phone checks become a sample). |
| Glossary (T5b) | **On** | **Off:** v1.2 T5 (a visible or anchored gloss on every slide that uses a term). Costs about 5 words per term per slide. |
| Navigation (N1) | **Topic bar** | **Dots:** the skill's default navigation. |
| Exact wording (F2) | **Every definition and every review-question list** (since 1.7) | **Review lists only:** v1.6 behaviour; about 15–20% fewer words, but a student who must quote a definition needs the slides. **Every bullet:** the slides' sentence for every bullet with a plain reading beside it; safest for strict marking, but it uses much of the room under the ceiling, leaving less for examples. |
| Slide errors | **Note and teach the slide's version** | **Correct the content.** Risk: it may differ from what the exam expects. |

---

## 12. Evidence base

| Tag | Source | Supports | Strength and caveats |
|---|---|---|---|
| [R] | Rosenshine (2012), *Principles of Instruction* | Small steps, worked models, frequent checks, ~80% success | Synthesis of classroom and cognitive research; widely used |
| [M] | Mayer (2020), *Multimedia Learning*, 3rd ed. | Multimedia, coherence, signalling, spatial contiguity, segmenting, pre-training, personalization | Many experiments; mostly short lessons |
| [D] | Dunlosky et al. (2013), *Psychological Science in the Public Interest* | Practice testing and distributed practice rated highest utility; rereading and highlighting low | Large review |
| [HN] | Hu & Nation (2000); Laufer (1989); Schmitt et al. (2011); Laufer & Ravenhorst-Kalovski (2010) | 95% known words = minimal, 98% = adequate comprehension | Replicated; measured on running texts, so the checker judges coverage at deck level |
| [STE] | ASD-STE100 Simplified Technical English | 20/25-word sentence caps, one word one meaning, one topic per paragraph, no dropped articles | Industry standard built for second-language readers |
| [A] | Abedi (2009); Sato et al. (2010), IES/NCEE report | Simplifying the wording of test items helps second-language readers without changing what is measured | Effect real but small |
| [WE] | Sweller; Kalyuga et al. (2003); Renkl et al. | Worked-example effect, expertise reversal, faded examples | Strong for novices; fades with expertise |
| [SG] | Margulieux & Catrambone (2016); Morrison, Margulieux & Decker | Subgoal-labelled worked examples in programming and STEM | Several studies; more replication called for |
| [PT] | Richland, Kornell & Kao (2009); Kornell, Hays & Bjork (2009) | Pretesting effect: failed attempts help when followed by teaching or feedback | Replicated, mostly with factual material |
| [PF] | Sinha & Kapur (2021), *Review of Educational Research* | Problem solving before instruction helps conceptual learning and transfer | Depends on design fidelity and on prior knowledge |
| [CF] | Fyfe et al. (2014); Kokkonen & Schalk (2021) | Concreteness fading | Promising in maths; may not generalize to every domain |
| [CFA] | Brown & Ryoo (2008), *Journal of Research in Science Teaching* | Everyday language before scientific terms | One small randomized study (n = 49, grade 5); fits pre-training |
| [TWA] | Glynn (1991) and later work | Teaching-with-analogies steps, including where the analogy breaks | Widely used; textbook analogies often skip the limits step |
| [RT] | Schroeder & Kucera (2022), *Educational Psychology Review* | Refutation text, g ≈ 0.41 | Some drift back at delayed tests → re-test |
| [SE] | Bisra et al. (2018), *Educational Psychology Review* | Self-explanation prompts, g ≈ 0.55; question-form prompts beat multiple-choice prompts | Mostly undergraduate samples |
| [MCQ] | Haladyna, Downing & Rodriguez (2002) | Multiple-choice item-writing guidelines | Consensus guidelines |
| [SD] | Sundararajan & Adesope (2020) | Seductive details lower learning, g ≈ −0.33; worse for novices and in learner-paced lessons | 58 studies; mostly short lessons |
| [CO] | Crossley, Allen & McNamara (2011) and related work | Classic readability formulas are weak proxies for second-language readers; word overlap (cohesion) helps them | Why the checker uses word lists, not Flesch scores |
| [RS] | Brysbaert (2019), *Journal of Memory and Language* | ~238 wpm for native non-fiction reading; slower for second-language readers | Second-language speed estimate comes from a single study |
| [GL] | "The relative effects of L1 and L2 glosses on L2 learning: A meta-analysis", *Language Teaching Research* | First-language glosses beat English-only glosses, especially for beginners | Mostly immediate vocabulary outcomes |
| [GL2] | Abraham (2008), *Computer Assisted Language Learning* | On-demand (computer-mediated) glosses: medium effect on reading comprehension, large on word learning | Learners in studies were asked to read; voluntary use in the wild may be lower |
| [WM] | Cowan (2001), *Behavioral and Brain Sciences* | Working memory holds about 3–5 chunks | Well established |
| [W] | WCAG 2.x, success criterion 1.4.8 | Line length ≤ 80 characters, line spacing ≥ 1.5, no justified text | Accessibility standard (AAA) |
| [WR] | WCAG 2.1, success criterion 1.4.10 Reflow | Content usable at 320 CSS px wide without scrolling in two directions | Accessibility standard (AA) |
| [WT] | WCAG 2.2, success criteria 2.5.5 Target Size (Enhanced) and 2.5.8 Target Size (Minimum) | Touch targets 44 × 44 CSS px (AAA); at least 24 × 24 with spacing (AA) | Accessibility standard |
| [SIG] | Richter, Scheiter & Eitel (2016), *Educational Research Review* | Signalling text–picture links (e.g., colour coding) improves comprehension and transfer | Small-to-medium effect; strongest for low prior knowledge |
| [AN] | Höffler & Leutner (2007), *Learning and Instruction*; Berney & Bétrancourt (2016) | Animation vs static pictures | d = 0.37 in the first meta-analysis, g ≈ 0.23 in later ones; benefit mainly when the change itself must be learned |
| [CM] | Nesbit & Adesope (2006), *Review of Educational Research*; Schroeder et al. (2018), *Educational Psychology Review* | Studying concept maps beats text; constructing them helps more | g ≈ 0.43 studying, 0.72 constructing; larger for lower-knowledge and lower-verbal learners |
| — | CEFR-J Wordlist 1.5 (Tono Laboratory, TUFS) | Word levels used by `plain_check.py` | Free for research and commercial use with citation |

### Researched and deliberately not turned into rules

- **Flesch / grade-level formulas:** weak proxies for second-language readers; the checker uses a CEFR word list and sentence length instead [CO].
- **"Vowel blindness" in Arabic-speaking readers of English:** a scoping review found the evidence too limited and conflicting to act on.
- **Redundancy principle** (do not repeat narration as on-screen text): it applies to narrated media; these decks have no narration.
- **"More animation is better":** the benefit over well-designed static frames is modest and depends on the content, so V9 prefers learner-paced step-throughs to autoplay.
- **Full productive failure** (long, unguided problem solving before teaching): it works best with high design fidelity and a teacher who builds on student attempts. A self-paced deck cannot do that, so TE3 uses the lighter pretesting form.
- **The level caps beyond B1 and B2** (15 words at A2, 30 at C1) and the checker's C1 frequency rule are design choices. The 98% coverage target applies at any level [HN].
- **A word ceiling as a learning principle:** no study sets "at most twice the source's words" as a learning target. The 2 × ceiling is the user's product requirement: room for plain wording and examples, with a limit on reading time. What fills the room rests on evidence: plain words and full sentences [HN][STE], concrete and worked examples [CF][WE], signalling and contiguity [M]. The number itself does not.

---

## Appendix A — `plain_check.py` (v1.8)

**What it checks, per slide:**
- visible word count;
- sentence length;
- words above the vocabulary ceiling or not on the list (field words allowed);
- terms used without a gloss (glossary terms count as glossed);
- unexpanded acronyms;
- back-reference phrases;
- banned question wording;
- likely passive voice.

**At deck level:**
- word coverage (target ≥ 98%);
- the topic list (N1);
- **deck words vs the original's and the word ceiling** (G5: 2 × the original by default, `--ceiling`; the original comes from the `BUDGET` comment or `--budget`). Only a deck over the ceiling is flagged.

**The HTML contract it relies on** (also required by the rules above):

| Markup | Meaning |
|---|---|
| `<dfn>term</dfn>` | The defining use of a course term (T1, T3) |
| `<dfn data-forms="matrices">matrix</dfn>` | Irregular forms of a term |
| `data-for="term"` on any element | A gloss or key entry for that term on this slide (T5, T9); on an anchored gloss, put it on the dotted `.gl-t` word |
| `<dl id="glossary"> <dt data-forms="…">term</dt><dd>…</dd>` | The deck glossary (T5b): its terms count as glossed on every slide |
| `.gl-card` / `role="tooltip"` (components §24) | Language-checked and counted toward the budget, but not counted as visible words (V5) |
| `.lf-pin` (components §22) | Each figure label is read as its own piece, not glued into a sentence |
| `class="formal"` | Exact course wording: skipped by the language checks (F2), counted toward the budget |
| `class="ours"` | The deck's own framing (F3b): checked and counted |
| `<!-- FACT-LEDGER -->`, `<!-- INDEPENDENT-CHECK -->` | F1 and F1b records (replace the v1.6 coverage map) |
| `<code>`, `<pre>`, `<kbd>` | Skipped by the language checks; counted toward the budget |
| `<svg>`, `<math>`, `<script>`, `<style>` | Skipped and not counted |
| `data-why="…"` | Quiz feedback: checked and counted |
| `<template>` runs (magic board) | Only the last state of each run is checked and counted |
| `data-sec="Name"` on a slide | The first slide of a topic (N1) |
| `data-budget="skip"` | Checked but not counted. Only for content the settings exclude (§11). On a `<section class="slide">` (the final quiz), the whole slide and its feedback stay outside the count |
| `<!-- BUDGET original=N -->` | The original's total words (W1b); the ceiling is N × `--ceiling` |

**How to run it:**

```bash
pip install wordfreq            # add --break-system-packages if pip asks
python plain_check.py deck.html --max-level B1          # the course's English level (B1 is the default)
python plain_check.py deck.html --known course-words.txt
python plain_check.py deck.html --max-level C1          # another level: A2, B1, B2 or C1
python plain_check.py deck.html --ceiling 1.5           # the "Tighter" word ceiling (§11); --ceiling 1 = "Shorter"
```

On its first run, it downloads the CEFR-J word list from GitHub and saves it next to the script. If the download fails, it prints the link so you can save the file by hand. Exit code 0 = clean, 1 = notes to fix or justify.

**Limits (read the output with judgment):**
- The lemmatizer is simple; a rare irregular form may be flagged wrongly.
- Capitalized words in the middle of a sentence are treated as names and listed for you to check, not counted.
- The passive-voice check is a hint, not a rule.
- It cannot judge meaning, or whether a term is load-bearing (T5). Q3–Q5 still need a careful read.
- The glossary cards are added at runtime. The checker trusts the glossary list; Q7's walk-through confirms that the cards appear.

**The script:** `deck-tools/plain_check.py`. `setup_tools.sh` copies it next to the rulebooks, so the commands above run as written. Open it only to change it.

---

## Appendix B — Topic bar (N1), deck glossary (T5b), label sizes (V14), phone layer (M1–M8) and phone-variant figures (M4)

All of them work on both canvases and every board: they read only the canvas and bridge tokens (`style-system.md §7`). Their scripts go **after** the engine, inside the deck's single `<script>`. None of them edits the engine. The code is in `deck-tools/snippets/`: copy each file into the deck with a script, never by retyping.

### B1. Topic bar

HTML, replacing the skill's nav block (keep `#dots`, because the engine writes to it):

→ `deck-tools/snippets/topic-bar.html`

Mark topics on the slides: `<section class="slide active" data-sec="Start">`, `<section class="slide" data-sec="Storage">`, and so on.

CSS (at the end of the style block):

→ `deck-tools/snippets/topic-bar.css`

Script (after the engine):

→ `deck-tools/snippets/topic-bar.js`

### B2. Deck glossary

The glossary slide (the last slide of the Review topic, before the final quiz):

→ `deck-tools/snippets/glossary-slide.html`

CSS:

→ `deck-tools/snippets/glossary.css`

The cards reuse the skill's anchored-gloss CSS (components §24); paste it if the deck has no anchored glosses yet. Add one line, so that a card near the edge of a phone screen moves sideways instead of making the slide scroll sideways (a hidden card still counts toward the scroll width):

```css
.gl-card{position-try-fallbacks:flip-block, top span-left, top span-right, bottom span-left, bottom span-right}
```

**Flex containers.** The script wraps a matched word in a span. Inside a flex container, such as the template's `ul.points li`, that span becomes a flex item and splits the text into columns. Wrap the item's text in a span:

```html
<li><span class="tick">…</span> <span class="t">Monitor users, so they follow the security policies.</span></li>
```

```css
ul.points li > span.t{flex:1;min-width:0}
```

Script (after the engine):

→ `deck-tools/snippets/glossary.js`

### B3. Figure labels that scale with their figure (V14, M4)

Add this to the §22 label CSS. Each label's size then follows the figure's own units, with an 11 px floor for phones (M4):

→ `deck-tools/snippets/figure-labels.css`

Courses that started before v1.5 keep their shell's floors (9 / 8.5 px), so their decks look the same; new courses use these. A figure whose labels collide at the new floor gets a phone variant (M4).

### B4. Phone layer (M1–M8)

Tested on the Applied OS chapter 4 deck: no sideways scrolling down to 320 px, every build in view after a touch walk, main controls 44 px, and laptop screenshots unchanged.

The viewport tag (replace the template's):

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

CSS (at the end of the style block, after the topic bar):

→ `deck-tools/snippets/phone-layer.css`

Script (after the engine and the other component code):

→ `deck-tools/snippets/phone-layer.js`

Wrap a wide table in `<div class="tbl-wrap">` only when it must keep its columns on a phone; otherwise give it `class="tbl stack"`.

### B5. Phone variants of wide figures (M4)

Tested on the 210 ISY deck 1 (four figures). A landscape figure at 390 px wide drops to about 0.5 px per unit, and its labels to their floor. Draw a second, portrait drawing for phones, and keep **one set of HTML labels**, so the budget counts each word once.

The `.lf` gets class `pv` and the phone viewBox size. It holds both drawings, and every label carries both positions plus a phone anchor class (`p-start`, `p-mid` or `p-end`):

→ `deck-tools/snippets/phone-variant.html`

CSS (after B3 and B4):

→ `deck-tools/snippets/phone-variant.css`

- Build groups (`data-build`) may sit in both drawings. Label layers that carry `data-build` are shared.
- One `.live` per slide: boil the stroke in the laptop drawing only.
- Keep each phone label line to about 35 characters: fallback fonts run wider than Caveat.

---

## Appendix C — The independent check (F1b): the checker's brief

Run it with `deck-tools/slide_text.py DECK audit/deck_text.txt` and the PDF text (`pdftotext -layout`). Give the checker those two files only. Replace the parts in angle brackets. Tested on the 210 ISY deck 2 (three passes, from 41 findings to none).

**The brief:** `deck-tools/checker-brief.txt`. Copy it with a script, fill the angle brackets, and send it to the checker as it is.

- **Who checks:** a fresh agent with no access to the build files. Resuming the same checker for later passes is fine: it remembers its own earlier findings, not the author's reasoning.
- **What to give it:** the two text files only. Never the ledger, the plan or the HTML: it must judge what the student sees.
- **Cost:** about 100–120K tokens for the first pass of a 30-page lecture, much less for later passes.

