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
The commands run in the Linux VM behind the desktop-app connection. Install everything into that VM. Check each requirement before the first run, from the repo root.

For each missing requirement, tell the user what is missing and the install command, and install it only after they agree. If an install fails, show the user the error and the command, and stop.

### System packages (Python, venv, pip, git)
These install with `apt-get`, which needs root. First check how to run it:
- `id -u` prints `0`: you are root. Run the `apt-get` commands as written.
- Otherwise, `sudo -n true` succeeds: prefix the `apt-get` commands with `sudo`.

1. Python 3.10 or newer, with `venv`
   - Check: `python3 --version` and `python3 -c "import venv"`
   - Install: `apt-get update && apt-get install -y python3 python3-venv`
2. pip
   - Check: `python3 -m pip --version`
   - Install: `apt-get install -y python3-pip`
3. git
   - Check: `git --version`
   - Install: `apt-get install -y git`
4. curl and unzip (needed to install deno)
   - Check: `command -v curl unzip`
   - Install: `apt-get install -y curl unzip`

### User packages
5. Python packages from `requirements.txt`
   - Check: `python3 -c "import pandas, yaml"`
   - Install: `python3 -m pip install --user -r requirements.txt`
   - If the install fails:
     <!-- TODO(Fabricio): what to do when pip refuses or fails -->
6. deno, installed in `~/.local/bin`
   - Check: `PATH="$HOME/.local/bin:$PATH" deno --version`
   - Install: `curl -fsSL https://deno.land/install.sh | DENO_INSTALL="$HOME/.local" sh -s -- -y`
   - Run the check again to confirm.

Network access to github.com, PyPI, deno.land and jsr.io is needed. If the validator step fails fetching `jsr.io`, report it to the user. Do not work around it.

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
