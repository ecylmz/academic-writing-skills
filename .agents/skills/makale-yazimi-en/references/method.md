# Method Section Guide

The Method section should be reproducible. A reader should know exactly what was done, in what order, and with what constraints.

## Required elements

- Data or materials.
- Preprocessing.
- Feature extraction or representation.
- Model or algorithm.
- Training and tuning protocol.
- Evaluation setup.
- Implementation details.

## Writing order

1. Overview paragraph.
2. Data/materials.
3. Processing pipeline.
4. Model/procedure.
5. Experimental protocol.
6. Metrics and statistical analysis.
7. Reproducibility details.

## Software engineering details

For defect prediction papers, specify:

- Projects and selection criteria.
- Granularity: commit/file/method.
- Labeling method.
- Feature families.
- Train/test split.
- Cross-project or within-project design.
- Fold-local preprocessing.
- Hyperparameter tuning.
- Decision threshold.
- Metrics for imbalanced data.

## Avoid

- "We preprocess the data" without details.
- "We tune the models" without search space.
- Mixing training and test information.
- Reporting implementation choices only in supplementary files when needed for reproducibility.
