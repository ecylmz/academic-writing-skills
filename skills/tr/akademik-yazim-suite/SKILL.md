---
name: akademik-yazim-suite
description: Agent-neutral academic writing orchestrator that selects among thesis writing, article writing, audits, citation checks, and style-review skills. It chooses the right sub-skill instead of performing all work itself.
---

# Academic Writing Suite

This is an orchestrator skill. Actual drafting, review, or formatting work must be handled by the relevant sub-skill.

## Selection Rules

- Thesis section, introduction, literature, method, findings, discussion, conclusion, abstract, or Turkish thesis prose: choose `tez-yazimi-tr`.
- Committee, defense, advisor view, risks, criticism, weak points, or readiness: choose `tez-denetim-tr`.
- OMU, LaTeX, template, format, `.cls`, `.sty`, or `.tex`: choose `tez-latex-format-tr`.
- Artificial Turkish, academic Turkish, style, translationese, naturalness, or simplification: choose `tez-yazimi-tr` in `style-review` mode.
- Claims, evidence, support, overclaim, or exaggeration: choose `research-integrity-audit` in `claim-evidence` mode.
- Bibliography, citation, BibTeX, DOI, or references: choose `research-integrity-audit` in `citation-integrity` mode.
- English paper section drafting or revision: choose `paper-writing-en`.
- Reviewer-like English manuscript review: choose `paper-review-en`.
- English AI-like academic prose cleanup: choose `paper-writing-en` in `style-review` mode.

## Recommended Workflows

Turkish thesis: `tez-yazimi-tr` -> `research-integrity-audit` (`claim-evidence`) -> `tez-denetim-tr` -> `tez-yazimi-tr` (`style-review`) -> `tez-latex-format-tr`.

English article: `paper-writing-en` -> `research-integrity-audit` (`claim-evidence`) -> `paper-review-en` -> `paper-writing-en` (`style-review`) -> `research-integrity-audit` (`citation-integrity`).

## Rules

- Do not draft directly; choose the relevant sub-skill.
- If multiple jobs are requested, explain the order and identify the first skill to apply.
- Do not invent missing data, tables, sources, results, or institutional rules.
- In Turkish thesis work, check academic defensibility first, style second, and formatting last.

## Output Contract

```text
Recommended skill: <skill-name>
Why: <short rationale>
Required input material: <files/text/data>
Recommended next step: <next skill or audit>
```
