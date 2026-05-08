---
name: research-integrity-audit
description: Academic integrity audit for claim-evidence alignment, citation/reference consistency, source support, bibliography quality, and unverifiable claims in English manuscripts or cross-language academic projects.
---

# Research Integrity Audit

Use this skill when the user asks whether claims are supported, whether a manuscript overclaims, whether citations and references are consistent, or whether sources actually support the claims near them.

This skill merges the former `research-integrity-audit` and `research-integrity-audit` scopes. They were separate files, but they usually operate on the same evidence chain: claim -> support -> citation/reference -> source verification.

## Modes

| Mode | Use When | Output |
|---|---|---|
| `claim-evidence` | The user asks whether claims are supported, overstated, or missing evidence. | Claim table, evidence status, rewrite actions. |
| `citation-integrity` | The user asks for citation, bibliography, BibTeX, DOI, or reference checks. | Citation-reference table, metadata issues, source-support risks. |
| `full-integrity` | The user asks for a complete integrity review before submission or defense. | Combined claim, citation, source-support, and bibliography audit. |

## What to Check

1. **Claim-evidence alignment**
   - Factual, quantitative, comparative, causal, interpretive, contribution, scope, validity, reproducibility, and literature-gap claims.
   - Evidence may be a citation, table, figure, experiment result, method description, dataset description, statistical test, ablation, appendix, artifact, or explicit limitation.
   - Status labels: `supported`, `weak`, `missing`, `overclaimed`, `misaligned`, `requires source check`.

2. **Citation-reference consistency**
   - Every in-text citation has a bibliography entry.
   - Every bibliography entry is cited unless intentionally included.
   - Citation style is consistent.
   - Citation keys are stable and not duplicated.

3. **Source support**
   - The cited source supports the claim near the citation.
   - Numerical claims match exact source values or a stated calculation.
   - Literature-gap claims are supported by representative coverage, not a single weak citation.
   - Review papers are not used as substitutes for primary empirical evidence when a claim depends on a specific result.

4. **Reference quality**
   - Missing year, title, venue, DOI, URL, access date, version, release, or commit when required.
   - Inconsistent capitalization or entry type.
   - Unstable webpages or non-authoritative sources.

## References

Load only when needed:

- `references/claim-taxonomy.md`
- `references/claim-verification-protocol.md`
- `references/citation-checklist.md`
- `templates/claim-evidence-map.md`
- `templates/citation-audit-report.md`

## Output Contract

For `claim-evidence` mode:

| # | Section | Claim | Type | Evidence | Status | Action |
|---|---|---|---|---|---|---|

For `citation-integrity` mode:

| Citation key / author-year | Reference entry | Status | Issue | Fix |
|---|---|---|---|---|

For `full-integrity` mode, include both tables plus:

```text
## Highest-Risk Claims
...

## Source Support Risks
| Claim | Citation | Risk | Required check |
|---|---|---|---|

## Full-Text Verification Needed
| Citation | Claim relying on it | Why full text is needed |
|---|---|---|

## Fix Plan
1. ...
```

## Hard Constraints

- Do not invent evidence, citations, references, DOI values, venue metadata, or source support.
- If full source text is unavailable, mark the support as `unverified`.
- Keep existing citation keys unless the user asks for renaming.
- Do not mark a claim as supported when evidence only supports a weaker or narrower version.
- Do not claim source support from title/abstract alone unless the claim is explicitly supported there.
