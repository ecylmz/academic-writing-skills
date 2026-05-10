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
6. Thesis structure and handoff risks: chapter order, missing required academic sections, and format issues only when they affect review readiness; detailed OMU/LaTeX checks belong to `tez-latex-format-tr`.
7. Source and evidence discipline: citations that support the claim, reference consistency, and result-table alignment.
8. Validity threats: internal, external, construct, and conclusion validity tied to this thesis.

## Risk Priority

- `P0`: submission/defense blocker, such as unsupported central contribution, missing method/data needed for reproducibility, unverifiable core result, fatal claim-evidence mismatch, or thesis structure that prevents evaluation.
- `P1`: major revision risk, such as weak literature gap, incomplete method detail, broad contribution scope, missing validity discussion, or important citation/source-support problem.
- `P2`: moderate clarity or organization risk, such as paragraph flow, terminology drift, weak table/figure explanation, or unclear link between research question and finding.
- `P3`: local style, caption, citation-style, or minor formatting issue that does not affect the thesis's academic defensibility.

## Required Reference Files

Load only when needed:

- `references/agent-neutral-skill-principles.md`
- `references/claim-evidence-principles.md`
- `templates/claim-evidence-map.md`
- `templates/revision-report.md`

## Output Contract

```text
## Overall Assessment
<brief direct assessment>

## Critical Risks
| Priority | Location | Issue | Evidence used / not verified | Why it matters | Recommended fix |
|---|---|---|---|---|---|

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
