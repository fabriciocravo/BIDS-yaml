---
name: yaml-workflow
description: Use after cloning or setting up bids-dev-validator, to compile a YAML dataset description into a BIDS dataset and run the validator on it. Do not use if the user says they are a developer working on the repo's code. 
---

# yaml-workflow

## First check
If the user has said they are a developer, stop here. Do not run this workflow. Work with the scripts directly as they ask.

## Setup
- Work from the repo root.
- [Dependencies to install — requiments.txt]

## Before running anything
List the files in `dataset_yamls/`, then ask the user, in one message:
- Which YAML file to use (a name from the list, or a full path).
- The URL of the BIDS schema repo (optional).
- The schema branch (optional).

## If the user has no YAML file
- Offer to draft one from `dataset_yamls/first_example.yaml`, based on their description, or let them paste their own in chat.
- If the user wants to edit it in an artifact, create a Claude Doc containing the YAML in a code block. When the user says they are done, read the doc back, extract the YAML, and show it before saving.
- Save it to `dataset_yamls/`
- If the file name already exists, confirm with user if he wants to override it or not

## Running the validator
1. Run `python3 bids-yaml.py <yaml path>`.
2. Add `--repo-url <url>` and `--branch <name>` only if the user gave them. Otherwise leave them off so the script's defaults apply.

## Working with the user
- Present the validator results as a list of errors first, then warnings
- After the user edits the YAML, ask before rerunning, then rerun and report what changed since the last run.