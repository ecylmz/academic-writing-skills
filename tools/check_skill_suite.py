#!/usr/bin/env python3
from pathlib import Path
import sys, re, json

root = Path(__file__).resolve().parents[1]
skills_root = root / "skills"
expected_by_language = {
    "tr": [
        "tez-yazimi-tr",
        "tez-denetim-tr",
        "tez-latex-format-tr",
        "humanizer-tr",
    ],
    "en": [
        "paper-writing-en",
        "paper-review-en",
        "research-integrity-audit",
        "humanizer",
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

def stable_files():
    files = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if ".git" in rel.parts:
            continue
        if path.name == ".DS_Store":
            continue
        files.append(str(rel))
    return sorted(files)

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

required_skill_resources = {
    ("tr", "tez-yazimi-tr"): [
        "references/agent-neutral-skill-principles.md",
        "references/claim-evidence-principles.md",
        "templates/claim-evidence-map.md",
        "templates/reverse-outline.md",
        "templates/revision-report.md",
    ],
    ("tr", "tez-denetim-tr"): [
        "references/agent-neutral-skill-principles.md",
        "references/claim-evidence-principles.md",
        "templates/claim-evidence-map.md",
        "templates/revision-report.md",
    ],
    ("tr", "tez-latex-format-tr"): [
        "references/agent-neutral-skill-principles.md",
    ],
    ("tr", "humanizer-tr"): [
        "LICENSE",
        "references/turkce-dogallastirma-kaliplari.md",
    ],
    ("en", "paper-writing-en"): [
        "references/agent-neutral-skill-principles.md",
        "references/claim-evidence-principles.md",
        "templates/claim-evidence-map.md",
        "templates/reverse-outline.md",
        "templates/revision-report.md",
    ],
    ("en", "paper-review-en"): [
        "references/agent-neutral-skill-principles.md",
        "references/claim-evidence-principles.md",
        "templates/claim-evidence-map.md",
        "templates/revision-report.md",
    ],
    ("en", "research-integrity-audit"): [
        "references/agent-neutral-skill-principles.md",
        "references/claim-evidence-principles.md",
        "templates/claim-evidence-map.md",
        "templates/revision-report.md",
    ],
    ("en", "humanizer"): [
        "LICENSE",
        "references/humanizer-patterns.md",
    ],
}

for (language, skill), resources in required_skill_resources.items():
    for rel in resources:
        if not (skills_root / language / skill / rel).exists():
            errors.append(f"Missing skill resource: skills/{language}/{skill}/{rel}")

if (skills_root / "_shared").exists():
    errors.append("skills/_shared should not exist; shared resources must live inside the skills that use them")

stale_scan_roots = [
    root / "AGENTS.md",
    root / "README.md",
    root / "SOURCE_NOTES.md",
    root / "PROJECT_MANIFEST.json",
    root / ".upstream",
    root / "examples",
    root / "skills",
]
for scan_root in stale_scan_roots:
    paths = [scan_root] if scan_root.is_file() else list(scan_root.rglob("*"))
    for path in paths:
        if not path.is_file() or path.name == ".DS_Store":
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        if "akademik-yazim-suite" in text:
            errors.append(f"Stale removed skill reference in {rel}: akademik-yazim-suite")
        if "skills/_shared/" in text:
            errors.append(f"Stale shared resource path in {rel}: skills/_shared/")

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
            "blader/humanizer",
        ]:
            if repo not in repos:
                errors.append(f"Upstream repo missing from sources.json: {repo}")
        for item in sources.get("sources", []):
            for target in item.get("local_targets", []):
                target_path = root / target
                if target.endswith("/"):
                    if not target_path.is_dir():
                        errors.append(f"Missing upstream local target directory: {target}")
                elif not target_path.exists():
                    errors.append(f"Missing upstream local target file: {target}")
        yaml_path = root / ".upstream" / "sources.yaml"
        if yaml_path.exists():
            yaml_text = yaml_path.read_text(encoding="utf-8")
            for repo in repos:
                if repo not in yaml_text:
                    errors.append(f"Upstream repo missing from sources.yaml: {repo}")
            for item in sources.get("sources", []):
                for target in item.get("local_targets", []):
                    if target not in yaml_text:
                        errors.append(f"Upstream local target missing from sources.yaml: {target}")
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid .upstream/sources.json: {exc}")

manifest_path = root / "PROJECT_MANIFEST.json"
if manifest_path.exists():
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("skill_count") != len(expected):
            errors.append(
                f"PROJECT_MANIFEST skill_count mismatch: {manifest.get('skill_count')} != {len(expected)}"
            )
        if manifest.get("skills") != expected_by_language:
            errors.append("PROJECT_MANIFEST skills list does not match validator expectations")
        computed_file_count = len(stable_files())
        if manifest.get("file_count") != computed_file_count:
            errors.append(
                f"PROJECT_MANIFEST file_count mismatch: {manifest.get('file_count')} != {computed_file_count}"
            )
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid PROJECT_MANIFEST.json: {exc}")

if errors:
    print("FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

files = stable_files()
print(json.dumps({
    "status": "ok",
    "skill_count": len(expected),
    "file_count": len(files),
    "skills": expected_by_language,
    "upstream_tracking": True,
    "agents_md": True
}, ensure_ascii=False, indent=2))
