---
name: asd-ste100
description: Writes, rewrites, and reviews technical content using ASD-STE100 Simplified Technical English principles. Use when a user asks for ASD-STE100, STE, Simplified Technical English, controlled technical English, or wants technical instructions made less ambiguous. For non-English output, apply the same clarity principles but do not claim ASD-STE100 compliance.
---

# ASD-STE100

Use this skill to make technical content clearer, more consistent, and less ambiguous with principles from ASD-STE100 Simplified Technical English.

Treat ASD-STE100 Issue 9 as the normative reference when strict compliance is required. Do not claim that AI-generated text is formally compliant unless it has been checked against the official writing rules, the controlled dictionary, and the applicable project terminology.

## Workflow

1. Identify whether the text is procedural or descriptive.
2. Identify the technical nouns and technical verbs that must keep their domain meaning.
3. Use one term for one concept. Do not vary terminology only for style.
4. Prefer short, direct sentence structures and explicit cause, condition, action, and result relationships.
5. Prefer active constructions for instructions and make the actor or required action clear.
6. Remove unnecessary synonyms, idioms, jargon, vague references, and decorative wording.
7. Use American English spelling unless the user or an applicable directive requires a different convention.
8. Preserve technical accuracy. Do not simplify a sentence if the simplification changes its technical meaning.
9. When the output is not English, state internally that the result is STE-inspired rather than ASD-STE100-compliant. Apply the clarity and terminology rules, but do not present the non-English text as formal STE.

## Reference files

Read `references/rules.md` when you need the detailed writing constraints or must review existing text.

Read `references/examples.md` when you need examples of transformations for procedures, descriptions, warnings, or software documentation.

## Important limits

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group (STEMG). This skill is unofficial and does not replace the official standard, approved terminology, specialist training, or human review.

Do not reproduce or invent the full ASD-STE100 controlled dictionary. If strict lexical compliance matters and the official Issue 9 material is available, use it as the source of truth.