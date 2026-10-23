# Lesson-Deck-Builder

**A Claude skill that turns any topic, or any attached lecture, into a calm, hand-drawn lesson deck — one self-contained HTML file that opens in any browser.**

📖 **Full documentation and live demos: https://mstrpxl.github.io/lesson-deck-builder/**

Attach a lecture and say "use /lesson-deck-builder to explain the attached file", or ask for a lesson on any topic, and get back a single `.html` file: a slide deck in the *Sketchbook* style (ruled paper or a chalkboard), with keyboard, click and swipe navigation, step-by-step builds, a library of 43 visual components, and a teaching method that opens with a challenge and ends with questions. Arabic (right to left) or English, with English written at the reader's level (A2–C1).

| | |
|---|---|
| **One file** | Styles, engine and drawings all inside the `.html`. Share it or host it anywhere. |
| **One-line requests** | The skill picks its route: an attached file → a complete study deck with a self-marking quiz; a topic → a researched lesson; a pitch → a presentation. |
| **Two canvases** | Bright paper, or a chalkboard in six boards (Slate re-inked, Midnight blue, Olive gold, Dusk indigo, Deep teal, Red graphite). |
| **Two languages, four levels** | Arabic RTL (Playpen Sans Arabic + IBM Plex Sans Arabic) or English LTR (Caveat + Karla); English at A2, B1, B2 or C1. |
| **Built to teach** | Opening challenge → one idea per slide (picture · why · real use) → the same challenge solved → recap → questions. |
| **Memory inside the decks** | A course's choices and notes travel in each deck's hidden record: for the next deck you attach only the previous one. |
| **Checked** | `scripts/validate.py` and the rulebooks' checks catch broken or hard-to-read decks before you see them. |

## Install

The skill is the [`lesson-deck-builder/`](lesson-deck-builder/) folder in this repo (its rulebooks and tools included).

**Claude Code (all projects)**

```bash
git clone https://github.com/MstrPxl/lesson-deck-builder.git
mkdir -p ~/.claude/skills
cp -r lesson-deck-builder/lesson-deck-builder ~/.claude/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/MstrPxl/lesson-deck-builder.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse lesson-deck-builder\lesson-deck-builder "$HOME\.claude\skills\"
```

**Claude Code (one project):** copy the folder to `<project>/.claude/skills/lesson-deck-builder/`.

**Claude apps (claude.ai, desktop):** download `lesson-deck-builder.zip` from the [latest release](https://github.com/MstrPxl/lesson-deck-builder/releases/latest), then upload it under **Settings → Capabilities → Skills** (code execution must be on). To update, upload the new zip in its place.

Python 3 is recommended so Claude can run the checks. Decks load their fonts from Google Fonts and fall back to system fonts offline.

## Use

**Explain a file** — attach a lecture or document (PDF or PPTX) and send:

```text
use /lesson-deck-builder to explain the attached file
```

The first deck of a course asks the canvas (paper or chalkboard, then the board) and the English level. For the next lecture, attach the new chapter's file **and the previous deck**: its hidden record remembers your choices and the course. If you forget the new file, Claude asks for it before doing anything. Nothing else is ever attached, and no Markdown file goes back and forth.

**Learn a topic** — no file:

```text
use /lesson-deck-builder to teach me how DNS finds a website
```

Claude confirms the topic, asks the canvas, the language and (for English) the level, then builds a researched lesson. Say the choices up front to skip the questions: "… English, level B2, chalkboard Midnight blue, about 15 minutes."

**A presentation** — "use /lesson-deck-builder to make a short pitch for our note-taking app".

## Routes and rulebooks

[`lesson-deck-builder/rulebooks/`](lesson-deck-builder/rulebooks/) ships inside the skill, and the skill reads what a route needs:

| Route | When | Rulebook |
|---|---|---|
| Lecture | a PDF or PPTX attached to explain | [`slides-rulebook.md`](lesson-deck-builder/rulebooks/slides-rulebook.md): complete, **easier to digest than the source in at most twice its words**, at the course's English level (default B1), standalone topics, phone first; ending with [`questions-rulebook.md`](lesson-deck-builder/rulebooks/questions-rulebook.md)'s self-marking quiz |
| Lesson | a teaching request, no file | [`lessons-rulebook.md`](lesson-deck-builder/rulebooks/lessons-rulebook.md): researched, correct and current, at the chosen level (default B2) and length |
| Presentation | a pitch, intro or showcase | the skill's base workflow |

Beside them: `deck-notes-general.md` (experience from earlier decks, advice not rules), `deck-tools/` (the language checker for A2–C1, quiz walk, code snippets, helpers) and `rulebooks-changelog.md`. Each run's report lists anything worth improving on a "Proposed for the skill" line, for a later maintenance session.

[`examples/isy-05-cryptography.html`](examples/isy-05-cryptography.html) is a real lecture deck ([open it live](https://mstrpxl.github.io/lesson-deck-builder/examples/isy-05-cryptography.html)).

## Repository layout

```text
lesson-deck-builder/     the skill — copy this folder to install
  SKILL.md               instructions Claude follows (routes, gates, teaching method, hard rules)
  CHANGELOG.md
  assets/                template.html (deck engine) + exemplar decks
  references/            style-system, design-system, components (43), use-cases (19 jobs)
  scripts/               validate.py, use_cases.py
  rulebooks/             slides, questions and lessons rulebooks, general notes, changelog
    deck-tools/          checker (A2–C1), quiz walk, snippets, setup, size_check
examples/                isy-05-cryptography.html
index.html, site/        the documentation site (GitHub Pages)
```

## Contributors

- **Ali AlQahtani** ([@MstrPxl](https://github.com/MstrPxl)) — creator and maintainer
- **Claude** (Anthropic) — co-author

Issues and pull requests are welcome. If you change the skill, run `python lesson-deck-builder/scripts/use_cases.py`, `validate.py` and `rulebooks/deck-tools/size_check.py`, and add a changelog entry.

## License

[MIT](LICENSE). The example deck quotes definitions from its source lecture; those quotations remain their authors'.
