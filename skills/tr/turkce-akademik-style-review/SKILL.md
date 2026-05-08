---
name: turkce-akademik-style-review
description: Use to clean Turkish academic prose that sounds artificial, overemphatic, vague, or translation-like. Suitable for thesis prose and other Turkish academic text.
---

# Turkish Academic Style Review

This skill performs a second-pass review for Turkish academic prose. The goal is not to conceal AI use; the goal is clearer, more natural, more moderate, and more evidence-aware academic writing.

## Review Categories

- Reader state: define technical terms and clarify references such as "this situation".
- Vague claims: specify phrases such as "many studies", "various factors", and "important results".
- Overemphasis: weaken critical, strong, comprehensive, innovative, best, superior, and generalizable unless evidence supports them.
- Unnecessary meta-discourse: remove empty transitions and future-tense section narration when they do not guide the reader.
- Terminology consistency: use one term for one concept.
- Sentence and paragraph flow: split overloaded sentences and paragraphs with multiple main claims.
- Claim calibration: match verbs such as demonstrates, suggests, proves, and indicates to evidence strength.
- Citation discipline: preserve citation keys and mark factual claims that need sources.
- Format preservation: preserve Markdown, LaTeX, tables, equations, figure references, code blocks, and BibTeX keys.

## Output Contract

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

- Adding new sources or data.
- Making the user's claims stronger than the evidence supports.
- Producing unnatural Turkish translations.
- Turning thesis prose into marketing copy.
- Writing with the purpose of hiding AI use.
