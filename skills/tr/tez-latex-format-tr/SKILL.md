---
name: tez-latex-format-tr
description: Use for OMU thesis-format and local LaTeX-template compliance checks. It reviews page layout, headings, numbering, abstracts, tables, figures, equations, bibliography, and LaTeX commands while preserving template structure.
---

# Turkish Thesis LaTeX Format

This skill focuses on format, LaTeX template compliance, and OMU thesis rules rather than academic content quality.

## Priority Order

1. Read the local LaTeX template first when it exists.
2. Preserve commands and file structure defined by the template.
3. Inspect the user's real `.cls`, `.sty`, `.tex`, `.bib`, `Makefile`, and build settings before relying on generic guidance.
4. Apply the OMU thesis-format guide summarized in `references/omu-tez-kurallari.md`.
5. If the template and guide differ, report the difference instead of making a definitive institutional claim.
6. Do not rewrite the main `.tex` file unless the user asks.

Load `references/agent-neutral-skill-principles.md` only when general agent-neutral operation or file protection rules are relevant to the format check.

## Local Template Discovery

Search for main `.tex` files, `.cls`, `.sty`, `.bib`, build files, chapter folders, and figure/table folders. Report the main file, class/style files, bibliography file, chapter files, build method, and template-specific commands.

## Review Flow

1. Discover LaTeX files.
2. Extract template commands.
3. Compare against OMU rules.
4. Classify issues as `format-critical`, `template-risk`, `latex-error`, `consistency`, or `style`.
5. Provide safe fixes; if requested, provide patches.

## Output Contract

```text
## Template Discovery
...

## OMU Rule Check
| Rule | Status | Rule source | Evidence / File | Recommendation |
|---|---|---|---|---|

## LaTeX Risks
| Priority | File | Issue | Fix |
|---|---|---|---|

## Safe Fix Plan
1. ...
```

## Prohibited

- Rewriting the template from scratch.
- Changing `.cls` or `.sty` files without a clear reason.
- Deleting cover, approval, or ethics-statement commands.
- Automatically renaming citation keys.
- Presenting non-OMU preferences as institutional rules.
- Presenting a format check as content approval.
