# Rulebooks

Optional companions to the `lesson-deck-builder` skill, for turning **university lecture slides** (PDF or PPTX) into a deck a student can study **instead of** the slides. Attach them to your request; they add to the skill and, where they say so, override it.

| File | Purpose |
|---|---|
| [`slides-rulebook.md`](slides-rulebook.md) (v1.9) | One deck per lecture: complete (every fact at full strength, definitions word for word), **easier to digest than the slides** (plain words, full sentences, an example for every key idea) in **at most twice their words** (no slide-count limit), plain English at A2–B1, topics that stand alone, phone first, consistent across every deck of a course. |
| [`questions-rulebook.md`](questions-rulebook.md) (v1.3) | A self-marking final quiz (~10 min, up to nine question kinds) with a score slide that sends the learner back to missed topics. Works with the slides rulebook or on its own. |
| [`deck-tools/`](deck-tools/) (1.6) | **Required with the rulebooks.** The code they point to: `plain_check.py` (language and word-ceiling checker), `quiz_walk.py` (browser walk), `checker-brief.txt`, and [`snippets/`](deck-tools/snippets/) (topic bar, glossary, phone layer, quiz markup/CSS/script), plus helper scripts for building, screenshots and checks. Attach it as `deck-tools.zip` (from the [latest release](https://github.com/MstrPxl/lesson-deck-builder/releases/latest), or zip this folder) and run `bash deck-tools/setup_tools.sh` once per session. |
| [`rulebooks-changelog.md`](rulebooks-changelog.md) | Both rulebooks' version history. Not needed for a run. |

## Prompts

First deck of a course (attach both rulebooks, `deck-tools.zip` and the lecture):

```text
/lesson-deck-builder
Follow slides-rulebook.md for the attached lecture, and end the deck with a final quiz following questions-rulebook.md. Read the attached notes before planning.
This is the first deck of a new course: ask me the canvas and board before building.
```

Later deck of the same course (also attach the newest deck of the course):

```text
/lesson-deck-builder
Follow slides-rulebook.md for the attached lecture, and end the deck with a final quiz following questions-rulebook.md. Read the attached notes before planning. The newest deck of this course is attached.
```

Quiz only, for an existing deck:

```text
Add a final quiz to the attached deck, following questions-rulebook.md.
```

**Why the code lives in `deck-tools`:** every run reads the rulebooks in full, so their size is paid on every deck. Since slides-rulebook 1.9 and questions-rulebook 1.3 the code ships as files, the history sits in the changelog, and both rulebooks have a size cap (slides 110,000 characters, questions 32,000) that `deck-tools/size_check.py` checks. Before: 140,126 + 65,805 characters; after: about 104,000 + 29,000.

The rulebooks also mention optional notes files (`deck-notes-general.md`, `<course>-notes.md`). They are not part of this repository and are not required: the first deck of a course creates its notes.

See the [documentation site](https://mstrpxl.github.io/lesson-deck-builder/#rulebooks) for a plain-language tour, and [`../examples/isy-05-cryptography.html`](../examples/isy-05-cryptography.html) for a deck built with both.
