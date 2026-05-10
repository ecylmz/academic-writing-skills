# Humanizer Pattern Reference

This reference adapts the pattern checklist from `blader/humanizer` for this academic writing suite. Use it to identify formulaic AI-output traces, then rewrite only where the change improves naturalness, clarity, and evidence discipline.

## Content patterns

| Pattern | Watch for | Preferred repair |
|---|---|---|
| Significance inflation | `pivotal`, `crucial`, `testament`, `landscape`, `underscores`, `marks a shift`, `broader trend` | State the concrete fact or contribution. Remove ceremonial importance unless evidence supports it. |
| Notability name-dropping | Lists of media outlets, authorities, or institutions without explaining relevance | Cite the exact source support or remove the notability padding. |
| Superficial `-ing` analysis | `highlighting`, `showcasing`, `reflecting`, `contributing to`, `fostering` attached as vague depth | Replace with the actual relation, evidence, or mechanism. |
| Promotional language | `boasts`, `vibrant`, `groundbreaking`, `renowned`, `breathtaking`, `must-visit`, `seamless` | Use neutral, specific description. |
| Vague attribution | `experts believe`, `observers note`, `industry reports suggest`, `some critics argue` | Name the source if verified. Otherwise mark `[SOURCE NEEDED]` or remove. |
| Formulaic challenge sections | `Despite these challenges`, `future outlook`, generic resilience endings | Name the actual limitation, constraint, or next step. |

## Language and grammar patterns

| Pattern | Watch for | Preferred repair |
|---|---|---|
| Overused AI vocabulary | `additionally`, `delve`, `intricate`, `interplay`, `tapestry`, `foster`, `showcase`, `underscore` | Use ordinary words when they are more precise. |
| Copula avoidance | `serves as`, `stands as`, `features`, `boasts`, `functions as` | Prefer `is`, `are`, `has`, or the direct verb when accurate. |
| Negative parallelism | `not just X, but Y`, `not merely`, tail fragments like `no guessing` | State the point directly. |
| Rule of three | Forced triples such as `innovation, inspiration, and insight` | Keep only the items the sentence actually needs. |
| Synonym cycling | Replacing the same clear term with several near-synonyms | Repeat the stable term when it prevents ambiguity. |
| False ranges | `from X to Y` when X and Y are not a meaningful scale | List the actual items or categories. |
| Unclear passive or subjectless fragments | `No configuration needed`, `The result is preserved automatically` | Name the actor when active voice improves clarity. |

## Style and formatting patterns

| Pattern | Watch for | Preferred repair |
|---|---|---|
| Em dash overuse | Multiple dash interruptions in prose | Use commas, periods, parentheses, or restructure. Keep an em dash only when it genuinely fits the voice. |
| Boldface overuse | Repeated bold keywords or bold inline labels | Remove emphasis or convert to normal headings/lists. |
| Inline-header lists | `**Performance:** Performance improved...` | Convert to prose or concise bullets without repeated labels. |
| Title Case headings | Every major word capitalized in plain headings | Use sentence case unless the target style requires title case. |
| Decorative emojis | Emojis in headings, bullets, or academic text | Remove for academic and professional contexts. |
| Quote-style drift | Mixed straight and curly quotation marks | Follow the document's existing style or the target venue style. |
| Hyphenated pair overuse | Mechanical hyphenation of common modifiers | Preserve correct grammar and venue style; remove only unnecessary or inconsistent hyphens. |
| Persuasive authority tropes | `the real question is`, `at its core`, `fundamentally`, `what really matters` | Make the claim directly. |
| Signposting announcements | `let's dive in`, `here's what you need to know`, `without further ado` | Start with the content. |
| Fragmented headers | Heading followed by a one-line warm-up that repeats the heading | Delete the warm-up or merge it into substantive content. |

## Communication artifacts

Remove chatbot residue unless the user explicitly wants conversational framing:

- `Great question`
- `Of course`
- `Certainly`
- `I hope this helps`
- `Let me know if`
- `Would you like me to`
- `Here is a`
- Knowledge-cutoff disclaimers such as `up to my last update` or `based on limited available information`
- Sycophantic responses such as `You're absolutely right` when direct acknowledgement is enough

## Filler and hedging

| Pattern | Repair |
|---|---|
| `in order to` | `to` |
| `due to the fact that` | `because` |
| `at this point in time` | `now` or the exact date/time |
| `in the event that` | `if` |
| `has the ability to` | `can` |
| `it is important to note that` | Usually delete and state the point. |
| `could potentially possibly` | Choose the warranted level: `may`, `could`, or remove. |
| Generic upbeat endings | Replace with the actual conclusion, limitation, or next step. |

## Academic adaptation

For academic text, naturalness must not weaken integrity:

- Keep methodological caution when evidence is limited.
- Keep discipline-specific terms even if repeated.
- Keep necessary citation markers and bibliography references.
- Mark unverifiable details as `[MATERIAL GAP]`, `[SOURCE NEEDED]`, or `[VERIFY]`.
- Prefer calibrated precision over lively prose.
- When the task is a manuscript or thesis, pair this skill with `research-integrity-audit` if claims or citations change.

## Final tell-check

Before returning the final rewrite, ask internally:

1. Does the text still rely on inflated significance instead of evidence?
2. Are there vague authorities, invented specifics, or unsupported examples?
3. Are the sentences too evenly paced or too mechanically structured?
4. Are headings, bullets, bolding, or transitions giving away pasted chatbot output?
5. Did the revision change the strength, scope, or source support of any claim?

If any answer is yes, revise once more or flag the remaining issue.
