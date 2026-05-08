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
- Artificial Turkish, academic Turkish, style, translationese, naturalness, or simplification: choose `turkce-akademik-style-review`.
- Claims, evidence, support, overclaim, or exaggeration: choose `claim-evidence-audit`.
- Bibliography, citation, BibTeX, DOI, or references: choose `citation-integrity-audit`.
- English paper section drafting or revision: choose `makale-yazimi-en`.
- Reviewer-like English manuscript review: choose `makale-denetim-en`.
- English AI-like academic prose cleanup: choose `academic-style-review-en`.

## Recommended Workflows

Turkish thesis: `tez-yazimi-tr` -> `claim-evidence-audit` -> `tez-denetim-tr` -> `turkce-akademik-style-review` -> `tez-latex-format-tr`.

English article: `makale-yazimi-en` -> `claim-evidence-audit` -> `makale-denetim-en` -> `academic-style-review-en` -> `citation-integrity-audit`.

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
