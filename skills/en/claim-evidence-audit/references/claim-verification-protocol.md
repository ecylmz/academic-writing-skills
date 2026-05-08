# Claim Verification Protocol

Use this reference when the user asks whether factual, quantitative, comparative, trend, or causal claims are accurate.

## Claim extraction

Extract claims that are review-critical:

- Numerical claims: percentages, counts, metrics, p-values, effect sizes, dates.
- Comparative claims: better, worse, higher, lower, first, largest, state-of-the-art.
- Trend claims: increasing, declining, stable, consistent.
- Causal claims: causes, leads to, improves, reduces, enables.
- Literature-gap claims: prior work lacks, no study has, existing methods fail to.
- Methodological claims: reproducible, leakage-free, fair comparison, robust.

## Evidence tracing

For each claim, identify the exact supporting material:

| Evidence type | What to verify |
|---|---|
| Table or figure | Number, metric, dataset, split, baseline, and caption match the text |
| Experiment log | Reported value matches the run, seed, fold, or aggregate |
| Method section | The method described can produce the claimed result |
| Citation | The cited source contains the claim, not merely a related topic |
| Appendix/artifact | Version, commit, dataset release, or supplementary file is available |

## Verdict labels

| Verdict | Meaning | Action |
|---|---|---|
| `verified` | Claim matches the evidence directly | Keep |
| `minor distortion` | Meaning is mostly preserved but wording is slightly stronger or less precise | Revise wording |
| `major distortion` | Claim exaggerates, simplifies, or changes what the evidence says | Fix before review |
| `unsupported` | No evidence is provided | Add evidence or remove |
| `unverifiable access` | Source exists but relevant passage is unavailable | Mark as requires source check |
| `scope mismatch` | Evidence supports only a narrower condition | Add scope condition |

## Sampling modes

- `pre-review`: Check all claims in Abstract and Introduction, plus a sample from other sections.
- `final-check`: Check every major claim before submission.
- `re-review`: Check claims changed during revision and claims involved in reviewer comments.

## Pass criteria

A manuscript is not reviewer-ready if any core claim is `major distortion`, `unsupported`, or `scope mismatch` without a revision plan.
