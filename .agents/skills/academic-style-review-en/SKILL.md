---
name: academic-style-review-en
description: English academic prose style review for AI-typical patterns, vague claims, overclaiming, unsupported assertions, filler, weak paragraph flow, and terminology drift. Works as a second-pass style and clarity audit.
---

# Academic Style Review EN

Use this skill as a post-drafting style and clarity pass. The goal is better academic prose, not detector evasion.

## Audit categories

1. **Reader state**
   - Define technical terms before use.
   - Avoid assuming the reader knows project-specific context.

2. **Concrete language**
   - Replace vague nouns such as `factors`, `aspects`, `issues`, and `various metrics` with specific items.

3. **Claim calibration**
   - Match verbs to evidence: `suggests`, `shows`, `demonstrates`, `proves`.
   - Avoid `state-of-the-art`, `best`, `novel`, or `comprehensive` unless supported.

4. **Filler and cliché**
   - Remove phrases such as `it is important to note`, `in order to`, `due to the fact that`, `paves the way`, `paradigm shift`, and `unlock the potential`.

5. **Punctuation and rhythm**
   - Avoid excessive em dashes.
   - Vary sentence length.
   - Avoid repetitive paragraph endings.

6. **Terminology consistency**
   - Use one term for one concept.
   - Do not cycle synonyms to avoid repetition.

7. **Citation discipline**
   - Mark factual claims without citation or internal evidence.

## Revision invariants

- No new facts.
- No new citations.
- No new metrics or results.
- Preserve Markdown, LaTeX, tables, equations, code fences, and citation keys.
- Revise only where the audit finds a problem.

## Output contract

```text
## Style Audit
| Rule | Location | Issue | Revision strategy |
|---|---|---|---|

## Revised Text
...

## Claim Calibration Notes
| Claim | Original strength | Recommended strength |
|---|---|---|

## Remaining Issues
- ...
```
