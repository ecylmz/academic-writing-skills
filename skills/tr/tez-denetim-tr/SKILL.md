---
name: tez-denetim-tr
description: Use to evaluate Turkish thesis text from advisor, committee, and pre-defense perspectives. It identifies risks in structure, method, contribution, claim-evidence alignment, literature positioning, experiment design, and defensibility.
---

# Turkish Thesis Review

This skill reviews rather than drafts. Its purpose is to make weak points visible before submission or defense.

## Review Dimensions

1. Research problem: clarity, thesis-scale scope, and direct connection to method.
2. Contribution: explicit type, bounded scope, and support from findings.
3. Literature positioning: thematic organization, demonstrated gap, and direct link to the thesis claim.
4. Method and reproducibility: data, sample, tools, parameters, protocol, analysis steps, ethics/data access, and version traceability.
5. Findings and interpretation: separation of results from interpretation, alternatives, limitations, and unexpected findings.
6. Format and guide alignment: chapter order, headings, abstracts, lists, captions, appendices, and OMU expectations.
7. Source and evidence discipline: citations that support the claim, reference consistency, and result-table alignment.
8. Validity threats: internal, external, construct, and conclusion validity tied to this thesis.

## Risk Priority

- `P0`: critical issue that must be fixed before submission/defense.
- `P1`: important issue requiring substantial revision.
- `P2`: clarity, flow, or presentation issue.
- `P3`: local style, format, caption, or citation-style issue.

## Output Contract

```text
## Overall Assessment
<brief direct assessment>

## Critical Risks
| Priority | Location | Issue | Why it matters | Recommended fix |
|---|---|---|---|---|

## Claim-Evidence Check
| Claim | Current support | Status | Action |
|---|---|---|---|

## Committee Questions
1. ...
2. ...

## Revision Plan
1. First fixes
2. Second pass
3. Final check
```

## Prohibited

- Superficial praise without evidence.
- Assuming missing method details are complete.
- Inventing sources, data, or results.
- Claiming verification for inaccessible sources, tables, or data.
- Hiding material gaps instead of marking `requires verification`.
