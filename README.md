# Academic Writing Skill Suite

This repository provides an agent-neutral academic writing skill suite for supervised, evidence-aware thesis and manuscript work. The suite is modular: each skill has a short `SKILL.md`, while longer rules live in focused `references/` and `templates/` files.

The suite adapts ideas from `yzhao062/agent-style`, `Master-cai/Research-Paper-Writing-Skills`, and `Imbad0202/academic-research-skills`. It is not a direct copy. It is a local adaptation for Turkish thesis writing, OMU thesis formatting, empirical computer science and software engineering workflows, and English research article writing.

## Repository Layout

```text
academic-writing-skills/
├── AGENTS.md
├── README.md
├── SOURCE_NOTES.md
├── PROJECT_MANIFEST.json
├── skills/
│   ├── tr/
│   └── en/
├── .upstream/
├── .github/workflows/upstream-watch.yml
├── examples/
└── tools/
```

`INSTALL.md` and `VALIDATION_REPORT.md` were intentionally removed. Installation guidance now lives here, and validation reports should be regenerated with `tools/check_skill_suite.py` instead of stored as stale documentation.

## Skills

| Skill | Language | Purpose |
|---|---:|---|
| `tez-yazimi-tr` | TR | Drafts, revises, and style-reviews Turkish thesis sections with evidence discipline and formal academic Turkish. |
| `tez-denetim-tr` | TR | Reviews a Turkish thesis from advisor, committee, and defense-readiness perspectives. |
| `tez-latex-format-tr` | TR | Checks OMU thesis-format and local LaTeX-template compliance. |
| `paper-writing-en` | EN | Drafts, revises, and style-reviews English research paper sections. |
| `paper-review-en` | EN | Reviews English manuscripts for reviewer risks. |
| `research-integrity-audit` | TR/EN | Audits claim-evidence alignment, citation/reference consistency, source support, and bibliography quality. |

## Installation

Copy the suite into another project:

```bash
cp -R skills /path/to/your/project/
cp AGENTS.md /path/to/your/project/
```

If the target project should also track upstream sources, copy the maintenance files:

```bash
cp -R .upstream /path/to/your/project/
cp -R .github /path/to/your/project/
cp -R tools /path/to/your/project/
```

Validate the local copy:

```bash
python3 tools/check_skill_suite.py
```

Expected output is a JSON object with `"status": "ok"`.

## Recommended Turkish Thesis Workflow

1. `tez-yazimi-tr`: build the section purpose, outline, paragraph roles, and first academic draft.
2. `research-integrity-audit`: run `claim-evidence` mode for major claims and evidence gaps.
3. `tez-yazimi-tr`: run `style-review` mode for artificial phrasing, vague generalizations, unnecessary emphasis, and translationese.
4. `tez-denetim-tr`: identify committee questions, methodological gaps, defense risks, and revision priorities.
5. `tez-latex-format-tr`: check OMU formatting, LaTeX commands, headings, tables, figures, equations, and references.

## Recommended English Article Workflow

1. `paper-writing-en`: build the paper story, section outline, paragraph roles, and section draft.
2. `research-integrity-audit`: run `claim-evidence` mode for claim-evidence alignment.
3. `research-integrity-audit`: run `citation-integrity` mode for in-text citations, bibliography entries, and citation style.
4. `paper-writing-en`: run `style-review` mode for AI-like phrasing, excessive transitions, weak claim calibration, and vague terms.
5. `paper-review-en`: run reviewer-risk analysis.

## OMU Thesis and LaTeX Template Use

`tez-latex-format-tr` must prioritize actual project files over generic memory: local OMU template files, `.cls`, `.sty`, `.tex`, `.bib`, build files, and only then the summary in `skills/tr/tez-latex-format-tr/references/omu-tez-kurallari.md`. When a local template exists, preserve its commands, document structure, and custom macros.

## Claim-Evidence Discipline

Every strong academic claim must be supported by the study's own evidence or verified literature. Unsupported claims should be narrowed, marked for verification, or removed.

Shared principles and templates are intentionally copied into the skills that use them. There is no central `skills/_shared` directory, so each skill remains self-contained when copied into another project.

## Upstream Tracking

The repository includes a lightweight monthly upstream tracking workflow. Classify upstream changes as `ignore`, `port`, `vendor`, or `defer`; never auto-merge upstream content into local skill files.
