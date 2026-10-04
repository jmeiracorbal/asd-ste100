# ASD-STE100 Agent Skill

An unofficial, domain-agnostic Agent Skill for explaining, writing, rewriting, and reviewing complex or technical information with principles from ASD-STE100 Simplified Technical English.

The primary goal is comprehension without semantic loss: reduce ambiguity and cognitive load while preserving the information that changes meaning.

## Install

Install from the public repository with the skills CLI:

```bash
npx skills add jmeiracorbal/asd-ste100
```

Inspect the skill before installing:

```bash
npx skills add jmeiracorbal/asd-ste100 --list
```

## What it does

The primary function is `explain`. The skill can also `write`, `rewrite`, and `review`.

It is intentionally domain-agnostic. The same method applies to software, physics, law, medicine, architecture, engineering, or any other subject. Domain terminology is preserved when replacing it could change technical meaning.

The skill applies these principles:

- understand the concept before simplifying it;
- preserve the original meaning;
- use one preferred term for one concept;
- explain one main idea at a time;
- use short and direct sentence structures;
- make conditions, causes, actions, results, sequence, and dependencies explicit;
- preserve quantities, units, negation, modality, uncertainty, exceptions, identifiers, and required terminology;
- use vertical lists when they make complex information easier to understand;
- keep one topic per paragraph and apply the Issue 9 six-sentence paragraph limit;
- identify ambiguity instead of silently inventing an interpretation;
- add detail progressively when it is necessary for understanding.

The core rule is:

> Clarity must not change meaning.

## Modes

### Practical STE

Practical STE is the default.

It uses ASD-STE100 principles as a comprehension-oriented output format without claiming formal or partial compliance. It is suitable for explanations, documentation, rewrites, and reviews where clarity and semantic fidelity matter.

### Strict mode

Strict mode is used only when the user explicitly asks for strict ASD-STE100 compliance, formal compliance, or a compliance review.

ASD-STE100 Issue 9 is the normative reference for strict mode. Formal compliance cannot be certified without the complete official writing rules, controlled dictionary, applicable approved terminology, and project-specific requirements.

For non-English output, the skill applies STE-inspired clarity principles but does not describe the result as formally ASD-STE100 compliant.

## Explanation structure

For explanations, the skill uses a comprehension-first order when the subject allows it:

1. State the concept or subject.
2. Give the essential explanation.
3. Explain the important relationships.
4. Add necessary details.
5. Add exceptions, limitations, or edge cases when they affect understanding.

This structure is not applied mechanically when a shorter explanation is sufficient.

## Deterministic verification

`scripts/ste-lint.py` is a dependency-free Python verifier for rules that can be checked mechanically.

### Lint structural rules

Procedural text:

```bash
python scripts/ste-lint.py lint --type procedure procedure.md
```

Descriptive text:

```bash
python scripts/ste-lint.py lint --type description description.md
```

The linter checks:

- maximum 20 words per procedural sentence;
- maximum 25 words per descriptive sentence;
- maximum six sentences per paragraph;
- contractions;
- semicolons;
- vertical-list introduction, capitalization, punctuation, and final period.

Exit code `0` means that no deterministic violation was found. Exit code `1` means that at least one violation was found.

### Verify rewrite fidelity

Compare a final rewrite with its source:

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

The command fails if one of these details disappears or a new one is introduced.

Machine-readable output is available for both commands:

```bash
python scripts/ste-lint.py --json lint --type description description.md
python scripts/ste-lint.py --json details original.md rewritten.md
```

The checker deliberately does not pretend to prove semantic equivalence. Conditions, causality, sequence, uncertainty, modality, terminology, and other semantic relationships still require the semantic-fidelity review defined by the skill.

## Rewrite verification workflow

For an English rewrite, the operational sequence is:

1. Preserve the original artifact.
2. Classify the target as procedural or descriptive.
3. Write the draft.
4. Run the applicable deterministic lint.
5. Correct every reported violation.
6. Run the fidelity comparison against the original.
7. Correct every missing or added technical detail.
8. Run both checks again on the final artifact.
9. Apply the semantic-fidelity checklist.
10. Deliver only the artifact that passed the final checks.

For new English text without a source artifact, the lint step applies. For reviews, deterministic lint is the first pass before the non-mechanical checklist.

## Usage examples

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

```text
Explain this in controlled technical English without changing the technical terminology.
```

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       ├── release.yml
│       └── validate-skill.yml
├── SKILL.md
├── README.md
├── LICENSE
├── VERSION
├── RELEASE_NOTES.md
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

`SKILL.md` contains the operational instructions and activation description.

`references/rules.md` contains the detailed writing and structural rules used by the skill.

`references/checklist.md` contains the systematic review and semantic-fidelity checklist.

`references/terminology.md` contains domain-neutral terminology guidance.

`references/examples.md` contains domain-neutral transformation examples.

`scripts/ste-lint.py` contains the deterministic structural linter and technical-detail fidelity checker.

`tests/test_ste_lint.py` contains regression tests for both verifier modes.

`evals/evals.json` contains behavioral evaluations for structure, semantic fidelity, ambiguity handling, explanation quality, strict-mode boundaries, and deterministic verification behavior.

`evals/trigger_set.json` contains 20 activation queries: 10 that should trigger the skill and 10 adjacent or near-miss requests that should not trigger it.

## Evaluation and CI

The repository validates the skill on every push and pull request.

The CI workflow:

1. validates the evaluation JSON and the 10/10 trigger balance;
2. runs the Python regression suite for `scripts/ste-lint.py`;
3. validates the linter CLI entry points;
4. runs the official Agent Skills reference validator with `skills-ref validate`;
5. verifies local discovery with the skills CLI;
6. verifies public discovery with `npx skills@latest add jmeiracorbal/asd-ste100 --list`.

Releases are versioned from `VERSION`. A change to that file runs the release workflow, validates the repository, creates the matching Git tag, and publishes the GitHub Release from `RELEASE_NOTES.md`.

## Scope and limitations

The deterministic verifier covers only properties that can be checked reliably without pretending that regex or heuristics understand the full meaning of a document.

It does not:

- certify formal ASD-STE100 compliance;
- reproduce or replace the official controlled dictionary;
- infer missing project terminology;
- prove that two texts are semantically equivalent;
- replace human review where formal compliance is required.

The skill does not silently rewrite controlled warnings, cautions, legal text, mandatory statements, or other wording that the user is not authorized to change.

## ASD-STE100 attribution

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or the ASD Simplified Technical English Maintenance Group (STEMG).

ASD-STE100 is maintained by STEMG. This repository does not replace the official standard, controlled dictionary, approved terminology, specialist training, or human review.

## License

The project is licensed under the MIT License. See `LICENSE` for details.
