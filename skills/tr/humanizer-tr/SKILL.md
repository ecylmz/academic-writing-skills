---
name: humanizer-tr
description: Use for making Turkish prose sound natural, clear, and authorial without changing meaning, hiding AI use, or weakening academic integrity. Focuses on Turkish-specific artificial phrasing, translationese, bureaucratic padding, generic AI-output patterns, and voice calibration.
---

# Turkish Humanizer

Use this skill when the user asks to make Turkish text sound more natural, less artificial, less translation-like, or closer to a supplied writing sample. This skill can revise thesis prose, Turkish academic paragraphs, project documentation, correspondence, reviewer responses, and explanatory text.

This is not a direct translation of the English `humanizer` skill. Turkish has its own artificiality signals: English-like noun stacks, over-nominalization, generic academic padding, bureaucratic passive voice, mechanical paragraph closings, unsupported contribution language, and unnatural connector chains.

This skill improves naturalness and readability. It must not be used to hide AI involvement, bypass AI detectors, fabricate specificity, or make unsupported claims sound more credible.

## Use cases

- Make Turkish academic prose natural, formal, and readable.
- Remove translationese from English-influenced Turkish sentences.
- Clean generic AI-output patterns in Turkish.
- Calibrate a Turkish rewrite to the user's own writing sample.
- Reduce bureaucratic padding and unnecessary nominalization.
- Preserve thesis/manuscript claims while improving sentence rhythm.

## Core workflow

1. Identify the text type: thesis, article, report, e-mail, response letter, documentation, or general explanation.
2. Identify the expected register: formal academic Turkish, plain professional Turkish, or conversational Turkish.
3. If the user supplies a writing sample, map sentence rhythm, connector use, terminology, paragraph openings, and punctuation habits.
4. Scan the text using `references/turkce-dogallastirma-kaliplari.md`.
5. Rewrite only the passages where naturalness, clarity, or voice actually improves.
6. Preserve factual claims, citations, numbers, terminology, LaTeX commands, headings, tables, figure references, and code snippets unless the user asks otherwise.
7. Run a final artificiality check: identify remaining translationese, filler, unsupported emphasis, and mechanical structure; revise once more.
8. Flag any claim whose strength, source support, or specificity changed during revision.

## Relationship to `tez-yazimi-tr`

Use `tez-yazimi-tr` in `style-review` mode when the task is part of a broader thesis writing workflow: section role, paragraph logic, claim calibration, and jury risk.

Use `humanizer-tr` when the task is narrower: the user already has the content and wants Turkish wording to sound natural, non-generic, and authorial without changing the research meaning.

## Voice calibration

When the user supplies Turkish writing samples, match style rather than content:

- Average sentence length and rhythm.
- Preference for short direct sentences or longer academic sentences.
- Use of connectors such as `bu nedenle`, `ancak`, `dolayısıyla`, `öte yandan`.
- Terminology stability and abbreviation style.
- Punctuation habits, especially commas, semicolons, parentheses, and colon use.
- Degree of first-person avoidance or use.

Do not copy private details, examples, or claims from the sample into the revised text.

## Output contract

Return:

1. **Doğallık Notları**: detected artificial Turkish patterns.
2. **Taslak Revizyon**: meaning-preserving rewrite.
3. **Son Yapaylık Kontrolü**: remaining translationese, filler, or generic patterns.
4. **Nihai Metin**: final revised text.
5. **Bütünlük Notları**: claims, citations, numbers, source support, or tone changes requiring verification.

For very short passages, combine the draft and final rewrite if the first version is already clean.

## Hard constraints

- Do not invent citations, sources, examples, dates, numbers, datasets, findings, institutional rules, or personal experiences.
- Do not make an unsupported claim more certain or more impressive.
- Do not remove necessary academic caution just to sound fluent.
- Do not add vivid detail unless it already exists in the supplied material.
- Do not turn formal academic Turkish into casual blog prose unless the user explicitly asks.
- Do not alter citation keys, LaTeX commands, equations, table references, figure references, variable names, file paths, or code blocks unless explicitly asked.
- Do not use this skill to conceal AI involvement or evade AI-detection systems.

## Source and license

This local Turkish skill adapts the naturalness-revision idea from `blader/humanizer` version 2.5.1, retrieved from `https://github.com/blader/humanizer` at commit `8b3a17889fbf12bedae20974a3c9f9de746ed754`. It is not a direct translation. The upstream project is MIT licensed. The required MIT license text is included in `LICENSE`.
