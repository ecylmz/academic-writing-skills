# Turkish Academic Writing Skills

This directory contains skills for Turkish thesis writing, thesis review, OMU LaTeX format checks, and Turkish academic style review. The goal is not only fluency. The text must be defensible in terms of research problem, method, evidence, contribution, limitations, and format.

## Skill Selection

| Need | Skill | Typical Output |
|---|---|---|
| Draft, expand, or restructure a thesis section | `tez-yazimi-tr` | Mini outline, paragraph roles, revised text, review notes |
| Review a thesis before advisor, committee, or defense evaluation | `tez-denetim-tr` | Critical risks, claim-evidence checks, committee questions, revision plan |
| Check OMU thesis template, LaTeX commands, and formatting rules | `tez-latex-format-tr` | Template discovery, OMU rule checks, LaTeX risks |
| Make Turkish academic prose natural, moderate, and consistent | `tez-yazimi-tr` in `style-review` mode | Style issues, revised text, claim calibration, remaining risks |

Although `research-integrity-audit` lives under `skills/en`, it is a language-independent audit skill and can be used in Turkish thesis workflows.

## Recommended Thesis Workflow

1. `tez-yazimi-tr`: establish section purpose, connection to the research question, and paragraph flow.
2. `research-integrity-audit` in `claim-evidence` mode: check whether strong claims are supported by evidence.
3. `tez-denetim-tr`: identify methodological, structural, and defense-readiness risks.
4. `tez-yazimi-tr` in `style-review` mode: clean language, terminology, moderation, and artificial phrasing.
5. `research-integrity-audit` in `citation-integrity` mode: check citation/reference alignment and source support.
6. `tez-latex-format-tr`: check OMU template, headings, numbering, tables, figures, and bibliography format.

If material is missing, do not invent it. Mark the gap as `[MATERIAL GAP]`, `[VERIFY SOURCE]`, `[METHOD GAP]`, or `requires verification`.
