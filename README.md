# ASD-STE100 skill

An unofficial Agent Skill for explaining, writing, rewriting, and reviewing complex or technical information with principles from ASD-STE100 Simplified Technical English.

The skill is domain-agnostic. Its primary function is to make explanations easier to understand by reducing ambiguity and cognitive load while preserving meaning.

## Installation

Install the skill with the skills CLI:

```bash
npx skills add jmeiracorbal/asd-ste100
```

To inspect the skills exposed by the repository before installing:

```bash
npx skills add jmeiracorbal/asd-ste100 --list
```

## What the skill does

The skill uses practical STE by default.

Practical STE applies ASD-STE100 principles as an output format for clear explanations without treating the result as partial formal compliance.

The skill instructs an agent to:

- understand the concept before simplifying it;
- preserve the original meaning;
- explain one main idea at a time;
- use one term for one concept;
- prefer short and direct sentence structures;
- make conditions, actions, causes, results, and dependencies explicit;
- preserve quantities, units, negation, modality, exceptions, and uncertainty;
- preserve domain-specific terminology, identifiers, symbols, codes, names, and mandatory nomenclature when required;
- use vertical lists when complex enumerations are easier to understand that way;
- keep one topic in each paragraph and limit paragraphs to six sentences when applying Issue 9 structure rules;
- avoid shortening text by deleting required grammatical or technical information;
- identify ambiguity instead of silently inventing an interpretation;
- add detail progressively when it is necessary for understanding.

Strict mode is reserved for explicit requests for formal ASD-STE100 compliance or compliance review.

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       └── validate-skill.yml
├── SKILL.md
├── README.md
├── LICENSE
├── evals/
│   ├── evals.json
│   └── trigger_set.json
└── references/
    ├── checklist.md
    ├── examples.md
    ├── rules.md
    └── terminology.md
```

`SKILL.md` contains the operational instructions for the agent and the activation description used during progressive disclosure.

`references/rules.md` contains the detailed writing and structural rules used by the skill.

`references/checklist.md` contains a systematic review checklist.

`references/terminology.md` contains domain-agnostic terminology guidance.

`references/examples.md` contains neutral transformation examples.

`evals/evals.json` contains domain-agnostic behavioral evaluations for structure, semantic fidelity, ambiguity handling, explanation quality, and strict-mode boundaries.

`evals/trigger_set.json` contains 20 activation queries: 10 that should trigger the skill and 10 near-miss or adjacent requests that should not trigger it.

## Usage

After installation, ask the agent to use the skill when you want information explained, written, rewritten, or reviewed in an ASD-STE100-oriented style.

Examples:

```text
Explain this concept using ASD-STE100.
```

```text
Rewrite this procedure using ASD-STE100.
```

```text
Review this explanation for ASD-STE100 issues.
```

```text
Check this text for strict ASD-STE100 compliance.
```

For non-English output, the skill applies the same clarity principles but treats the result as STE-inspired rather than formally ASD-STE100-compliant.

## Structural behavior from Issue 9

The reference rules include structural behavior derived from ASD-STE100 Issue 9, including:

- do not shorten sentences by removing words that are necessary for complete and unambiguous meaning;
- use vertical lists when they make multiple related items, conditions, actions, or requirements easier to read;
- keep one topic in each paragraph;
- do not use more than six sentences in one paragraph when applying the Issue 9 paragraph rule;
- divide text at logical boundaries instead of deleting information to meet structural limits.

## Evaluations

The evaluation suite is intentionally domain-agnostic.

Behavioral evaluations check observable output properties such as:

- preserving complete sentences;
- converting complex enumerations into vertical lists without losing items;
- splitting paragraphs longer than six sentences without losing information;
- preserving negation, modality, quantities, and units;
- detecting ambiguous references instead of inventing a meaning;
- producing comprehension-first explanations;
- refusing to certify strict compliance when the required official material is unavailable.

Trigger evaluations test the `SKILL.md` description independently from output quality. They include explicit ASD-STE100 requests, implicit controlled-language requests, non-English STE requests, and adjacent tasks such as ordinary simplification, proofreading, translation, summarization, and marketing rewrites that should not activate the skill.

## Validation

GitHub Actions validates the repository on every push and pull request.

The validation workflow:

1. validates the syntax and expected 10/10 positive-negative balance of the trigger evaluation set;
2. installs the Agent Skills reference validator and runs `skills-ref validate` against the skill directory;
3. runs `npx skills@latest add <skill-directory> --list` and verifies local CLI discovery;
4. runs `npx skills@latest add jmeiracorbal/asd-ste100 --list` and verifies public repository discovery.

This checks Agent Skills specification compatibility and the same public skills CLI path documented for installation.

## Compliance and attribution

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or the ASD Simplified Technical English Maintenance Group (STEMG).

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group. This repository does not replace the official standard, its controlled dictionary, approved project terminology, specialist training, or human review.

The skill must not be used as evidence that generated text is formally compliant with ASD-STE100. Formal compliance requires verification against the applicable official ASD-STE100 issue and the relevant approved terminology.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
