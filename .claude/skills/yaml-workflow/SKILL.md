---
name: yaml-workflow
description: Use only when the user types "yaml-workflow" or asks to run the yaml-workflow. Compiles a YAML dataset description from bids-dev-validator into a BIDS dataset and runs the validator on it. Do not use otherwise.
---

# yaml-workflow

## Locate the repo
- Work in the user's local copy of the repo, on their computer. Never clone the repo. The repo is named BIDS-yaml.
- If you are running on the user's computer (for example, Claude Code opened in the repo), the repo is the current directory.
- If you are in a cloud session, use the repo folder connected from the user's computer, and run every command in that folder's shell, not in the cloud workspace. If no folder is connected, ask the user to connect the repo folder through the Claude desktop app ("Add folder" in the + menu), then wait.
- If the user gave a path to a different copy, use that copy.
- Check that `bids-yaml.py` exists in the folder. If it doesn't, say so and ask for a corrected path.

## Requirements
Check each requirement before the first run, from the repo root.

Automatic installation is supported only on macOS with Homebrew at the moment.
- Check the system with `uname -s` (macOS prints `Darwin`) and `brew --version`. If not, request the user to install Homebrew.
- On macOS with Homebrew: if something is missing, tell the user what is missing and the command you would use to install it, and install it only after they agree. If an installation fails, give the user the command so they can try it themselves.
- On any other system, or if Homebrew is missing: do not install anything. List what is missing and ask the user to install it themselves, then wait.

The requirements are:
1. Python 3.10 or newer, with `venv`
   - Check: `python3 --version` and `python3 -c "import venv"`
   - Install (macOS): `brew install python`
2. git
   - Check: `git --version`
   - Install (macOS): `brew install git`
3. Python packages from `requirements.txt`
   - Check: `python3 -c "import pandas, yaml"`
   - Install (macOS): `python3 -m pip install -r requirements.txt`
   - If the install fails:
     <!-- TODO(Fabricio): what to do when pip refuses or fails -->
4. deno, on `PATH`, because the validator step calls it by name
   - Check: `deno --version`
   - Install (macOS): `brew install deno`

Network access to github.com, PyPI and jsr.io is needed. If the validator step fails fetching `jsr.io`, report it to the user. Do not work around it.

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
1. Work from the repo root on the user's computer.
2. Run `python3 bids-yaml.py <yaml file>`. A bare filename is looked up in `dataset_yamls/`.
3. Add `--repo-url <url>` and `--branch <name>` only if the user gave them. Otherwise leave them off so the script's defaults apply.

## Working with the user
- Show the validator results to the user.
- Let them edit the YAML, then ask before rerunning.
