---
name: claim-evidence-audit
description: Academic claim-evidence alignment audit. Extracts factual, quantitative, comparative, causal, interpretive, and contribution claims; maps them to evidence; flags unsupported, weak, overclaimed, or misaligned claims.
---

# Claim-Evidence Audit

Use this skill when the user asks whether a section's claims are supported, whether an abstract/introduction overclaims, or whether a thesis/manuscript is ready for review.

## Scope

Audit these claim types:

- Factual claims.
- Quantitative claims.
- Comparative claims.
- Causal claims.
- Interpretive claims.
- Contribution or novelty claims.
- Scope/generalization claims.
- Methodological validity claims.
- Reproducibility or artifact-availability claims.
- Citation-backed literature-gap claims.

## Workflow

1. Extract claims from the text.
2. Classify each claim.
3. Identify its support:
   - citation,
   - table,
   - figure,
   - experiment result,
   - method description,
   - dataset description,
   - statistical test or uncertainty estimate,
   - ablation or sensitivity analysis,
   - released artifact or appendix,
   - explicit limitation.
4. Compare claim strength with evidence strength.
5. Assign status:
   - `supported`
   - `weak`
   - `missing`
   - `overclaimed`
   - `misaligned`
   - `requires source check`
6. Recommend action:
   - keep,
   - weaken,
   - add evidence,
   - move to limitation,
   - remove.
7. Identify claims that require `citation-integrity-audit` because source support cannot be verified from the provided material.

## References

Load only when needed:

- `references/claim-taxonomy.md`
- `references/claim-verification-protocol.md`

## Output contract

Use this table:

| # | Section | Claim | Type | Evidence | Status | Action |
|---|---|---|---|---|---|---|

Then provide:

```text
## Highest-Risk Claims
...

## Evidence Gaps
| Missing material | Affected claim | Needed from user |
|---|---|---|

## Suggested Rewrites
Original:
Revised:
Reason:
```

## Hard constraints

- Do not invent evidence.
- Do not resolve a missing citation by fabricating a citation.
- If a table/figure is referenced but not provided, mark as `requires source check`.
- If the claim is true only under a narrow condition, revise it to include that condition.
- Do not treat a citation key as evidence unless the cited content is available or supplied.
- Do not mark a claim as supported when the evidence only supports a weaker or narrower version.
