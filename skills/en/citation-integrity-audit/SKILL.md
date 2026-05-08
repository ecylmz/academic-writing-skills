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
   - Literature-gap claims require representative coverage, not a single weak citation.
   - Review papers should not be used as substitutes for primary empirical evidence when the claim is about a specific result.

4. **Reference quality**
   - Missing year, title, venue, DOI, URL, or access date if required.
   - Inconsistent capitalization.
   - Broken BibTeX keys or duplicated keys.
   - Preprint, arXiv, conference, journal, dataset, and software entries should be typed consistently.

5. **Electronic sources**
   - Prefer reliable sources.
   - Mark unstable webpages, commercial pages, missing access date, or non-authoritative sources.
   - For software, datasets, and web artifacts, check whether version, commit, release, or access date is needed.

## Workflow

1. Identify citation style.
2. Extract in-text citations and reference entries.
3. Build citation-reference table.
4. Identify orphan and missing entries.
5. Check high-risk claims near citations.
6. Produce correction plan.
7. Separate fixes that can be made from metadata from fixes that require reading the full source.

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

## Full-Text Verification Needed
| Citation | Claim relying on it | Why full text is needed |
|---|---|---|

## Bibliography Fixes
| Entry | Problem | Suggested correction |
|---|---|---|
```

## Hard constraints

- Do not create fake bibliography entries.
- Do not invent DOI values.
- If full source is unavailable, mark it as `unverified`.
- Keep existing citation keys unless the user asks for renaming.
- Do not infer DOI, venue, year, or author metadata from memory.
- Do not change citation style unless the user asks for style conversion.
- Do not claim source support from title/abstract alone unless the claim is explicitly supported there.
