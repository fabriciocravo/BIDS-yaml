# BIDS-yaml

## What this repo is
A tool for creating and debugging BIDS datasets. Developers write a BIDS dataset as a YAML file and edit it there, instead of editing the dataset files directly.

## Where to work
- Work in the user's local copy of this repo, on their computer. Never clone this repo.
- If you are running on the user's computer (for example, Claude Code opened in the repo), the repo is the current directory.
- If you are in a cloud session, read and run everything in the repo folder connected from the user's computer, not in the cloud workspace. If no folder is connected, ask the user to connect it through the Claude desktop app ("Add folder" in the + menu), then wait.

## Layout
- `bids-yaml.py`: compiles a YAML file into a dataset and runs the validator on it.
- `scripts/dataset_generation/`: builds a dataset from a YAML file.
- `scripts/validator_code/`: clones the BIDS specification repo at runtime, builds the schema from it, and runs the validator.
- `dataset_yamls/`: YAML files that describe datasets.
- `*_cache/`: temporary folders for the cloned specification and generated datasets. These are gitignored; never commit them.

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
