#!/usr/bin/env python3
"""Check upstream repositories and produce a monthly Markdown diff report.

This script intentionally does not merge upstream changes. It only reports
relevant changed files so the maintainer can decide whether to ignore, port,
vendor, or defer each change.

Dependencies: Python standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

GITHUB_API = "https://api.github.com"


def _read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def github_get(path: str, token: str | None = None) -> Dict[str, Any]:
    url = f"{GITHUB_API}{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "academic-writing-skill-suite-upstream-watch",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API error {exc.code} for {url}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GitHub API connection error for {url}: {exc}") from exc


def latest_commit(repo: str, branch: str, token: str | None) -> Tuple[str, str]:
    data = github_get(f"/repos/{repo}/commits/{branch}", token)
    sha = data["sha"]
    date = data.get("commit", {}).get("committer", {}).get("date", "")
    return sha, date


def compare(repo: str, base: str, head: str, token: str | None) -> Dict[str, Any]:
    return github_get(f"/repos/{repo}/compare/{base}...{head}", token)


def path_matches(path: str, prefixes: Iterable[str]) -> bool:
    normalized = path.strip("/")
    for prefix in prefixes:
        p = prefix.strip("/")
        if not p:
            continue
        if prefix.endswith("/"):
            if normalized.startswith(p + "/") or normalized == p:
                return True
        elif normalized == p or normalized.startswith(p + "/"):
            return True
    return False


def classify_action(source: Dict[str, Any], relevant_files: List[Dict[str, Any]]) -> str:
    if not relevant_files:
        return "ignore"
    policy = source.get("update_policy", "selective-port")
    risk = source.get("risk_level", "medium")
    if policy == "review-carefully" or risk == "high":
        return "review-required"
    return "selective-port"


def summarize_file_status(files: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in files:
        status = item.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    return counts


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def build_report(run_at: str, results: List[Dict[str, Any]], errors: List[str]) -> str:
    total_relevant = sum(len(r.get("relevant_files", [])) for r in results)
    lines: List[str] = []
    lines.append(f"# Upstream Update Report — {run_at[:10]}")
    lines.append("")
    lines.append("This report is generated automatically. It does not merge upstream changes.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Source | Previous | Current | Relevant files | Suggested action |")
    lines.append("|---|---:|---:|---:|---|")
    for r in results:
        prev = r.get("previous_commit") or "initial"
        cur = r.get("current_commit") or "unknown"
        rel = len(r.get("relevant_files", []))
        action = r.get("suggested_action", "unknown")
        lines.append(f"| {md_escape(r['name'])} | `{prev[:8]}` | `{cur[:8]}` | {rel} | {action} |")
    lines.append("")
    lines.append(f"Relevant changed files: **{total_relevant}**")
    lines.append("")

    if errors:
        lines.append("## Errors")
        lines.append("")
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")

    lines.append("## Recommended Decision Vocabulary")
    lines.append("")
    lines.append("- `ignore`: The upstream change does not affect this suite.")
    lines.append("- `port`: Adapt the idea/checklist/template into the local skill suite.")
    lines.append("- `vendor`: Keep the upstream file as a reference artifact without rewriting local skills yet.")
    lines.append("- `defer`: Revisit in the next maintenance cycle.")
    lines.append("")

    for r in results:
        lines.append(f"## {r['name']}")
        lines.append("")
        lines.append(f"- Repository: `{r['repo']}`")
        lines.append(f"- Branch: `{r['branch']}`")
        lines.append(f"- Policy: `{r.get('update_policy', 'selective-port')}`")
        lines.append(f"- Risk level: `{r.get('risk_level', 'medium')}`")
        lines.append(f"- Reason: {r.get('reason', '')}")
        lines.append("")
        if r.get("previous_commit") == r.get("current_commit"):
            lines.append("No upstream commit change since the last snapshot.")
            lines.append("")
            continue
        if r.get("initial_run"):
            lines.append("Initial tracking run. Snapshot was populated; no comparison was possible.")
            lines.append("")
            continue
        relevant = r.get("relevant_files", [])
        ignored = r.get("ignored_files", [])
        counts = summarize_file_status(relevant)
        if counts:
            count_text = ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
            lines.append(f"Relevant file status counts: {count_text}.")
            lines.append("")
        if relevant:
            lines.append("### Relevant Changed Files")
            lines.append("")
            lines.append("| Status | File |")
            lines.append("|---|---|")
            for f in relevant:
                lines.append(f"| {f.get('status', 'unknown')} | `{f.get('filename', '')}` |")
            lines.append("")
        else:
            lines.append("No changed files matched this source's `watch_paths`.")
            lines.append("")
        if ignored:
            lines.append("<details>")
            lines.append("<summary>Ignored changed files outside watch paths</summary>")
            lines.append("")
            for f in ignored[:100]:
                lines.append(f"- `{f.get('filename', '')}` ({f.get('status', 'unknown')})")
            if len(ignored) > 100:
                lines.append(f"- ... {len(ignored) - 100} more")
            lines.append("")
            lines.append("</details>")
            lines.append("")

        local_targets = r.get("local_targets", [])
        if relevant and local_targets:
            lines.append("### Local Areas to Review")
            lines.append("")
            for target in local_targets:
                lines.append(f"- `{target}`")
            lines.append("")

        if relevant:
            if r.get("name") == "agent-style":
                lines.append("Suggested action: review rule changes and executable detector changes separately. Do not auto-port Python/NPM behavior into Turkish thesis skills without manual adaptation.")
            else:
                lines.append("Suggested action: compare the changed upstream guide/template with the local skill references and port only the parts that improve this suite's thesis or paper workflow.")
            lines.append("")

    lines.append("## Maintenance Checklist")
    lines.append("")
    lines.append("- [ ] Read each relevant changed file.")
    lines.append("- [ ] Decide `ignore`, `port`, `vendor`, or `defer` for each source.")
    lines.append("- [ ] If porting, update local `SKILL.md`, `references/`, or `templates/` files.")
    lines.append("- [ ] Run `python tools/check_skill_suite.py`.")
    lines.append("- [ ] Update `SOURCE_NOTES.md` if attribution or adaptation scope changes.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check upstream repository updates.")
    parser.add_argument("--sources", default=".upstream/sources.json", type=Path)
    parser.add_argument("--snapshot", default=".upstream/snapshots/latest.json", type=Path)
    parser.add_argument("--report", default=".upstream/reports/upstream-report.md", type=Path)
    parser.add_argument("--state", default=".upstream/reports/upstream-state.json", type=Path)
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    parser.add_argument("--no-update-snapshot", action="store_true")
    args = parser.parse_args()

    sources_doc = _read_json(args.sources, {})
    sources = sources_doc.get("sources", [])
    if not sources:
        raise SystemExit(f"No sources found in {args.sources}")

    snapshot = _read_json(args.snapshot, {"schema_version": "1.0", "repos": {}})
    repos_snapshot: Dict[str, Any] = snapshot.setdefault("repos", {})
    run_at = dt.datetime.now(dt.timezone.utc).isoformat()

    results: List[Dict[str, Any]] = []
    errors: List[str] = []

    for source in sources:
        name = source["name"]
        repo = source["repo"]
        branch = source.get("branch", "main")
        previous = repos_snapshot.get(repo, {}).get("last_seen_commit")
        result: Dict[str, Any] = {
            "name": name,
            "repo": repo,
            "branch": branch,
            "previous_commit": previous,
            "update_policy": source.get("update_policy"),
            "risk_level": source.get("risk_level"),
            "reason": source.get("reason"),
            "local_targets": source.get("local_targets", []),
            "relevant_files": [],
            "ignored_files": [],
        }
        try:
            current, current_date = latest_commit(repo, branch, args.token)
            result["current_commit"] = current
            result["current_commit_date"] = current_date
            if not previous:
                result["initial_run"] = True
            elif previous == current:
                result["initial_run"] = False
            else:
                diff = compare(repo, previous, current, args.token)
                files = diff.get("files", [])
                watch_paths = source.get("watch_paths", [])
                result["relevant_files"] = [f for f in files if path_matches(f.get("filename", ""), watch_paths)]
                result["ignored_files"] = [f for f in files if not path_matches(f.get("filename", ""), watch_paths)]
            result["suggested_action"] = classify_action(source, result.get("relevant_files", []))
            if not args.no_update_snapshot:
                repos_snapshot[repo] = {
                    "name": name,
                    "branch": branch,
                    "last_seen_commit": current,
                    "last_seen_commit_date": current_date,
                    "last_checked_at": run_at,
                }
        except Exception as exc:  # report all repos; do not fail the whole maintenance run immediately
            msg = f"{name} ({repo}): {exc}"
            errors.append(msg)
            result["error"] = str(exc)
            result["suggested_action"] = "manual-check-required"
        results.append(result)

    report = build_report(run_at, results, errors)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")

    relevant_count = sum(len(r.get("relevant_files", [])) for r in results)
    state = {
        "run_at": run_at,
        "relevant_count": relevant_count,
        "has_relevant_changes": relevant_count > 0,
        "error_count": len(errors),
        "has_errors": bool(errors),
        "report": str(args.report),
    }
    _write_json(args.state, state)

    if not args.no_update_snapshot:
        snapshot["last_checked_at"] = run_at
        _write_json(args.snapshot, snapshot)

    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
