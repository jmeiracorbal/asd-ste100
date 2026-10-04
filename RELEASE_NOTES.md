# v1.0.0

Initial stable release of the ASD-STE100 Agent Skill.

## Highlights

- Domain-agnostic `explain`, `write`, `rewrite`, and `review` behavior.
- Practical STE as the default mode, with strict mode only for explicit formal-compliance requests.
- Semantic-fidelity rules that preserve quantities, units, negation, modality, uncertainty, conditions, sequence, dependencies, identifiers, and technical terminology.
- Issue 9 structural behavior for sentence length, paragraph limits, complete grammar, and vertical lists.
- Deterministic `scripts/ste-lint.py` structural checks for procedural and descriptive text.
- Deterministic source-to-rewrite fidelity checks for numbers, ranges, percentages, units, acronyms, identifiers, negation count, inline code, and fenced code blocks.
- Behavioral evals plus a balanced 20-case trigger evaluation set.
- Regression tests for the verifier.
- CI validation with `skills-ref` and public discovery through the skills CLI.
- MIT license declared both in the repository and skill metadata.

## Install

```bash
npx skills add jmeiracorbal/asd-ste100
```

This project is unofficial and is not affiliated with, endorsed by, or certified by ASD or STEMG.
