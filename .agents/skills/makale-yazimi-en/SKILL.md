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
2. Build a compact section outline before writing.
3. Define the section-level thesis.
4. Assign a role to each paragraph.
5. Draft or revise paragraph by paragraph.
6. Check claim-evidence alignment.
7. Run reverse outlining.
8. Produce a short self-review.

## Section references

Load only the relevant reference file:

- `references/abstract.md`
- `references/introduction.md`
- `references/related-work.md`
- `references/method.md`
- `references/experiments-results.md`
- `references/discussion-conclusion.md`
- `references/paragraph-flow.md`
- `references/software-engineering-paper.md`

## Global principles

- One paragraph should carry one main message.
- The first sentence should usually state the paragraph message.
- Each technical term should be introduced before reuse.
- Claims in the Abstract and Introduction must be supported by results, method, or cited literature.
- Do not overstate novelty or empirical strength.
- Prefer concrete contributions over generic novelty language.
- Keep terminology stable across sections.
- Preserve citations, LaTeX commands, equations, tables, and figure references.

## Output contract

When drafting or revising, return:

1. **Section Outline**: 3-7 bullets.
2. **Paragraph Role Map**: paragraph role, message, evidence.
3. **Revised Text**: polished academic English.
4. **Claim-Evidence Notes**: major claims and support status.
5. **Remaining Risks**: missing evidence, overclaim, unclear method, weak transition.

## Hard constraints

- Do not invent citations.
- Do not invent numbers, datasets, metrics, baselines, or results.
- Do not add unsupported claims to make the paper sound stronger.
- Do not rewrite code, equations, or LaTeX structures unless explicitly asked.
- If evidence is missing, mark it as `[MATERIAL GAP]`.
