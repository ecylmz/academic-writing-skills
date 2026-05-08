# English Academic Writing Skills

This directory contains skills for English research paper writing, reviewer-risk analysis, and research-integrity auditing.

The goal is not generic polishing. The skills are designed to make a manuscript reviewer-readable, evidence-backed, methodologically defensible, and honest about its scope.

## Which skill should be used?

| Need | Skill | Typical output |
|---|---|---|
| Draft or revise an English paper section | `paper-writing-en` | Section outline, paragraph role map, revised text, claim-evidence notes |
| Simulate peer review or assess reviewer risk | `paper-review-en` | Reviewer lenses, risk matrix, likely decision, revision roadmap |
| Clean academic English style without changing meaning | `paper-writing-en` in `style-review` mode | Style audit, revised text, claim calibration notes |
| Check whether claims or citations are supported | `research-integrity-audit` | Claim table, citation-reference table, evidence gaps, bibliography fixes |

## Recommended manuscript workflow

1. `paper-writing-en`: Build or revise the section logic.
2. `research-integrity-audit` in `claim-evidence` mode: Check whether major claims match the available evidence.
3. `research-integrity-audit` in `citation-integrity` mode: Check citation-reference consistency and source support.
4. `paper-writing-en` in `style-review` mode: Clean style, vague language, overclaiming, and terminology drift.
5. `paper-review-en`: Run reviewer-risk analysis before submission.
6. `paper-review-en` in `re-review` mode: Check revised manuscript against reviewer comments and author response.

Use a narrower skill when the user asks for a narrow task. Do not run the whole workflow by default.

## Automatic trigger phrases

| User phrase | Skill |
|---|---|
| `write my introduction`, `revise related work`, `improve method section`, `rewrite abstract` | `paper-writing-en` |
| `review my paper`, `simulate peer review`, `referee report`, `editorial decision`, `desk reject risk` | `paper-review-en` |
| `quick review`, `first look`, `is this submission ready` | `paper-review-en` with `quick` mode |
| `check methodology`, `protocol risk`, `statistics`, `reproducibility`, `leakage` | `paper-review-en` with `methodology-focus` mode |
| `check revisions`, `response letter`, `did we address reviewers` | `paper-review-en` with `re-review` mode |
| `AI-like`, `style cleanup`, `academic prose`, `remove filler`, `claim calibration` | `paper-writing-en` with `style-review` mode |
| `are claims supported`, `overclaim`, `claim-evidence`, `unsupported statement` | `research-integrity-audit` with `claim-evidence` mode |
| `citation check`, `bibliography`, `BibTeX`, `DOI`, `source support`, `missing reference` | `research-integrity-audit` with `citation-integrity` mode |

## Review skill comparison with upstream

The upstream `academic-paper-reviewer` skill from `Imbad0202/academic-research-skills` is broader than this local reviewer skill. It includes a full multi-agent journal simulation, EIC, multiple peer reviewers, devil's advocate, guided review, calibration mode, and formal editorial decision templates.

This local `paper-review-en` is useful when:

- The manuscript is in computer science, empirical software engineering, AI/ML, software systems, HCI, data science, or another empirical/technical field.
- The user needs a compact reviewer-risk audit rather than a large multi-agent simulation.
- The review must emphasize experimental protocol, baselines, ablations, reproducibility, statistical uncertainty, artifact availability, and validity threats.
- The output should be immediately usable as a revision roadmap inside this skill suite.

Use the upstream reviewer directly when:

- The user wants a full journal-style simulation with several independent reviewer personas.
- Calibration, guided Socratic review, or formal re-review protocol is required.
- The paper needs a field-general journal simulation with rich reviewer personas beyond this suite's compact reviewer-risk audit.

The local reviewer should not pretend to be a complete replacement for the upstream skill. It borrows the useful ideas that fit this suite: reviewer lenses, editorial synthesis, devil's-advocate challenge, read-only review, risk severity, decision rationale, and revision traceability.

## Upstream sources reviewed

These local EN skills are adapted from three upstream sources without vendoring their full content:

| Upstream | Useful material found | Local adaptation |
|---|---|---|
| `Imbad0202/academic-research-skills` | `academic-paper`, `academic-paper-reviewer`, `academic-pipeline`, and `deep-research` skills; reviewer personas, editorial synthesis, claim verification, integrity gates, reproducibility audit, paper structure patterns | `paper-review-en` reviewer modes; `review-quality-framework.md`; `editorial-review-package.md`; claim verification checks |
| `Master-cai/Research-Paper-Writing-Skills` | Section guides for Abstract, Introduction, Related Work, Method, Experiments, Conclusion; paper review checklist; paragraph flow / reverse outlining | `paper-writing-en` section workflow; reviewer-ready writing reference; stronger paragraph and self-review checks |
| `yzhao062/agent-style` | Style-review skill, rule-based prose audit, no-new-facts revision invariant, reader-state and concrete-language rules | `paper-writing-en` style-review mode; `style-rule-checklist.md`; preserve-structure and no-new-facts constraints |

When an upstream skill is broader and better suited to the user request, use it directly instead of forcing the local skill. The local skills are optimized for this suite's English research-paper workflow, with extra care for empirical computer science and software engineering but without excluding other academic fields.

## Input checklist

Ask for or inspect these materials when available:

- Manuscript text or `.tex`/`.docx`/Markdown source.
- Target venue or venue tier, if known.
- Paper type: empirical, method, systems, survey, case study, position paper.
- Research questions or hypotheses.
- Results tables, figures, appendices, artifact links, and experiment logs.
- Bibliography file and citation style.
- Reviewer comments and response letter for `re-review` mode.

If material is missing, mark it as `[MATERIAL GAP]`, `requires verification`, or `requires source check`.

## Hard boundaries

- Do not invent citations, reviewer comments, results, datasets, baselines, or venue rules.
- Do not edit the manuscript during review mode.
- Do not hide serious methodological problems behind polite language.
- Do not treat fluent prose as evidence of research quality.
- Do not mark source support as verified unless the source or relevant passage is available.
- Do not let numerical scores override fatal validity issues.
