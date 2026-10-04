# ASD-STE100 skill

An unofficial Agent Skill for writing, rewriting, and reviewing technical content with principles from ASD-STE100 Simplified Technical English.

The skill is intended for technical documentation, procedures, explanations, software documentation, and other content where clarity, consistency, and reduced ambiguity are important.

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

The skill instructs an agent to:

- distinguish procedural text from descriptive text;
- use one term for one concept;
- prefer short and direct sentence structures;
- make conditions, actions, causes, and results explicit;
- reduce unnecessary synonyms, vague wording, and decorative language;
- preserve domain-specific technical terms when simplification would change the meaning;
- review existing technical text for ambiguity and consistency;
- apply STE-inspired clarity principles to non-English text without claiming formal ASD-STE100 compliance.

## Repository structure

```text
.
├── SKILL.md
├── README.md
├── LICENSE
└── references/
    ├── examples.md
    └── rules.md
```

`SKILL.md` contains the operational instructions for the agent.

`references/rules.md` contains additional writing constraints and review guidance.

`references/examples.md` contains transformation examples for technical content.

## Usage

After installation, ask the agent to use the skill when you want technical content written or reviewed in an ASD-STE100-oriented style.

Examples:

```text
Rewrite this procedure using ASD-STE100.
```

```text
Review this technical explanation for ASD-STE100 issues.
```

```text
Explain this architecture in an ASD-STE100 style.
```

For non-English output, the skill applies the same clarity principles but treats the result as STE-inspired rather than formally ASD-STE100-compliant.

## Compliance and attribution

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or the ASD Simplified Technical English Maintenance Group (STEMG).

ASD-STE100 is maintained by the ASD Simplified Technical English Maintenance Group. This repository does not replace the official standard, its controlled dictionary, approved project terminology, specialist training, or human review.

The skill must not be used as evidence that generated text is formally compliant with ASD-STE100. Formal compliance requires verification against the applicable official ASD-STE100 issue and the relevant project terminology.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
