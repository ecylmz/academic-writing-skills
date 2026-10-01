# Upstream Update Report — 2026-10-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `a62908b8` | `4bc29bdf` | 0 | ignore |
| research-paper-writing-skills | `77e7c2c1` | `77e7c2c1` | 0 | ignore |
| academic-research-skills | `e8bf858b` | `ef44b8f4` | 51 | review-required |
| humanizer | `e2e92e7b` | `225a6f39` | 2 | selective-port |

Relevant changed files: **53**

## Recommended Decision Vocabulary

- `ignore`: The upstream change does not affect this suite.
- `port`: Adapt the idea/checklist/template into the local skill suite.
- `vendor`: Keep the upstream file as a reference artifact without rewriting local skills yet.
- `defer`: Revisit in the next maintenance cycle.

## agent-style

- Repository: `yzhao062/agent-style`
- Branch: `main`
- Policy: `review-carefully`
- Risk level: `high`
- Reason: Style rules and executable review logic may change. Port ideas selectively; do not auto-merge.

No changed files matched this source's `watch_paths`.

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.github/workflows/adapter-gemini-smoke.yml` (modified)
- `.gitignore` (modified)
- `todo/README.md` (added)

</details>

## research-paper-writing-skills

- Repository: `Master-cai/Research-Paper-Writing-Skills`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `medium`
- Reason: Section-level paper writing guides and templates may improve. Port structure and checklists manually.

No upstream commit change since the last snapshot.

## academic-research-skills

- Repository: `Imbad0202/academic-research-skills`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `high`
- Reason: Large academic writing pipeline. Track architecture, integrity protocols, review gates, and shared schemas; adapt to Turkish thesis workflow manually.

Relevant file status counts: modified: 51.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `CHANGELOG.md` |
| modified | `README.md` |
| modified | `academic-paper-reviewer/SKILL.md` |
| modified | `academic-paper-reviewer/agents/editorial_synthesizer_agent.md` |
| modified | `academic-paper-reviewer/agents/field_analyst_agent.md` |
| modified | `academic-paper-reviewer/references/re_review_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/sprint_contract_protocol.md` |
| modified | `academic-paper-reviewer/templates/editorial_decision_template.md` |
| modified | `academic-paper/SKILL.md` |
| modified | `academic-paper/agents/abstract_bilingual_agent.md` |
| modified | `academic-paper/agents/citation_compliance_agent.md` |
| modified | `academic-paper/agents/draft_writer_agent.md` |
| modified | `academic-paper/agents/formatter_agent.md` |
| modified | `academic-paper/agents/intake_agent.md` |
| modified | `academic-paper/agents/literature_strategist_agent.md` |
| modified | `academic-paper/agents/revision_coach_agent.md` |
| modified | `academic-paper/agents/structure_architect_agent.md` |
| modified | `academic-paper/references/abstract_writing_guide.md` |
| modified | `academic-paper/references/academic_writing_style.md` |
| modified | `academic-paper/references/apa7_chinese_citation_guide.md` |
| modified | `academic-paper/references/committee_correspondence_protocol.md` |
| modified | `academic-paper/references/journal_submission_guide.md` |
| modified | `academic-paper/references/mode_selection_guide.md` |
| modified | `academic-paper/references/paper_structure_patterns.md` |
| modified | `academic-paper/references/revision_patch_protocol.md` |
| modified | `academic-paper/references/workflow_phase_details.md` |
| modified | `academic-paper/references/writing_judgment_framework.md` |
| modified | `academic-paper/references/writing_quality_check.md` |
| modified | `academic-paper/templates/bilingual_abstract_template.md` |
| modified | `academic-pipeline/SKILL.md` |
| modified | `academic-pipeline/agents/claim_ref_alignment_audit_agent.md` |
| modified | `academic-pipeline/agents/integrity_verification_agent.md` |
| modified | `academic-pipeline/agents/pipeline_orchestrator_agent.md` |
| modified | `academic-pipeline/agents/state_tracker_agent.md` |
| modified | `academic-pipeline/references/claim_verification_protocol.md` |
| modified | `academic-pipeline/references/passport_as_reset_boundary.md` |
| modified | `academic-pipeline/references/pipeline_state_machine.md` |
| modified | `deep-research/SKILL.md` |
| modified | `deep-research/agents/bibliography_agent.md` |
| modified | `deep-research/agents/devils_advocate_agent.md` |
| modified | `deep-research/agents/editor_in_chief_agent.md` |
| modified | `deep-research/agents/ethics_review_agent.md` |
| modified | `deep-research/agents/report_compiler_agent.md` |
| modified | `deep-research/agents/risk_of_bias_agent.md` |
| modified | `deep-research/agents/synthesis_agent.md` |
| modified | `deep-research/agents/timeline_extraction_agent.md` |
| modified | `deep-research/references/failure_paths.md` |
| modified | `deep-research/references/mode_selection_guide.md` |
| modified | `deep-research/references/socratic_mode_protocol.md` |
| modified | `deep-research/templates/evidence_assessment_template.md` |
| modified | `docs/ARCHITECTURE.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.claude/CLAUDE.md` (modified)
- `.github/workflows/command-invariants.yml` (modified)
- `.github/workflows/spec-consistency.yml` (modified)
- `.gitignore` (modified)
- `CITATION.cff` (modified)
- `CONTRIBUTING.md` (modified)
- `MODE_REGISTRY.md` (modified)
- `POSITIONING.md` (modified)
- `QUICKSTART.md` (modified)
- `README.es-ES.md` (added)
- `README.ja-JP.md` (modified)
- `README.ko-KR.md` (modified)
- `README.zh-CN.md` (modified)
- `README.zh-TW.md` (modified)
- `THIRD_PARTY.md` (modified)
- `agents/report_compiler_agent.md` (modified)
- `agents/synthesis_agent.md` (modified)
- `audits/harness-retirement-2026-09-model-update.md` (added)
- `audits/harness-retirement-2026-09-opus-5-5.md` (added)
- `audits/harness-retirement-2026-09.md` (added)
- `commands/ars-3w.md` (modified)
- `commands/ars-abstract.md` (modified)
- `commands/ars-citation-check.md` (modified)
- `commands/ars-disclosure.md` (modified)
- `commands/ars-format-convert.md` (modified)
- `commands/ars-full.md` (modified)
- `commands/ars-lit-review.md` (modified)
- `commands/ars-outline.md` (modified)
- `commands/ars-plan.md` (modified)
- `commands/ars-rebuttal-audit.md` (modified)
- `commands/ars-reviewer.md` (modified)
- `commands/ars-revision-coach.md` (modified)
- `commands/ars-revision.md` (modified)
- `docs/CONTROL_AVAILABILITY.md` (modified)
- `docs/DATA_FLOWS.md` (modified)
- `docs/PERFORMANCE.md` (modified)
- `docs/PERFORMANCE.zh-TW.md` (modified)
- `docs/RISK_REGISTER.md` (modified)
- `docs/ROADMAP-v3.20.1-v3.22.md` (modified)
- `docs/SETUP.md` (modified)
- `docs/SETUP.zh-TW.md` (modified)
- `docs/STAGE_CAPABILITY_MATRIX.md` (modified)
- `docs/changelog-archive/es-ES.md` (added)
- `docs/changelog-archive/ja-JP.md` (added)
- `docs/changelog-archive/ko-KR.md` (added)
- `docs/changelog-archive/zh-CN.md` (added)
- `docs/changelog-archive/zh-TW.md` (added)
- `docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md` (modified)
- `docs/design/2026-09-23-887-handoff-integrity-design.md` (added)
- `docs/design/2026-09-23-890-instruction-data-boundary-extension.md` (added)
- `docs/design/2026-09-24-894-instruction-data-boundary-tool-calls.md` (added)
- `evals/heldout/MEASUREMENT_CONTRACT.md` (modified)
- `evals/heldout/experiment_alignment_overclaim/README.md` (added)
- `evals/heldout/experiment_alignment_overclaim/heldout_set.json` (added)
- `evals/heldout/experiment_alignment_overclaim/passports/st2-01-negative-transfer.yaml` (added)
- `evals/heldout/experiment_alignment_overclaim/passports/st2-02-neighbour-attention.yaml` (added)
- `evals/heldout/per_source_method_weaknesses/README.md` (added)
- `evals/heldout/per_source_method_weaknesses/heldout_set.json` (added)
- `evals/heldout/reviewer_calibration/README.md` (added)
- `evals/heldout/reviewer_calibration/RUN_PLAN.md` (added)
- `evals/heldout/reviewer_calibration/adjudication_rubric.md` (added)
- `evals/heldout/reviewer_calibration/corpus/papers.json` (added)
- `evals/heldout/reviewer_calibration/corpus/pool_accepted_ids.txt` (added)
- `evals/heldout/reviewer_calibration/corpus/pool_rejected_ids.txt` (added)
- `evals/heldout/reviewer_calibration/manifests/gold_labels.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/model_probe.txt` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_AOUa1Ae9qg.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_CPxZClPMiy.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_CU5EHe1KUt.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_GDYaNzxt9T.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_If8O8CdCbi.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_KN2RD4fpnH.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_KqCU5rfcMm.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_OKUGAxu6Ww.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_SqQYMnfyLS.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_TIDaHgj0Yj.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_UbWy2QVmke.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_VVstc2W3RW.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_XrgZp1NFDT.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_ZumVIktGbt.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_nCEs0tSwc2.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_prompts.txt` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_qRTJWXentH.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_ssWi0rC3mx.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/contamination_probe/probe_xPEsxcO7F7.json` (added)
- `evals/heldout/reviewer_calibration/runs/raw/selection.json` (added)
- `evals/heldout/suite_registry.json` (modified)
- `evals/heldout/unsupported_claim_recovery/README.md` (added)
- `evals/heldout/unsupported_claim_recovery/heldout_set.json` (added)
- `examples/showcase/README.md` (modified)
- `pi/README.md` (modified)
- `pi/wrapper.js` (modified)
- `pi/wrapper.test.mjs` (modified)
- `plugin-evals-citation-check/01-apa-en-misattribution/graders/content-caught.md` (added)
- `plugin-evals-citation-check/01-apa-en-misattribution/graders/format-caught.md` (added)
- `plugin-evals-citation-check/01-apa-en-misattribution/graders/honest-unverified.md` (added)
- `plugin-evals-citation-check/01-apa-en-misattribution/graders/no-false-positive.md` (added)
- `plugin-evals-citation-check/01-apa-en-misattribution/graders/no-overreach.md` (added)
- ... 149 more

</details>

### Local Areas to Review

- `skills/tr/tez-yazimi-tr/`
- `skills/tr/tez-denetim-tr/`
- `skills/tr/tez-latex-format-tr/`
- `skills/en/research-integrity-audit/`

Suggested action: compare the changed upstream guide/template with the local skill references and port only the parts that improve this suite's thesis or paper workflow.

## humanizer

- Repository: `blader/humanizer`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `medium`
- Reason: Naturalness and AI-output pattern guidance may change. Port selectively and preserve this suite's academic integrity boundaries.

Relevant file status counts: modified: 2.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `README.md` |
| modified | `SKILL.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.cursor-plugin/plugin.json` (added)
- `.github/ISSUE_TEMPLATE/config.yml` (added)
- `.github/ISSUE_TEMPLATE/new-pattern.yml` (added)
- `.github/ISSUE_TEMPLATE/rewrite-problem.yml` (added)
- `.github/workflows/validate.yml` (modified)
- `AGENTS.md` (modified)
- `CHANGELOG.md` (added)
- `scripts/validate-package.py` (modified)

</details>

### Local Areas to Review

- `skills/en/humanizer/`
- `skills/tr/humanizer-tr/`

Suggested action: compare the changed upstream guide/template with the local skill references and port only the parts that improve this suite's thesis or paper workflow.

## Maintenance Checklist

- [ ] Read each relevant changed file.
- [ ] Decide `ignore`, `port`, `vendor`, or `defer` for each source.
- [ ] If porting, update local `SKILL.md`, `references/`, or `templates/` files.
- [ ] Run `python3 tools/check_skill_suite.py`.
- [ ] Update `SOURCE_NOTES.md` if attribution or adaptation scope changes.
