# Computer Science and Empirical SE Review Checklist

Use this reference for empirical computer science, software engineering, AI/ML, systems, HCI, data science, and related technical manuscripts. The checklist is not limited to defect prediction; defect prediction, CPDP, and ML4SE are examples within the broader scope.

## Problem and contribution

- Is the task, system, dataset, method, analysis, or empirical finding clearly identified?
- Is the contribution type explicit: method, dataset, tool, benchmark, protocol, empirical result, theory, replication, negative result, or artifact?
- Does the paper explain why the contribution matters for the target research community?
- Is the novelty claim scoped to the evidence and literature coverage?

## Data and artifacts

- Are dataset construction, sampling, filtering, annotation, labeling, or instrumentation decisions transparent?
- Is the dataset public, reproducible, or sufficiently described for independent inspection?
- Are code, model, benchmark, configuration, logs, or analysis scripts available when the paper claims reproducibility?
- Are artifact versions, commits, model checkpoints, package versions, or environment details reported where needed?
- Are privacy, licensing, consent, or data-use constraints acknowledged?

## Experimental protocol

- Are train/validation/test boundaries explicit?
- Are preprocessing, feature selection, normalization, balancing, tuning, model selection, and threshold choices performed without test leakage?
- Is nested validation used when hyperparameters, model families, prompts, or thresholds are selected?
- Are random seeds, repeated runs, confidence intervals, variance, or statistical tests reported when the result depends on stochasticity?
- Are baselines implemented and tuned fairly?

## Evaluation

- Are metrics appropriate for the task and data distribution?
- For imbalanced classification, are positive-class metrics, MCC, PR-AUC, recall, precision, or task-appropriate alternatives reported?
- For ranking/retrieval, are metrics such as MRR, NDCG, recall@k, precision@k, or calibration appropriate?
- For generative models, are automatic metrics supplemented by human evaluation, error analysis, or qualitative examples when needed?
- Are negative, mixed, or per-case results reported honestly?

## Baselines, ablations, and robustness

- Are strong, recent, and relevant baselines included?
- Is each claimed component supported by an ablation, sensitivity analysis, or controlled comparison?
- Are robustness checks included for dataset shift, project/domain variation, prompt variation, random seeds, or hyperparameter sensitivity when relevant?
- Does the paper distinguish raw vs cleaned/sanitized data, or easy vs hard evaluation settings?

## Validity threats

- Construct validity: Do labels, metrics, prompts, proxies, or features measure the intended concept?
- Internal validity: Could leakage, confounding, preprocessing, tuning, sampling, or implementation bugs explain the result?
- External validity: What population, language, project type, domain, dataset, or user group does the result generalize to?
- Conclusion validity: Are effect sizes, uncertainty, statistical power, and practical significance addressed?

## Field-specific examples

- In defect prediction or CPDP, keep the target project unseen during preprocessing, tuning, and fitting if making strict transfer claims.
- In ML/NLP/CV, separate test-set use from prompt/model selection and report dataset contamination risks when relevant.
- In systems papers, include workload representativeness, hardware/software environment, and measurement variance.
- In HCI/user studies, report recruitment, demographics, study protocol, ethics approval or exemption, and qualitative coding reliability where relevant.
- In data mining papers, report sampling, deduplication, leakage, temporal splits, and label noise.
