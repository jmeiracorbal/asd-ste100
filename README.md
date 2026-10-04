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
- add detail progressively when it is necessary for understanding;
- verify English output with a deterministic linter;
- compare rewrites against the source with a deterministic technical-detail fidelity check.

Strict mode is reserved for explicit requests for formal ASD-STE100 compliance or compliance review.

## Deterministic verification

`scripts/ste-lint.py` is a dependency-free Python verifier for rules that can be checked mechanically.

Lint procedural text:

```bash
python scripts/ste-lint.py lint --type procedure procedure.md
```

Lint descriptive text:

```bash
python scripts/ste-lint.py lint --type description description.md
```

The linter checks:

- 20-word procedure sentence limit;
- 25-word description sentence limit;
- maximum six sentences per paragraph;
- contractions;
- semicolons;
- vertical-list introduction, capitalization, punctuation, and final period.

Exit code `0` means no deterministic violation was found. Exit code `1` means one or more violations were found.

For a rewrite, compare the final result with the original:

```bash
python scripts/ste-lint.py details original.md rewritten.md
```

The fidelity checker compares mechanically extractable details in both artifacts:

- numbers;
- numeric ranges;
- percentages;
- units associated with numeric values;
- acronyms;
- identifiers and inline-code tokens;
- negation count;
- fenced code-block content.

The check fails if one of these details disappears or a new one is introduced.

Machine-readable output is available for both commands:

```bash
python scripts/ste-lint.py --json lint --type description description.md
python scripts/ste-lint.py --json details original.md rewritten.md
```

The checker is intentionally narrower than semantic equivalence. Conditions, causality, sequence, uncertainty, modality, terminology, and other meaning still require the semantic-fidelity review defined by the skill.

A successful deterministic check does not certify formal ASD-STE100 compliance.

## Verification workflow

For an English rewrite, the skill uses this sequence:

1. preserve the original artifact;
2. classify the target as procedural or descriptive;
3. write the draft;
4. run the applicable deterministic lint;
5. correct all reported violations;
6. run the fidelity comparison against the original;
7. correct all missing or added technical details;
8. run both checks again on the final artifact;
9. apply the semantic-fidelity checklist;
10. deliver the final text only after the deterministic checks pass.

For new English text with no source artifact, only the lint step applies. For reviews, deterministic lint is the first pass before the non-mechanical checklist.

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
├── references/
│   ├── checklist.md
│   ├── examples.md
│   ├── rules.md
│   └── terminology.md
├── scripts/
│   └── ste-lint.py
└── tests/
    └── test_ste_lint.py
```

`SKILL.md` contains the operational instructions for the agent and the activation description used during progressive disclosure.

`references/rules.md` contains the detailed writing and structural rules used by the skill.

`references/checklist.md` contains the systematic review and semantic-fidelity checklist.

`references/terminology.md` contains domain-agnostic terminology guidance.

`references/examples.md` contains neutral transformation examples.

`scripts/ste-lint.py` contains the deterministic structural linter and technical-detail fidelity checker.

`tests/test_ste_lint.py` contains regression tests for both verifier modes.

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

The Python regression suite separately verifies the deterministic linter and fidelity checker, including their exit codes and JSON output.

Trigger evaluations test the `SKILL.md` description independently from output quality. They include explicit ASD-STE100 requests, implicit controlled-language requests, non-English STE requests, and adjacent tasks such as ordinary simplification, proofreading, translation, summarization, and marketing rewrites that should not activate the skill.

## Validation

GitHub Actions validates the repository on every push and pull request.

The validation workflow:

1. validates the syntax and expected 10/10 positive-negative balance of the trigger evaluation set;
2. runs the full Python regression suite for `scripts/ste-lint.py`;
3. validates all linter CLI entry points;
4. installs the Agent Skills reference validator and runs `skills-ref validate` against the skill directory;
5. runs `npx skills@latest add <skill-directory> --list` and verifies local CLI discovery;
6. runs `npx skills@latest add jmeiracorbal/asd-ste100 --list` and verifies public repository discovery.

This checks Agent Skills specification compatibility, verifier behavior, and the same public skills CLI path documented for installation.

## Compliance and attribution

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or the ASD Simplified Technical English Maintenance Group (STEMG).

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group. This repository does not replace the official standard, its controlled dictionary, approved project terminology, specialist training, or human review.

The skill must not be used as evidence that generated text is formally compliant with ASD-STE100. Formal compliance requires verification against the applicable official ASD-STE100 issue and the relevant approved terminology.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
