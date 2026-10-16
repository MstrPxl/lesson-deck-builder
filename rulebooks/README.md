# Rulebooks

Optional companions to the `lesson-deck-builder` skill, for turning **university lecture slides** (PDF or PPTX) into a deck a student can study **instead of** the slides. Attach them to your request; they add to the skill and, where they say so, override it.

| File | Purpose |
|---|---|
| [`slides-rulebook.md`](slides-rulebook.md) (v1.7) | One deck per lecture: complete (every fact at full strength, definitions word for word), shorter than the slides, plain English at A2–B1, topics that stand alone, phone first, consistent across every deck of a course. |
| [`questions-rulebook.md`](questions-rulebook.md) (v1.2.1) | A self-marking final quiz (~10 min, up to nine question kinds) with a score slide that sends the learner back to missed topics. Works with the slides rulebook or on its own. |

## Prompts

First deck of a course (attach both rulebooks + the lecture):

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

The rulebooks also mention optional notes files (`deck-notes-general.md`, `<course>-notes.md`) and a `deck-tools.zip` of helper scripts. They are not part of this repository and are not required: the first deck of a course creates its notes, and the rulebooks' appendices carry the code they need (`plain_check.py`, topic bar, glossary, phone layer, quiz markup/CSS/script, Playwright browser walk).

See the [documentation site](https://mstrpxl.github.io/lesson-deck-builder/#rulebooks) for a plain-language tour, and [`../examples/isy-05-cryptography.html`](../examples/isy-05-cryptography.html) for a deck built with both.
