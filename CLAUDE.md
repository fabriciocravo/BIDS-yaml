# bids-dev-validator

## What this repo is
A tool for creating and debugging BIDS datasets. Developers write a BIDS dataset as a YAML file and edit it there, instead of editing the dataset files directly.

## Layout
- `bids-yaml.py`: compiles a YAML file into a dataset and runs the validator on it.
- `scripts/dataset_generation/`: builds a dataset from a YAML file.
- `scripts/validator_code/`: clones the BIDS schema from git and runs the validators.
- `dataset_yamls/`: YAML files that describe datasets.
- `*_cache/`: temporary folders for cloned repos and generated datasets. These are gitignored; never commit them.

## How to work here
- Read the skill at `.claude/skills/bids-validator/SKILL.md` before running any script.
- If the user asks you to clone this repo and does not say they are a developer, follow the standard workflow in the skill and use the hook at [hook location].
- If the user says they are a developer, skip the standard workflow and work with the scripts directly.
- Ask before running scripts or changing files outside this repo.
- Do not commit or push unless the user asks.

## Skill
Detailed usage instructions are in `.claude/skills/bids-validator/SKILL.md`.

