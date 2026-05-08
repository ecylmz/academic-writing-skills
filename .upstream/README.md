# Upstream Tracking

This directory tracks changes in upstream projects that informed this skill suite.

## Files

- `sources.json`: machine-readable tracking manifest.
- `sources.yaml`: human-readable manifest copy.
- `snapshots/latest.json`: last seen commit records.
- `reports/`: generated monthly diff reports.

## Policy

This project does not automatically import upstream repositories. Each change is reported first and then handled by a human maintenance decision.

Decision types:

- `ignore`: the change does not affect this project.
- `port`: adapt an idea, checklist, or template into a local skill.
- `vendor`: keep an upstream file separately as a reference.
- `defer`: reconsider the change in a later maintenance cycle.

## Why There Is No Automatic Merge

This suite is adapted for Turkish thesis writing, OMU thesis templates, software engineering papers, and user-specific academic workflows. Direct upstream merges can break local terminology, Turkish academic style rules, and thesis-format assumptions.
