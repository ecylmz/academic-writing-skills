# Review Quality Framework

This reference defines what a strong academic review should check before making a decision.

## Universal review dimensions

| Dimension | Review question | Common failure |
|---|---|---|
| Originality | Is the contribution new, scoped, and non-trivial? | The paper claims novelty without showing a specific gap |
| Methodological rigor | Can the method answer the research question? | Design, sampling, tuning, or analysis does not support the conclusion |
| Evidence sufficiency | Do results, sources, tables, figures, or artifacts support the claims? | Major claims are asserted rather than demonstrated |
| Argument coherence | Does the paper move logically from problem to implication? | Sections are locally clear but globally disconnected |
| Literature integration | Does the paper position itself in the field? | Related Work is a list rather than an argument |
| Writing quality | Is the manuscript clear enough to review? | Terminology drift, vague claims, weak paragraph flow |
| Significance and impact | Why should this paper matter to this venue? | The contribution is correct but too narrow or undersold |

## Paper-type checks

### Empirical paper

- Are research questions explicit?
- Are variables, datasets, sampling, and inclusion/exclusion criteria defined?
- Are methods appropriate for the research question?
- Are effect sizes, confidence intervals, variance, or statistical tests reported when needed?
- Are validity threats specific and credible?

### Method or system paper

- Is the claimed method contribution separated from implementation details?
- Are baselines fair and current?
- Are ablations tied to claimed components?
- Is the artifact reproducible or sufficiently specified?
- Are limitations and failure cases discussed?

### Literature review or survey

- Is the search strategy reproducible?
- Are inclusion/exclusion criteria explicit?
- Is the synthesis analytical rather than a catalog?
- Are publication bias, selection bias, and coverage limits discussed?

### Case study

- Is case selection justified?
- Is the context described sufficiently?
- Are multiple sources or triangulation used where possible?
- Is transferability discussed carefully?

## Constructive review standard

Every serious criticism should include:

1. **What is wrong**: the specific issue.
2. **Where it occurs**: section, paragraph, table, figure, citation, or missing item.
3. **Why it matters**: effect on validity, contribution, clarity, reproducibility, or decision.
4. **How to fix it**: concrete revision or evidence needed.
5. **Severity**: Critical, Major, Minor, or Cosmetic.

## Reviewer bias checks

- Do not require the authors to use your preferred method if their method can answer the question.
- Do not over-penalize language issues when the research design is sound.
- Do not overvalue novelty while ignoring replication, negative results, or careful empirical confirmation.
- Do not inflate scores to be polite.
- Do not treat long papers as more rigorous than concise papers.
- Distinguish "I cannot verify this from the provided material" from "the authors did not do this."

## Decision logic

- `Accept`: no critical or major unresolved issue; contribution and evidence are clear.
- `Minor Revision`: core claims are sound; fixes are local or presentational.
- `Major Revision`: paper has value but needs substantial evidence, structure, method clarification, or analysis.
- `Reject and Resubmit`: central idea may be valuable, but current design or evidence does not support the paper.
- `Reject`: out of scope, insufficient contribution, fatal method flaw, or unsupported core claim.
