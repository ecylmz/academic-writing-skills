---
name: citation-integrity-audit
description: Citation and reference integrity audit for thesis and manuscript projects. Checks in-text citations, bibliography consistency, source support, missing references, orphan references, DOI/URL presence, and citation style consistency.
---

# Citation Integrity Audit

Use this skill when the user asks to check citations, references, bibliography consistency, or whether sources support claims.

## What to check

1. **Citation-reference matching**
   - Every in-text citation has a bibliography entry.
   - Every bibliography entry is cited unless intentionally included.

2. **Citation style consistency**
   - APA / IEEE / Vancouver / ISNAD / footnote style should not be mixed.
   - Turkish texts using APA-style author-year citations should use language-appropriate conjunctions where needed.

3. **Source support**
   - The cited source should support the claim near the citation.
   - Numerical claims require exact source match or clearly stated calculation.

4. **Reference quality**
   - Missing year, title, venue, DOI, URL, or access date if required.
   - Inconsistent capitalization.
   - Broken BibTeX keys or duplicated keys.

5. **Electronic sources**
   - Prefer reliable sources.
   - Mark unstable webpages, commercial pages, missing access date, or non-authoritative sources.

## Workflow

1. Identify citation style.
2. Extract in-text citations and reference entries.
3. Build citation-reference table.
4. Identify orphan and missing entries.
5. Check high-risk claims near citations.
6. Produce correction plan.

## Output contract

```text
## Citation Style Detected
...

## Citation-Reference Consistency
| Citation key / author-year | Reference entry | Status | Issue |
|---|---|---|---|

## Source Support Risks
| Claim | Citation | Risk | Required check |
|---|---|---|---|

## Bibliography Fixes
| Entry | Problem | Suggested correction |
|---|---|---|
```

## Hard constraints

- Do not create fake bibliography entries.
- Do not invent DOI values.
- If full source is unavailable, mark it as `unverified`.
- Keep existing citation keys unless the user asks for renaming.
