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

## Computer science and empirical software engineering details

For empirical computer science, software engineering, AI/ML, systems, HCI, data science, or related technical papers, specify the relevant subset:

- Data, benchmark, project, workload, participant, or artifact selection criteria.
- Unit of analysis: sample, instance, repository, commit, file, user, query, session, run, workload, or system component.
- Labeling, annotation, measurement, instrumentation, or data collection method.
- Feature, representation, prompt, model, system, or intervention design.
- Train/validation/test split or evaluation protocol.
- Cross-domain, cross-project, temporal, user-level, benchmark-level, or deployment-like design if applicable.
- Split-local preprocessing, feature selection, prompt selection, thresholding, and hyperparameter tuning.
- Metrics appropriate for the task and data distribution.
- Artifact, code, configuration, environment, or reproducibility details.

## Avoid

- "We preprocess the data" without details.
- "We tune the models" without search space.
- Mixing training and test information.
- Reporting implementation choices only in supplementary files when needed for reproducibility.
