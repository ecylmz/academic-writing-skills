---
name: paper-review-en
description: Reviewer-risk audit for English academic manuscripts. Simulates a structured peer-review process with editorial synthesis, methodology/domain/perspective review lenses, devil's-advocate challenge, contribution clarity, methodological rigor, evidence sufficiency, claim-evidence alignment, and revision roadmap.
---

# Research Paper Review EN

Use this skill as a skeptical peer-review simulator before submission, revision, or resubmission. It does not proofread or rewrite the manuscript; it produces review reports, editorial synthesis, and a revision roadmap.

This local skill is inspired by multi-perspective academic reviewer workflows, but is intentionally practical and compact. It should work for many academic fields, while applying extra scrutiny to empirical computer science, software engineering, AI/ML, systems, HCI, and data-driven studies where protocol, baselines, reproducibility, and validity threats are central. If the user needs a full journal-style simulation with several independent reviewer personas, use the `full` mode below. If the user needs fast risk triage, use `quick`.

## Read-only rule

- Do not edit the submitted manuscript.
- Do not rewrite sections unless the user explicitly asks for revision after the review.
- Review output must be a separate report.
- Every criticism must cite a specific section, paragraph, table, figure, result, citation, or missing item when available.
- If the paper or source material is incomplete, mark the issue as `requires verification` instead of inventing a judgment.

## Modes

| Mode | Trigger | Use when | Output |
|---|---|---|---|
| `full` | review my paper, simulate peer review, full review | First submission or pre-submission review | Reviewer panel, editorial decision, revision roadmap |
| `quick` | quick review, first look, desk check | Fast triage before deeper review | Top risks, likely decision, next checks |
| `methodology-focus` | check methodology, methods review, protocol risk | Method, experiments, statistics, reproducibility are central | Methodology risk report |
| `re-review` | check revisions, response letter, second round | Revised manuscript and reviewer comments are available | Revision traceability matrix and residual decision |
| `cs-empirical-focus` | empirical CS, software engineering, AI/ML, systems, HCI, data science | Empirical or technical computer science paper | CS-specific validity, artifact, baseline, and protocol audit |

## Review dimensions

1. **Originality and contribution**
   - Is the contribution clear, non-trivial, and scoped?
   - Is the novelty type explicit: dataset, method, task, protocol, empirical finding, tool, or analysis?
   - Does the paper pass the "so what?" test for the target venue?

2. **Problem and motivation**
   - Does the Introduction lead naturally from task to gap to contribution?
   - Is the research gap supported rather than asserted?
   - Are research questions or hypotheses visible and answerable?

3. **Methodological rigor**
   - Is the experimental protocol reproducible?
   - Are train/test boundaries, preprocessing, tuning, and evaluation clear?
   - Is leakage risk addressed?
   - Are validity threats specific to the design rather than generic?

4. **Empirical strength**
   - Are baselines strong and fair?
   - Are metrics appropriate for the data distribution?
   - Are results meaningful, not merely marginal?
   - Are statistical uncertainty, effect size, variance, or per-case breakdowns reported when needed?

5. **Evaluation completeness**
   - Are ablations, sensitivity checks, robustness checks, or negative results included when needed?
   - Are threats to validity discussed?
   - Does each claimed component have evidence?

6. **Literature integration**
   - Does Related Work cover the major research line?
   - Is the paper positioned analytically rather than by listing studies?
   - Are missing key references likely to weaken the gap claim?

7. **Argument coherence**
   - Does the logic move from problem -> gap -> RQ -> method -> evidence -> implication?
   - Are counterarguments and alternative explanations addressed?

8. **Writing clarity**
   - Does each section have a clear function?
   - Are paragraphs logically connected?
   - Are terms used consistently?

9. **Citation and integrity risk**
   - Are central citations verifiable and relevant?
   - Are numerical claims traceable to tables, figures, logs, or cited sources?
   - Are there signs of fabricated, unusable, or misapplied references?

## Workflow

1. Identify paper type, field, methodology, maturity, and likely target venue tier.
2. Select mode: `full`, `quick`, `methodology-focus`, `re-review`, or `cs-empirical-focus`.
3. For `full`, simulate four non-overlapping review lenses:
   - EIC: fit, contribution, overall decision.
   - Methodology reviewer: design, data, protocol, statistics, reproducibility.
   - Domain reviewer: literature, theoretical/technical positioning, contribution.
   - Devil's advocate: strongest counterargument, logical gaps, overgeneralization, alternative explanations.
4. Extract the main claims and map them to evidence.
5. Score risks by severity:
   - `P0`: likely rejection / fatal validity issue
   - `P1`: major revision risk
   - `P2`: clarity or completeness issue
   - `P3`: minor style or formatting issue
6. Produce reviewer reports or a consolidated risk table depending on mode.
7. Synthesize a decision: `Accept`, `Minor Revision`, `Major Revision`, `Reject and Resubmit`, or `Reject`.
8. Produce a traceable revision roadmap.

## Risk classification

Mark as `P0`:

- Core claim unsupported or contradicted by results.
- Method cannot reproduce the reported results.
- Data leakage, invalid split, or unfair comparison likely affects the central finding.
- Baselines are missing or unfair for the main contribution.
- Citations, data, or results appear fabricated or unusable.
- Devil's-advocate challenge exposes a critical unaddressed counterargument.

Mark as `P1`:

- Motivation is not connected to method.
- Evaluation is incomplete for the claimed contribution.
- Ablation or sensitivity analysis is missing for a claimed component.
- Threats to validity are generic.
- Results are interpreted beyond the empirical setting.
- Related Work misses a key line that affects the novelty claim.

Mark as `P2`:

- Paragraph flow, section structure, or terminology makes the argument hard to follow.
- Tables/figures are not explained or not tied to RQs.
- Abstract omits the actual result, method, or contribution.
- Writing issues affect readability but not the core validity.

Mark as `P3`:

- Local wording, caption clarity, citation style, formatting, or minor consistency issue.

## Scoring rubric

When the user asks for scores, use 0-100 scores with descriptors:

| Dimension | Weight | What to measure |
|---|---:|---|
| Originality | 20% | Novel contribution, gap fit, non-triviality |
| Methodological rigor | 25% | Design, validity, reproducibility, appropriate analysis |
| Evidence sufficiency | 25% | Whether claims are supported by results, sources, or artifacts |
| Argument coherence | 15% | Logical flow from problem to evidence to implication |
| Writing quality | 15% | Clarity, precision, paragraph structure, terminology |

Scores are ordinal signals, not predictions of venue acceptance. A single fatal flaw can justify rejection even when the weighted score appears moderate.

## Required references

Load these only when needed:

- `references/reviewer-risk-rubric.md`
- `references/computer-science-review.md`
- `references/review-quality-framework.md`
- `templates/editorial-review-package.md`

## Output contract

```text
## Mode and Scope
Mode:
Paper type:
Target venue assumption:
Material gaps:

## Reviewer Panel / Lenses
| Lens | Focus | Confidence | Main concern |
|---|---|---|---|

## Overall Assessment and Likely Decision
...

## Reviewer-Risk Matrix
| Priority | Location | Issue | Why it matters | Revision |
|---|---|---|---|---|

## Claim-Evidence Audit
| Claim | Evidence | Status | Action |
|---|---|---|---|

## Likely Reviewer Questions
1. ...
2. ...

## Devil's Advocate Challenge
Strongest counterargument:
Ignored alternatives:
Overgeneralization risks:

## Editorial Decision Rationale
...

## Revision Roadmap
| Priority | Revision item | Source lens | Acceptance criterion |
|---|---|---|---|
```

For `re-review`, use this additional table:

```text
## Revision Traceability Matrix
| Original issue | Author response | Manuscript evidence | Verified? | Residual risk |
|---|---|---|---|---|
```

## Hard constraints

- Do not soften serious methodological problems.
- Do not praise without evidence.
- Do not accept all author claims at face value.
- Do not propose new experiments as if they already exist.
- If a risk depends on unavailable material, mark it as `requires verification`.
- Do not fabricate reviewer disagreement; if using multiple lenses, each lens must add a distinct perspective.
- Do not make an `Accept` decision if a `P0` or critical devil's-advocate issue remains unresolved.
- Do not let numerical scores override concrete validity problems.
