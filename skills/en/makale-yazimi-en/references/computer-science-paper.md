# Computer Science Paper Notes

Use this reference for empirical computer science, software engineering, AI/ML, systems, HCI, data science, and related technical manuscripts. It gives extra checks for technical papers without restricting the skill to one subfield.

## Common reviewer concerns

- Dataset, benchmark, workload, or participant selection is not transparent.
- Experimental protocol leaks test or target-domain information.
- Baselines are weak, outdated, unfairly tuned, or not comparable.
- Metrics do not match the task, data distribution, or user-facing claim.
- Results are not interpreted by dataset, project, domain, workload, user group, or failure mode.
- Ablations do not isolate the claimed contribution.
- Threats to validity are generic rather than tied to the design.
- Artifacts are claimed but not reproducible from the provided material.

## Empirical CS safeguards

- Keep test data, target domains, target projects, benchmark labels, and evaluation prompts out of preprocessing, tuning, model selection, and threshold selection.
- Explain fold-local or split-local model selection when applicable.
- Report task-appropriate metrics and uncertainty.
- Discuss imbalance, dataset shift, annotation noise, benchmark contamination, or workload representativeness when relevant.
- Include ablation for any module, feature family, prompt strategy, system component, or dataset cleaning step that supports a contribution claim.
- Avoid broad generalization unless the dataset, benchmark, domains, participants, or systems support it.

## Section-specific emphasis

| Section | Extra check |
|---|---|
| Introduction | State the task, gap, contribution type, and evidence without overclaiming novelty |
| Method | Provide enough detail to reproduce data processing, model/system design, and evaluation |
| Experiments | Align each research question with baselines, metrics, tables, figures, and statistical checks |
| Results | Lead with findings, include exceptions, and avoid reading every table cell aloud |
| Discussion | Interpret why results occur, what does not generalize, and what failure modes remain |
| Threats to validity | Make threats specific to labels, metrics, data, implementation, users, systems, or benchmarks |

## Contribution phrasing

Prefer scoped claims:

```text
This study evaluates the method under a split-local experimental protocol across eight datasets and reports where the gains are consistent, marginal, or absent.
```

Avoid unsupported universal claims:

```text
This study proves that the framework is a robust solution for all software analytics tasks.
```

## Examples of subfield-specific checks

- Defect prediction / CPDP: target project isolation, SZZ or labeling assumptions, class imbalance, temporal/project-aware splits.
- ML/NLP/CV: dataset contamination, prompt/model selection leakage, benchmark saturation, seed variance.
- Systems: workload representativeness, hardware/software environment, warm-up, repetitions, tail latency.
- HCI: participant recruitment, task design, ethics, qualitative coding, effect sizes.
- Data mining: sampling frame, deduplication, temporal leakage, source reliability.
