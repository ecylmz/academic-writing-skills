---
name: makale-denetim-en
description: Reviewer-risk audit for English academic manuscripts. Evaluates contribution clarity, writing clarity, methodological rigor, empirical strength, evaluation completeness, claim-evidence alignment, and rejection risks.
---

# Research Paper Review EN

Use this skill as a skeptical reviewer before submission or revision. It does not merely proofread; it identifies why a reviewer might reject or request major revisions.

## Review dimensions

1. **Contribution**
   - Is the contribution clear, non-trivial, and scoped?
   - Is the novelty type explicit: dataset, method, task, protocol, empirical finding, tool, or analysis?

2. **Problem and motivation**
   - Does the Introduction lead naturally from task to gap to contribution?
   - Is the research gap supported rather than asserted?

3. **Methodological rigor**
   - Is the experimental protocol reproducible?
   - Are train/test boundaries, preprocessing, tuning, and evaluation clear?
   - Is leakage risk addressed?

4. **Empirical strength**
   - Are baselines strong and fair?
   - Are metrics appropriate for the data distribution?
   - Are results meaningful, not merely marginal?

5. **Evaluation completeness**
   - Are ablations, sensitivity checks, robustness checks, or negative results included when needed?
   - Are threats to validity discussed?

6. **Writing clarity**
   - Does each section have a clear function?
   - Are paragraphs logically connected?
   - Are terms used consistently?

## Workflow

1. Read the manuscript or section as a skeptical reviewer.
2. Extract the main claims.
3. Score risks by severity:
   - `P0`: likely rejection / fatal validity issue
   - `P1`: major revision risk
   - `P2`: clarity or completeness issue
   - `P3`: minor style or formatting issue
4. Produce a reviewer-risk table.
5. Suggest a revision plan.

## Output contract

```text
## Overall Assessment
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

## Revision Plan
1. Immediate fixes
2. Structural revisions
3. Optional strengthening
```

## Hard constraints

- Do not soften serious methodological problems.
- Do not praise without evidence.
- Do not accept all author claims at face value.
- Do not propose new experiments as if they already exist.
- If a risk depends on unavailable material, mark it as `requires verification`.
