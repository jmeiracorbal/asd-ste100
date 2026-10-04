# ASD-STE100 review checklist

Use this checklist when you review technical content. Apply it without assuming a specific subject field.

## Scope and intent

- Identify whether the text is procedural, descriptive, or mixed.
- Preserve the original technical intent.
- Do not add facts, requirements, warnings, or domain assumptions that are not present in the source or approved context.

## Terminology

- Use one preferred term for one concept.
- Remove unnecessary synonym variation.
- Preserve established technical nouns and technical verbs when changing them could alter meaning.
- Preserve identifiers, symbols, units, codes, names, and mandatory nomenclature when required.
- Check whether each technical term is defined by the applicable domain, organization, project, or source material.
- Do not replace a valid technical term only because a more common word exists.

## Vocabulary

- Prefer approved ASD-STE100 vocabulary when the official dictionary is available.
- Use words with the intended approved meaning and part of speech when strict compliance is required.
- Remove idioms, slang, rhetorical wording, and unnecessary jargon.
- Remove decorative or vague qualifiers that do not add technical meaning.

## Sentence structure

- Keep sentences short and direct.
- Keep one main topic in each sentence.
- Make the actor and action clear when relevant.
- Make the object, condition, cause, and result explicit when relevant.
- Put conditions before actions when the reader must know the condition first.
- Split long logical chains into separate sentences.
- Remove ambiguous references when the referenced item can be named directly.
- Do not shorten a sentence by deleting a required subject, verb, noun, article, condition, negation, quantity, unit, exception, or dependency.
- Write contractions in full when applying Issue 9 rules.
- If a sentence is too long, split it while preserving all information that affects meaning.
- Reject telegraphic fragments that are shorter but less complete or less clear.

## Vertical lists

- Identify sentences or paragraphs that contain many related items, actions, conditions, or requirements.
- Use a vertical list when it makes that information materially easier to read.
- Put a colon before the first list item.
- Use consistent list markers.
- Start each list item with an uppercase letter.
- Use an article before the subject noun when applicable.
- Use a period after a full-sentence item.
- Do not use a comma or semicolon at the end of a list item.
- Put a period at the end of the last list item.
- Preserve every relevant item when converting prose to a list.
- Preserve meaningful order, conditions, and dependencies.
- Prefer parallel structure across list items when practical.
- Do not create a vertical list when a simple sentence is clearer.

## Paragraphs

- Keep one topic in each paragraph.
- Count the sentences in each paragraph.
- Do not allow more than six sentences in a paragraph when applying Issue 9 structure rules.
- Divide paragraphs longer than six sentences at a logical boundary.
- Do not remove information only to satisfy the six-sentence limit.
- Keep conditions and dependent information together after a paragraph split.

## Procedures

- Use direct instructions.
- Prefer the imperative form.
- Avoid passive constructions in procedural steps.
- Separate independent actions when sequence or responsibility could be unclear.
- Apply the Issue 9 procedural sentence-length limit when strict compliance is required.

## Descriptions

- Prefer active voice.
- Use passive voice only when it is necessary for technical accuracy or when the actor is unknown or irrelevant.
- Apply the Issue 9 descriptive sentence-length limit when strict compliance is required.

## Deterministic verification

For English text, use `scripts/ste-lint.py` before the manual semantic review.

For procedural text:

```text
python scripts/ste-lint.py lint --type procedure <file>
```

For descriptive text:

```text
python scripts/ste-lint.py lint --type description <file>
```

The final text must have zero deterministic violations before delivery.

For a rewrite, compare the original and final artifacts:

```text
python scripts/ste-lint.py details <original-file> <rewritten-file>
```

The fidelity check must pass. It checks numbers, numeric ranges, percentages, numeric units, acronyms, identifiers, inline-code tokens, negation count, and fenced code-block content.

Do not claim that either command passed unless it was actually executed on the final artifact.

## Semantic fidelity

- Confirm that quantities and units are unchanged.
- Confirm that conditions and exceptions are unchanged.
- Confirm that negation is unchanged.
- Confirm that cause-and-effect relationships are unchanged.
- Confirm that sequence and dependency are unchanged.
- Confirm that uncertainty and probability are unchanged.
- Confirm that obligation, permission, recommendation, and possibility keep the same force.
- If the source is ambiguous, identify the ambiguity instead of resolving it without evidence.
- Treat the deterministic fidelity check as a guard, not as proof of semantic equivalence.

## Controlled text

- Identify warnings, cautions, legal text, mandatory statements, or other controlled wording.
- Do not silently rewrite controlled text that the user is not authorized to change.

## Final verification

- Confirm that the rewritten text has the same technical meaning as the source.
- Confirm that terminology is consistent throughout the text.
- Confirm that no domain assumptions were introduced.
- Confirm that non-English output is not presented as formally ASD-STE100-compliant.
- Confirm that the final English artifact passed the applicable deterministic checks.
- Do not claim strict compliance unless the text was checked against the complete official rules, controlled dictionary, and applicable technical terminology.