# Upstream Update Report — 2026-11-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `4bc29bdf` | `d1bdb0fa` | 2 | review-required |
| research-paper-writing-skills | `77e7c2c1` | `77e7c2c1` | 0 | ignore |
| academic-research-skills | `ef44b8f4` | `f2d109ea` | 56 | review-required |
| humanizer | `225a6f39` | `0ef9fe5b` | 1 | selective-port |

Relevant changed files: **59**

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

Relevant file status counts: modified: 2.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `CHANGELOG.md` |
| modified | `RULES.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.github/workflows/validate.yml` (modified)
- `.markdownlint-cli2.jsonc` (modified)
- `README.md` (modified)
- `RELEASING.md` (modified)
- `adapter-matrix.md` (modified)
- `agent-config.yaml` (added)
- `agents/AGENTS.md` (modified)
- `agents/aider-conventions.md` (modified)
- `agents/anthropic-skill/SKILL.md` (modified)
- `agents/claude-code.md` (modified)
- `agents/codex.md` (modified)
- `agents/copilot-instructions.md` (modified)
- `agents/copilot-path-instructions.md` (modified)
- `agents/cursor-rule.mdc` (modified)
- `agents/kiro-steering.md` (modified)
- `docs/assets/brand/Inter-OFL.txt` (added)
- `docs/assets/brand/README.md` (added)
- `docs/assets/brand/favicon.svg` (added)
- `docs/assets/brand/logo-dark.png` (added)
- `docs/assets/brand/logo-dark.svg` (added)
- `docs/assets/brand/logo.png` (added)
- `docs/assets/brand/logo.svg` (added)
- `docs/assets/brand/mark-dark.png` (added)
- `docs/assets/brand/mark-dark.svg` (added)
- `docs/assets/brand/mark-mono.png` (added)
- `docs/assets/brand/mark-mono.svg` (added)
- `docs/assets/brand/mark-white.png` (added)
- `docs/assets/brand/mark-white.svg` (added)
- `docs/assets/brand/mark.png` (added)
- `docs/assets/brand/mark.svg` (added)
- `docs/bench-habit-v0.5.0-drafts/packs/pack-A-v0.4.2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/packs/pack-B-run1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/packs/pack-B-run2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t1-abstract__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t2-contributions__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t3-results__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t4-proposal__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t5-conclusion__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/codex__t6-mixed__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t1-abstract__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t2-contributions__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t3-results__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t4-proposal__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__A__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__A__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__A__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__B__g1.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__B__g2.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t5-conclusion__B__g3.md` (added)
- `docs/bench-habit-v0.5.0-drafts/run1/drafts/opus__t6-mixed__A__g1.md` (added)
- ... 198 more

</details>

### Local Areas to Review

- `skills/en/paper-writing-en/`
- `skills/tr/tez-yazimi-tr/`
- `skills/en/paper-review-en/`

Suggested action: review rule changes and executable detector changes separately. Do not auto-port Python/NPM behavior into Turkish thesis skills without manual adaptation.

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

Relevant file status counts: added: 2, modified: 54.

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
| modified | `academic-paper-reviewer/agents/methodology_reviewer_agent.md` |
| modified | `academic-paper-reviewer/agents/perspective_reviewer_agent.md` |
| modified | `academic-paper-reviewer/references/re_review_mode_protocol.md` |
| modified | `academic-paper-reviewer/templates/editorial_decision_template.md` |
| modified | `academic-paper/SKILL.md` |
| modified | `academic-paper/agents/abstract_bilingual_agent.md` |
| modified | `academic-paper/agents/citation_compliance_agent.md` |
| modified | `academic-paper/agents/draft_writer_agent.md` |
| modified | `academic-paper/agents/formatter_agent.md` |
| modified | `academic-paper/agents/intake_agent.md` |
| modified | `academic-paper/agents/literature_strategist_agent.md` |
| modified | `academic-paper/agents/peer_reviewer_agent.md` |
| modified | `academic-paper/agents/structure_architect_agent.md` |
| modified | `academic-pipeline/SKILL.md` |
| modified | `academic-pipeline/agents/integrity_verification_agent.md` |
| modified | `academic-pipeline/agents/pipeline_orchestrator_agent.md` |
| modified | `academic-pipeline/references/ai_research_failure_modes.md` |
| modified | `academic-pipeline/references/claim_verification_protocol.md` |
| modified | `academic-pipeline/references/mode_advisor.md` |
| modified | `academic-pipeline/references/passport_as_reset_boundary.md` |
| modified | `academic-pipeline/references/pipeline_state_machine.md` |
| modified | `academic-pipeline/references/process_summary_protocol.md` |
| modified | `academic-pipeline/references/two_stage_review_protocol.md` |
| modified | `deep-research/SKILL.md` |
| modified | `deep-research/agents/bibliography_agent.md` |
| modified | `deep-research/agents/editor_in_chief_agent.md` |
| modified | `deep-research/agents/ethics_review_agent.md` |
| modified | `deep-research/agents/meta_analysis_agent.md` |
| modified | `deep-research/agents/research_architect_agent.md` |
| modified | `deep-research/agents/research_question_agent.md` |
| modified | `deep-research/agents/risk_of_bias_agent.md` |
| modified | `deep-research/agents/socratic_mentor_agent.md` |
| modified | `deep-research/agents/source_verification_agent.md` |
| modified | `deep-research/agents/synthesis_agent.md` |
| modified | `deep-research/agents/timeline_extraction_agent.md` |
| modified | `docs/ARCHITECTURE.md` |
| modified | `shared/agents/compliance_agent.md` |
| modified | `shared/contracts/README.md` |
| modified | `shared/contracts/degradation_registry.json` |
| added | `shared/contracts/passport/excluded_source_entry.schema.json` |
| added | `shared/contracts/passport/standing_constraint_entry.schema.json` |
| modified | `shared/contracts/patch/block_manifest.schema.json` |
| modified | `shared/cross_model_verification.md` |
| modified | `shared/handoff_schemas.md` |
| modified | `shared/mode_spectrum.md` |
| modified | `shared/model_tiering.md` |
| modified | `shared/references/evidence_row_protocol.md` |
| modified | `shared/references/review_form_note.md` |
| modified | `shared/references/routing_core.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.claude/CLAUDE.md` (modified)
- `.github/workflows/spec-consistency.yml` (modified)
- `CITATION.cff` (modified)
- `CONTRIBUTING.md` (modified)
- `MODE_REGISTRY.md` (modified)
- `POSITIONING.md` (modified)
- `QUICKSTART.md` (modified)
- `README.es-ES.md` (modified)
- `README.ja-JP.md` (modified)
- `README.ko-KR.md` (modified)
- `README.pt-BR.md` (added)
- `README.zh-CN.md` (modified)
- `README.zh-TW.md` (modified)
- `THIRD_PARTY.md` (modified)
- `agents/research_architect_agent.md` (modified)
- `agents/screening_reviewer_agent.md` (added)
- `agents/synthesis_agent.md` (modified)
- `docs/CONTROL_AVAILABILITY.md` (modified)
- `docs/DATA_FLOWS.md` (modified)
- `docs/PERFORMANCE.md` (modified)
- `docs/PERFORMANCE.zh-TW.md` (modified)
- `docs/RISK_REGISTER.md` (modified)
- `docs/SETUP.md` (modified)
- `docs/SETUP.zh-TW.md` (modified)
- `docs/design/2026-05-18-ars-v3.9.2-agent-phase-classification.md` (modified)
- `evals/heldout/MEASUREMENT_CONTRACT.md` (modified)
- `evals/heldout/panel_claim_factuality/PREREGISTRATION.md` (added)
- `evals/heldout/panel_claim_factuality/README.md` (added)
- `evals/heldout/panel_claim_factuality/plan.json` (added)
- `evals/heldout/panel_claim_factuality/prompts/auditor.md` (added)
- `evals/heldout/panel_claim_factuality/prompts/contrast_generate.md` (added)
- `evals/heldout/panel_claim_factuality/prompts/contrast_verify.md` (added)
- `evals/heldout/panel_claim_factuality/rubric.md` (added)
- `evals/heldout/suite_registry.json` (modified)
- `evals/heldout/within_session_ideation_diversity/nonproduction_variant.json` (modified)
- `hooks/run_guard.sh` (modified)
- `pi/README.md` (modified)
- `pi/wrapper.integration.test.mjs` (added)
- `pi/wrapper.js` (modified)
- `pi/wrapper.test.mjs` (modified)
- `requirements-dev.txt` (modified)
- `scripts/_ci_pytest_manifest.toml` (modified)
- `scripts/adapters/obsidian.py` (modified)
- `scripts/adapters/tests/test_obsidian.py` (modified)
- `scripts/announce-ars-loaded.sh` (modified)
- `scripts/ars_mark_read.py` (modified)
- `scripts/ars_write_scope_guard.py` (modified)
- `scripts/audit_panel_claims.py` (added)
- `scripts/check_670_revision_roadmap_integration.py` (modified)
- `scripts/check_684_review_criteria_binding.py` (modified)
- `scripts/check_agents_mirror_sync.py` (modified)
- `scripts/check_collaboration_depth_rubric.py` (modified)
- `scripts/check_content_coverage_advisory_integration.py` (modified)
- `scripts/check_cross_document_consistency_advisory_integration.py` (modified)
- `scripts/check_data_access_level.py` (modified)
- `scripts/check_decision_contract.py` (modified)
- `scripts/check_degradation_registry.py` (modified)
- `scripts/check_evidence_row_integration.py` (modified)
- `scripts/check_field_norm_severity.py` (modified)
- `scripts/check_instruction_data_boundary.py` (modified)
- `scripts/check_model_tiering.py` (modified)
- `scripts/check_pipeline_boundary_semantics.py` (modified)
- `scripts/check_re_review_synthesis.py` (modified)
- `scripts/check_reviewer_card_confirmation.py` (added)
- `scripts/check_reviewer_role_label.py` (modified)
- `scripts/check_skill_description_length.py` (modified)
- `scripts/check_spec_consistency.py` (modified)
- `scripts/check_surface_form_parity.py` (modified)
- `scripts/check_tools_allowlist.py` (modified)
- `scripts/check_tortured_phrase_screening_integration.py` (modified)
- `scripts/check_v3_10_134_write_scope.py` (modified)
- `scripts/check_v3_6_6_ab_manifest.py` (modified)
- `scripts/check_v3_9_2_phase_boundary.py` (modified)
- `scripts/check_v3_9_4_temporal_verification.py` (modified)
- `scripts/claim_strength_drift_disposition.py` (modified)
- `scripts/dispatch_panel_claim_audit.py` (added)
- `scripts/evidence_rows.py` (modified)
- `scripts/extract_panel_claims.py` (added)
- `scripts/fixtures/write_scope_guard/captured_payloads.json` (added)
- `scripts/human_read_attestation_resolver.py` (modified)
- `scripts/model_tiering_manifest.json` (modified)
- `scripts/run_ledger.py` (modified)
- `scripts/test_ars_mark_read.py` (modified)
- `scripts/test_ars_update_check.py` (modified)
- `scripts/test_ars_write_scope_guard.py` (modified)
- `scripts/test_audit_panel_claims.py` (added)
- `scripts/test_check_684_review_criteria_binding.py` (modified)
- `scripts/test_check_agents_mirror_sync.py` (modified)
- `scripts/test_check_collaboration_depth_rubric.py` (modified)
- `scripts/test_check_command_skill_dispatch.py` (modified)
- `scripts/test_check_content_coverage_advisory_integration.py` (modified)
- `scripts/test_check_cross_document_consistency_advisory_integration.py` (modified)
- `scripts/test_check_decision_contract.py` (modified)
- `scripts/test_check_distribution_surface_claims.py` (modified)
- `scripts/test_check_evidence_row_integration.py` (modified)
- `scripts/test_check_field_norm_severity.py` (modified)
- `scripts/test_check_instruction_data_boundary.py` (modified)
- `scripts/test_check_model_tiering.py` (modified)
- ... 62 more

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

Relevant file status counts: modified: 1.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `README.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/plugin.json` (modified)

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
