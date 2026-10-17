# Lesson-Deck-Builder

**A Claude skill that turns any topic into a calm, hand-drawn lesson deck — one self-contained HTML file that opens in any browser.**

📖 **Full documentation and live demos: https://mstrpxl.github.io/lesson-deck-builder/**

Ask Claude for a lesson ("make slides explaining how vaccines work") and get back a single `.html` file: a slide deck in the *Sketchbook* style (ruled paper or a chalkboard), with keyboard, click and swipe navigation, step-by-step builds, a library of 43 visual components, and a teaching method that opens with a challenge and ends with questions. Arabic (right to left) or English.

| | |
|---|---|
| **One file** | Styles, engine and drawings all inside the `.html`. Share it or host it anywhere. |
| **Two canvases** | Bright paper, or a chalkboard in six boards (Slate re-inked, Midnight blue, Olive gold, Dusk indigo, Deep teal, Red graphite). |
| **Two languages** | Arabic RTL (Playpen Sans Arabic + IBM Plex Sans Arabic) or English LTR (Caveat + Karla). |
| **Built to teach** | Opening challenge → one idea per slide (picture · why · real use) → the same challenge solved → recap → questions and an answer box. |
| **Learning journeys** | In Claude Code, it can run a whole researched roadmap with lessons, notes and an adaptive question loop. |
| **Checked** | `scripts/validate.py` catches broken decks before you see them. |

## Install

The skill is the [`lesson-deck-builder/`](lesson-deck-builder/) folder in this repo.

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

**Claude apps (claude.ai, desktop):** download `lesson-deck-builder.zip` from the [latest release](https://github.com/MstrPxl/lesson-deck-builder/releases/latest), then upload it under **Settings → Capabilities → Skills** (code execution must be on).

Python 3 is recommended so Claude can run the validator. Decks load their fonts from Google Fonts and fall back to system fonts offline.

## Use

Type `/lesson-deck-builder` in Claude Code, or just ask for "slides", "a deck" or "a lesson" on any topic. Claude will:

1. confirm the topic with you (always, for a new journey);
2. ask the canvas (paper or chalkboard, then the board) and the language (Arabic or English);
3. ask audience and length if you didn't say;
4. plan, build from the template and component library, validate, and hand you the file.

Say the choices up front to skip the questions:

```text
/lesson-deck-builder
Make an English teaching deck about how DNS finds a website. Canvas: chalkboard, board Midnight blue. Audience: complete beginners. Length: about 15 minutes.
```

## Rulebooks (optional)

[`rulebooks/`](rulebooks/) holds two companion files for turning **university lecture slides** into a deck a student can study instead of the slides:

- [`slides-rulebook.md`](rulebooks/slides-rulebook.md) — complete, **easier to digest than the slides in at most twice their words** (measured in words only, no slide-count limit), plain English (A2–B1), standalone topics, phone first, consistent across a course.
- [`questions-rulebook.md`](rulebooks/questions-rulebook.md) — a self-marking ~10-minute final quiz in up to nine question kinds, with a score slide that sends you back to missed topics.

Attach both, `deck-tools.zip` (the code they point to: [`rulebooks/deck-tools/`](rulebooks/deck-tools/), also in the release) and the lecture, then send:

```text
/lesson-deck-builder
Follow slides-rulebook.md for the attached lecture, and end the deck with a final quiz following questions-rulebook.md. Read the attached notes before planning.
This is the first deck of a new course: ask me the canvas and board before building.
```

[`examples/isy-05-cryptography.html`](examples/isy-05-cryptography.html) is a real deck built this way ([open it live](https://mstrpxl.github.io/lesson-deck-builder/examples/isy-05-cryptography.html)).

## Repository layout

```text
lesson-deck-builder/     the skill — copy this folder to install
  SKILL.md               instructions Claude follows
  CHANGELOG.md
  assets/                template.html (deck engine) + exemplar decks
  references/            style-system, design-system, components (43), use-cases (19 jobs)
  scripts/               validate.py, use_cases.py
rulebooks/               slides-rulebook.md, questions-rulebook.md, rulebooks-changelog.md
  deck-tools/            the rulebooks' code: checker, quiz walk, snippets, helper scripts
examples/                isy-05-cryptography.html
index.html, site/        the documentation site (GitHub Pages)
```

## Contributors

- **Ali AlQahtani** ([@MstrPxl](https://github.com/MstrPxl)) — creator and maintainer
- **Claude** (Anthropic) — co-author

Issues and pull requests are welcome. If you change the skill, run `python lesson-deck-builder/scripts/use_cases.py` and `validate.py`, and add a `CHANGELOG.md` entry.

## License

[MIT](LICENSE). The example deck quotes definitions from its source lecture; those quotations remain their authors'.
