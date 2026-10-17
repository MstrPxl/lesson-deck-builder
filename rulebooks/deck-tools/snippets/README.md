# deck-tools/snippets

Code that a deck pastes in, moved out of the rulebooks' appendices (slides-rulebook 1.9, questions-rulebook 1.3) so a run doesn't read it. Copy each file into the deck with a script, never by retyping. The rulebook section says where it goes and why.

| File | Rule | Goes |
|---|---|---|
| `topic-bar.html` | slides B1 (N1) | replaces the skill's nav block (keep `#dots`) |
| `topic-bar.css` | slides B1 (N1) | end of the style block |
| `topic-bar.js` | slides B1 (N1) | after the engine |
| `glossary-slide.html` | slides B2 (T5b) | last slide of the Review topic, before the final quiz |
| `glossary.css` | slides B2 (T5b) | style block |
| `glossary.js` | slides B2 (T5b) | after the engine |
| `figure-labels.css` | slides B3 (V14, M4) | with the skill's §22 label CSS |
| `phone-layer.css` | slides B4 (M1–M8) | end of the style block, after the topic bar |
| `phone-layer.js` | slides B4 (M1–M8) | after the engine and the other component code |
| `phone-variant.html` | slides B5 (M4) | example markup for a figure with a phone drawing |
| `phone-variant.css` | slides B5 (M4) | after B3 and B4 |
| `quiz-markup.html` | questions Appendix A | one part per quiz kind, plus the slide shell and the intro and score slides |
| `quiz.css` | questions Appendix B | end of the style block |
| `quiz.js` | questions Appendix C | end of the deck's single script |

The scripts beside this folder: `plain_check.py` (slides Appendix A), `quiz_walk.py` (questions Appendix D), `checker-brief.txt` (slides Appendix C) and `size_check.py` (slides §0, "Size cap").
