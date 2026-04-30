# Software Engineering Review Checklist

## Dataset

- Are project selection criteria justified?
- Is the dataset public or reproducible?
- Are labels generated with a transparent process?
- Is label noise acknowledged?

## Protocol

- Is the target project kept unseen in CPDP?
- Are preprocessing and tuning train-only?
- Is nested validation used when model family or hyperparameters are selected?
- Are thresholds fixed or tuned without test leakage?

## Metrics

- Does the paper report positive-class metrics?
- Is MCC included for imbalanced data?
- Are confidence intervals, variance, or per-project breakdowns shown?

## Baselines and ablations

- Are baselines appropriate and fairly tuned?
- Is each claimed component ablated?
- Are raw vs sanitized or leakage-related variants clearly separated?

## Threats to validity

- Construct validity: labels, metrics, features.
- Internal validity: leakage, preprocessing, tuning.
- External validity: project/language/domain scope.
- Conclusion validity: statistical uncertainty and effect size.
