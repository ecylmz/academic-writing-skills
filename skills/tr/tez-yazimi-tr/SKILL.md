---
name: tez-yazimi-tr
description: Use for drafting, revising, or style-reviewing Turkish master's and doctoral thesis sections in clear, evidence-based, formal academic Turkish. Suitable for introductions, literature reviews, methods, findings, discussion, conclusions, abstracts, transitions, and Turkish academic style cleanup.
---

# Turkish Thesis Writing

This skill supports Turkish thesis writing. The aim is not only smoother prose, but stronger thesis logic, section function, claim-evidence alignment, and formal academic Turkish.

## Priorities

1. Preserve the thesis's main claim and research problem.
2. Connect research question, method, findings, and conclusion.
3. Write according to section function; not every section has the same rhetorical structure.
4. Give each paragraph one main message.
5. Support important claims with sources, method details, experimental results, tables, figures, or clear reasoning.
6. Keep Turkish academic language clear, moderate, and direct.

## Modes

| Mode | Use when | Output |
|---|---|---|
| `draft` | The user asks to write a thesis section from supplied notes, data, source passages, or method/result material. | Mini outline, paragraph plan, draft text with `[MATERIAL GAP]` placeholders where evidence is missing. |
| `revise` | The user provides existing thesis prose to restructure or improve. | Reverse outline, revised text, review notes. |
| `style-review` | The user asks to make Turkish academic prose natural, moderate, and less artificial. | Style issues, revised text, claim calibration notes. |

## Reference Loading

Load the narrowest set of files for the task:

| Need | Files |
|---|---|
| Always | `references/agent-neutral-skill-principles.md`, `references/tez-bolum-akisi.md`, `references/akademik-kalite-kontrol.md` |
| Draft/revise | `templates/reverse-outline.md`, `templates/revision-report.md` |
| Claim-evidence check inside a writing task | `references/claim-evidence-principles.md`, `references/iddia-kanit-tez.md`, `templates/claim-evidence-map.md` |
| Style review | `references/turkce-akademik-uslup.md`, `references/style-review/turkce-yapay-kaliplar.md`, `templates/turkce-style-audit-report.md` |
| Section-specific guidance | Load only the relevant file: `references/bolum-rehberi-giris.md`, `references/bolum-rehberi-literatur.md`, `references/bolum-rehberi-yontem.md`, `references/bolum-rehberi-bulgular-tartisma.md`, `references/bolum-rehberi-sonuc.md`, or `references/ozet-ve-abstract.md` |
| CS/SE thesis | `references/yazilim-muhendisligi-tezi.md` |

## Workflow

1. Identify whether the user wants drafting, revision, expansion, or simplification.
2. Identify the section type.
3. Identify missing material: research questions, data, source passages, result tables, method details, citation style, or institutional rules.
4. Start with a mini outline: section purpose, main claim, paragraph roles, necessary evidence, and missing material.
5. If existing text is provided, create a reverse outline.
6. Revise without changing technical meaning or inventing missing data.
7. End with brief review notes.

## Output Contract

1. **Mini Outline**: section purpose, main message, paragraph roles.
2. **Revised Text**: formal academic Turkish, appropriate section flow, preserved citations and technical terms.
3. **Claim-Evidence Map**: include when the text contains factual, empirical, quantitative, comparative, causal, or contribution claims; include claim, support location, status, and action.
4. **Review Notes**: strengthened points, missing evidence, overstated claims, and the next recommended audit.
5. **Remaining Risks**: short list of reviewer/jury risks, especially unsupported claims, unclear method, weak scope, or missing source passages.

For `style-review` mode, return:

```text
## Detected Style Issues
| Location | Issue | Recommendation |
|---|---|---|

## Revised Text
...

## Preserved Technical Meaning
- ...

## Claim Calibration
| Claim | Original strength | Recommended strength | Rationale |
|---|---|---|---|

## Remaining Risks
- ...
```

## Prohibited

- Inventing sources, results, numbers, tables, or metrics.
- Treating advisor or committee approval as known.
- Deleting LaTeX commands without understanding them.
- Changing technical meaning for stylistic polish.
- Hiding missing evidence behind stronger prose.
- Writing generalizations or causal conclusions that the findings do not support.
