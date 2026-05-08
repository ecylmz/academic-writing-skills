# Reviewer-Ready Writing

This reference collects revision checks that make an English manuscript easier for reviewers to evaluate.

## Paper story check

Before rewriting sentences, identify the paper story:

1. What problem does the paper address?
2. What gap or limitation in prior work makes this problem unresolved?
3. What is the paper's concrete contribution?
4. What evidence supports the contribution?
5. What is the scope of the claim?

If any answer is missing, mark it as `[MATERIAL GAP]` rather than filling the section with generic prose.

## Load-bearing paragraph test

For each paragraph, ask:

- If this paragraph is removed, does the argument break?
- If not, what context or transition would be lost?
- If nothing is lost, remove or merge the paragraph.

Load-bearing paragraphs deserve the most careful revision. Supporting paragraphs should be short and specific.

## Reader journey test

At any point, a reviewer should know:

1. Where am I in the paper?
2. Why does this section matter for the research question?
3. What should I take away?
4. How does this connect to the next section?

If the reader must infer the purpose of a paragraph, revise the topic sentence or transition.

## Adversarial self-review

Before finalizing a section, answer these questions:

| Dimension | Question |
|---|---|
| Contribution | What new knowledge, artifact, dataset, method, or empirical finding does this section support? |
| Clarity | Can a knowledgeable reviewer reproduce or inspect the method from the description? |
| Evidence | Does each major claim point to a result, source, table, figure, or artifact? |
| Evaluation | Are baselines, ablations, metrics, and robustness checks adequate for the claim? |
| Scope | Are limitations, negative results, and boundary conditions visible? |

## Revision order

1. Fix unsupported or overbroad claims.
2. Clarify research-question-to-evidence mapping.
3. Add missing method or experiment detail if the user supplied it.
4. Repair paragraph roles and transitions.
5. Run style cleanup last.
