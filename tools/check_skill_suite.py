#!/usr/bin/env python3
from pathlib import Path
import sys, re, json

root = Path(__file__).resolve().parents[1]
skills_root = root / "skills"
expected_by_language = {
    "tr": [
        "akademik-yazim-suite",
        "tez-yazimi-tr",
        "tez-denetim-tr",
        "tez-latex-format-tr",
    ],
    "en": [
        "paper-writing-en",
        "paper-review-en",
        "research-integrity-audit",
    ],
}
expected = [skill for skills in expected_by_language.values() for skill in skills]
required_project_files = [
    "AGENTS.md",
    "README.md",
    "SOURCE_NOTES.md",
    "PROJECT_MANIFEST.json",
    ".upstream/README.md",
    ".upstream/sources.json",
    ".upstream/sources.yaml",
    ".upstream/snapshots/latest.json",
    ".upstream/reports/upstream-report.md",
    ".upstream/reports/upstream-state.json",
    ".github/workflows/upstream-watch.yml",
    "skills/tr/README.md",
    "skills/en/README.md",
    "tools/check_upstream_updates.py",
]

errors = []

for rel in required_project_files:
    if not (root / rel).exists():
        errors.append(f"Missing project file: {rel}")

for language, skills in expected_by_language.items():
    if not (skills_root / language).is_dir():
        errors.append(f"Missing language directory: skills/{language}")
    for skill in skills:
        path = skills_root / language / skill / "SKILL.md"
        if not path.exists():
            errors.append(f"Missing SKILL.md: skills/{language}/{skill}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"Missing frontmatter: {skill}")
        if f"name: {skill}" not in text:
            errors.append(f"Frontmatter name mismatch: {skill}")

for rel in [
    "references/agent-neutral-skill-principles.md",
    "references/claim-evidence-principles.md",
    "templates/claim-evidence-map.md",
    "templates/reverse-outline.md",
    "templates/revision-report.md",
]:
    if not (skills_root / "_shared" / rel).exists():
        errors.append(f"Missing shared resource: skills/_shared/{rel}")

# Check referenced local files in SKILL.md when written as references/... or templates/...
for language, skills in expected_by_language.items():
    for skill in skills:
        base = skills_root / language / skill
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

files = [
    str(p.relative_to(root))
    for p in root.rglob("*")
    if p.is_file() and ".git" not in p.relative_to(root).parts
]
print(json.dumps({
    "status": "ok",
    "skill_count": len(expected),
    "file_count": len(files),
    "skills": expected_by_language,
    "upstream_tracking": True,
    "agents_md": True
}, ensure_ascii=False, indent=2))
