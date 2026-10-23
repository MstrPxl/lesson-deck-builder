# Lessons Rulebook

**Version 2.0 · 23 October 2026 · written against `lesson-deck-builder` v1.4 · derived from `slides-rulebook.md` v1.4.3; shares its code with slides-rulebook 2.0**

> **New in 2.0:** this file ships inside the skill (`rulebooks/`), and the skill routes any teaching request without a lecture file here, so a run starts from one line. Nothing is attached but the previous lesson (HTML), and no notes file goes back and forth (W12). The English level is the user's choice, A2–C1 (default B2). Goals over procedures (§0). The code is the shared `deck-tools`. Full history: `rulebooks-changelog.md`.

This file tells you how to build **one lesson deck** for a personal learning repo: a lesson the learner (the user) studies on their own, about a topic chosen outside this file. Each lesson is:
- **researched** on the web, thoroughly but within a cap;
- **correct and complete** for its scope;
- written in clear English at the chosen level (**A2–C1**, default **B2**);
- organised in topics that each stand alone;
- taught with methods that have research behind them;
- **built like the user's reference decks**: the same look, density and figure-first style, with components chosen freely by teaching job.

The file is subject-neutral. It ships with the skill (`rulebooks/`) and works in a learning repo (repo mode) or in a chat (chat mode).

---

## 0. How to use this file

- **Read order, before you plan anything:**
  1. this whole file;
  2. the general notes (`deck-notes-general.md`, beside this file): experience, not rules; read the parts that help;
  3. the repo's own instruction files, if any (they decide topics and research, see below);
  4. the lesson-deck-builder `SKILL.md` and the references it tells you to read, including `use-cases.md` and `components.md`. When there is a shell ("Starting a run"), the skill's `template.html` and example decks are optional.
- **This file adds to the skill.** Where §2 says so, it overrides the skill. Where this file says nothing, follow the skill.
- **Who decides what:**

  | Question | Decided by |
  |---|---|
  | Which topic comes next, the roadmap and its changes, the learner notes and personalization | The skill (its roadmap and notes machinery) and the repo's own instruction files. **This file never creates, edits or reorders a roadmap.** |
  | Whether a topic is researched now, re-researched because time has passed, or taken from stored research | The repo's own instruction files. If they say nothing, research (W2). |
  | How a lesson is researched, written, drawn, checked and reported | This file |
  | How the lesson looks | The reference decks and the DECK-SETTINGS record ("Starting a run") |

- **Who wins on how to build:**
  1. The user's instructions.
  2. The repo's choices in the DECK-SETTINGS record.
  3. This file.
  4. The general notes, which record experience, not rules.
  5. How an earlier deck happened to be built.
- Every rule has an ID (L2, T5, H3, N1 …) so the user can point at it in feedback.
- **Goals over procedures.** Fixed: the goals (G1–G5), the user's choices and the DECK-SETTINGS record. Everything that says *how* (the workflow, the numbers marked *(target)*, the research cap, the tools, the code in `deck-tools`) is a tested default for the models of its date. When another way meets the goals better, use it and name it on the report's "Departures" line (§10). A departure never trades away a goal or a choice.
- **Size cap:** this file stays under **75,000 characters**. Code stays in `deck-tools`, history in `rulebooks-changelog.md` (`slides-rulebook.md` §0 has the full rule; `deck-tools/size_check.py` checks it).
- "Why" lines give the mechanism. Tags in square brackets (for example [HN]) point to the evidence table in §12.
- This file was written against **lesson-deck-builder v1.4** (Sketchbook only; engine v2; `use-cases.md`; components §1–§32, where §32a–§32l hold the stepper skeleton and the mechanics ported from the retired style families). Component numbers (§22, §25, §32h …) refer to that version's `components.md`.
  - If your version of the skill renamed or replaced something named here, apply the rule to its current equivalent and mention the mismatch in the report (§10).
  - The topic bar (N1) and the deck glossary (T5b) are not in the skill's components yet. Their code is in `deck-tools/snippets/` (beside this file); Appendix B says where each file goes.
- Numbers marked *(target)* are design choices, not research findings. They may be tuned. Numbers without that mark come from a standard or a study.

### Starting a run

**What the user sends.** One line, for example "use /lesson-deck-builder to teach me <topic>", "… the next lesson", or "… a lesson on <topic>, length: medium". The skill routes here by itself (SKILL.md, step 0b): a teaching request with no lecture file attached.

**Inputs:**

| Input | Where it comes from | If missing |
|---|---|---|
| The topic | The prompt, or the skill's roadmap step for "the next lesson" (with the step's goal and research directives) | Ask. Never pick a topic yourself. |
| Length (§11) | The prompt | Use the repo default in the DECK-SETTINGS record. If there is none, ask once and record the answer as the default. |
| English level | The DECK-SETTINGS record (`level:`) | First lesson: ask it with the canvas gate (SKILL.md, step 2b; suggest B2). |
| Canvas and board | The DECK-SETTINGS record | First lesson in a repo: the skill's canvas gate, with the reference decks' canvas suggested first. A record that says `canvas: chalkboard` but has no `board:` line means `slate-reinked` (the skill's default); write the line in. |
| Reference decks | Attached, or kept in the repo (for example a `reference-decks/` folder; the prompt may name another place) | Optional. Without them, follow §8 and the skill's style. |
| Earlier lessons | The repo's `lessons/` folder (repo mode), or the previous lesson attached (chat mode). Older lessons are not attached: ask for one only when you need its figure or glossary wording. | None means this is the first lesson. |
| General notes | Beside this file (`deck-notes-general.md`) | Read the parts that help. |
| Stored research | Wherever the repo's instruction files keep it | Research (W2). |

Anything the user writes in the prompt (a length, a canvas or board, a scope) wins over everything below.

**Which case is this?**

- **A. First lesson in a repo.** No earlier lesson exists.
  - Run the skill's canvas gate once (paper or chalkboard, then the board), suggesting the reference decks' canvas first. Ask the English level (suggest B2), and the length default if the prompt didn't give one, in the same message.
  - **Shell:** the newest reference deck, if its canvas matches the choice (bring it to v1.3 tokens first, H1b). Otherwise the skill's template.
  - Start the DECK-SETTINGS record at lesson 1.
- **B. Later lesson.** Earlier lessons exist.
  - Don't ask anything the DECK-SETTINGS record already answers.
  - **Shell:** the newest lesson.
  - Copy the DECK-SETTINGS record into the new deck and raise its lesson number by one.

**The DECK-SETTINGS record.** Every lesson carries the repo's standing choices in one HTML comment, next to the coverage map:

```html
<!-- DECK-SETTINGS
subject: Applied AI engineering · slug: applied-ai
lesson: 3 · topic: Retrieval-augmented generation
style: Sketchbook · canvas: chalkboard · board: slate-reinked
level: B2 · length default: medium
settings changed (§11): none
field words: none beyond the checker's built-in list
standing decisions: none
reusable figures: lesson 2 · slide 7 · the retrieval pipeline
-->
```

- The record holds the **user's choices** for the repo. They win over this file's defaults (§11).
- **This file wins over how an older deck was built.** Add the parts an older deck lacks (a glossary slide, a record), but don't rewrite code the shell already has.
- In repo mode the skill may also record the canvas and board in `docs/`. The two must agree; if they don't, ask.
- **Canvas and board in the deck:** the `<html>` element carries `data-canvas="chalkboard" data-board="<board>"` (or `data-canvas="paper"`), matching the record. The six boards: `slate-reinked` · `midnight-blue` · `olive-gold` · `dusk-indigo` · `deep-teal` · `red-graphite`.
- **Field words** beyond the checker's built-in list: list them in the record, write them to a file, and pass it to the checker with `--known` (Q2). Each lesson inherits the list and may add to it (L1).

**The shell and the reference decks.**
- **The shell** is everything in a deck except its slides: styles, shared SVG defs, engine, component code, topic bar and glossary code.
  - Split it off and reuse it **unchanged**. Copying code, not re-writing it from a description, is what keeps every lesson looking and behaving the same.
  - The newest lesson is the shell, even when an older one is also attached.
- **The shell is a source of code, not a list of allowed components.**
  - Choose each slide's component from the skill's full catalog, by teaching job (W9, H2).
  - When a component comes back, reuse its code from the shell.
  - When it is new, take its code from the skill and add it to the shell, so the next lesson inherits it.
- **Reference decks** show the look the user wants (§8, "House style"). Study how they use components and how dense their slides are. Don't copy their slides or their content.
- **Older lessons and reference decks:** don't read them in full. Pull what you need with a short script: the glossary entries (`dl#glossary`), the DECK-SETTINGS record, or one figure the record's `reusable figures` line points to. In chat mode only the previous lesson is attached; ask for an older one when you need it.

**Naming.** Follow the skill: `lessons/NN-<step-slug>.html` in repo mode. In chat mode: `<subject-slug>-NN-<topic-slug>.html`.

**Order of work:** W1–W6, then W7 only if it has something to ask, then W8–W12.

---

## 1. The five goals and how each one is measured

| Goal | What it means here | How it is checked |
|---|---|---|
| **G1 — Correct and complete for the scope** | Every core concept of the lesson's scope is taught, and every claim is right and current. The scope comes from research (W3) and the chosen length. | Coverage map against the concept inventory (F1); sources for every load-bearing claim (F2–F4) |
| **G2 — Clear English at the chosen level** (A2–C1, default B2) | Words and sentences that a reader at that level takes in with ease; plain grammar. Technical terms stay and are taught. | `plain_check.py --max-level <level> --cs-grad`: ≥ 98% of running words at the level or below (field words allowed, L1); no sentence over the level's cap (SKILL.md step 2b) |
| **G3 — Independent topics, no unexplained words** | Any topic (N1) can be understood without the other topics. On any slide, every term is explained, visibly or by its glossary card. "No jargon" means **no unexplained word**, not "no technical word". | `plain_check.py` gloss, acronym and back-reference checks; cold read (Q4) |
| **G4 — The best ways to teach** | The Concept Pattern (§6) and the teaching rules TE1–TE10. | Checklist Q5 |
| **G5 — The house style, at the chosen length** | The lesson looks and reads like the reference decks (H1–H5) and fits the length the user chose (§11). | Visual check (Q7); length check (Q6) |

### Precedence when rules conflict

1. **Correctness, and the skill's technical hard rules** (untouched engine script, validator passes, one `<script>`, no storage APIs).
2. **The core concepts, taught fully** (G1). Never drop or shrink a core concept to meet a length or a simplicity target.
3. **Understandability** (G2, G3).
4. **The chosen length** (G5).
5. **Supporting concepts and the optional teaching steps** (§6).
6. **Style** (the skill's reading-time budget, Law 5 "little text").

*Why this order:* a wrong or missing core idea defeats the lesson, so it comes first. The user chose the length, so it beats supporting material, but not the core. When the core alone does not fit the length, say so (W7) instead of cutting it.

### Improve on the sources, keep the facts

The lesson is not a summary of what you read. It is a better teaching of the same facts.

| You are expected to improve | You must keep exactly |
|---|---|
| The order of ideas (W4) | Every fact and claim, as the best sources state it |
| How ideas are grouped into topics | The meaning of every definition |
| Explanations, missing steps, examples, analogies, practice | Formulas, notation, code and official names (F5–F7) |
| Visual form: lists into tables, flows, maps or step-throughs (§8); descriptive sentences into figure labels (V13) | Dates and versions of fast-moving facts (F3) |
| Background the topic assumes (T8) | Disagreements between good sources, shown, not hidden (F4) |

---

## 2. How this file changes the lesson-deck-builder workflow

| Skill step | Under this file |
|---|---|
| **Environment, topic conversation, scope and roadmap mode** | Unchanged. The skill and the repo's instruction files own them. This file starts once the topic is known. |
| **Deck kind** | Always a **teaching deck** (teaching arc, challenge pair, question set). |
| **Canvas gate (step 1b)** | Unchanged in shape: always the skill's exact question (paper or chalkboard, then the board). Ask **once per repo**, at the first lesson, suggesting the reference decks' canvas first. Later lessons read canvas and board from the DECK-SETTINGS record. |
| **Language (step 2)** | Answered by this file: **English**, `dir="ltr" lang="en"`. Do not ask. |
| **English level (step 2b)** | Asked once, at the first lesson, with the canvas gate (B2 suggested); later lessons read it from the DECK-SETTINGS record. |
| **Intake (step 4)** | Audience: the user, an independent learner with a computer-science background who reads English at the DECK-SETTINGS level. Length: the preset (§11). Ask only what the prompt and the record leave open. |
| **Teaching arc (step 5)** | Keep it. Order: cover · opening challenge · map (the topics, named as in the topic bar) · any slide the skill requires here (for example its roadmap slide) · the topics · challenge revisited · recap (with a one-line closing) · glossary "Words in this lesson" (T5b) · "Go deeper" (F8) · question set · answer box. |
| **Length** | From the length preset (§11), not the skill's default sizing. |
| **Law 5: little text** | Applies fully. Hover/tap depth is only for supporting-term glosses (T5, T5b) and extras ("Going further"). Core content is never hidden (F9). |
| **Visual-first** | Visuals carry structure, sequence, comparison and change (§8). Every visual must teach something (V1). Where this file and the skill disagree about *how* a visual is built, the skill wins; this file decides *what* it must show. |
| **Matching slides to teaching jobs (step 5)** | Use it fully, with the whole catalog (H2). |
| **Per-lesson research** | Required, at the depth of W2, unless the repo's instruction files say stored research is fresh. |
| **Question set and the adaptive loop** | The skill's, including its personalization from the learner notes. Items also follow TE7. |
| **Navigation** | The topic bar (N1) replaces the slide dots. |
| **Writing state back** | Repo mode: the skill's job (roadmap, notes, answers, commits). Chat mode: the skill's learner notes travel in the lesson's `LEARNER-NOTES` comment. This file adds only the records inside the deck (W12). |

---

## 3. Workflow

**W1 — Settle the inputs** ("Starting a run"): topic, length, style, shell, reference decks, field words, stored research.

**W2 — Research the topic (thorough, capped).** Skip or shorten this step only when the repo's instruction files say stored research for this topic is fresh; then reuse it and verify only claims you doubt.
1. **Scope.** 2–4 searches for how strong sources structure the topic: university courses and syllabi, official documentation, standard textbooks, well-known courses. If the skill gives the roadmap step's goal and research directives, start from them. The output is a candidate list of concepts.
2. **Correctness.** Check every load-bearing claim, definition and formula against **two independent reliable sources**. Disagreement → F4.
3. **Best explanation.** How strong teachers and textbooks explain each heavy concept, and which visual they use. Build your own version; never copy text or images.
4. **Misconceptions** for the 3–5 heaviest concepts *(target)*. They feed Concept Pattern step 7 and the question-set distractors.
5. **Examples.** Concrete cases and real applications.
6. **Currency.** For fast-moving topics (tools, versions, models, prices, rankings, standards), find the current state and its date (F3).

**The cap:** about **10–15 strong sources** *(target)*. Stop when the sources agree. Use 1–2 extra searches per disagreement or doubt. By default, search yourself: in an earlier build one broad research agent cost about 140K tokens, mostly confirming what one good source said. Use agents when the scope needs them or the user's setting asks for them (§11, research depth).

**Source ladder** (prefer the higher rung; use a lower rung only for what the higher ones don't cover):
1. Official documentation, specifications and standards.
2. Standard textbooks and university course material.
3. Peer-reviewed papers and reviews.
4. The maker's own engineering writing; respected practitioners.
5. Forums and Q&A sites: only for misconceptions and real-world pitfalls.

Record the sources in an HTML comment at the end of the deck. If the repo's instruction files name a place for stored research, also save a short summary there (sources, dates, open doubts):

```html
<!-- SOURCES
researched: 2026-10-07
scope: <URL>; <URL>
correctness: chunk size trade-offs: <URL>; <URL>
dated (F3): "context windows of up to 1M tokens", as of Oct 2026: <URL>
misconceptions: <URL> (learners think RAG retrains the model)
-->
```

**W3 — Build the concept inventory.**
- Give every concept unit an ID `C<topic>.<n>` and its **teaching job** from the skill's `use-cases.md`. Use each job's "Spot it when" lines as the classifier.

  `state-thesis · orient · predict-first · define-term · label-parts · highlight-passage · explain-mechanism · follow-procedure · show-transformation · build-intuition · compare-options · show-quantity · correct-misconception · tell-story · walk-code · demo-interface · list-parallel · recap · check-recall`

- Give each unit a **priority**:
  - `core`: the lesson fails without it. Always taught fully.
  - `supporting`: makes the core clearer or more useful. Taught when the length allows.
  - `extension`: worth knowing later. Listed on the "Go deeper" slide and in the report.
- Also list the **prerequisites**: words, symbols and ideas the topic uses without teaching them. Mark the ones an earlier lesson taught (their glossary wording is reusable, W8).

**W4 — Order the concepts for learning.** Prerequisites first, concrete before abstract, simple before complex, the "why" before the details.

**W5 — Plan the deck.**
- **Topics (N1).** Group the units into topics that the learner would revise as a unit. Aim for **3 or more slides per topic** *(target)*, never 1.
  - The arc slides form a "Start" topic (cover, challenge, map) and a "Review" topic (revisited challenge, recap, glossary, go deeper, question set, answer box).
  - The map slide names the same topics as the topic bar.
- **Slides.** Within the length preset (§11). Arc slides count toward it.
- **Words.** About **50–80 words per content slide, labels included** *(target)*; soft cap 110.
- **Per slide, write down:** its job, its component, its word cap, and the units it covers.
- **Fitting the length:**
  1. All core units first.
  2. Then supporting units, by importance.
  3. If the plan is too long: move facts into figures (V13), merge slides that teach the same idea, say things once (L11).
  4. Still too long: move supporting units to "Go deeper".
  5. The core alone doesn't fit: W7.
- **Write a draft opening challenge** (TE3).

**W6 — Write the term sheet.** For every term:
- the plain meaning (≤ 15 words);
- one everyday comparison, if a good one exists (T10);
- the exact formal wording or notation from the best source;
- the forms that appear (plural, verb).

The term sheet feeds the visible definitions (T3), the glossary (T5b) and the "Words in this lesson" slide. Use the **same gloss text** for a term everywhere, and across lessons: copy it from earlier lessons' glossaries when the term comes back.

**W7 — Confirm only what needs a decision.** Send **one** message, and only if at least one of these applies:
- the canvas gate and the English level, at the first lesson (the skill's shape);
- the length, if neither the prompt nor the record gives it;
- the core units don't fit the chosen length: offer a longer preset, or a narrower scope that the user (or the skill's roadmap) can follow up;
- good sources disagree in a way that changes what to teach (F4), and the right handling is unclear.

Never ask what the record or the prompt already answers. Otherwise, don't stop: build, and put the plan's essentials (topics, slide count, scope) in the report.

**W8 — Draft every concept** with the Concept Pattern (§6), in clear language (§4), with independence (§5). Count words after the first draft, not at the end.

**W9 — Build** the deck with the skill (engine v2, Sketchbook, the record's canvas and board on `<html>`; the template already defines the bridge tokens). Start from the shell; otherwise from the skill's template. Then:
- For each slide, take its job and choose a component from that job's reverse index in `use-cases.md`, from the whole catalog (H2). Vary components across the deck.
- Add the topic bar (N1) and the glossary (T5b), from the shell or `deck-tools/snippets/` (Appendix B).
- Add the `COVERAGE-MAP`, `SOURCES` and `DECK-SETTINGS` comments (F1, W2, "Starting a run").

**W10 — Check** (§9): `validate.py`, `plain_check.py`, coverage map, facts, length, cold read, visual check, checklist. Fix and re-run until clean, or until every remaining flag has a written reason.

**W11 — Deliver** with the short report (§10). In repo mode, the skill then writes its state back.

**W12 — Carry what this lesson learned.** No notes file goes back and forth.
- **Into the DECK-SETTINGS record** (facts about this subject, inherited by the next lesson): new standing decisions, field words (L1), figures a later lesson can reuse (lesson · slide · what). Keep it short.
- **Lessons for every subject** (a better method, a costly problem and what solved it, a note proved wrong, a rule worth adding): list them on the report's "Proposed for the skill" line (§10). The user brings them to a maintenance session, where the rulebooks, the general notes and `deck-tools` change.
- In repo mode the skill also writes its own state back (roadmap, learner notes, answers).

---

## 4. Language rules (G2)

**L1 — Words.**
- Use common words first. A word at the chosen level is fine; a rarer word only when no common word says the same thing.
- A word above the level is either a **term** (teach it, §5), a **field word**, or it gets replaced (L5).
- **Field words** are words the learner already owns from their background or daily life. They count as known. `plain_check.py` has a built-in list (general computing words, plus words a computer-science graduate uses daily); extend it per repo with `--known`.
  - **New field words.** When the checker flags a word, add it to the repo's field words only if all three hold:
    1. the lesson uses it without teaching it;
    2. the learner knows it from their background or everyday use;
    3. it isn't one of the ideas the lesson is about.
  - **When in doubt, it is a term.** Define it (§5). Never add a word to the field list just to pass the checker.
  - **Where they go:** the DECK-SETTINGS record's `field words:` line, so later lessons inherit them. The list only changes what the checker flags; it never removes a word from the deck.
  - **Report** every word added (§10), so the user can veto it.
- Target: **at least 98% of running words known**. A term counts as known on slides where it is defined, glossed, or in the lesson glossary (T5b).

*Why:* readers need about 95% known words for minimal comprehension and about 98% for adequate comprehension; going from 95% to 98% more than halves the unknown words met [HN]. At B2 and C1 the 98% target costs little rewriting and still catches the rare words that slow a second-language reader down; at A2 and B1 it asks for more.

**L2 — Sentences.** One idea per sentence, within **the level's cap** (SKILL.md step 2b): 15 words at A2, 20 at B1, **25 at B2**, 30 at C1. Aim for the level's usual range *(target)*. Split long sentences instead of chaining them with "which", "that", "and", semicolons or colons.

*Why:* Simplified Technical English, a standard written for second-language readers of technical manuals, caps procedures at 20 words and descriptions at 25 [STE]: the B1 and B2 caps. The A2 and C1 caps are design choices.

**L3 — Grammar.**
- Active voice: "The retriever finds the passages", not "The passages are found by the retriever". Use passive only when the actor truly does not matter.
- Talk to the reader with "you" and "we" [M].
- Positive statements. No double negatives.
- From B2, common phrasal verbs are fine when they are the clearest way to say it (*set up*, *find out*); at A2–B1 use the one-word verb. No idioms.
- No noun stacks longer than 3 words: *"vector index refresh schedule" → "the schedule for refreshing the vector index"* [STE].
- Do not drop small words ("the", "a", "that") to save space. Telegraphic text is harder for second-language readers [STE]. Save words with L11 and V13 instead.

**L4 — One concept, one word.** Pick one word for each concept and never switch to a synonym: "retriever" stays "retriever", never "the search part" or "the component". Repeat the noun instead of "it / this / they" when the thing was named more than one sentence earlier.

*Why:* for second-language readers, repeating key content words makes text easier to process; a synonym looks like a new thing [CO][STE].

**L5 — Replace inflated words.** Use the right column (at C1 it is advice: keep a formal word when it is the precise one). **Exception:** if the field uses the word as a technical term (*implement*, *yield*, *allocate*, *instantiate*), it is a term: teach it (§5).

| Instead of | Write |
|---|---|
| utilize, employ | use |
| facilitate | help, make easier |
| commence, initiate | start |
| terminate | stop, end |
| subsequently | then, later |
| prior to | before |
| in order to | to |
| aforementioned | (name it again) |
| the former / the latter | (repeat the noun) |
| respectively | (split into two sentences) |
| via | through, by, using |
| e.g. | for example |
| i.e. | this means |
| etc. | and more (or list them all) |

**L6 — Numbers, symbols, units.**
- Write numbers as digits.
- Write a unit in full the first time it appears in each topic: "5 ms (milliseconds)". Later, the glossary carries it.
- Read every symbol in words the first time it appears on each slide: "x² (x squared)".

**L7 — Headings.** Sentence case, plain words, **2–6 words** *(target)*. A statement or a question: "Why retrieval beats retraining".

**L8 — Abbreviations.** Every acronym is a term (T9). No Latin abbreviations (e.g., i.e., etc., vs., cf.).

**L9 — Questions and feedback follow L1–L8 too.**

*Why:* hard wording in a question tests English instead of the concept [A].

**L10 — Keep the meaning exact.**
- Clear words must not change the claim.
- Words like *usually, typically, always, only, at most, at least* must survive.
- When the clear version loses precision, keep the exact wording in a **Formal version** box (F5) and explain it next to it.

**L11 — Say it once, in its best place.**
- A fact that names or describes a part goes on the figure, next to that part (V13), not in a sentence that repeats the label.
- Don't restate in prose what the figure already shows. The caption says what to *notice*.
- Number steps only in real procedures. Elsewhere use plain bullets.
- Tags and eyebrows only on topic-opening slides.
- Quiz feedback: 4–10 words. The answer box refers to questions by number instead of repeating them.
- Don't gloss a term the slide's figure already explains.

*Why:* words that don't serve the learning goal lower learning (coherence), and words placed next to the parts they describe save search effort (spatial contiguity) [M].

---

## 5. Terms and independence (G3)

**T1 — Idea first, name second.** First explain the idea in everyday words on a concrete example. Then attach the name: "This is called `<dfn>chunking</dfn>`." Never open a slide with a term the slide has not explained, unless the glossary (T5b) carries it.

*Why:* learners who met concepts in everyday language before the technical terms understood more and used the terms better. The study was small, but it agrees with the pre-training principle [CFA][M].

**T2 — Teach every term the scope needs.** The terms the field uses (in documentation, papers, interviews, job tasks) are taught, not avoided.

**T3 — Definition (the defining slide).** For each term, on the slide that teaches it:
1. the plain meaning in ≤ 15 words (from the term sheet);
2. a picture or diagram (often the slide's main figure);
3. one everyday comparison, if a good one exists (T10);
4. a **Formal version** with the exact wording from the best source, only when F5 requires it.

Mark the defining use with `<dfn>`. Add `data-forms` for irregular forms: `<dfn data-forms="indices">index</dfn>`.

**T4 — New-term load.** At most **2 new terms per slide** *(target)*, 3 as a hard limit. At most **4 new terms before the next check question or topic boundary**.

*Why:* working memory holds about 3–5 new chunks at a time, and each new term is one chunk [WM].

**T5 — Every term is explained where it is used.**

| Where the term is used | How |
|---|---|
| Its defining slide | **Visible** definition (T1, T3). Never hidden. |
| Its **first use in another topic**, when that slide's main sentence makes no sense without it (**load-bearing**) | A **visible** short gloss, inline and ≤ 8 words: `the retriever <span class="gloss" data-for="retriever">(the part that finds passages)</span>` |
| Anywhere else | The **glossary card** (T5b), added automatically at the term's first use on each slide. Or a hand-made anchored gloss (components §24) for a supporting term that isn't in the glossary. |

When a lesson uses on-demand glosses, the cover's hint line says so: "Tap dotted words for their meaning."

*Why:* revision happens by topic: the learner jumps in with the topic bar (N1). So a topic must stand alone, and a load-bearing term needs its meaning visible where a topic starts using it. On-demand glosses work for second-language readers [GL2], but optional content is often never opened, so a slide's main sentence must not depend on one.

**T5b — The lesson glossary.**
- The term sheet's cross-topic terms and every acronym go on one slide, **"Words in this lesson"**, as `<dl id="glossary" class="glossary">`:

  ```html
  <dt data-forms="embeddings">embedding</dt><dd>a list of numbers that stands for a text's meaning</dd>
  ```

- A small script (Appendix B) turns the first use of each glossary term on every other slide into an anchored gloss card. It skips headings, figure labels, buttons, `<dfn>` and formal text, and it skips the term's own defining slide.
- The glossary slide doubles as the revision sheet (TE8).
- `plain_check.py` reads the glossary and treats its terms as glossed on every slide.
- Keep each entry ≤ 12 words, in the term sheet's wording (W6). Acronym entries give the full form first: "RAG — retrieval-augmented generation: …".

**T6 — No back-references.** Never write "as we saw", "recall that", "the previous slide", "mentioned above" or "see slide 4". Restate the needed fact in one short sentence, or rely on the glossary card. *Exception:* the challenge-revisited slide may say "your first answer", but it must restate the full problem.

**T7 — Every topic stands alone, and so does every lesson.** Never write "see Part 1" or "as in lesson 2". An earlier lesson's idea that this lesson needs is restated in one line, or carried by the glossary.

**T8 — "What you need first."** For knowledge the topic assumes:
- When one line is enough, put it in the glossary.
- When the lesson leans on the prerequisite across several topics, teach only the pieces it uses, on a "Background" slide in the Start topic (the skill's "Ground the newcomer" slide). If an earlier lesson taught it, keep that lesson's wording.

*Why:* knowing the names and basic meaning of the key parts before the main explanation frees attention for how the parts work together (pre-training) [M].

**T9 — Acronyms are terms.**
- At the first use in each topic, write the full form and the plain meaning, then the short form: "retrieval-augmented generation (RAG): answering with passages found first".
- On other slides, the glossary card carries it.
- Every acronym the lesson uses goes in the glossary.

**T10 — Analogies: map them and say where they stop.**
1. Name the familiar thing.
2. Show which part matches which (a two-column table or a labelled picture).
3. Say where the comparison stops working.
4. Return to the real concept.

Use one analogy per concept and keep it the same through the lesson. Use an analogy only where it carries something the figure alone does not.

*Why:* analogies help, but an unmapped analogy can plant a misconception, and the "where it breaks" step is the one most often skipped [TWA].

---

## 6. Teaching rules (G4)

### The Concept Pattern

Use this for every **core concept**, in this order. It is the skill's click trio (structure · mechanism · application) with research-backed steps added. Each step names its teaching job in the skill's vocabulary, so the component comes from that job's reverse index in `use-cases.md`. Steps share slides; a typical concept takes **1–3 slides** *(target)*.

| # | Step | What to write | Required? | Why |
|---|---|---|---|---|
| 1 | **Ask** · `predict-first` | A one-line prediction question before teaching | Optional; use it for counter-intuitive concepts | Trying to answer before learning improves later learning, when teaching or feedback follows [PT] |
| 2 | **Plain idea + one concrete case** · `define-term` or `build-intuition` | The idea in everyday words, shown on one specific example | Required | Content first [CFA]; concrete before general [CF] |
| 3 | **Name it** · `define-term` | `<dfn>` + definition (T3) | Required | T1 |
| 4 | **Picture** · `label-parts`, `explain-mechanism` or `compare-options` | The visual chosen by V7, with labels next to the parts (V2), colour links where useful (V8) and a "Notice:" caption. For a process, a step-through (V9) | Required. The picture carries the facts (V13) | Words + pictures beat words alone [M][SIG] |
| 5 | **Why it works** · `explain-mechanism` | The mechanism | Required | The skill's click trio |
| 6 | **Worked example** · `follow-procedure`, `walk-code` or `show-transformation` | Step by step, each step with a short label. Then a similar problem for the learner | Required for procedures, calculations and code | Studying solved examples beats solving alone for newcomers; step labels show the reusable steps [WE][SG] |
| 7 | **Common mistake** · `correct-misconception` | "Many learners think X. This is not true, because Y. The correct idea is Z." | Required where research found a misconception (W2) | Texts that name and refute a misconception correct it better than plain explanation; re-test it later [RT] |
| 8 | **Check** · `check-recall` | One quick question with feedback that explains why each wrong option is wrong | At the topic's end (TE4) or in the question set | Practice testing with feedback is a top-utility study technique [D][R] |

For a pure definition, steps 2–5 (and 8) are enough. For **supporting** concepts, steps 2–4 are enough.

### Teaching rules

**TE1 — Small steps.** One idea per slide. Split any slide that teaches two unrelated things; merge two slides that teach one idea [R][M].

**TE2 — Concrete, then general.** A specific example, then the general rule, then the formal notation, saying in words what each symbol stands for. *Caveat:* the evidence is strongest in mathematics; for a pure definition, a direct definition plus an example is fine [CF].

**TE3 — The opening challenge** (skill arc, step 2) must:
- be answerable from everyday knowledge, or from an earlier lesson's idea restated in the question;
- be written one level below the lesson's English level;
- ask for a **committed answer** (a tappable MCQ);
- be "attemptable but uncertain", as the skill says;
- ideally touch several topics, so the revisited challenge pulls them together.

*Why:* guessing before teaching helps [PT]; a self-paced deck cannot rescue a hopeless attempt, so the challenge must be attemptable [PF].

**TE4 — Topic checks.** A setting (§11), **on** by default: one quick question at the end of each content topic, with feedback. Core checks should be answerable by most careful readers (about 80% *(target)*); save hard items for `[stretch]` [R].

*Why:* retrieval practice is one of the highest-utility study techniques [D], and spacing questions through the lesson beats saving them all for the end.

**TE5 — "Why…?" prompt.** At least one per lesson: an open question in the answer box. When space allows, also one in the deck: a text box and a model answer revealed after typing, using one of the skill's legal depth mechanics.

*Why:* prompting learners to explain why something works has a medium effect; question-form prompts beat multiple-choice prompts [SE].

**TE6 — Fade support across lessons.** Early lessons on a skill: fully worked examples. Later lessons on the same skill: partly worked examples, then full problems. The learner notes (the skill's) show when to fade.

*Why:* worked examples help newcomers but become redundant as expertise grows (expertise reversal) [WE].

**TE7 — Question set** (the skill's end-of-lesson set, 3–6 items *(target)*, plus the skill's personalization). Each item:
- has a stem that is a full question, worded positively: no NOT / EXCEPT, no "all of the above", no "none of the above";
- has 3–4 options of similar length and grammar, and one clearly best answer;
- uses wrong options taken from real misconceptions (W2, step 7);
- stands alone: it restates any fact it needs;
- has short feedback (4–10 words, L11) that says why.

Across the set:
- at least half the items ask the learner to **apply or explain**, not only recall;
- the lesson's main misconception is re-tested (the revisited challenge counts);
- keep the skill's 1–2 `[stretch]` items;
- the answer box lists the questions by number, plus one open "Why…?" question (TE5) [MCQ][A].

**TE8 — Recap and revision sheet.**
- Keep the skill's "you can now …" capabilities slide, with a one-line closing ("Next: …" when the skill's roadmap names the next step).
- The **glossary slide** (T5b) is the revision sheet.

**TE9 — Earlier lessons.** The skill's personalization re-tests earlier misses (its learner notes). Any such item restates the facts it needs (T7), and its feedback re-teaches the idea in one line.

*Why:* spaced retrieval is one of the highest-utility techniques [D]; self-contained wording keeps T7.

**TE10 — Examples.** Correct, specific and real: real tools, real numbers, real cases from the field, dated when they can change (F3). No jokes or fun facts that don't serve the concept (V1).

---

## 7. Correctness and scope (G1)

**F1 — Coverage map (required).** Every inventory unit maps to the slide(s) that teach it, or to "Go deeper" for an extension or a supporting unit that didn't fit. Put the map at the end of the deck as an HTML comment (`validate.py` strips comments before checking):

```html
<!-- COVERAGE-MAP
topic: Retrieval-augmented generation · lesson 3 · length: medium (19 slides)
C1.1 core define-term "retrieval-augmented generation"   -> slide 5
C1.2 core explain-mechanism "embed, retrieve, generate"  -> slides 6, 7 (builds)
C2.1 core compare-options "chunk size trade-offs"        -> slide 9
C2.2 supporting show-quantity "recall vs chunk size"     -> go deeper (length)
C3.1 extension "graph-based retrieval"                   -> go deeper
-->
```

Before delivering, confirm that every core unit maps to a taught slide.

**F2 — Every load-bearing claim has a source.** Each claim the learner could rely on is backed by the sources in the `SOURCES` comment (W2). If you could not confirm a claim, don't teach it as fact: drop it, or mark it "unconfirmed" and list it in the report.

**F3 — Date what can change.** Versions, model names, prices, limits, rankings, market shares and "the latest X" carry a visible date: "(as of Oct 2026)". Teach the stable idea first and the dated example second, so the lesson ages well.

**F4 — When good sources disagree.**
- Teach the best-supported view (higher on the source ladder, more recent for fast-moving facts).
- Show the disagreement in one visible line: "Some sources say X; the official documentation says Y."
- List it in the report. When it changes what to teach and the handling is unclear, ask (W7).

**F5 — Keep exact forms exactly.**
- Formulas, notation, code, official names of algorithms, laws, standards and APIs are written exactly.
- When the clear wording would lose something the field relies on (a standard's definition, a spec's wording), show the exact wording in a **Formal version** box (`class="formal"`) and explain it beside it with a "How to read it" line.

```html
<div class="aside formal"><b>Formal version:</b> …exact wording from the standard…</div>
<p>How to read it: <span class="formal">idempotent</span> = doing it twice has the same effect as once.</p>
```

- In Sketchbook decks, the ink marks (§28) can circle and underline the load-bearing words of the formal sentence in order.

**F6 — Code.**
- Code is complete enough to run, in the language and style the field uses.
- **Run it** before delivering, and show real output. If code execution is off, say so in the report and mark the code "not run".
- Explain each block with a step label and plain comments.
- When values change over time (loops, recursion, state), add a **trace table**.

**F7 — Math.**
- Show the formula exactly, with a "How to read it" line.
- Give a symbol table:

  | Symbol | Read as | Meaning | Unit |
  |---|---|---|---|

- Then a worked numeric example (Concept Pattern step 6), with its numbers in a table. **Compute the numbers with code**, not by hand.

**F8 — "Go deeper" slide** (a setting, §11, on by default). In the Review topic:
- the 3–5 best sources for going further, each with one line on what it adds and its rung on the source ladder;
- the extension units and any supporting units that didn't fit, each in one line.

*Why:* the lesson is one sitting; the learner owns the rest of the path. Good next sources save the next search.

**F9 — "Trim" means emphasis, never deletion.**
- The skill's catalogue often advises showing less at once ("three load-bearing rows", "the range that matters", at most six labels on a figure). Follow that advice for **what comes first and largest**.
- Everything else a core unit needs is still taught on the visible layer: in further builds (§25), in a second pane, or in a table.
- Never move core content into hover/tap depth. Record where each part went in the coverage map.

---

## 8. Visual and layout rules (adds to the skill's style system)

**V1 — Every image explains.** Each illustration, icon scene or animation shows the concept or its example, never only a mood. When the skill's scene-brief procedure invents a "skin", the skin must be the concept's own example.

*Why:* interesting but irrelevant extras lower learning, and they hurt most when the learner controls the pace, which is exactly a self-paced deck [SD][M].

**V2 — Labels next to the parts.**
- Words sit on or right beside the part of the picture they name: the skill's labels on the figure (§22), not a numbered legend.
- Every part name must be readable without opening anything. Past about six new labels, split the figure into builds (§25) or slides.
- When labels arrive with builds, put `data-build` on a wrapper layer that holds the labels, never on a label itself. The build style resets the label's position transform.
- One SVG path per arrow: a path with several subpaths gets an arrowhead only at its last end [M].

**V3 — Signalling.** One consistent look for defined terms and one for the key sentence of each slide. Add this CSS to the deck's style block (never to the engine). It reads the skill's bridge tokens (`style-system.md §7`):

```css
dfn { font-style: normal; font-weight: 700; color: var(--k-ink);
      background: var(--k-hi); border-radius: 3px; padding: 0 .12em; }
.gloss { color: var(--k-soft); }
.formal { font-style: italic; }
```

Keep the linked colours `--k-a`, `--k-b`, `--k-c` for linked figures (V8), not for terms, so a colour always means "this word = that part".

**V4 — Readable text blocks.** Lines no longer than about 70–80 characters, line height at least 1.5, left-aligned (never justified), sentence case [W].

**V5 — Visible words per slide.** About **50–80** *(target)*; soft cap 110 (the checker's default). More than that → move facts into the figure (V13), then split. A slide that shows a real table or code listing may exceed the cap; note it in the report.

*Why:* second-language readers read English more slowly than the native average of about 238 words per minute [RS], and the skill budgets 60–90 seconds per slide, which must also cover the picture.

**V6 — Colour is never the only signal.** Pair it with a label, shape, position or fill pattern.

**V7 — Choose the visual by the teaching job.**
- Each slide's job (W3) points to its components in `use-cases.md`. Pick from the top of that list unless the content argues for another, and vary components across the deck.
- Two jobs the catalogue leaves to you: code that changes values → a trace table (F6); how several concepts relate → a map with labelled links (V10).
- **Use a component only when it does a job text cannot.** Builds for an order of events; the magic board when the *same* items move; a draggable number or lab only when a variable really varies, with a resting state that shows the answer (V12).
- A good visual replaces descriptive sentences. It does not replace the "why" sentence or the labels.

*Why:* words and pictures together beat words alone, but pictures alone are not the proven condition [M].

**V8 — Link the words to the picture.** Use the skill's linked figure (§23) where one sentence names 2–3 parts of one picture: each key term has the same colour in the sentence and on its part, and touching either lights both. At most three linked colours. Add a one-line caption that says what to notice.

*Why:* signals that connect text and picture improve comprehension, most for learners new to a topic [SIG].

**V9 — Processes are step-throughs, not autoplay.**
- Show a changing process one step per key press with the skill's builds (§25): 3–5 builds per slide, each caption arriving with its strokes.
- Captions **accumulate**, so the finished slide is a complete revision view.
- When the same pieces move from one state to another (memory blocks, a sorted list, algebra, refactored code), use the magic board (§26).
- In Sketchbook decks, the eraser (§29) shows a misconception being replaced; the better idea always comes last.
- Motion only when the change itself is what must be learned, and always under the learner's control.

*Why:* animations beat static pictures only modestly, mainly when the change itself must be learned; learner-paced steps fix the transience of autoplay [AN][M].

**V10 — Show how ideas connect.** For the `orient` and `recap` jobs, prefer components that draw links: the flow recap (§15) with arrow labels that say how ideas connect ("causes", "is a kind of", "needs"), or the map slide (§3). The map slide names the lesson's topics (N1).

*Why:* studying ready-made concept maps beats studying text [CM].

**V11 — One visual, one job.** Each visual answers one question. If a figure tries to show everything at once, split it across slides or builds.

**V12 — Interactives are a bonus, never the lesson.** For the reactive sentence (§27) or a lab widget (§32b), the resting state already shows the key result in words and numbers.

*Why:* many readers never touch interactive elements, so anything that appears only after interaction is invisible to them.

**V13 — Facts live on the figure.** When a sentence would only name a part, say where it is, or give its property, write it as a label beside that part instead. The prose that remains carries the mechanism, the "why" and the conditions.

*Why:* spatial contiguity [M]. It also removes the repeated names a separate list would need.

**V14 — Legible at every width.**
- Figure labels scale with their figure: size them in container query units with a minimum size (Appendix B). Display faces like Caveat become hard to read below about 1rem on a laptop.
- Labels on patterned fills get a backing chip.
- Check a sample of slides at phone width (Q7).

### Navigation

**N1 — A topic bar instead of slide dots.**
- **What it shows:** a row of **rounded-corner rectangles**, one per **topic**, each with the topic's name inside.
- **Length = size:** each rectangle's length is proportional to the number of slides in its topic.
- **Only the current topic is marked.** No progress indicator inside a topic: the thin progress line is hidden, the current rectangle is highlighted, and topics already passed get a light fill.
- **Click to jump:** clicking a rectangle goes to the topic's first slide.
- **Topics:** mark the first slide of each topic with `data-sec="Name"`. 3 or more slides per topic *(target)*; 2 only with a very short name; never 1. Names of 1–3 words, ≤ 24 characters, matching the map slide.
- **Phones:** the rectangles keep their lengths but drop their text; the current topic's name shows just above the bar.
- **Same in every lesson:** later lessons copy the topic bar's code from the shell unchanged. Appendix B's code is for a deck that has none yet. In Sketchbook, it reproduces the reference decks' bar exactly.
- **Build:** keep the engine untouched; keep the hidden dots element (the engine writes to it); add the topic bar after the engine.
- `plain_check.py` lists the topics and flags 1-slide topics.

*Why:* dozens of dots read as a to-do list. Topic blocks show the lesson's structure, which signals its organisation [M], and each block is a natural revision unit. Showing no in-topic progress is a design choice, not a research finding.

### House style

The user wants every lesson to look and read like their **reference decks**: the lecture decks built with `slides-rulebook.md` (Sketchbook, chalkboard canvas). These rules say what to take from them and what not.

**H1 — The look comes from code, not from a description.** The canvas and board come from the DECK-SETTINGS record. The first lesson in a repo takes its shell from the newest reference deck when the canvas matches; later lessons take it from the newest lesson ("Starting a run"). Never restyle the shell by hand, and never hand-edit a board's colours.

**H1b — Bringing an older shell to v1.3 (once).** A shell from before lesson-deck-builder v1.3 has its own colour tokens (the old slate `#2B322D`) and no `data-canvas` on `<html>` (`validate.py` notes it). Before the first v1.3 lesson built on it:
1. Replace the shell's token rules in `:root` (canvas colours, pens, marker, bridge tokens) with the token section of the skill's `assets/template.html`: the paper block, the chalkboard blocks for all six boards, and the bridge block.
2. Set `data-canvas` and `data-board` on `<html>` from the record.
3. Change hard-coded colours in the shell's shared SVG defs (arrowheads, patterns) to `style="stroke:var(--ink)"`, `var(--red)` and so on, as the template does.
4. Keep everything else unchanged, run `validate.py`, and look at two slides. The next lesson inherits the updated shell; never repeat this step.

**H2 — Inspiration, not a menu.**
- Study how the reference decks match components to teaching jobs. For example: builds for a process, labels on the figure for parts, the magic board when the same items move, ink marks for a formal definition, the eraser for the main misconception, a linked figure for "three parts of one picture".
- Reuse a pattern when the job matches. Choose a different component from the skill's full catalog when it fits the job better, including components the reference decks never used.
- Vary components across the lesson. Never use a component because a reference deck had one, and never avoid one because none did.

**H3 — Figure first.** Most content slides are built around one figure that carries the facts (V13), with one or two sentences for the mechanism and a "Notice:" caption. A slide of bullets alone is the exception and needs a reason (a short list that no picture improves).

**H4 — The same rhythm.** The arc of §2, the topic bar (N1), the glossary slide (T5b), short headings that state the idea (L7), 50–80 words per slide (V5), one "alive" element per slide at most (the skill's line-boil, §31).

**H5 — Borrow patterns, never content.** Don't copy a reference deck's slides, wording or figures into a lesson on another topic. A figure skeleton (for example a layered stack or a timeline) may be reused when it fits the new content, redrawn for it.

---

## 9. Quality checks before delivery

**Q1 —** `python scripts/validate.py deck.html` (the skill's validator) passes. Its "more than 20 slides" note is expected for long lessons.

**Q2 —** `python plain_check.py deck.html --max-level <level> --cs-grad --known field-words.txt` (Appendix A). Fix every flag, or list it in the report with a reason.
- *If you cannot run code:* say so in the report's "Checker" line; check L1, L2, T5, T6 by a careful read instead; never report a percentage you did not measure. The same goes for `validate.py`.

**Q3 — Coverage.** Every core unit maps to a taught slide; every other unit maps to a slide or to "Go deeper" (F1).

**Q4 — Cold read.** Pick 2 random topics; read each as a learner who opened only that topic. Then pick 3 random slides: is every term explained, visibly or by its glossary card? If not, add a visible gloss (T5) or restate the missing fact.

**Q5 — Checklist.**
- [ ] Every term: idea first, then `<dfn>`; formal version kept where F5 requires it.
- [ ] Every core concept follows the Concept Pattern; procedures, calculations and code have a labelled worked example and a practice problem.
- [ ] Misconceptions found in research are refuted, and the main one is re-tested.
- [ ] The opening challenge is attemptable (TE3); the question set follows TE7; topic checks follow TE4.
- [ ] No decorative visuals (V1); every component does a job text cannot (V7); components vary (H2).
- [ ] Nothing core is hidden behind hover/tap or trimmed away (F9).
- [ ] Topic bar present; topics named as on the map slide; no 1-slide topic (N1).
- [ ] Glossary slide present; every acronym and cross-topic term is in it (T5b, T9).
- [ ] Canvas and board match the DECK-SETTINGS record (`data-canvas`, `data-board` on `<html>`); the shell's code is unchanged, apart from a one-time H1b update (H1).
- [ ] `COVERAGE-MAP`, `SOURCES` and `DECK-SETTINGS` comments present.

**Q6 — Length.** The slide count fits the preset (§11), and visible words per content slide average about 50–80.

**Q7 — Visual check.**
- Look at every slide **fully built** at laptop size (about 1280 × 800), and at a sample of slides at phone width (about 390 px).
- Check that labels don't overlap lines or each other, every arrow has its head (V2), nothing overflows sideways, and the topic bar marks the right topic.
- Step through every build once with the keyboard. Click each quiz once.

**Q8 — Facts.** Every load-bearing claim has a source (F2); every changeable fact has a date (F3); every disagreement is shown (F4); all code ran, and all worked numbers were computed (F6, F7).

---

## 10. Delivery report (chat, keep it short)

```
Lesson <NN>: <topic> · length <preset>: <x> slides, about <m> min · <w> words.
Topics: <name · slides> | …
Scope: core <a>/<a> taught · supporting <b>/<c> · in "Go deeper": <list or "none">.
Research: <n> sources (<k> official or textbook) · stored research reused: <yes/no> · disputes: <list or "none"> · dated facts: <n>.
Checker: word coverage <c>% at <level>; kept flags: <word or rule — reason>.
Code: <ran / not run — why>.
Shell: <file, or "skill template"> · reference decks: <names or "none">.
Settings changed: <list or "none">. Field words added: <list or "none"> (L1).
Skill mismatches: <parts of this file that did not match the skill, or "none">.
Departures: <procedures of this file done another way, and why, or "none">.
Proposed for the skill: <lessons for every subject (W12), or "none">.
```

---

## 11. Settings the user can change

| Setting | Default | Other options and their effect |
|---|---|---|
| Length | **Asked once per repo, then the repo default** | **Short:** 10–14 slides, about 15 minutes; recap and glossary may share a slide, and "Go deeper" moves into the answer box. **Medium:** 15–22 slides, about 25 minutes. **Long:** 23–32 slides, about 40 minutes. **Topic:** as many slides as the core and supporting units need, with the per-slide caps (V5) as the only limit. All counts are *(target)* and include the arc. |
| English level | **B2** (asked at the first lesson) | **A2 · B1 · C1:** SKILL.md step 2b sets the words and the sentence caps; the checker runs with `--max-level`. Recorded as `level:` in DECK-SETTINGS. |
| Field vocabulary (L1) | **Built-in list** (general computing + words a computer-science graduate uses daily) | **Repo list:** words in the DECK-SETTINGS record, passed with `--known`. **Smaller:** run the checker without `--cs-grad`. |
| Research depth (W2) | **Thorough, capped:** 10–15 strong sources | **Deep:** research agents per concept; most complete, several times the cost. **Reuse:** decided by the repo's instruction files, not by this setting. |
| Topic checks (TE4) | **On** | **Off:** retrieval only from the challenges and the question set; saves a slide per topic. |
| "Go deeper" slide (F8) | **On** | **Off:** sources stay in the `SOURCES` comment only. |
| Glossary (T5b) | **On** | **Off:** a visible or anchored gloss on every slide that uses a term; costs about 5 words per term per slide. |
| Navigation (N1) | **Topic bar** | **Dots:** the skill's default navigation. |
| Canvas and board | **From the DECK-SETTINGS record** | Paper, or any of the six chalkboard boards, through the skill's canvas gate. Changing the board only recolours (one attribute); changing to paper breaks the match with the chalkboard reference decks (H1). |
| Arabic support | **Off** | **On:** each definition and glossary entry adds the Arabic term in one line [GL]. |

---

## 12. Evidence base

| Tag | Source | Supports | Strength and caveats |
|---|---|---|---|
| [R] | Rosenshine (2012), *Principles of Instruction* | Small steps, worked models, frequent checks, ~80% success | Synthesis of classroom and cognitive research; widely used |
| [M] | Mayer (2020), *Multimedia Learning*, 3rd ed. | Multimedia, coherence, signalling, spatial contiguity, segmenting, pre-training, personalization | Many experiments; mostly short lessons |
| [D] | Dunlosky et al. (2013), *Psychological Science in the Public Interest* | Practice testing and distributed practice rated highest utility; rereading and highlighting low | Large review |
| [HN] | Hu & Nation (2000); Laufer (1989); Schmitt et al. (2011); Laufer & Ravenhorst-Kalovski (2010) | 95% known words = minimal, 98% = adequate comprehension | Replicated; measured on running texts, so the checker judges coverage at deck level |
| [STE] | ASD-STE100 Simplified Technical English | 20/25-word sentence caps, one word one meaning, no dropped articles | Industry standard built for second-language readers |
| [A] | Abedi (2009); Sato et al. (2010), IES/NCEE report | Simplifying the wording of test items helps second-language readers without changing what is measured | Effect real but small |
| [WE] | Sweller; Kalyuga et al. (2003); Renkl et al. | Worked-example effect, expertise reversal, faded examples | Strong for newcomers; fades with expertise |
| [SG] | Margulieux & Catrambone (2016); Morrison, Margulieux & Decker | Subgoal-labelled worked examples in programming and STEM | Several studies; more replication called for |
| [PT] | Richland, Kornell & Kao (2009); Kornell, Hays & Bjork (2009) | Pretesting effect: failed attempts help when followed by teaching or feedback | Replicated, mostly with factual material |
| [PF] | Sinha & Kapur (2021), *Review of Educational Research* | Problem solving before instruction helps conceptual learning and transfer | Depends on design fidelity and prior knowledge |
| [CF] | Fyfe et al. (2014); Kokkonen & Schalk (2021) | Concreteness fading | Promising in maths; may not generalize to every domain |
| [CFA] | Brown & Ryoo (2008), *Journal of Research in Science Teaching* | Everyday language before scientific terms | One small randomized study; fits pre-training |
| [TWA] | Glynn (1991) and later work | Teaching-with-analogies steps, including where the analogy breaks | Widely used |
| [RT] | Schroeder & Kucera (2022), *Educational Psychology Review* | Refutation text, g ≈ 0.41 | Some drift back at delayed tests → re-test |
| [SE] | Bisra et al. (2018), *Educational Psychology Review* | Self-explanation prompts, g ≈ 0.55; question-form prompts beat multiple-choice prompts | Mostly undergraduate samples |
| [MCQ] | Haladyna, Downing & Rodriguez (2002) | Multiple-choice item-writing guidelines | Consensus guidelines |
| [SD] | Sundararajan & Adesope (2020) | Seductive details lower learning, g ≈ −0.33; worse in learner-paced lessons | 58 studies; mostly short lessons |
| [CO] | Crossley, Allen & McNamara (2011) and related work | Readability formulas are weak proxies for second-language readers; word overlap (cohesion) helps them | Why the checker uses word lists, not Flesch scores |
| [RS] | Brysbaert (2019), *Journal of Memory and Language* | ~238 wpm for native non-fiction reading; slower for second-language readers | Second-language estimate from a single study |
| [GL] | "The relative effects of L1 and L2 glosses on L2 learning: A meta-analysis", *Language Teaching Research* | First-language glosses beat English-only glosses, especially for beginners | Mostly immediate vocabulary outcomes |
| [GL2] | Abraham (2008), *Computer Assisted Language Learning* | On-demand glosses: medium effect on reading comprehension, large on word learning | Voluntary use in the wild may be lower |
| [WM] | Cowan (2001), *Behavioral and Brain Sciences* | Working memory holds about 3–5 chunks | Well established |
| [W] | WCAG 2.x, success criterion 1.4.8 | Line length ≤ 80 characters, line spacing ≥ 1.5, no justified text | Accessibility standard (AAA) |
| [SIG] | Richter, Scheiter & Eitel (2016), *Educational Research Review* | Signalling text–picture links improves comprehension and transfer | Small-to-medium effect; strongest for low prior knowledge |
| [AN] | Höffler & Leutner (2007); Berney & Bétrancourt (2016) | Animation vs static pictures | Modest effects; benefit mainly when the change itself must be learned |
| [CM] | Nesbit & Adesope (2006); Schroeder et al. (2018) | Studying concept maps beats text; constructing them helps more | Larger for lower-knowledge learners |
| — | CEFR-J Wordlist 1.5 (Tono Laboratory, TUFS) | Word levels used by `plain_check.py` (A1–B2) | Free for research and commercial use with citation |

### Researched and deliberately not turned into rules

- **Flesch / grade-level formulas:** weak proxies for second-language readers; the checker uses a CEFR word list and sentence length instead [CO].
- **Redundancy principle** (don't repeat narration as on-screen text): it applies to narrated media; these decks have no narration.
- **"More animation is better":** the benefit over well-designed static frames is modest, so V9 prefers learner-paced step-throughs.
- **Full productive failure:** it needs a teacher who builds on the learner's attempts; a self-paced deck can't, so TE3 uses the lighter pretesting form.
- **The level defaults (B2 here), the A2 and C1 sentence caps, the checker's C1 frequency rule and the length presets** are choices, not research findings. The 98% coverage target applies at any level [HN].
- **The source ladder and the 10–15 source cap** are working rules for reliable, affordable research, not findings from learning research.

---

## Appendix A — `plain_check.py` (shared with the slides rulebook)

**What it checks, per slide:** visible word count; sentence length; words above the vocabulary ceiling or not on the list (field words allowed); terms used without a gloss (glossary terms count as glossed); unexpanded acronyms; back-reference phrases; banned question wording; likely passive voice.

**At deck level:** word coverage (target ≥ 98%); the topic list (N1); the deck's total readable words.

**The HTML contract it relies on:**

| Markup | Meaning |
|---|---|
| `<dfn>term</dfn>` | The defining use of a term (T1, T3) |
| `<dfn data-forms="indices">index</dfn>` | Irregular forms of a term |
| `data-for="term"` on any element | A gloss for that term on this slide (T5, T9); on an anchored gloss, put it on the dotted `.gl-t` word |
| `<dl id="glossary"> <dt data-forms="…">term</dt><dd>…</dd>` | The lesson glossary (T5b): its terms count as glossed on every slide |
| `.gl-card` / `role="tooltip"` (components §24) | Language-checked, but not counted as visible words (V5) |
| `.lf-pin` (components §22) | Each figure label is read as its own piece |
| `class="formal"` | Exact wording: skipped by the language checks (F5) |
| `<code>`, `<pre>`, `<kbd>` | Skipped by the language checks |
| `<svg>`, `<math>`, `<script>`, `<style>` | Skipped and not counted |
| `data-why="…"` | Quiz feedback: checked and counted |
| `<template>` runs (magic board) | Only the last state of each run is checked and counted |
| `data-sec="Name"` on a slide | The first slide of a topic (N1) |

**How to run it:**

```bash
pip install wordfreq            # add --break-system-packages if pip asks (setup_tools.sh does it)
python plain_check.py deck.html --max-level B2 --cs-grad                         # the default level
python plain_check.py deck.html --max-level B2 --cs-grad --known field-words.txt # plus the record's field words (L1)
python plain_check.py deck.html --max-level C1 --cs-grad                         # another level (§11)
```

On its first run, it downloads the CEFR-J word list from GitHub and saves it next to the script. If the download fails, it prints the link so you can save the file by hand. Exit code 0 = clean, 1 = notes to fix or justify.

**Limits (read the output with judgment):**
- The lemmatizer is simple; a rare irregular form may be flagged wrongly.
- Capitalized words in the middle of a sentence are treated as names and listed for you to check, not counted.
- The passive-voice check is a hint, not a rule.
- It cannot judge meaning, or whether a term is load-bearing (T5). Q3–Q5 still need a careful read.
- The glossary cards are added at runtime. The checker trusts the glossary list; Q7's walk-through confirms that the cards appear.

**The script:** the shared `deck-tools/plain_check.py` (one checker for every route since lessons-rulebook 2.0). `setup_tools.sh` copies it into your working folder. Run it with the DECK-SETTINGS level and `--cs-grad` (the field words of a computer-science graduate, L1). Open it only to change it.

---

## Appendix B — Topic bar (N1) and deck glossary (T5b)

Both work on both canvases and every board: they read the bridge tokens (`style-system.md §7`) and the canvas tokens the template defines. Both go **after** the engine, inside the deck's single `<script>`. Neither edits the engine.

### B1. Topic bar

HTML, replacing the skill's nav block (keep `#dots`, because the engine writes to it):

→ `deck-tools/snippets/topic-bar.html`

Mark topics on the slides: `<section class="slide active" data-sec="Start">`, `<section class="slide" data-sec="Storage">`, and so on.

CSS (at the end of the style block):

→ `deck-tools/snippets/topic-bar.css`

Script (after the engine):

→ `deck-tools/snippets/topic-bar.js`

### B2. Deck glossary

The glossary slide (in the Review topic, before "Go deeper" and the question set):

→ `deck-tools/snippets/glossary-slide.html` (title the slide "Words in this lesson")

CSS:

→ `deck-tools/snippets/glossary.css`

The cards reuse the skill's anchored-gloss CSS (components §24); paste it if the deck has no anchored glosses yet.

Script (after the engine):

→ `deck-tools/snippets/glossary.js`

### B3. Figure labels that scale with their figure (V14)

Add this to the §22 label CSS. Each label's size then follows the figure's own units, with a floor for small screens:

→ `deck-tools/snippets/figure-labels.css`

