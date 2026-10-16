# Use cases — the teaching jobs a slide can do

Every component in `components.md` carries a short **Suggested for** list: the teaching jobs it does
well, **best fit first**. This file explains each job once, with examples, and ends each entry with a
reverse index — the components that suit that job, best fit first.

**These are suggestions, not obligations.** A component's first-listed use case is where it usually
shines, not where it must go; its last-listed use case is a reasonable but weaker fit — and may be the
first fit of another component. The same use case appears in many components on purpose. Pick a
lower-ranked or unlisted component whenever the content argues for it, and vary components across a
deck: a deck where every slide uses its "rank 1" component looks templated.

## How to use it (step 5 of the workflow)

1. For each planned slide, name its job in one phrase from this list.
2. Open that job's entry; read its reverse index.
3. Choose a component — usually from the top of the index, checked against the content and against
   what the neighbouring slides already use.

When converting lecture slides, the **Spot it when** lines are the classifier: they describe what a
source slide doing that job usually looks like.

## One vocabulary with `style-system.md §3`

The §3 table is the coarse map (8 content categories); this file refines it into 19 jobs:

| §3 category | Teaching jobs here |
|---|---|
| Academic / definitional | `define-term` · `label-parts` · `highlight-passage` |
| Process / mechanism | `explain-mechanism` · `follow-procedure` · `show-transformation` |
| Intuition / tradeoff | `build-intuition` |
| Comparison | `compare-options` · `show-quantity` |
| Narrative / history | `tell-story` |
| Code walkthrough | `walk-code` · `show-transformation` |
| Anchor / thesis | `state-thesis` |
| Check / recall | `check-recall` · `predict-first` |
| (deck structure) | `orient` · `recap` · `list-parallel` · `demo-interface` · `correct-misconception` |

The reverse index under each entry is generated: after changing any **Suggested for** list, run
`python scripts/use_cases.py --write` (and `python scripts/use_cases.py` to check).

---

## State the one big idea (`state-thesis`)
**The job:** put one claim on the screen and let it carry the slide — the sentence the reader should
still remember tomorrow. Nothing competes with it.
**Spot it when:** a lecture slide with a single bold sentence, a quote, a "key takeaway" box, a title
slide's promise, or a conclusion the whole section builds toward.
**Examples:**
- Everyday: "Sleep is when memory is saved, not when it rests."
- Lecture slide: "Key point: TCP guarantees delivery; UDP does not." → one poster line, the rest of
  the section unpacks it.
- Tech: the cover of a deck on caching — "The fastest request is the one you never send."
**Watch out:** a thesis slide with three claims is a list; pick one, or split.
<!-- idx:state-thesis -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §1 Cover slide (#1) · §32i Pointer spotlight cover (#1) · §2 Closing slide (#2) · §32l Key passage frame (#2) · §6 Aside / callout (#3) · §12 Tri-grid (three parallel ideas, centered) (#3)
<!-- /idx -->

## Show where we are going (`orient`)
**The job:** give the reader a map — what's coming, how the parts relate, where they are now — so each
later slide has a place to land.
**Spot it when:** an agenda or outline slide, "Today we will cover…", a course roadmap, a section
divider, "Part 2 of 4".
**Examples:**
- Everyday: four parts of a cooking class shown as four cards before the first recipe.
- Lecture slide: "Outline: 1. Layers 2. Addressing 3. Routing 4. Transport" → a map slide with one
  line per part, the current part marked.
- Tech: a roadmap step marked "you are here" at the start of lesson 3.
**Watch out:** an agenda that only lists headings orients nobody; give each part one line of why.
<!-- idx:orient -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §3 Section head + feature cards (the "map") (#1) · §18 Roadmap / learning-path (current + completed steps marked) (#1) · §1 Cover slide (#2) · §17 Icon set (drop-in 24×24 strokes) (#2) · §2 Closing slide (#3) · §13 Tiles (labelled list with icons, 2 columns) (#3) · §31 Live element (line boil) (#3)
<!-- /idx -->

## Predict first, then verify (`predict-first`)
**The job:** ask the reader to commit to an answer before the explanation, then come back to it. A
prediction — even a wrong one — makes the explanation land harder.
**Spot it when:** a lecture slide that poses a puzzle or "What do you think happens if…?", a classic
counter-intuitive result, or any topic where learners arrive with a confident wrong guess.
**Examples:**
- Everyday: "Which falls first on the Moon: a hammer or a feather?" — answered at the end.
- Lecture slide: "What happens to throughput if we double the window size?" → opening challenge,
  revisited after the mechanism slides.
- Tech: "Will this loop finish? Pick yes or no" before the slide on integer overflow.
**Watch out:** the revisit must be the same question, not a new one (see components §19–§20).
<!-- idx:predict-first -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §19 Opening challenge (commit before teaching) (#1) · §20 Challenge revisited (close the loop) (#1) · §21 Question set + copyable answer box (the adaptive loop) (#2) · §32g Sketch quiz (#2) · §29 Eraser (write, erase, rewrite) (#3)
<!-- /idx -->

## Define a new term (`define-term`)
**The job:** hand the reader a word they will need, in plain language, before or exactly where it is
first used, so the later explanation isn't carrying two loads at once.
**Spot it when:** "X is…", "Definition:", a bold term, a glossary column, or any word a B1–A2 reader
would not know.
**Examples:**
- Everyday: "proofing" in a bread lesson — one sentence, attached to the word.
- Lecture slide: "Definition: A protocol is a set of rules for communication." → a gloss on
  "protocol" where it first appears, plus one concrete instance (a phone call's "hello").
- Tech: "latency" glossed on first use; the mechanism slide then uses it freely.
**Watch out:** a definition without an example is a dictionary entry; pair it with an instance or a
picture.
<!-- idx:define-term -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §24 Anchored gloss (define it where it stands) (#1) · §32c Note stack (reserved flow) (#1) · §32e Gloss footnotes (overlay) (#1) · §4 Two-column: text + figure (#2) · §6 Aside / callout (#2) · §32j Smudge panels (#2) · §23 Linked figure (same color, same thing) (#3) · §28 Ink marks (hand-drawn annotations in order) (#3)
<!-- /idx -->

## Name the parts of a thing (`label-parts`)
**The job:** teach the anatomy of something — what each part is called and where it sits — so later
slides can say "the vent" and the reader can see it.
**Spot it when:** a labeled diagram, a "parts of…" slide, a figure with a legend or numbered callouts,
a screenshot with arrows.
**Examples:**
- Everyday: the parts of a bicycle gear — chainring, chain, cog.
- Lecture slide: a packet diagram with a numbered legend → labels placed on the drawing with leader
  lines (components §22).
- Tech: the regions of an IDE window, each named on the screenshot.
**Watch out:** past about six parts, number them and move the names to a tray; past twelve, split the
figure.
<!-- idx:label-parts -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §22 Labels on the figure (#1) · §13 Tiles (labelled list with icons, 2 columns) (#2) · §23 Linked figure (same color, same thing) (#2) · §32d Detail tray (fixed) (#2) · §4 Two-column: text + figure (#3) · §17 Icon set (drop-in 24×24 strokes) (#3) · §24 Anchored gloss (define it where it stands) (#3) · §25 Builds (engine v2 — one idea per press) (#3)
<!-- /idx -->

## Point at what matters in a passage (`highlight-passage`)
**The job:** take a sentence, quote or paragraph the reader must read closely and show, mark by mark,
which words carry the meaning.
**Spot it when:** a lecture slide with a dense paragraph, a quoted definition from a standard, a legal
clause, a poem line, an error message.
**Examples:**
- Everyday: underline "both sides" in an explanation of tides.
- Lecture slide: a textbook definition pasted on a slide → keep the sentence, then circle and underline
  its two load-bearing words in order (components §28).
- Tech: box the one argument in a long function signature that causes the bug.
**Watch out:** marking everything marks nothing; three to six marks per passage.
<!-- idx:highlight-passage -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §28 Ink marks (hand-drawn annotations in order) (#1) · §32l Key passage frame (#1) · §24 Anchored gloss (define it where it stands) (#2) · §32e Gloss footnotes (overlay) (#2)
<!-- /idx -->

## Show how something works inside (`explain-mechanism`)
**The job:** reveal the cause-and-effect chain inside a system — what pushes what — so the reader can
predict its behaviour, not just name it.
**Spot it when:** "How X works", arrows between boxes, a process diagram, a slide that says "because",
"which causes", "therefore".
**Examples:**
- Everyday: why a raindrop splits light into colors — enter, bounce, leave.
- Lecture slide: a block diagram of the TCP handshake → a figure built one step per press, with one
  caption per step (components §25).
- Tech: how a hash map finds a key — hash, bucket, compare.
**Watch out:** a mechanism shown all at once makes the reader find the order; give the order away.
<!-- idx:explain-mechanism -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §4 Two-column: text + figure (#1) · §23 Linked figure (same color, same thing) (#1) · §25 Builds (engine v2 — one idea per press) (#1) · §31 Live element (line boil) (#1) · §32a Steppable figure (the stepper skeleton) (#1) · §32h Token journey (#1) · §22 Labels on the figure (#2) · §32c Note stack (reserved flow) (#2) · §10 Linked cards (timeline / progression) (#3) · §15 Flow recap (pills + arrows) (#3) · §27 Reactive sentence (a number you can drag) (#3) · §32j Smudge panels (#3)
<!-- /idx -->

## Walk through a procedure (`follow-procedure`)
**The job:** list the steps the reader will DO, in order, so they can repeat them without the slides.
Different from a mechanism: a procedure is what you do; a mechanism is why it works.
**Spot it when:** numbered steps, "How to…", a lab procedure, a recipe, a configuration checklist.
**Examples:**
- Everyday: making tea — boil, steep three minutes, remove the bag.
- Lecture slide: "Steps to subnet a network: 1… 2… 3…" → a step card or a build, one step per press,
  each with one worked number.
- Tech: setting up a virtual environment, command by command.
**Watch out:** steps longer than one line hide a sub-procedure; split it out.
<!-- idx:follow-procedure -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §11 Step card (process / reusable "recipe") (#1) · §10 Linked cards (timeline / progression) (#2) · §15 Flow recap (pills + arrows) (#2) · §25 Builds (engine v2 — one idea per press) (#2) · §32a Steppable figure (the stepper skeleton) (#2) · §32h Token journey (#2) · §5 Point list (#3) · §26 Magic board (marks that move between states) (#3)
<!-- /idx -->

## Show one state turning into another (`show-transformation`)
**The job:** make a change visible as movement — the same pieces before and after — so the reader
sees what moved, what vanished and what appeared.
**Spot it when:** algebra steps, before/after code, a sorted vs unsorted list, a data structure after
an operation, "becomes", "is rewritten as".
**Examples:**
- Everyday: re-ordering a to-do list by deadline, items sliding into place.
- Lecture slide: three lines of algebra solving for x → one board where the 3 walks across the equals
  sign (components §26).
- Tech: a refactor where two functions merge; surviving lines slide, deleted lines fade.
**Watch out:** if nothing persists between the two states, it isn't a transformation — use two panes.
<!-- idx:show-transformation -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §26 Magic board (marks that move between states) (#1) · §32k Skins stepper (one skeleton, swappable skins) (#1) · §29 Eraser (write, erase, rewrite) (#2) · §32f Duo panes (final-geometry) (#2) · §16 Code window (dark, for code/tech topics) (#3) · §32a Steppable figure (the stepper skeleton) (#4) · §32h Token journey (#4)
<!-- /idx -->

## Let the reader push a variable (`build-intuition`)
**The job:** give the reader a control over one quantity and let them feel how the outcome responds —
including the edge where the rule breaks.
**Spot it when:** a formula with a parameter, a tradeoff ("more X means less Y"), a graph showing a
curve, "what if" questions.
**Examples:**
- Everyday: a seesaw — move one person and see where the other must sit.
- Lecture slide: Ohm's law V = IR on a slide → a sentence where the voltage can be dragged and the
  current rewrites itself (components §27).
- Tech: a cache size slider showing hit rate rising, then flattening.
**Watch out:** the resting state must already tell the story; most readers never touch the control.
<!-- idx:build-intuition -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §27 Reactive sentence (a number you can drag) (#1) · §32b Lab widget (#1) · §31 Live element (line boil) (#2) · §32i Pointer spotlight cover (#2) · §32k Skins stepper (one skeleton, swappable skins) (#2) · §19 Opening challenge (commit before teaching) (#3)
<!-- /idx -->

## Compare options side by side (`compare-options`)
**The job:** put two or more alternatives in the same frame, on the same criteria, so the reader can
choose or explain the difference.
**Spot it when:** "X vs Y", a pros/cons table, a comparison matrix, "advantages and disadvantages".
**Examples:**
- Everyday: renting vs buying — the same three criteria for both.
- Lecture slide: a table "TCP vs UDP" with eight rows → two panes with three load-bearing rows and one
  number each.
- Tech: three database plans with meters for cost, speed and safety.
**Watch out:** comparisons on different criteria aren't comparisons; align the rows.
<!-- idx:compare-options -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §14 Comparison tiers (with meters) (#1) · §32f Duo panes (final-geometry) (#1) · §9 Bar chart (data / generated artifact) (#2) · §12 Tri-grid (three parallel ideas, centered) (#2) · §30 Sketch chart (Sketchbook skin for §9) (#2) · §32b Lab widget (#2) · §32d Detail tray (fixed) (#3) · §26 Magic board (marks that move between states) (#4) · §27 Reactive sentence (a number you can drag) (#4)
<!-- /idx -->

## Show numbers and evidence (`show-quantity`)
**The job:** present data so its size and shape are seen at a glance, with the exact values still
readable.
**Spot it when:** a chart, a table of figures, statistics, results of a study, "X% of…".
**Examples:**
- Everyday: how many hours each activity takes in a week.
- Lecture slide: a results table from a paper → a bar chart with the exact value printed at each bar.
- Tech: latency per region as hand-drawn bars with numbers at the tips.
**Watch out:** a sketchy chart reads as "roughly" — print the numbers when precision matters.
<!-- idx:show-quantity -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §9 Bar chart (data / generated artifact) (#1) · §30 Sketch chart (Sketchbook skin for §9) (#1) · §8 Source rows (search result look) (#2) · §14 Comparison tiers (with meters) (#2) · §27 Reactive sentence (a number you can drag) (#2) · §22 Labels on the figure (#3) · §32b Lab widget (#3) · §4 Two-column: text + figure (#4)
<!-- /idx -->

## Correct a misconception (`correct-misconception`)
**The job:** name a common wrong belief, say plainly that it is wrong, then give the better explanation
— in that order. Naming the wrong idea is what makes the correction stick.
**Spot it when:** "Common mistake", "Myth vs fact", "Students often think…", a counter-intuitive
result, a warning box.
**Examples:**
- Everyday: "Heavier things fall faster" → erased → "With no air, a hammer and a feather land
  together" (components §29).
- Lecture slide: "Note: a bigger bandwidth does NOT mean lower latency" → the belief, the refutation,
  the mechanism.
- Tech: "More threads always means faster" struck through, then the explanation of contention.
**Watch out:** don't leave the misconception as the last thing on screen; the better idea comes last.
<!-- idx:correct-misconception -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §6 Aside / callout (#1) · §29 Eraser (write, erase, rewrite) (#1) · §19 Opening challenge (commit before teaching) (#2) · §20 Challenge revisited (close the loop) (#2) · §28 Ink marks (hand-drawn annotations in order) (#2) · §32c Note stack (reserved flow) (#3) · §32f Duo panes (final-geometry) (#3) · §32g Sketch quiz (#3)
<!-- /idx -->

## Tell a history or story in order (`tell-story`)
**The job:** walk through events in time so causes come before effects and the reader can retell it.
**Spot it when:** dates, a timeline, "In 1969…", a case study, a narrative example, a dialogue.
**Examples:**
- Everyday: how a city's water supply grew, decade by decade.
- Lecture slide: "History of the Internet: ARPANET → TCP/IP → WWW" → linked cards, one beat each.
- Tech: the story of one request through a system, told as a short chat or journey.
**Watch out:** more than about six beats on one slide is a chapter; split it.
<!-- idx:tell-story -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §10 Linked cards (timeline / progression) (#1) · §7 Window mockup + chat (#2) · §18 Roadmap / learning-path (current + completed steps marked) (#3) · §32a Steppable figure (the stepper skeleton) (#3) · §32h Token journey (#3) · §32k Skins stepper (one skeleton, swappable skins) (#3) · §25 Builds (engine v2 — one idea per press) (#4)
<!-- /idx -->

## Walk through code (`walk-code`)
**The job:** take a piece of code and explain it a line-range at a time, so the reader can read it alone
afterwards.
**Spot it when:** a code listing on a slide, pseudo-code, a terminal session, "the following
program…".
**Examples:**
- Everyday-tech: a five-line script that renames files, explained line by line.
- Lecture slide: a full function pasted on one slide → a code window that highlights one range per step
  with an overlay note.
- Tech: a refactor shown as lines sliding into their new places (components §26, code variant).
**Watch out:** more than about 15 visible lines at once is a wall; show the range that matters.
<!-- idx:walk-code -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §16 Code window (dark, for code/tech topics) (#1) · §11 Step card (process / reusable "recipe") (#2) · §26 Magic board (marks that move between states) (#2) · §7 Window mockup + chat (#3) · §28 Ink marks (hand-drawn annotations in order) (#4) · §32a Steppable figure (the stepper skeleton) (#5)
<!-- /idx -->

## Show a tool or interface in use (`demo-interface`)
**The job:** show what using a tool looks like — the window, the messages, the results — so the reader
recognises it when they open it.
**Spot it when:** screenshots of an app, a chat with an assistant, search results, "click here, then…".
**Examples:**
- Everyday: a booking site's three screens, mocked up.
- Lecture slide: a screenshot of Wireshark → a window mockup with the one panel that matters.
- Tech: a chat between a user and an AI tool, message by message.
**Watch out:** a full screenshot is noise; mock up only the parts the slide talks about.
<!-- idx:demo-interface -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §7 Window mockup + chat (#1) · §8 Source rows (search result look) (#1) · §16 Code window (dark, for code/tech topics) (#2)
<!-- /idx -->

## Present parallel ideas of equal weight (`list-parallel`)
**The job:** show a set of items that sit side by side — types, features, principles — where no item
leads to the next.
**Spot it when:** bullet lists of categories, "three types of…", feature lists, icon grids.
**Examples:**
- Everyday: four food groups as four tiles.
- Lecture slide: "Types of network topology: bus, star, ring, mesh" → tiles with one sketch each.
- Tech: three principles of a design system as a tri-grid.
**Watch out:** if the items have an order, it's a procedure or a story; if they compete, it's a
comparison.
<!-- idx:list-parallel -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §5 Point list (#1) · §12 Tri-grid (three parallel ideas, centered) (#1) · §13 Tiles (labelled list with icons, 2 columns) (#1) · §17 Icon set (drop-in 24×24 strokes) (#1) · §32d Detail tray (fixed) (#1) · §32j Smudge panels (#1) · §3 Section head + feature cards (the "map") (#2) · §8 Source rows (search result look) (#3)
<!-- /idx -->

## Recap and connect (`recap`)
**The job:** bring the lesson's pieces back together and show how they connect, so the reader leaves
with a structure, not a pile of slides.
**Spot it when:** "Summary", "In conclusion", "Key takeaways", the last slides of a section.
**Examples:**
- Everyday: the three steps of a habit loop as pills joined by arrows.
- Lecture slide: a five-bullet summary → a flow recap where each pill names a slide's idea and the
  arrows say how they link.
- Tech: the request path from browser to database, each hop one word.
**Watch out:** a recap that adds new content is a lesson; only reconnect what was taught.
<!-- idx:recap -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §2 Closing slide (#1) · §15 Flow recap (pills + arrows) (#1) · §5 Point list (#2) · §18 Roadmap / learning-path (current + completed steps marked) (#2) · §3 Section head + feature cards (the "map") (#3) · §11 Step card (process / reusable "recipe") (#3) · §20 Challenge revisited (close the loop) (#3) · §25 Builds (engine v2 — one idea per press) (#5)
<!-- /idx -->

## Check understanding (`check-recall`)
**The job:** ask the reader to retrieve what was taught — retrieval strengthens memory — and give a
verdict and the right answer.
**Spot it when:** "Quiz", "Review questions", "Test yourself", exercises at the end of a chapter.
**Examples:**
- Everyday: "Which step comes after steeping?" with three options.
- Lecture slide: end-of-chapter questions → the question set with a copyable answer box
  (components §21).
- Tech: "Which line causes the bug?" with the code still visible.
**Watch out:** questions that only re-read the slide test recognition, not understanding; ask for
transfer at least once.
<!-- idx:check-recall -->
**Components that suit it** (best fit first; #n = its rank in that component's list): §21 Question set + copyable answer box (the adaptive loop) (#1) · §32g Sketch quiz (#1)
<!-- /idx -->
