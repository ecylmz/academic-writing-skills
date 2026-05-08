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
   - Make pronoun references explicit when `this`, `these`, or `such` could refer to multiple concepts.

2. **Concrete language**
   - Replace vague nouns such as `factors`, `aspects`, `issues`, and `various metrics` with specific items.

3. **Claim calibration**
   - Match verbs to evidence: `suggests`, `shows`, `demonstrates`, `proves`.
   - Avoid `state-of-the-art`, `best`, `novel`, or `comprehensive` unless supported.
   - Weaken causal, universal, and generalization claims unless the design supports them.

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

8. **Paragraph function**
   - Each paragraph should have one main message.
   - Split paragraphs with two independent messages.
   - Remove or revise generic paragraph-final summary sentences.

9. **Reviewer-facing precision**
   - Replace promotional claims with contribution, method, or result-specific wording.
   - Preserve field-standard terminology even when repetition looks stylistically plain.

## Revision invariants

- No new facts.
- No new citations.
- No new metrics or results.
- Preserve Markdown, LaTeX, tables, equations, code fences, and citation keys.
- Revise only where the audit finds a problem.
- Do not make a claim more fluent by making it less precise.
- Do not erase uncertainty, limitations, or scope conditions.

## References

Load only when needed:

- `references/ai-writing-patterns.md`
- `references/style-rule-checklist.md`

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

## Hard constraints

- Do not use this skill to hide AI use or evade detection.
- Do not add new facts, citations, results, limitations, or methods.
- Do not silently change the claim strength.
- If a sentence requires source verification, mark it instead of rewriting it as certain.
