# Agent-Neutral Skill Principles

This suite is not tied to a specific agent platform. Skill files define task scope, inputs, process, and output contracts instead of assuming host-specific commands or slash-command behavior.

## General Rules

1. Identify the user's goal and available material first.
2. Do not invent missing material; mark it as `[MATERIAL GAP]`.
3. Preserve existing meaning during revisions; do not invent data, sources, results, or experiments.
4. Match every important claim with at least one support type: source, experiment result, table/figure, method rationale, or explicit limitation.
5. Preserve the structure of LaTeX, Markdown, BibTeX, and code blocks.
6. When needed, return both the revised text and an audit report.

## File Protection Rules

- Do not modify the user's source file directly unless explicitly asked.
- If proposing a revision, explain the changes and rationale.
- Do not delete LaTeX commands merely to simplify; identify what they do first.
- Do not change citation keys; report them if they appear broken.
