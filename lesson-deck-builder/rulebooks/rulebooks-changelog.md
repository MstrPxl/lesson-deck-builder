# Rulebooks changelog

The version history of `slides-rulebook.md`, `questions-rulebook.md` and `lessons-rulebook.md`. It moved out of the rulebooks in slides-rulebook 1.9 and questions-rulebook 1.3, so that a run no longer reads it. **Not needed for a run:** read it to see why a rule looks the way it does. Newest first. Earlier entries keep their wording, including appendix names from before the code moved to `deck-tools`.

---

## slides-rulebook.md

**Changes in 2.0.1 (23 October 2026).**
- **A course deck without its new lecture:** when only a deck of the course is attached, ask for the new chapter's PDF (or PPTX) before planning or building, instead of falling back to the lesson route ("Which case is this?", SKILL.md step 0b). Requests to change the attached deck itself are not affected.

**Changes in 2.0 (23 October 2026): one-line start, bundled files, English level A2–C1, course memory in the deck.**
- **The file ships inside the skill** (`rulebooks/`, lesson-deck-builder v1.4) with the questions and lessons rulebooks, the general notes and `deck-tools`. The skill routes an attached lecture here by itself, so the user sends one line ("use /lesson-deck-builder to explain the attached file") with the lecture and, from the second deck on, the previous deck. "Starting a run" lists the inputs instead of the attachments.
- **No Markdown goes back and forth.** The course notes file is retired: its facts (the lecturer's habits, reusable figures, what comes next) move into the COURSE record, which now carries the course's memory (W11). General lessons go on the report's new "Proposed for the skill" line and change the skill's files only in a maintenance session. W11 no longer sends notes or tools back.
- **English level A2–C1** (G2, L1, L2, L3, L5, TE3, W6, §11): asked at the first deck with the canvas gate (B1 suggested) and recorded as `english level:`. Words and sentence caps follow the level (SKILL.md step 2b); `plain_check.py --max-level`. Records made before 2.0 mean B1.
- **Fewer tool prescriptions:** W1 reads files with the best reader available; W1b's `pdftotext` recipe is "one tested way"; "goals over procedures" names the tools as defaults.
- Older decks are not attached: ask for one only when a figure or a glossary wording from it is needed (§0).

**Changes in 1.9 (17 October 2026): structure only, no rule changed.**
- **The code moved to `deck-tools` 1.6:** `plain_check.py` (Appendix A); the topic bar, glossary, figure-label, phone-layer and phone-variant snippets (Appendix B, now in `deck-tools/snippets/`); the independent checker's brief (Appendix C, now `deck-tools/checker-brief.txt`). The appendices keep their explanations and name each file. `deck-tools.zip` is now always attached.
- **The version history moved here.** The rulebook keeps a one-line "New in" note.
- **Size cap (§0):** this file stays under 110,000 characters, `questions-rulebook.md` under 32,000, the general notes under about 30,000. `deck-tools/size_check.py` reports them. Before 1.9 this file was 140,126 characters; after, about 104,000.

**Changes in 1.8: easier to digest, not shorter.** G5 used to say "shorter than the slides". It now says **easier to digest than the slides, in at most twice their words**.
- **The word ceiling is 2 × the original's words** (W1b: its text plus the words inside its figures and tables). Plain words that are longer, full sentences instead of telegraphic bullets, the "why", and examples may use that room. The deck never passes the ceiling.
- **Words are the only measure of size.** There is no slide-count limit (the old "about 0.8 × the source's slides" is gone). The slide count follows from one idea per slide (TE1) and the words per slide (V5).
- **Where the room goes** is a ranked list (§1, "Where the extra words go"). When a plan passes the ceiling, cut from the bottom of that list up (W4). Facts and their exact wording are never cut. If they alone would pass the ceiling, stop and ask the user (precedence, W5).
- The Concept Pattern's "budget form" is now its **deck form** (§6): every load-bearing concept gets a concrete example, and a concept may take 1–3 slides.
- **Checks and report:** Q6 checks the ceiling and digestibility, not the slide count. The report shows words against the 200% ceiling and says what the room above 100% was spent on (§10).
- **`plain_check.py` v1.8** reports deck words against the ceiling (`--ceiling`, default 2.0) and flags only a deck over it.
- **Settings (§11):** the word ceiling is 2 × by default. **Tighter** (1.5 ×) and **Shorter** (the v1.7 rule: no more words than the source, about 0.8 × its slides) remain as options.
- **Courses started before 1.8** switch to the 2 × ceiling from their next deck, unless the user keeps the Shorter setting (§0).

**Changes in 1.7: the deck must stand alone, and that is now checked fact by fact.** G1 always said the student never needs the slides, but its check (a coverage map of slide units) let small losses through: a 210 ISY deck passed with 13 weakened facts, 2 contradictions and 9 quiz problems, all found by an independent reader.
- **F1 — Fact ledger** replaces the coverage map. Every bullet is split into single facts, qualifiers kept, each with its slide and a status. Re-run after every trimming pass (W9).
- **F1b — Independent check (new, required).** A separate agent that did not build the deck compares the PDF text with the deck's slide text and reports missing, weakened, contradicted, misquoted and unlabelled content. Fix and re-run until it reports nothing. Its brief is Appendix C.
- **F2 — Exact wording for every definition** (the user's choice): every sentence that says what a term is, means, includes or covers, and every list a review question asks, is quoted word for word, with a plain reading beside it.
- **F3 — The deck's own framing is labelled** (`class="ours"`), and framing that could contradict a slide fact is not used.
- **L10** lists the qualifiers that must survive. **TE7:** quiz items test the lecture, never the deck's own pictures, and feedback states slide facts at full strength.
- **The word budget gives way** to completeness and exact wording; the report gives the overrun (G5, precedence).
- The report has a **"Standalone"** line (§10); a new setting chooses how much wording is exact (§11).

**Changes in 1.6.1:** goals over procedures (§0). The goals, the user's choices and the limits that serve them are fixed. Every procedure is a tested default that may give way to a better method, reported on a new "Departures" line (§10). Review the procedures when the model or the skill changes.

**Changes in 1.6:**
- **The field notes are split.** A general notes file serves every course. Each course has its own notes file, which lives from the course's first deck to its last (§0 "Starting a run", W11).
- **W11 merges instead of appending.** It sorts each lesson into the general or the course notes, replaces outdated points, and caps the general file.
- **Deck tools:** the helper scripts (build and word count, screenshots, checks) travel as `deck-tools.zip`, attached with the notes.
- **First deck of a course:** the template's header comment contains the text `<script>`. Take the engine from the script tag itself (§0, case A).
- **Phone variants of wide figures** get a pattern and its code (M4, Appendix B5): one set of labels, two drawings, words counted once.
- **Two fixes for the deck glossary** (Appendix B2): gloss cards near the edge of a phone screen no longer make the slide scroll sideways, and glossary cards no longer split flex list items into columns.

**Changes in 1.5:**
- **Phone first (new goal G6, rules M1–M8, Appendix B4).** Every deck is designed and checked at phone size first, then at laptop size, and the laptop view stays as it was. A small phone layer (CSS + one script, Appendix B4) fixes the browser-bar height, the notch, tap-target sizes and builds that land below the fold. Q7 now checks the phone first.
- **The canvas is always the user's choice.** At the first deck of a course, the canvas gate (paper or chalkboard, then the board) is always asked before anything is built, and never decided silently (§0, W5). Skill v1.3 retired the other style families, so "style family" now means the canvas and board.
- **The final quiz is standard.** `questions-rulebook.md` is attached to every run, and its final quiz replaces the skill's end-of-deck question set and answer box (§2, TE5, TE7, §11).
- **Starting a run:** the attachment list includes `questions-rulebook.md`; sample prompts for a first and a later deck.
- **`plain_check.py` v1.5:** a slide marked `data-budget="skip"` (the quiz) now stays outside the word count, its feedback included.
- The glossary script skips quiz slides (Appendix B2); bridge tokens are `style-system.md §7` in skill v1.3.


**Changes in 1.4.3:** new field words found in a lecture are added by a set test, kept in the COURSE record so later decks inherit them, and listed in the report so the user can veto them (L1).

**Changes in 1.4.2:** the topic bar stays identical across a course's decks. Later decks copy the shell's code unchanged (§0, N1), and Appendix B's CSS reproduces the Applied OS look exactly in Sketchbook (checked in a browser).

**Changes in 1.4.1:** the field notes are read before planning (§0), and one notes file serves every course.

**Changes in 1.4** (one system for every course and every deck):
- **§0 "Starting a run" covers every case:** the first deck of a course, a later deck, or decks from another course attached. The prompt stays the same; the attachments decide the case.
- **COURSE record:** every deck carries the course's standing choices (style, canvas, exam focus, settings, decisions) in an HTML comment, so later decks don't ask them again.
- **Earlier decks:** the newest one is the shell, a source of code, not a list of allowed components. Components still come from the skill's full catalog.
- **Naming** `<course>-NN-<lecture>.html`, and a new step **W11**: update the field notes after each deck.

**Changes in 1.3** (what building the Applied OS chapter 1 deck showed):
- **One deck per lecture, shorter than the slides.** New goal G5, with a word budget (W1b, W4, Q6): the deck has fewer slides than the source, and no more words than the source's text plus the words inside its figures and tables. The old series model (14–18 slides per deck) is now a setting (§11).
- **New precedence.** Completeness still comes first. The cost is paid by compressing wording and moving facts into figures (L11, V13), not by adding slides.
- **Independence moves from the slide to the topic.** Each topic (N1) stands alone. On any slide, every term is explained either visibly or by a deck glossary card (T5, T5b). The glossary keeps the definitions once and makes per-slide glossing affordable.
- **New navigation rule N1.** A topic bar replaces the slide dots: rounded blocks named by topic, sized by slide count, marking only the current topic.
- **Smaller changes:**
  - formal-version boxes only where the wording matters (F2);
  - a field-vocabulary allowlist (L1);
  - narrower research (W2b);
  - a shorter confirmation step (W5);
  - the Concept Pattern gets a budget form (§6);
  - visual checks include phone width and arrowheads (Q7).
- **`plain_check.py` v1.3** now reports the word budget, the topics and the glossary, and accepts a known-words file. Appendix B holds the topic-bar and glossary code until the skill ships them.

**Changes in 1.2.1:**
- The rulebook carries its own start-up procedure (§0, "Starting a run").
- W5 asks for the exam focus when it was not given.
- Q2 says what to do when code cannot run.

**Changes in 1.2:**
- Aligned with lesson-deck-builder v1.2 (teaching jobs, components §22–§29, bridge tokens).
- On-demand glosses allowed for supporting terms.
- F9: "trim" means emphasis, never deletion.

**Changes in 1.1:**
- Decks improve on the slides instead of transcribing them.
- A research step for every concept.
- Concepts are ordered for learning.
- Evidence-based visual rules.

---

## questions-rulebook.md

**Changes in 1.4 (23 October 2026).**
- Ships inside the skill (`rulebooks/`). Every lecture deck ends with this quiz without being asked; "add a final quiz to the attached deck" is a one-line request. Nothing else is attached.

**Changes in 1.3 (17 October 2026): structure only, no rule changed.**
- **The code moved to `deck-tools` 1.6:** the markup templates (Appendix A, now `deck-tools/snippets/quiz-markup.html`, one part per kind), the quiz CSS and script (Appendices B–C, now `snippets/quiz.css` and `snippets/quiz.js`) and the browser walk (Appendix D, now `deck-tools/quiz_walk.py`). The QUIZ-MAP record format stays in Appendix A.
- **The version history moved here.**
- **Size cap (§0):** under 32,000 characters (it was 65,805; now about 29,000).

**Changes in 1.2.1:** goals over procedures (§0). The goals and the user's settings are fixed. The catalogue, layout and code are tested defaults that may give way to a better method, reported on a new "Departures" line (§8).

**Changes in 1.2:** Sort rows put the item above its group buttons (Appendix B). With three groups, the buttons used to stack into a column beside a long item, so the slide ran past one screen even on a laptop. Found in the 210 ISY deck 1.

**Changes in 1.1:**
- **The quiz replaces the skill's question set and answer box** whenever this file is attached (the default in `slides-rulebook.md` v1.5): QL1, QW10.
- **Label the figure is now a proven kind (K9)**, built in Applied OS deck 2 and reused in decks 3–4. Its markup, CSS, script and walk branch are in Appendices A–D, so a new course needs no earlier deck to build it.
- **Phone first (QL7, §6, §7):** quiz slides are checked at phone size first, with touch.
- `slides-rulebook.md` v1.5's checker keeps whole quiz slides (`data-budget="skip"`) outside the word count, feedback included.

---

## lessons-rulebook.md

**Changes in 2.1 (23 October 2026): phone first.**
- **New goal G6, phone first,** with the lecture route's phone rules: the slides rulebook's §8 "Phone first" (M1–M8), its Q7 phone checks and its phone layer and phone-variant figures (Appendix B4–B5) are now required reading (§0) and apply to lessons exactly as written. One source for both routes: this file points to them instead of copying them.
- Precedence, §2 (new "Phone" row), W5 (phone shape per slide), W9 (phone layer, CSS phone first), V14, Q5, Q7 (now the slides rulebook's phone-first check), §10 (a "Phone" report line) and §11 (a "Phone first" setting, on by default).

**Changes in 2.0 (23 October 2026): bundled, one-line start, English level A2–C1, goals over procedures, no notes files.**
- **Ships inside the skill** (`rulebooks/`, lesson-deck-builder v1.4). The skill routes any teaching request without a lecture file here. "Starting a run" takes one line; in chat mode only the previous lesson is attached.
- **English level A2–C1** (G2, L1, L2, L3, L5, TE3, §11): asked at the first lesson with the canvas gate (B2 suggested), recorded as `level:` in DECK-SETTINGS.
- **Goals over procedures** (§0, new) and a "Departures" line in the report; the research-agent rule is now a default with its reason.
- **No notes files:** the field notes became the bundled general notes (`deck-notes-general.md`). W12 puts subject facts (including reusable figures, a new DECK-SETTINGS line) into the record and general lessons on the report's new "Proposed for the skill" line.
- **The code moved to the shared `deck-tools`:** `plain_check.py` is one checker for every route (`--max-level A2–C1`, `--cs-grad` for the computer-science graduate's field words); Appendix B points to the shared snippets, so lessons now get the newer figure-label floors (11–12 px instead of 9 px) and the slides decks' topic-bar comments. Size cap 75,000 characters (it was 89,062; now about 69,500).

**Changes in 1.1** (lesson-deck-builder v1.3: Sketchbook is the only style; the chalkboard has six boards):
- The skill's style gate is now the **canvas gate**: paper or chalkboard, then the board (default **Slate re-inked**). The DECK-SETTINGS record gains a `board:` field.
- **Pre-v1.3 shells** (decks with the old `#2B322D` slate and no `data-canvas`) get the template's token section once, then stay unchanged (H1b).
- Section references follow the skill's new numbering (`style-system.md §7` for bridge tokens). Appendix B drops the "other families" notes.
