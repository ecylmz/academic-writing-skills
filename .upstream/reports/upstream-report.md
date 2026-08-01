# Upstream Update Report — 2026-08-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `e3f14369` | `e3f14369` | 0 | ignore |
| research-paper-writing-skills | `77e7c2c1` | `77e7c2c1` | 0 | ignore |
| academic-research-skills | `96e4f98b` | `462b32bf` | 71 | review-required |
| humanizer | `1b485648` | `523374de` | 2 | selective-port |

Relevant changed files: **73**

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

No upstream commit change since the last snapshot.

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

Relevant file status counts: added: 1, modified: 70.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `CHANGELOG.md` |
| modified | `README.md` |
| modified | `academic-paper-reviewer/SKILL.md` |
| modified | `academic-paper-reviewer/agents/devils_advocate_reviewer_agent.md` |
| modified | `academic-paper-reviewer/agents/domain_reviewer_agent.md` |
| modified | `academic-paper-reviewer/agents/editorial_synthesizer_agent.md` |
| modified | `academic-paper-reviewer/agents/eic_agent.md` |
| modified | `academic-paper-reviewer/agents/field_analyst_agent.md` |
| modified | `academic-paper-reviewer/agents/methodology_reviewer_agent.md` |
| modified | `academic-paper-reviewer/agents/perspective_reviewer_agent.md` |
| modified | `academic-paper-reviewer/examples/hei_paper_review_example.md` |
| modified | `academic-paper-reviewer/examples/interdisciplinary_review_example.md` |
| modified | `academic-paper-reviewer/examples/subclaim_decomposition_example.md` |
| modified | `academic-paper-reviewer/references/calibration_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/editorial_decision_standards.md` |
| modified | `academic-paper-reviewer/references/guided_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/re_review_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/review_criteria_framework.md` |
| modified | `academic-paper-reviewer/references/review_quality_thinking.md` |
| modified | `academic-paper-reviewer/references/sprint_contract_protocol.md` |
| modified | `academic-paper-reviewer/references/statistical_reporting_standards.md` |
| modified | `academic-paper-reviewer/templates/editorial_decision_template.md` |
| modified | `academic-paper-reviewer/templates/peer_review_report_template.md` |
| modified | `academic-paper-reviewer/templates/revision_response_template.md` |
| modified | `academic-paper/SKILL.md` |
| modified | `academic-paper/agents/abstract_bilingual_agent.md` |
| modified | `academic-paper/agents/citation_compliance_agent.md` |
| modified | `academic-paper/agents/draft_writer_agent.md` |
| modified | `academic-paper/agents/formatter_agent.md` |
| modified | `academic-paper/agents/literature_strategist_agent.md` |
| modified | `academic-paper/agents/peer_reviewer_agent.md` |
| modified | `academic-paper/agents/socratic_mentor_agent.md` |
| modified | `academic-paper/agents/structure_architect_agent.md` |
| modified | `academic-paper/agents/visualization_agent.md` |
| modified | `academic-paper/examples/revision_recovery_example.md` |
| modified | `academic-paper/references/anti_leakage_protocol.md` |
| modified | `academic-paper/references/failure_paths.md` |
| added | `academic-paper/references/intro_title_rhetoric_guide.md` |
| modified | `academic-paper/references/revision_patch_protocol.md` |
| modified | `academic-pipeline/SKILL.md` |
| modified | `academic-pipeline/agents/claim_ref_alignment_audit_agent.md` |
| modified | `academic-pipeline/agents/collaboration_depth_agent.md` |
| modified | `academic-pipeline/agents/integrity_verification_agent.md` |
| modified | `academic-pipeline/agents/pipeline_orchestrator_agent.md` |
| modified | `academic-pipeline/agents/state_tracker_agent.md` |
| modified | `academic-pipeline/examples/full_pipeline_example.md` |
| modified | `academic-pipeline/examples/integrity_failure_recovery.md` |
| modified | `academic-pipeline/examples/mid_entry_example.md` |
| modified | `academic-pipeline/references/adapters/overview.md` |
| modified | `academic-pipeline/references/claim_verification_protocol.md` |
| modified | `academic-pipeline/references/integrity_review_protocol.md` |
| modified | `academic-pipeline/references/pipeline_state_machine.md` |
| modified | `academic-pipeline/references/process_summary_protocol.md` |
| modified | `academic-pipeline/references/team_collaboration_protocol.md` |
| modified | `academic-pipeline/references/two_stage_review_protocol.md` |
| modified | `deep-research/SKILL.md` |
| modified | `deep-research/agents/bibliography_agent.md` |
| modified | `deep-research/agents/editor_in_chief_agent.md` |
| modified | `deep-research/agents/ethics_review_agent.md` |
| modified | `deep-research/agents/meta_analysis_agent.md` |
| modified | `deep-research/agents/report_compiler_agent.md` |
| modified | `deep-research/agents/research_architect_agent.md` |
| modified | `deep-research/agents/research_question_agent.md` |
| modified | `deep-research/agents/risk_of_bias_agent.md` |
| modified | `deep-research/agents/socratic_mentor_agent.md` |
| modified | `deep-research/agents/source_verification_agent.md` |
| modified | `deep-research/agents/synthesis_agent.md` |
| modified | `deep-research/agents/timeline_extraction_agent.md` |
| modified | `deep-research/references/arxiv_api_protocol.md` |
| modified | `deep-research/references/openalex_api_protocol.md` |
| modified | `docs/ARCHITECTURE.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.claude/CLAUDE.md` (modified)
- `.command-invariants.toml` (added)
- `.github/copilot-instructions.md` (modified)
- `.github/workflows/changelog-covers-merges.yml` (added)
- `.github/workflows/command-invariants.yml` (added)
- `.github/workflows/eval-harness.yml` (modified)
- `.github/workflows/spec-consistency.yml` (modified)
- `.github/workflows/tag-version-match.yml` (added)
- `.gitignore` (modified)
- `CITATION.cff` (modified)
- `CONTRIBUTING.md` (modified)
- `MODE_REGISTRY.md` (modified)
- `POSITIONING.md` (modified)
- `README.ja-JP.md` (modified)
- `README.ko-KR.md` (modified)
- `README.zh-CN.md` (modified)
- `README.zh-TW.md` (modified)
- `THIRD_PARTY.md` (added)
- `agents/report_compiler_agent.md` (modified)
- `agents/research_architect_agent.md` (modified)
- `agents/synthesis_agent.md` (modified)
- `audits/harness-retirement-2026-07-04.md` (added)
- `audits/rq-advisory-505-exemption-sharpening-2026-07-11.md` (added)
- `audits/rq-advisory-heldout-measurement-2026-07-11.md` (added)
- `commands/ars-cache-invalidate.md` (modified)
- `commands/ars-mark-read.md` (modified)
- `docs/PERFORMANCE.md` (modified)
- `docs/PERFORMANCE.zh-TW.md` (modified)
- `docs/SETUP.md` (modified)
- `docs/SETUP.zh-TW.md` (modified)
- `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` (modified)
- `docs/design/2026-06-13-changelog-covers-merges-release-gate-spec.md` (added)
- `docs/design/2026-07-12-517-model-tiering-spec.md` (added)
- `docs/design/2026-07-12-518-cross-model-gate-hardening-spec.md` (added)
- `docs/design/2026-07-15-510-panel-synthesis-checker-design.md` (added)
- `docs/design/2026-07-15-511-degradation-registry-design.md` (added)
- `docs/design/2026-07-18-544-update-reminder-spec.md` (added)
- `docs/design/2026-07-20-512-pdf-read-preflight-spec.md` (added)
- `docs/design/2026-07-20-513-read-scope-attestation-spec.md` (added)
- `docs/design/2026-07-25-574-spec-a-role-scoped-scoring-decision-contract-spec.md` (added)
- `docs/design/2026-07-27-576-spec-b-re-review-precommitment-contract-spec.md` (added)
- `evals/heldout/pipeline_behavior_robustness/README.md` (added)
- `evals/heldout/pipeline_behavior_robustness/heldout_set.json` (added)
- `evals/heldout/re_review_persuasion_invariance/README.md` (added)
- `evals/heldout/re_review_persuasion_invariance/heldout_set.json` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p1_letter_rhetoric/packet.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p2_manuscript_substance/packet.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-c.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/arms/arm-c.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p3_new_issue_attribution/packet.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p4_rebuttal_evidence/packet.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-c.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/arms/arm-c.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p5_change_surface/packet.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-a.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-a.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-b.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-b.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-c.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/arms/arm-c.zh-TW.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/ground_truth.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/packet.en.md` (added)
- `evals/heldout/re_review_persuasion_invariance/scenarios/p6_escalation_exception/packet.zh-TW.md` (added)
- `evals/heldout/reviewer_seeded_defects/README.md` (added)
- `evals/heldout/reviewer_seeded_defects/manifests/ms01_quant.defects.json` (added)
- `evals/heldout/reviewer_seeded_defects/manifests/ms02_qual.defects.json` (added)
- `evals/heldout/reviewer_seeded_defects/manuscripts/ms00_clean_control.md` (added)
- `evals/heldout/reviewer_seeded_defects/manuscripts/ms01_quant_defective.md` (added)
- ... 129 more

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

- `.claude-plugin/plugin.json` (modified)
- `.github/workflows/validate.yml` (added)
- `AGENTS.md` (modified)
- `agents/openai.yaml` (added)
- `scripts/validate-package.py` (added)

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
