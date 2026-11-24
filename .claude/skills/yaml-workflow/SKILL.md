---
name: yaml-workflow
description: Use only when the user types "yaml-workflow" or asks to run the yaml-workflow. Compiles a YAML dataset description from bids-dev-validator into a BIDS dataset and runs the validator on it. Do not use otherwise.
---

# yaml-workflow

## Locate the repo
- This skill is part of the repo, so the repo is already present. Work from its root.
- If the user gave a path to a different copy, use that copy. Check that `bids-yaml.py` exists there. If it doesn't, say so and ask for a corrected path.

## Before running anything
List the files in `dataset_yamls/`, then ask in one message:
- Which YAML file to use (a name from the list, or a full path).
- The URL of the BIDS schema repo (optional).
- The schema branch (optional).

## If the user has no YAML file
- Offer to draft one from `dataset_yamls/first_example.yaml`, based on their description, or let them paste their own.
- If they want to edit it in an artifact, create a Claude Doc with the YAML in a code block. When they say they are done, read it back, extract the YAML, and show it before saving.
- If Docs are unavailable, show the YAML in chat and take edits there.
- Save to `dataset_yamls/` only when asked. Never overwrite an existing file.

## Running the validator
1. Work from the repo root.
2. Run `python3 bids-yaml.py <yaml path>`.
3. Add `--repo-url <url>` and `--branch <name>` only if the user gave them. Otherwise leave them off so the script's defaults apply.

## Working with the user
- Show the validator results to the user.
- Let them edit the YAML, then ask before rerunning.