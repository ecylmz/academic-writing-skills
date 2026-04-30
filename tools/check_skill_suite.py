#!/usr/bin/env python3
from pathlib import Path
import sys, re, json

root = Path(__file__).resolve().parents[1]
skills_root = root / ".agents" / "skills"
expected = [
    "akademik-yazim-suite",
    "tez-yazimi-tr",
    "tez-denetim-tr",
    "tez-latex-format-tr",
    "makale-yazimi-en",
    "makale-denetim-en",
    "academic-style-review-en",
    "turkce-akademik-style-review",
    "claim-evidence-audit",
    "citation-integrity-audit",
]
required_project_files = [
    "AGENTS.md",
    "README.md",
    "INSTALL.md",
    "SOURCE_NOTES.md",
    "PROJECT_MANIFEST.json",
    ".upstream/README.md",
    ".upstream/sources.json",
    ".upstream/sources.yaml",
    ".upstream/snapshots/latest.json",
    ".upstream/reports/upstream-report.md",
    ".upstream/reports/upstream-state.json",
    ".github/workflows/upstream-watch.yml",
    "tools/check_upstream_updates.py",
]

errors = []

for rel in required_project_files:
    if not (root / rel).exists():
        errors.append(f"Missing project file: {rel}")

for skill in expected:
    path = skills_root / skill / "SKILL.md"
    if not path.exists():
        errors.append(f"Missing SKILL.md: {skill}")
        continue
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"Missing frontmatter: {skill}")
    if f"name: {skill}" not in text:
        errors.append(f"Frontmatter name mismatch: {skill}")

# Check referenced local files in SKILL.md when written as references/... or templates/...
for skill in expected:
    base = skills_root / skill
    skill_file = base / "SKILL.md"
    if not skill_file.exists():
        continue
    text = skill_file.read_text(encoding="utf-8")
    for rel in re.findall(r"`((?:references|templates)/[^`]+)`", text):
        if not (base / rel).exists():
            errors.append(f"Broken reference in {skill}: {rel}")

# Check upstream manifest shape without requiring network access.
sources_path = root / ".upstream" / "sources.json"
if sources_path.exists():
    try:
        sources = json.loads(sources_path.read_text(encoding="utf-8"))
        repos = [item.get("repo") for item in sources.get("sources", [])]
        for repo in [
            "yzhao062/agent-style",
            "Master-cai/Research-Paper-Writing-Skills",
            "Imbad0202/academic-research-skills",
        ]:
            if repo not in repos:
                errors.append(f"Upstream repo missing from sources.json: {repo}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid .upstream/sources.json: {exc}")

if errors:
    print("FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

files = [str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()]
print(json.dumps({
    "status": "ok",
    "skill_count": len(expected),
    "file_count": len(files),
    "skills": expected,
    "upstream_tracking": True,
    "agents_md": True
}, ensure_ascii=False, indent=2))
