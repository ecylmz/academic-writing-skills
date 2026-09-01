# Upstream Update Report — 2026-09-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `e3f14369` | `a62908b8` | 53 | review-required |
| research-paper-writing-skills | `77e7c2c1` | `77e7c2c1` | 0 | ignore |
| academic-research-skills | `462b32bf` | `e8bf858b` | 86 | review-required |
| humanizer | `523374de` | `e2e92e7b` | 2 | selective-port |

Relevant changed files: **141**

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

Relevant file status counts: added: 30, modified: 23.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `CHANGELOG.md` |
| modified | `SOURCES.md` |
| modified | `packages/npm/data/skills/style-review/SKILL.md` |
| modified | `packages/npm/data/skills/style-review/references/fixture-prose/mech-violations.expected.json` |
| modified | `packages/npm/data/skills/style-review/references/fixture-prose/mixed.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w1-rule-i.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w1-rule-i.md` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w2-rule-b.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w2-rule-b.md` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w3-rule-g.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w3-rule-g.md` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w4-rule-a.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w4-rule-a.md` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w5-rule-05-d.expected.json` |
| added | `packages/npm/data/skills/style-review/references/fixture-prose/regression-w5-rule-05-d.md` |
| modified | `packages/npm/data/skills/style-review/references/fixture-prose/struct-violations.expected.json` |
| modified | `packages/npm/data/skills/style-review/references/rule-detectors.md` |
| modified | `packages/pypi/agent_style/data/skills/style-review/SKILL.md` |
| modified | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/mech-violations.expected.json` |
| modified | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/mixed.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w1-rule-i.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w1-rule-i.md` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w2-rule-b.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w2-rule-b.md` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w3-rule-g.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w3-rule-g.md` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w4-rule-a.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w4-rule-a.md` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w5-rule-05-d.expected.json` |
| added | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/regression-w5-rule-05-d.md` |
| modified | `packages/pypi/agent_style/data/skills/style-review/references/fixture-prose/struct-violations.expected.json` |
| modified | `packages/pypi/agent_style/data/skills/style-review/references/rule-detectors.md` |
| modified | `packages/pypi/agent_style/review/__init__.py` |
| modified | `packages/pypi/agent_style/review/detectors_mech.py` |
| modified | `packages/pypi/agent_style/review/detectors_sem.py` |
| modified | `packages/pypi/agent_style/review/detectors_struct.py` |
| modified | `packages/pypi/agent_style/review/loader.py` |
| modified | `packages/pypi/agent_style/review/primitive.py` |
| modified | `skills/style-review/SKILL.md` |
| modified | `skills/style-review/references/fixture-prose/mech-violations.expected.json` |
| modified | `skills/style-review/references/fixture-prose/mixed.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w1-rule-i.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w1-rule-i.md` |
| added | `skills/style-review/references/fixture-prose/regression-w2-rule-b.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w2-rule-b.md` |
| added | `skills/style-review/references/fixture-prose/regression-w3-rule-g.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w3-rule-g.md` |
| added | `skills/style-review/references/fixture-prose/regression-w4-rule-a.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w4-rule-a.md` |
| added | `skills/style-review/references/fixture-prose/regression-w5-rule-05-d.expected.json` |
| added | `skills/style-review/references/fixture-prose/regression-w5-rule-05-d.md` |
| modified | `skills/style-review/references/fixture-prose/struct-violations.expected.json` |
| modified | `skills/style-review/references/rule-detectors.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.gitattributes` (added)
- `.github/workflows/publish.yml` (modified)
- `.github/workflows/real-agent-smoke.yml` (modified)
- `.github/workflows/validate.yml` (modified)
- `README.md` (modified)
- `RELEASING.md` (modified)
- `TODO.md` (modified)
- `adapter-matrix.md` (modified)
- `agents/AGENTS.md` (modified)
- `agents/aider-conventions.md` (modified)
- `agents/anthropic-skill/SKILL.md` (modified)
- `agents/claude-code.md` (modified)
- `agents/codex.md` (modified)
- `agents/copilot-instructions.md` (modified)
- `agents/copilot-path-instructions.md` (modified)
- `agents/cursor-rule.mdc` (modified)
- `agents/kiro-steering.md` (modified)
- `docs/bench-0.2.0-gemini-archive.md` (modified)
- `docs/bench-0.2.0.md` (modified)
- `docs/bench-0.3.0-claude.md` (modified)
- `docs/bench-0.3.0-codex.md` (modified)
- `docs/bench-0.3.0-copilot-noisy-archive.md` (modified)
- `docs/bench-0.3.0-copilot.md` (modified)
- `docs/bench-0.3.0-gemini-2.5-pro-archive.md` (modified)
- `docs/bench-0.3.0-gemini-3.1-pro-partial-archive.md` (modified)
- `docs/bench-0.3.0-gemini-flash.md` (modified)
- `docs/bench-0.3.0-gemini.md` (modified)
- `docs/bench-0.3.0-rescored.md` (added)
- `docs/bench-0.3.0.md` (modified)
- `docs/bench.png` (modified)
- `docs/followups/2026-08-11-release-as-unit-of-consumption.md` (added)
- `docs/hero-source/bench.html` (modified)
- `docs/hero-source/hero.html` (modified)
- `docs/hero-source/sources.html` (modified)
- `docs/hero.png` (modified)
- `docs/preregistration-generation-decay.md` (added)
- `docs/sources.png` (modified)
- `packages/npm/README.md` (modified)
- `packages/npm/data/agents/AGENTS.md` (modified)
- `packages/npm/data/agents/aider-conventions.md` (modified)
- `packages/npm/data/agents/anthropic-skill/SKILL.md` (modified)
- `packages/npm/data/agents/claude-code.md` (modified)
- `packages/npm/data/agents/codex.md` (modified)
- `packages/npm/data/agents/copilot-instructions.md` (modified)
- `packages/npm/data/agents/copilot-path-instructions.md` (modified)
- `packages/npm/data/agents/cursor-rule.mdc` (modified)
- `packages/npm/data/agents/kiro-steering.md` (modified)
- `packages/npm/data/tools.json` (modified)
- `packages/npm/lib/review/detectors_mech.js` (modified)
- `packages/npm/lib/review/detectors_struct.js` (modified)
- `packages/npm/lib/review/loader.js` (modified)
- `packages/npm/lib/review/primitive.js` (modified)
- `packages/npm/package.json` (modified)
- `packages/npm/test/review.test.js` (modified)
- `packages/pypi/README.md` (modified)
- `packages/pypi/agent_style/__init__.py` (modified)
- `packages/pypi/agent_style/data/agents/AGENTS.md` (modified)
- `packages/pypi/agent_style/data/agents/aider-conventions.md` (modified)
- `packages/pypi/agent_style/data/agents/anthropic-skill/SKILL.md` (modified)
- `packages/pypi/agent_style/data/agents/claude-code.md` (modified)
- `packages/pypi/agent_style/data/agents/codex.md` (modified)
- `packages/pypi/agent_style/data/agents/copilot-instructions.md` (modified)
- `packages/pypi/agent_style/data/agents/copilot-path-instructions.md` (modified)
- `packages/pypi/agent_style/data/agents/cursor-rule.mdc` (modified)
- `packages/pypi/agent_style/data/agents/kiro-steering.md` (modified)
- `packages/pypi/agent_style/data/tools.json` (modified)
- `packages/pypi/pyproject.toml` (modified)
- `packages/pypi/tests/test_handshake_parity.py` (added)
- `packages/pypi/tests/test_rescore_provenance.py` (added)
- `packages/pypi/tests/test_review_fixtures.py` (modified)
- `packages/pypi/tests/test_rule07_classification.py` (modified)
- `scripts/bench/rescore.py` (added)
- `scripts/bench/run.sh` (modified)
- `scripts/bump-version.py` (modified)
- `scripts/run-tests.sh` (added)
- `scripts/verify-fresh-install.py` (modified)
- `scripts/verify-install.sh` (modified)

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

Relevant file status counts: added: 4, modified: 82.

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
| modified | `academic-paper-reviewer/references/changelog.md` |
| modified | `academic-paper-reviewer/references/editorial_decision_standards.md` |
| modified | `academic-paper-reviewer/references/guided_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/quality_rubrics.md` |
| modified | `academic-paper-reviewer/references/re_review_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/review_criteria_framework.md` |
| added | `academic-paper-reviewer/references/review_panel_provenance_protocol.md` |
| modified | `academic-paper-reviewer/references/review_quality_thinking.md` |
| added | `academic-paper-reviewer/references/reviewer_sprint_prompt_source.md` |
| modified | `academic-paper-reviewer/references/sprint_contract_protocol.md` |
| modified | `academic-paper-reviewer/references/statistical_reporting_standards.md` |
| modified | `academic-paper-reviewer/references/top_journals_by_field.md` |
| modified | `academic-paper-reviewer/templates/editorial_decision_template.md` |
| modified | `academic-paper-reviewer/templates/peer_review_report_template.md` |
| modified | `academic-paper-reviewer/templates/revision_response_template.md` |
| modified | `academic-paper/SKILL.md` |
| modified | `academic-paper/agents/argument_builder_agent.md` |
| modified | `academic-paper/agents/draft_writer_agent.md` |
| modified | `academic-paper/agents/formatter_agent.md` |
| modified | `academic-paper/agents/intake_agent.md` |
| modified | `academic-paper/agents/literature_strategist_agent.md` |
| modified | `academic-paper/agents/peer_reviewer_agent.md` |
| modified | `academic-paper/agents/revision_coach_agent.md` |
| modified | `academic-paper/agents/structure_architect_agent.md` |
| modified | `academic-paper/examples/revision_mode_example.md` |
| modified | `academic-paper/examples/revision_recovery_example.md` |
| modified | `academic-paper/references/citation_format_switcher.md` |
| added | `academic-paper/references/committee_correspondence_protocol.md` |
| modified | `academic-paper/references/disclosure_mode_protocol.md` |
| modified | `academic-paper/references/failure_paths.md` |
| modified | `academic-paper/references/mode_selection_guide.md` |
| modified | `academic-paper/references/policy_anchor_disclosure_protocol.md` |
| modified | `academic-paper/references/revision_patch_protocol.md` |
| modified | `academic-paper/references/venue_disclosure_policies.md` |
| modified | `academic-paper/references/workflow_phase_details.md` |
| modified | `academic-pipeline/SKILL.md` |
| modified | `academic-pipeline/agents/integrity_verification_agent.md` |
| modified | `academic-pipeline/agents/pipeline_orchestrator_agent.md` |
| modified | `academic-pipeline/agents/state_tracker_agent.md` |
| modified | `academic-pipeline/examples/full_pipeline_example.md` |
| modified | `academic-pipeline/examples/integrity_failure_recovery.md` |
| modified | `academic-pipeline/examples/mid_entry_example.md` |
| modified | `academic-pipeline/references/adapters/overview.md` |
| modified | `academic-pipeline/references/claim_verification_protocol.md` |
| modified | `academic-pipeline/references/integrity_review_protocol.md` |
| modified | `academic-pipeline/references/literature_corpus_consumers.md` |
| modified | `academic-pipeline/references/passport_as_reset_boundary.md` |
| modified | `academic-pipeline/references/pipeline_state_machine.md` |
| modified | `academic-pipeline/references/process_summary_protocol.md` |
| modified | `academic-pipeline/references/reinforcement_content.md` |
| modified | `academic-pipeline/references/reproducibility_audit.md` |
| modified | `academic-pipeline/references/score_trajectory_protocol.md` |
| modified | `academic-pipeline/references/team_collaboration_protocol.md` |
| modified | `academic-pipeline/references/two_stage_review_protocol.md` |
| modified | `deep-research/SKILL.md` |
| modified | `deep-research/agents/bibliography_agent.md` |
| modified | `deep-research/agents/devils_advocate_agent.md` |
| modified | `deep-research/agents/ethics_review_agent.md` |
| modified | `deep-research/agents/research_architect_agent.md` |
| modified | `deep-research/agents/research_question_agent.md` |
| modified | `deep-research/agents/socratic_mentor_agent.md` |
| modified | `deep-research/examples/handoff_to_paper.md` |
| added | `deep-research/references/chinese_literature_api_protocol.md` |
| modified | `deep-research/references/crossref_api_protocol.md` |
| modified | `deep-research/references/equator_reporting_guidelines.md` |
| modified | `deep-research/references/ethics_checklist.md` |
| modified | `deep-research/references/failure_paths.md` |
| modified | `deep-research/references/irb_decision_tree.md` |
| modified | `deep-research/references/openalex_api_protocol.md` |
| modified | `deep-research/references/preregistration_guide.md` |
| modified | `deep-research/references/socratic_mode_protocol.md` |
| modified | `docs/ARCHITECTURE.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.claude/CLAUDE.md` (modified)
- `.github/workflows/command-invariants.yml` (modified)
- `.github/workflows/harness-retirement-monthly.yml` (modified)
- `.github/workflows/spec-consistency.yml` (modified)
- `.gitignore` (modified)
- `.gitleaks.toml` (modified)
- `.gitleaksignore` (added)
- `CITATION.cff` (modified)
- `CONTRIBUTING.md` (modified)
- `GOVERNANCE.md` (added)
- `MODE_REGISTRY.md` (modified)
- `NOTICE.md` (modified)
- `POSITIONING.md` (modified)
- `README.ja-JP.md` (modified)
- `README.ko-KR.md` (modified)
- `README.zh-CN.md` (modified)
- `README.zh-TW.md` (modified)
- `SECURITY.md` (modified)
- `THIRD_PARTY.md` (modified)
- `agents/research_architect_agent.md` (modified)
- `audits/575-scope-closure-audit-2026-08-24.md` (added)
- `audits/575-source-backed-proving-set-2026-08-24.md` (added)
- `audits/684-expert-readiness-2026-08-24.md` (added)
- `audits/bakeoff-gpt-5-6-sol-codex-2026-08-19.md` (added)
- `audits/external-contribution-audit-prompt.md` (added)
- `audits/harness-retirement-2026-08.md` (added)
- `audits/iso42001-spirit-gap-assessment-2026-08-17.md` (added)
- `commands/ars-3w.md` (modified)
- `commands/ars-abstract.md` (modified)
- `commands/ars-cache-invalidate.md` (modified)
- `commands/ars-citation-check.md` (modified)
- `commands/ars-disclosure.md` (modified)
- `commands/ars-format-convert.md` (modified)
- `commands/ars-full.md` (modified)
- `commands/ars-lit-review.md` (modified)
- `commands/ars-mark-read.md` (modified)
- `commands/ars-outline.md` (modified)
- `commands/ars-plan.md` (modified)
- `commands/ars-rebuttal-audit.md` (modified)
- `commands/ars-reviewer.md` (modified)
- `commands/ars-revision-coach.md` (modified)
- `commands/ars-revision.md` (modified)
- `commands/ars-unmark-read.md` (modified)
- `docs/CONTROL_AVAILABILITY.md` (added)
- `docs/DATA_FLOWS.md` (added)
- `docs/PERFORMANCE.md` (modified)
- `docs/PERFORMANCE.zh-TW.md` (modified)
- `docs/RISK_REGISTER.md` (added)
- `docs/ROADMAP-v3.11.md` (modified)
- `docs/ROADMAP-v3.20.1-v3.22.md` (added)
- `docs/SETUP.md` (modified)
- `docs/SETUP.zh-TW.md` (modified)
- `docs/STAGE_CAPABILITY_MATRIX.md` (added)
- `docs/design/2026-06-07-272-instruction-data-boundary-design.md` (modified)
- `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` (modified)
- `docs/design/2026-07-20-512-pdf-read-preflight-spec.md` (modified)
- `docs/design/2026-07-20-513-read-scope-attestation-spec.md` (modified)
- `docs/design/2026-07-27-576-spec-b-re-review-precommitment-contract-spec.md` (modified)
- `docs/design/2026-08-02-610-statistical-recompute-baseline-spec.md` (added)
- `docs/design/2026-08-06-610-step5-script-adapter-spec.md` (added)
- `docs/design/2026-08-08-651-retraction-status-spec.md` (added)
- `docs/design/2026-08-08-668-committee-correspondence-spec.md` (added)
- `docs/design/2026-08-08-683-review-target-context-spec.md` (added)
- `docs/design/2026-08-09-656-shared-evidence-row-contract-spec.md` (added)
- `docs/design/2026-08-09-666-human-subjects-authority-contract-spec.md` (added)
- `docs/design/2026-08-09-667-submission-packet-manifest-spec.md` (added)
- `docs/design/2026-08-09-680-human-subjects-reference-migration-spec.md` (added)
- `docs/design/2026-08-09-681-authority-content-coverage-advisory-spec.md` (added)
- `docs/design/2026-08-10-658-outcome-level-evaluation-design.md` (added)
- `docs/design/2026-08-10-660-tortured-phrase-screening-spec.md` (added)
- `docs/design/2026-08-10-670-non-ranking-revision-roadmap-spec.md` (added)
- `docs/design/2026-08-10-672-cross-document-consistency-advisory-spec.md` (added)
- `docs/design/2026-08-10-673-cross-run-adjudication-activity-spec.md` (added)
- `docs/design/2026-08-10-679-revision-claim-drift-suite-v2-spec.md` (added)
- `docs/design/2026-08-11-630-codex-subscription-citation-transport-spec.md` (added)
- `docs/design/2026-08-11-669-review-pathway-rule-trace-spec.md` (added)
- `docs/design/2026-08-11-684-review-criteria-consumer-binding-spec.md` (added)
- `docs/design/2026-08-13-512-pdf-content-classification-sandbox-spec.md` (added)
- `docs/design/2026-08-13-582-role-topology-utility-design.md` (added)
- `docs/design/2026-08-13-655-search-bounded-claim-standing-probe-design.md` (added)
- `docs/design/2026-08-13-659-within-session-ideation-diversity-design.md` (added)
- `docs/design/2026-08-13-675-indirect-prompt-injection-behavior-eval-spec.md` (added)
- `docs/design/2026-08-17-742-research-family-profile-contract-design.md` (added)
- `docs/design/2026-08-17-743-inquiry-branch-ledger-design.md` (added)
- `docs/design/2026-08-24-744-alternative-explanation-register-design.md` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/probe_set.json` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/receipt_contract.py` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/run7_call_index.jsonl` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/run7_receipts_gpt-5.5.jsonl` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/run7_receipts_gpt-5.6-sol.jsonl` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/run_fleet.py` (added)
- `evals/bakeoff/2026-08-19-gpt-5-6-sol-codex/score_run.py` (added)
- `evals/gold/citation_extraction/README.md` (modified)
- `evals/gold/citation_extraction/manifest.yaml` (modified)
- `evals/heldout/MEASUREMENT_CONTRACT.md` (added)
- `evals/heldout/authority_content_coverage/README.md` (added)
- `evals/heldout/claim_standing_probe/README.md` (added)
- `evals/heldout/claim_standing_probe/adjudicated_labels.schema.json` (added)
- ... 114 more

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
- `.github/workflows/validate.yml` (modified)
- `AGENTS.md` (modified)
- `agents/openai.yaml` (modified)
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
