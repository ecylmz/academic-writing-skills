# Upstream Update Report — 2026-06-01

This report is generated automatically. It does not merge upstream changes.

## Summary

| Source | Previous | Current | Relevant files | Suggested action |
|---|---:|---:|---:|---|
| agent-style | `initial` | `ba2e4729` | 0 | ignore |
| research-paper-writing-skills | `initial` | `9ee5eddc` | 0 | ignore |
| academic-research-skills | `initial` | `4c385717` | 0 | ignore |
| humanizer | `initial` | `a2ace14a` | 0 | ignore |

Relevant changed files: **0**

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

Initial tracking run. Snapshot was populated; no comparison was possible.

## research-paper-writing-skills

- Repository: `Master-cai/Research-Paper-Writing-Skills`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `medium`
- Reason: Section-level paper writing guides and templates may improve. Port structure and checklists manually.

Initial tracking run. Snapshot was populated; no comparison was possible.

## academic-research-skills

- Repository: `Imbad0202/academic-research-skills`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `high`
- Reason: Large academic writing pipeline. Track architecture, integrity protocols, review gates, and shared schemas; adapt to Turkish thesis workflow manually.

Initial tracking run. Snapshot was populated; no comparison was possible.

## humanizer

- Repository: `blader/humanizer`
- Branch: `main`
- Policy: `selective-port`
- Risk level: `medium`
- Reason: Naturalness and AI-output pattern guidance may change. Port selectively and preserve this suite's academic integrity boundaries.

Initial tracking run. Snapshot was populated; no comparison was possible.

## Maintenance Checklist

- [ ] Read each relevant changed file.
- [ ] Decide `ignore`, `port`, `vendor`, or `defer` for each source.
- [ ] If porting, update local `SKILL.md`, `references/`, or `templates/` files.
- [ ] Run `python3 tools/check_skill_suite.py`.
- [ ] Update `SOURCE_NOTES.md` if attribution or adaptation scope changes.
