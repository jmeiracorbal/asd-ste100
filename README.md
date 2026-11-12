# ASD-STE100 Agent Skill

[![Validate skill](https://github.com/jmeiracorbal/asd-ste100/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/jmeiracorbal/asd-ste100/actions/workflows/validate-skill.yml)
[![GitHub Release](https://img.shields.io/github/v/release/jmeiracorbal/asd-ste100)](https://github.com/jmeiracorbal/asd-ste100/releases/latest)
[![License](https://img.shields.io/github/license/jmeiracorbal/asd-ste100)](LICENSE)

An unofficial, domain-agnostic Agent Skill for explaining, writing, rewriting, and reviewing complex or technical information with principles from ASD-STE100 Simplified Technical English.

The primary goal is comprehension without semantic loss: reduce ambiguity and cognitive load while preserving the information that changes meaning.

## Install

Install the skill directly with the standard skills CLI:

```bash
npx skills add jmeiracorbal/asd-ste100
```

That is the complete installation. The skill does not install hooks, run bootstrap code, execute local helpers, or require Python or another runtime from the user.

Inspect the skill before installing:

```bash
npx skills add jmeiracorbal/asd-ste100 --list
```

## Native Agent Skill

The skill is declarative. Its behavior is defined by `SKILL.md` and the reference files that the agent reads when needed.

It does not depend on:

- hooks;
- bootstrap scripts;
- background processes;
- local linters;
- wrapper commands;
- runtime-specific integration code.

Any compatible Agent Skills client can consume the same instructions without an additional installation step.

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

## Scope and limitations

The skill applies the rules and review guidance directly through the agent. It does not claim that an instruction set can prove semantic equivalence or certify formal ASD-STE100 compliance by itself.

It does not:

- certify formal ASD-STE100 compliance without the official sources required for that review;
- reproduce or replace the official controlled dictionary;
- infer missing project terminology;
- silently change quantities, conditions, modality, uncertainty, negation, sequence, or dependencies;
- replace human review where formal compliance is required.

The skill does not silently rewrite controlled warnings, cautions, legal text, mandatory statements, or other wording that the user is not authorized to change.

## ASD-STE100 attribution

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or the ASD Simplified Technical English Maintenance Group (STEMG).

ASD-STE100 is maintained by STEMG. This repository does not replace the official standard, controlled dictionary, approved terminology, specialist training, or human review.

## License

The project is licensed under the MIT License. See `LICENSE` for details.
