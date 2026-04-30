# Claim Taxonomy

| Claim type | Definition | Required support |
|---|---|---|
| factual | A statement about what exists or occurred | source, dataset documentation, method section |
| quantitative | A number, percentage, metric, count, date, or comparison | table, figure, experiment log, source passage |
| comparative | A is better/worse/different than B | fair comparison under same protocol |
| causal | X causes Y or leads to Y | design supporting causality, ablation, controlled comparison |
| interpretive | Meaning assigned to results | results + reasoning + alternative explanations |
| contribution | novelty, first, new, original, fills gap | literature review + explicit scope |
| generalization | claims beyond observed data | external validation or narrowed wording |

## Status labels

- `supported`: evidence directly supports claim.
- `weak`: evidence partially supports claim.
- `missing`: no evidence found.
- `overclaimed`: wording exceeds evidence.
- `misaligned`: evidence supports a different claim.
- `requires source check`: source not available in the current context.
