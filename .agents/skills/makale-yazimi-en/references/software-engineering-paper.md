# Software Engineering Paper Notes

## Common reviewer concerns

- Dataset construction not transparent.
- Defect labels too noisy.
- Experimental protocol leaks target information.
- Baselines are weak or outdated.
- Metrics do not match class imbalance.
- Results are not interpreted by repository or granularity.
- Threats to validity are generic.

## CPDP and defect prediction safeguards

- Keep target project unseen during preprocessing, tuning, and fitting if making strict CPDP claims.
- Explain fold-local model selection.
- Report positive-class metrics.
- Discuss prevalence and imbalance.
- Include ablation for language-specific features when claiming language-specific value.
- Avoid "generalizes to all Go projects" unless dataset scope supports it.

## Contribution phrasing

Prefer:

```text
This study evaluates cross-project defect prediction for Go under a strict nested leave-one-project-out protocol.
```

Avoid:

```text
This study proves that our framework is a robust solution for software defect prediction.
```
