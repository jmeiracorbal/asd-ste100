# ASD-STE100 working rules

This file is an operational summary for an AI agent. It is not a replacement for the official ASD-STE100 Issue 9 standard.

## Scope

ASD-STE100 is a controlled form of English for technical documentation. Formal compliance applies to English text. If the requested output is in another language, apply these clarity principles but describe the result only as STE-inspired.

Apply these rules without assuming a specific subject field. Use only the domain context present in the source material, user request, or approved terminology.

## Vocabulary

- Prefer approved ASD-STE100 general vocabulary when the official dictionary is available.
- Use an approved word only with its approved meaning and part of speech.
- Keep one preferred term for one concept. Do not introduce synonyms for stylistic variation.
- Preserve necessary technical nouns and technical verbs from the applicable domain, organization, project, or subject field.
- Preserve identifiers, symbols, units, codes, names, and mandatory nomenclature when changing them could alter meaning.
- Prefer technical terms that are short and easy to understand when more than one valid term exists.
- Do not introduce regional expressions, slang, or unnecessary jargon.
- Use American English spelling unless an applicable directive requires a different convention.
- Avoid `-ing` forms when they create grammatical or semantic ambiguity. Keep them only when their use is permitted, such as an approved word or a valid technical noun.

## Procedures

- Write direct instructions.
- Prefer the imperative form: `Install the component.`
- Do not use passive constructions for procedural steps.
- Put a condition before the action when the reader must know the condition before doing the action.
- Keep each procedural sentence to a maximum of 20 words when applying the formal Issue 9 sentence-length rule.
- Separate independent actions when combining them could make the sequence or responsibility unclear.

## Descriptions

- Prefer active voice.
- Use passive voice only when it is necessary, such as when the agent that performs the action is unknown.
- Keep each descriptive sentence to a maximum of 25 words when applying the formal Issue 9 sentence-length rule.
- Keep one main topic in each sentence.

## Sentence completeness

Do not make text shorter by deleting words that are necessary for a complete and unambiguous sentence.

When you simplify a sentence:

- keep the subject when the sentence requires an explicit subject;
- keep the verb;
- keep articles and other grammatical words when they are necessary;
- keep conditions, negation, modality, quantities, units, exceptions, and dependencies;
- split the sentence instead of deleting information when the sentence is too long;
- preserve the same technical meaning after the split.

A shorter sentence is not better if it becomes incomplete, telegraphic, ambiguous, or technically different.

This behavior implements the intent of Issue 9 Rule 4.2.

## Vertical lists

Use a vertical list when a sentence or paragraph contains multiple related items, conditions, actions, requirements, or other elements that are difficult to read in continuous prose.

A vertical list must make the structure clearer. It must not change the relationship between the listed items.

When you convert prose to a vertical list:

- preserve all items from the source;
- preserve their order when the order has meaning;
- preserve conditions and dependencies;
- use parallel grammatical structure where practical;
- keep introductory text sufficient to explain what the list means.

Do not use a vertical list for a simple statement that is clearer as one sentence.

This behavior implements the intent of Issue 9 Rule 4.3.

## Paragraphs

Keep one topic in each paragraph.

Do not write more than six sentences in one paragraph. If a paragraph needs more than six sentences, divide it into two or more paragraphs at a logical topic boundary.

When you divide a paragraph:

- do not remove information only to meet the sentence limit;
- keep related information together;
- do not separate a condition from the information that depends on it;
- keep the sequence of ideas clear.

This behavior implements the intent of Issue 9 Rule 6.6.

## Structure and ambiguity

- Make the actor, action, object, condition, and result explicit when they are relevant.
- Do not use vague references when the referenced item can be named directly.
- Do not use decorative wording, idioms, rhetorical language, or unnecessary qualifiers.
- Split long logical chains into separate sentences.
- Preserve the technical meaning even when a simpler sentence would be shorter.
- If the source is ambiguous, identify the ambiguity instead of silently selecting one interpretation.

## Semantic fidelity

Clarity must not change meaning.

Preserve information that can affect interpretation, including:

- quantities and units;
- conditions and exceptions;
- negation;
- cause and effect;
- sequence and dependency;
- uncertainty and probability;
- obligation, permission, recommendation, and possibility;
- established technical terminology.

## Controlled or mandatory text

Do not silently rewrite controlled warnings, cautions, legal text, mandatory statements, or other wording that the user is not authorized to change. Preserve required wording unless the user explicitly asks for a proposed STE revision and has authority to change it.

## Compliance

Do not claim formal ASD-STE100 compliance from these rules alone. Strict compliance requires verification against the complete Issue 9 writing rules, controlled dictionary, and applicable technical terminology.