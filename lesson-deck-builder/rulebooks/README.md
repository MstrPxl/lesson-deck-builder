# rulebooks/

Part of the `lesson-deck-builder` skill since v1.4. The skill reads these files by itself when a request needs them (SKILL.md, step 0b): nobody attaches them, and no Markdown file goes back and forth.

| File | Used when |
|---|---|
| [`slides-rulebook.md`](slides-rulebook.md) (2.0.1) | **Lecture route:** a lecture or document (PDF or PPTX) is attached to explain. One complete deck per lecture, easier to digest than the slides, at most twice their words, at the course's English level (A2–C1, default B1), phone first, consistent across a course. |
| [`questions-rulebook.md`](questions-rulebook.md) (1.4) | The self-marking final quiz that ends every lecture deck (~10 min, up to nine kinds, a score slide that sends the reader back to missed topics). |
| [`lessons-rulebook.md`](lessons-rulebook.md) (2.1) | **Lesson route:** a teaching request without a lecture file. A researched lesson at the chosen English level (A2–C1, default B2), within a length preset, phone first (it reads the slides rulebook's phone rules, so both routes match). |
| [`deck-notes-general.md`](deck-notes-general.md) | Experience from earlier decks (word budgets, figure pitfalls, checks). Advice, not rules. |
| [`deck-tools/`](deck-tools/) (1.7) | The language checker (`plain_check.py`, A2–C1), the quiz walk, the checker's brief, the [`snippets/`](deck-tools/snippets/) a deck pastes in, build and screenshot helpers, and `size_check.py`. Run `setup_tools.sh` once per session from a working folder. |
| [`rulebooks-changelog.md`](rulebooks-changelog.md) | Version history of the three rulebooks. Not read by a run. |

## Prompts

```text
use /lesson-deck-builder to explain the attached file
```

Attach the lecture and, from the second deck of a course on, the previous deck (HTML). The first deck of a course asks the canvas, the board and the English level; later decks read them from the previous deck's COURSE record, which also carries the course's memory.

```text
use /lesson-deck-builder to teach me <topic>
```

No file attached: the lesson route. For the next lesson of a journey in a chat, attach the previous lesson.

## Size caps

Every run reads the rulebooks in full, so their size is paid on every deck. Code lives in `deck-tools`, history in the changelog, and each file has a cap that `deck-tools/size_check.py` checks: slides 110,000 characters, lessons 75,000, questions 32,000, notes 30,000.

## Changing them

The files change only in a maintenance session, from the "Proposed for the skill" lines that each run's report lists. After an edit: run `size_check.py`, add a changelog entry, and keep each rulebook's one-line "New in" note current.
