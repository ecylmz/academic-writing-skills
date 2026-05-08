# Validation Report

Validation command:

```bash
/usr/bin/python3 tools/check_skill_suite.py
```

Validation result:

```json
{
  "status": "ok",
  "skill_count": 10,
  "file_count": 75,
  "skills": {
    "tr": [
      "akademik-yazim-suite",
      "tez-yazimi-tr",
      "tez-denetim-tr",
      "tez-latex-format-tr",
      "turkce-akademik-style-review"
    ],
    "en": [
      "makale-yazimi-en",
      "makale-denetim-en",
      "academic-style-review-en",
      "claim-evidence-audit",
      "citation-integrity-audit"
    ]
  },
  "upstream_tracking": true,
  "agents_md": true
}
```

Checked items:

- All 10 expected skill directories exist under `skills/tr` and `skills/en`.
- Every skill has a `SKILL.md` file.
- `SKILL.md` frontmatter names match directory names.
- Local `references/` and `templates/` links mentioned in `SKILL.md` files resolve.
- Shared resources under `skills/_shared` exist.
- `skills/tr/README.md` exists.
- `skills/en/README.md` exists.
- `AGENTS.md` exists.
- Upstream tracking files exist.
- GitHub Actions workflow for monthly upstream checks exists.
- Upstream manifest includes the three tracked repositories.

Notes:

- `tools/check_upstream_updates.py` requires network access when actually checking GitHub. This validation checks its presence and the local manifest structure, not live GitHub connectivity.
