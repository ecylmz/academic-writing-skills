# Upstream Update Report — 2026-07-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `ba2e4729` | `e3f14369` | 9 | review-required |
| research-paper-writing-skills | `9ee5eddc` | `77e7c2c1` | 1 | selective-port |
| academic-research-skills | `4c385717` | `96e4f98b` | 49 | review-required |
| humanizer | `a2ace14a` | `1b485648` | 2 | selective-port |

Relevant changed files: **61**

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

Relevant file status counts: modified: 9.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `CHANGELOG.md` |
| modified | `RULES.md` |
| modified | `packages/npm/data/skills/style-review/SKILL.md` |
| modified | `packages/npm/data/skills/style-review/references/rule-detectors.md` |
| modified | `packages/pypi/agent_style/data/skills/style-review/SKILL.md` |
| modified | `packages/pypi/agent_style/data/skills/style-review/references/rule-detectors.md` |
| modified | `packages/pypi/agent_style/review/primitive.py` |
| modified | `skills/style-review/SKILL.md` |
| modified | `skills/style-review/references/rule-detectors.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.github/workflows/publish.yml` (added)
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
- `docs/rule-pack-compact.md` (modified)
- `docs/rule-pack.md` (modified)
- `packages/npm/README.md` (modified)
- `packages/npm/data/RULES.md` (modified)
- `packages/npm/data/agents/AGENTS.md` (modified)
- `packages/npm/data/agents/aider-conventions.md` (modified)
- `packages/npm/data/agents/anthropic-skill/SKILL.md` (modified)
- `packages/npm/data/agents/claude-code.md` (modified)
- `packages/npm/data/agents/codex.md` (modified)
- `packages/npm/data/agents/copilot-instructions.md` (modified)
- `packages/npm/data/agents/copilot-path-instructions.md` (modified)
- `packages/npm/data/agents/cursor-rule.mdc` (modified)
- `packages/npm/data/agents/kiro-steering.md` (modified)
- `packages/npm/data/rule-pack-compact.md` (modified)
- `packages/npm/lib/review/primitive.js` (modified)
- `packages/npm/package.json` (modified)
- `packages/npm/test/review.test.js` (modified)
- `packages/pypi/README.md` (modified)
- `packages/pypi/agent_style/__init__.py` (modified)
- `packages/pypi/agent_style/data/RULES.md` (modified)
- `packages/pypi/agent_style/data/agents/AGENTS.md` (modified)
- `packages/pypi/agent_style/data/agents/aider-conventions.md` (modified)
- `packages/pypi/agent_style/data/agents/anthropic-skill/SKILL.md` (modified)
- `packages/pypi/agent_style/data/agents/claude-code.md` (modified)
- `packages/pypi/agent_style/data/agents/codex.md` (modified)
- `packages/pypi/agent_style/data/agents/copilot-instructions.md` (modified)
- `packages/pypi/agent_style/data/agents/copilot-path-instructions.md` (modified)
- `packages/pypi/agent_style/data/agents/cursor-rule.mdc` (modified)
- `packages/pypi/agent_style/data/agents/kiro-steering.md` (modified)
- `packages/pypi/agent_style/data/rule-pack-compact.md` (modified)
- `packages/pypi/pyproject.toml` (modified)
- `packages/pypi/tests/test_rule07_classification.py` (added)
- `scripts/verify-fresh-install.py` (modified)

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

Relevant file status counts: modified: 1.

### Relevant Changed Files

| Status | File |
|---|---|
| modified | `research-paper-writing/SKILL.md` |

### Local Areas to Review

- `skills/en/paper-writing-en/`
- `skills/en/paper-review-en/`
- `skills/en/research-integrity-audit/`

Suggested action: compare the changed upstream guide/template with the local skill references and port only the parts that improve this suite's thesis or paper workflow.

## academic-research-skills

- Repository: `Imbad0202/academic-research-skills`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `high`
- Reason: Large academic writing pipeline. Track architecture, integrity protocols, review gates, and shared schemas; adapt to Turkish thesis workflow manually.

Relevant file status counts: added: 3, modified: 46.

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
| added | `academic-paper-reviewer/examples/subclaim_decomposition_example.md` |
| modified | `academic-paper-reviewer/references/calibration_mode_protocol.md` |
| modified | `academic-paper-reviewer/references/review_criteria_framework.md` |
| modified | `academic-paper-reviewer/templates/editorial_decision_template.md` |
| modified | `academic-paper/SKILL.md` |
| modified | `academic-paper/agents/abstract_bilingual_agent.md` |
| modified | `academic-paper/agents/citation_compliance_agent.md` |
| modified | `academic-paper/agents/draft_writer_agent.md` |
| modified | `academic-paper/agents/formatter_agent.md` |
| modified | `academic-paper/agents/intake_agent.md` |
| modified | `academic-paper/agents/literature_strategist_agent.md` |
| modified | `academic-paper/agents/peer_reviewer_agent.md` |
| modified | `academic-paper/agents/socratic_mentor_agent.md` |
| modified | `academic-paper/agents/visualization_agent.md` |
| modified | `academic-paper/references/disclosure_mode_protocol.md` |
| modified | `academic-paper/references/mode_selection_guide.md` |
| modified | `academic-paper/references/plan_mode_protocol.md` |
| added | `academic-paper/references/revision_patch_protocol.md` |
| modified | `academic-paper/references/venue_disclosure_policies.md` |
| modified | `academic-paper/references/vlm_figure_verification.md` |
| modified | `academic-pipeline/SKILL.md` |
| modified | `academic-pipeline/agents/claim_ref_alignment_audit_agent.md` |
| modified | `academic-pipeline/agents/collaboration_depth_agent.md` |
| modified | `academic-pipeline/agents/integrity_verification_agent.md` |
| modified | `academic-pipeline/agents/pipeline_orchestrator_agent.md` |
| modified | `academic-pipeline/references/adapters/overview.md` |
| modified | `academic-pipeline/references/claim_audit_calibration_protocol.md` |
| modified | `academic-pipeline/references/process_summary_protocol.md` |
| modified | `academic-pipeline/references/score_trajectory_protocol.md` |
| modified | `deep-research/SKILL.md` |
| modified | `deep-research/agents/bibliography_agent.md` |
| modified | `deep-research/agents/devils_advocate_agent.md` |
| modified | `deep-research/agents/report_compiler_agent.md` |
| modified | `deep-research/agents/research_question_agent.md` |
| modified | `deep-research/agents/socratic_mentor_agent.md` |
| modified | `deep-research/agents/source_verification_agent.md` |
| modified | `deep-research/agents/synthesis_agent.md` |
| added | `deep-research/references/arxiv_api_protocol.md` |
| modified | `deep-research/references/mode_selection_guide.md` |
| modified | `docs/ARCHITECTURE.md` |

<details>
<summary>Ignored changed files outside watch paths</summary>

- `.claude-plugin/marketplace.json` (modified)
- `.claude-plugin/plugin.json` (modified)
- `.claude/CLAUDE.md` (modified)
- `.gitattributes` (added)
- `.github/copilot-instructions.md` (added)
- `.github/pull_request_template.md` (modified)
- `.github/workflows/eval-harness.yml` (modified)
- `.github/workflows/platform-port-reminder.yml` (added)
- `.github/workflows/post-squash-review.yml` (removed)
- `.github/workflows/pytest.yml` (modified)
- `.github/workflows/repository-hygiene.yml` (added)
- `.github/workflows/spec-consistency.yml` (modified)
- `.gitignore` (modified)
- `.gitleaks.toml` (added)
- `CITATION.cff` (added)
- `CONTRIBUTING.md` (modified)
- `MODE_REGISTRY.md` (modified)
- `POSITIONING.md` (modified)
- `QUICKSTART.md` (modified)
- `README.ja-JP.md` (modified)
- `README.ko-KR.md` (added)
- `README.zh-CN.md` (modified)
- `README.zh-TW.md` (modified)
- `agents/report_compiler_agent.md` (removed)
- `agents/report_compiler_agent.md` (added)
- `agents/research_architect_agent.md` (removed)
- `agents/research_architect_agent.md` (added)
- `agents/synthesis_agent.md` (removed)
- `agents/synthesis_agent.md` (added)
- `audits/ars-researcher-blindspot-audit-2026-06-10.md` (added)
- `audits/harness-retirement-2026-06-10.md` (added)
- `audits/harness-retirement-2026-07.md` (added)
- `commands/ars-3w.md` (added)
- `commands/ars-cache-invalidate.md` (added)
- `commands/ars-full.md` (modified)
- `commands/ars-rebuttal-audit.md` (added)
- `commands/ars-reviewer.md` (modified)
- `commands/ars-revision-coach.md` (modified)
- `conftest.py` (removed)
- `docs/PERFORMANCE.md` (modified)
- `docs/PERFORMANCE.zh-TW.md` (modified)
- `docs/ROADMAP-v3.11.md` (added)
- `docs/SETUP.md` (modified)
- `docs/SETUP.zh-TW.md` (modified)
- `docs/cross-paper-workflow.md` (added)
- `docs/design/2026-04-29-ars-v3.6.7-downstream-agent-pattern-protection-spec.md` (modified)
- `docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md` (modified)
- `docs/design/2026-05-17-ars-v3.9.0-cross-index-triangulation-measurement-spec.md` (modified)
- `docs/design/2026-05-21-v3.10-182-promote-citation-gate-spec.md` (modified)
- `docs/design/2026-06-01-ars-134-conductor-rescope-deterministic-write-guard-spec.md` (modified)
- `docs/design/2026-06-02-co-scientist-220-l1-hidden-ranking.md` (added)
- `docs/design/2026-06-02-co-scientist-221-l2-feedback-propagation.md` (added)
- `docs/design/2026-06-02-co-scientist-222-l3-transfer-matrix.md` (added)
- `docs/design/2026-06-02-co-scientist-223-l4-control-plane-ownership.md` (added)
- `docs/design/2026-06-06-213-subclaim-decomposition-design.md` (added)
- `docs/design/2026-06-07-272-instruction-data-boundary-design.md` (added)
- `docs/design/2026-06-08-214-synthesizer-subclaim-design.md` (added)
- `docs/design/2026-06-08-255-kong-meta-negative-scope-and-design-lessons.md` (added)
- `docs/design/2026-06-08-260-experiment-provenance-intake-spec.md` (added)
- `docs/design/2026-06-08-262-cross-paper-contradiction-design.md` (added)
- `docs/design/2026-06-08-273-rubric-aware-calibration-note-design.md` (added)
- `docs/design/2026-06-08-274-concise-pressure-guidance-design.md` (added)
- `docs/design/2026-06-08-kong-255-l1-copilot-not-auto-research.md` (added)
- `docs/design/2026-06-08-kong-255-l2-advisory-not-generation.md` (added)
- `docs/design/2026-06-09-216-surface-form-parity-design.md` (added)
- `docs/design/2026-06-10-390-diff-patch-revision-mode-spec.md` (added)
- `docs/design/2026-06-10-394-family-d-repro-lock-assessment.md` (added)
- `docs/design/2026-06-10-394-submission-package-verifier-spec.md` (added)
- `docs/design/2026-06-13-431-author-agree-removal-impact.md` (added)
- `docs/design/2026-06-13-431-title-match-hardening-spec.md` (added)
- `docs/design/2026-06-15-439-format-profile-design.md` (added)
- `docs/design/2026-06-16-448-infra-protection-plugin-root-scope-spec.md` (added)
- `docs/design/2026-06-16-453-provider-agnostic-cross-model-verifier-spec.md` (added)
- `docs/design/2026-06-17-454-windows-python-hook-portability-design.md` (added)
- `docs/design/2026-06-18-socratic-adjacent-framing-probe-spec.md` (added)
- `docs/design/TODO-l-doc-1-18-patterns-prose-retirement.md` (removed)
- `evals/gold/citation_extraction/README.md` (modified)
- `evals/gold/citation_extraction/expected_outcomes.json` (modified)
- `evals/gold/citation_extraction/manifest.yaml` (modified)
- `evals/gold/citation_extraction/tuples/051-fabricated-title-only-no-identifier.json` (added)
- `evals/gold/field_norm_severity/README.md` (added)
- `evals/gold/field_norm_severity/gold_set.json` (added)
- `evals/gold/field_norm_severity/manifest.yaml` (added)
- `evals/gold/surface_form_parity/README.md` (added)
- `evals/gold/surface_form_parity/gold_set.json` (added)
- `evals/gold/surface_form_parity/manifest.yaml` (added)
- `examples/contradiction_pairs_example.md` (added)
- `examples/figure_table_trace_example.md` (added)
- `examples/passport_with_experiment_provenance.yaml` (added)
- `hooks/hooks.json` (modified)
- `hooks/run_guard.sh` (added)
- `pyproject.toml` (added)
- `requirements-dev.txt` (modified)
- `scripts/_block_parser.py` (added)
- `scripts/_ci_pytest_manifest.toml` (modified)
- `scripts/_claim_audit_constants.py` (modified)
- `scripts/_eval_threshold_gate.py` (modified)
- `scripts/_skill_lint.py` (modified)
- `scripts/_text_similarity.py` (modified)
- `scripts/adapters/folder_scan.py` (modified)
- ... 151 more

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

- `.claude-plugin/marketplace.json` (added)
- `.claude-plugin/plugin.json` (added)
- `AGENTS.md` (modified)

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
