---
name: asd-ste100
description: Use this skill when the user explicitly asks for ASD-STE100, Simplified Technical English (STE), controlled technical English, or wants complex or technical information explained, written, rewritten, or reviewed in a controlled, low-ambiguity style with consistent terminology and short direct sentences. Use it for comprehension-first technical explanations and STE-oriented rewrites or reviews. Do not use it for ordinary explanations, generic simplification, creative or marketing copy, translation, or proofreading unless controlled-language or STE behavior is requested. For non-English output, apply STE-inspired clarity principles without claiming ASD-STE100 compliance.
---

# ASD-STE100

Use this skill primarily as an output format for clear explanations.

Apply ASD-STE100 principles to reduce ambiguity and cognitive load while preserving meaning. The skill is domain-agnostic. Apply the same method to information from any subject field. Do not introduce domain assumptions that are not present in the source material or user request.

The primary function is to explain. The secondary functions are to write, rewrite, and review.

## Default mode: practical STE

Use practical STE unless the user explicitly asks for strict ASD-STE100 compliance.

In practical STE:

1. Understand the concept before you simplify it.
2. Preserve the original meaning.
3. Identify the essential concepts and the relationships between them.
4. Use one term for one concept.
5. Explain one main idea at a time.
6. Use short and direct sentence structures.
7. Make conditions, causes, actions, and results explicit.
8. Remove wording that does not help comprehension.
9. Preserve necessary domain terminology, identifiers, symbols, units, codes, names, and required nomenclature.
10. Add detail progressively when it is necessary for understanding.

Do not treat practical STE as a compliance score. Do not describe it as partial formal compliance.

## Explanation structure

For explanations, present information in a comprehension-first order when the subject allows it:

1. State the concept or subject.
2. Give the essential explanation.
3. Explain the important relationships.
4. Add necessary details.
5. Add exceptions, limitations, or edge cases when they affect understanding.

Do not add sections mechanically when a shorter explanation is sufficient.

## Semantic fidelity

Clarity must not change meaning.

Preserve all information that can affect interpretation, including:

- quantities and units;
- conditions and exceptions;
- negation;
- cause-and-effect relationships;
- sequence and dependency;
- uncertainty and probability;
- obligation, permission, recommendation, and possibility;
- established technical terminology.

If the source is ambiguous, identify the ambiguity. Do not silently invent an interpretation.

## Strict mode

Use strict mode only when the user explicitly asks for strict ASD-STE100 compliance, formal compliance, or a compliance review.

Treat ASD-STE100 Issue 9 as the normative reference for strict mode.

Do not claim that AI-generated text is formally compliant unless it has been checked against:

- the complete official writing rules;
- the controlled dictionary;
- the applicable approved terminology;
- any project-specific requirements that apply to the text.

When these sources are not available, identify what can be checked and what cannot be verified.

## General writing behavior

- Identify whether the text is procedural or descriptive when that distinction affects the writing rules.
- Prefer active constructions for instructions and make the actor or required action clear.
- Remove unnecessary synonyms, idioms, jargon, vague references, and decorative wording.
- Use American English spelling unless the user or an applicable directive requires a different convention.
- Preserve technical accuracy. Do not simplify a sentence if the simplification changes its technical meaning.
- Preserve established terminology when changing it could alter meaning.
- When the output is not English, treat the result as STE-inspired rather than ASD-STE100-compliant.

## Reference files

Read `references/rules.md` when you need detailed writing constraints or must review existing text.

Read `references/checklist.md` when you need a systematic review of a text.

Read `references/terminology.md` when you need to decide whether a term must be preserved, normalized, or treated as domain terminology.

Read `references/examples.md` when you need domain-neutral transformation examples.

## Important limits

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group (STEMG). This skill is unofficial and does not replace the official standard, approved terminology, specialist training, or human review.

Do not reproduce or invent the full ASD-STE100 controlled dictionary. If strict lexical compliance matters and the official Issue 9 material is available, use it as the source of truth.