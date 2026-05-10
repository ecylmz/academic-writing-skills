---
name: humanizer
description: Naturalness and voice-revision skill for removing generic AI-output patterns while preserving meaning, evidence, citations, and academic integrity. Adapted from blader/humanizer under the MIT License.
---

# Humanizer

Use this skill when the user asks to make English prose sound more natural, less generic, less formulaic, or closer to a supplied writing sample. This skill can work on academic prose, project documentation, correspondence, reviewer responses, and general explanatory text.

This is a style and voice revision skill. It is not a tool for hiding AI use, bypassing AI detectors, fabricating specificity, or making unsupported claims feel credible.

## Use cases

- Remove generic AI-output patterns from English text.
- Calibrate a rewrite to a user-provided writing sample.
- Replace inflated, promotional, or formulaic language with specific and direct prose.
- Clean chatbot artifacts such as greetings, meta-commentary, and signposting from pasted text.
- Make academic English less padded while preserving claim strength and evidence.

## Core workflow

1. Identify the target audience, genre, and expected tone.
2. If a writing sample is supplied, map its voice before revising.
3. Scan the text using `references/humanizer-patterns.md`.
4. Rewrite only the passages that need style repair.
5. Preserve factual claims, citations, numbers, terminology, LaTeX commands, headings, tables, and code snippets unless the user asks to change them.
6. Run a final tell-check: identify remaining formulaic or generic traces, then revise once more.
7. Report any claims that became unverifiable, too specific, or too strong during revision.

## Voice calibration

When the user supplies their own writing sample, use it as the voice reference:

- Sentence length and rhythm.
- Vocabulary level.
- Paragraph openings.
- Transition habits.
- Punctuation habits.
- Level of directness, uncertainty, and first-person use.

Do not imitate private, sensitive, or identifying details from the sample. Match style, not content.

## Output contract

Return:

1. **Pattern Notes**: compact list of the main AI-output patterns found.
2. **Draft Rewrite**: meaning-preserving revision.
3. **Final Tell-Check**: remaining generic or artificial traces after the draft.
4. **Final Rewrite**: revised version after the tell-check.
5. **Integrity Notes**: any claim, citation, number, source, or tone change that needs user verification.

For very short text, combine the draft and final rewrite if the first pass is already clean.

## Hard constraints

- Do not invent citations, source details, studies, dates, names, examples, numbers, or user experiences.
- Do not make an unsupported claim sound more certain.
- Do not add vivid specificity unless it is already in the source text or supplied evidence.
- Do not remove necessary academic caution just to sound more casual.
- Do not use this skill to conceal AI involvement or evade AI-detection systems.
- Do not flatten a formal academic register into casual blog prose unless the user asks for that tone.
- Do not rewrite technical terms, citations, equations, LaTeX commands, or code blocks unless explicitly asked.

## Source and license

This local skill adapts `blader/humanizer` version 2.5.1, retrieved from `https://github.com/blader/humanizer` at commit `8b3a17889fbf12bedae20974a3c9f9de746ed754`. The upstream project is MIT licensed. The required MIT license text is included in `LICENSE`.
