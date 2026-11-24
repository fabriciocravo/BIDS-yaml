# bids-dev-validator

## What this repo is
A tool for creating and debugging BIDS datasets. Developers write a BIDS dataset as a YAML file and edit it there, instead of editing the dataset files directly.

## Layout
- `bids-yaml.py`: compiles a YAML file into a dataset and runs the validator on it.
- `scripts/dataset_generation/`: builds a dataset from a YAML file.
- `scripts/validator_code/`: clones the BIDS schema from git and runs the validators.
- `dataset_yamls/`: YAML files that describe datasets.
- `*_cache/`: temporary folders for cloned repos and generated datasets. These are gitignored; never commit them.

## Workflows
Each workflow runs only when the user asks for it by its keyword. Otherwise, do not start a workflow; work on what the user asks.

```yaml
workflows:
  yaml-workflow:
    skill: .claude/skills/yaml-workflow/SKILL.md
    purpose: Compile a YAML dataset description and run the validator on it.
```

The trigger for each workflow is citing the name of the workflow itself. 
Check .claude/skills for all workflow skills.

## Permissions
`.claude/settings.json` restricts which commands and edits are allowed in this repo. Do not work around it.