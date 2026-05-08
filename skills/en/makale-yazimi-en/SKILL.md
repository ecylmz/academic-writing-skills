---
name: makale-yazimi-en
description: English research paper drafting and revision skill for Abstract, Introduction, Related Work, Method, Experiments, Results, Discussion, Conclusion, and reviewer-oriented presentation. Uses claim-evidence alignment, reverse outlining, and section-specific writing guides.
---

# Research Paper Writing EN

Use this skill to draft or revise English academic manuscripts. The goal is not only grammatical polishing; the goal is to make the paper story, section logic, paragraph flow, and evidence-backed claims reviewer-readable.

## Use cases

- Abstract drafting and compression.
- Introduction revision.
- Related Work restructuring.
- Method and experimental setup writing.
- Results and Discussion writing.
- Conclusion and limitations.
- Paragraph-level flow repair.
- Claim-evidence mapping during revision.

## Core workflow

1. Identify the target section.
2. Identify paper type, target venue assumptions, and available evidence.
3. Build a compact section outline before writing.
4. Define the section-level thesis.
5. Assign a role to each paragraph.
6. Draft or revise paragraph by paragraph.
7. Check claim-evidence alignment.
8. Run reverse outlining.
9. Produce a short reviewer-oriented self-review.

## Academic quality priorities

Prioritize reviewer readability and defensible claims over polished phrasing:

1. **Task-gap-contribution logic**: The reader should understand the problem, what prior work leaves unresolved, and what this paper contributes.
2. **Research questions and evidence**: Each RQ should map to a method, result, table, figure, or analysis.
3. **Reproducibility**: Data, preprocessing, model selection, statistical tests, and implementation details should be clear enough to inspect.
4. **Contribution scope**: Novelty and impact claims must be scoped to the evidence.
5. **Negative and limited results**: Do not hide weak or mixed results; interpret them carefully.
6. **Threats to validity**: Limitations should be specific to the design, data, methods, and claims.
7. **Citation discipline**: Do not insert new citations or imply a source supports a claim unless the source has been checked or supplied.

## Section references

Load only the relevant reference file:

- `references/abstract.md`
- `references/introduction.md`
- `references/related-work.md`
- `references/method.md`
- `references/experiments-results.md`
- `references/discussion-conclusion.md`
- `references/paragraph-flow.md`
- `references/computer-science-paper.md`
- `references/reviewer-ready-writing.md`

## Global principles

- One paragraph should carry one main message.
- The first sentence should usually state the paragraph message.
- Each technical term should be introduced before reuse.
- Claims in the Abstract and Introduction must be supported by results, method, or cited literature.
- Do not overstate novelty or empirical strength.
- Prefer concrete contributions over generic novelty language.
- Keep terminology stable across sections.
- Preserve citations, LaTeX commands, equations, tables, and figure references.
- Mark missing evidence as `[MATERIAL GAP]` rather than filling it with generic academic prose.
- Keep deliberate terminology repetition when it prevents ambiguity.

## Output contract

When drafting or revising, return:

1. **Section Outline**: 3-7 bullets.
2. **Paragraph Role Map**: paragraph role, message, evidence.
3. **Revised Text**: polished academic English.
4. **Claim-Evidence Notes**: major claims and support status.
5. **Reviewer Readiness Notes**: likely reviewer questions, missing evidence, overclaim, unclear method, weak transition.
6. **Recommended Next Skill**: `claim-evidence-audit`, `citation-integrity-audit`, `academic-style-review-en`, or `makale-denetim-en`.

## Hard constraints

- Do not invent citations.
- Do not invent numbers, datasets, metrics, baselines, or results.
- Do not add unsupported claims to make the paper sound stronger.
- Do not rewrite code, equations, or LaTeX structures unless explicitly asked.
- If evidence is missing, mark it as `[MATERIAL GAP]`.
- Do not convert a reviewer-facing research paper into promotional or grant-style prose.
- Do not smooth over methodological gaps with vague transition sentences.
