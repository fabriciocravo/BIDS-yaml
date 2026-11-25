---
name: yaml-workflow
description: Use only when the user types "yaml-workflow" or asks to run the yaml-workflow. Compiles a YAML dataset description from BIDS-yaml into a BIDS dataset and runs the validator on it. Do not use otherwise.
---

# yaml-workflow

## Locate the repo
- Work in the user's local copy of the repo, on their computer. Never clone the repo. The repo is named BIDS-yaml.
- If you are running on the user's computer (for example, Claude Code opened in the repo), the repo is the current directory.
- If you are in a cloud session, use the repo folder connected from the user's computer, and run every command in that folder's shell, not in the cloud workspace. If no folder is connected, ask the user to connect the repo folder through the Claude desktop app ("Add folder" in the + menu), then wait.
- If the user gave a path to a different copy, use that copy.
- Check that `bids-yaml.py` exists in the folder. If it doesn't, say so and ask for a corrected path.

## Permissions to confirm before running
Before the requirement checks, list these permissions and ask the user to confirm them in one message:

1. **Folder access.** Read and write access to the connected BIDS-yaml repo folder.
2. **Delete access.** The validator's pip install removes temporary files inside `validator_cache/`. Include this in the permissions message, and request delete permission for the repo folder once, up front. Do not start the install or the validator until it's granted. Only delete inside `validator_cache/`.
3. **Reads.** `bids-yaml.py`, this skill, `CLAUDE.md`, a listing of `dataset_yamls/`, and the YAML file the user picks.
4. **Writes.** The validator creates `dataset_cache/` and `validator_cache/` inside the repo. Both are git-ignored. Write to `dataset_yamls/` only when the user asks to save a YAML there, and never overwrite an existing file.
5. **Installs.** Missing system packages go through `apt-get` (root or `sudo` required). Missing Python packages and deno go through `pip --user`. Installs run without a separate confirmation, but report each one afterward.
6. **Network access.** `github.com`, `pypi.org`, `jsr.io`, and `deno.land` must all be reachable. If one is blocked, report which host and ask user to add permission in the desktop app.
7. **Command permissions.** The run command must be allowed in `.claude/settings.json`. Both `python3 bids-yaml.py` and the `PATH="$HOME/.local/bin:$PATH" python3 bids-yaml.py` form should be on the allow list.

Don't run `rm` through the shell, even with delete access. The deny list blocks it. Use the desktop app's delete permission instead.

## Requirements
The commands run in the Linux VM behind the desktop-app connection. Install everything into that VM. Check each requirement before the first run, from the repo root.

For each missing requirement, install it without asking, then tell the user what you installed. If an install fails, show the user the error and the command, and stop.

### System packages (Python, venv, pip, git)
These install with `apt-get`, which needs root. First check how to run it:
- `id -u` prints `0`: you are root. Run the `apt-get` commands as written.
- Otherwise, `sudo -n true` succeeds: prefix the `apt-get` commands with `sudo`.
- Otherwise: do not install. Tell the user the requirement is missing and cannot be installed in this environment without root, and stop.

1. Python 3.10 or newer, with `venv`
   - Check: `python3 --version` and `python3 -c "import venv"`
   - Install: `apt-get update && apt-get install -y python3 python3-venv`
2. pip
   - Check: `python3 -m pip --version`
   - Install: `apt-get install -y python3-pip`
3. git
   - Check: `git --version`
   - Install: `apt-get install -y git`

### User packages (installed with pip, no root needed)
4. Python packages from `requirements.txt`
   - Check: `python3 -c "import pandas, yaml"`
   - Install: `python3 -m pip install --user -r requirements.txt`
5. deno, installed in `~/.local/bin`
   - Check: `PATH="$HOME/.local/bin:$PATH" deno --version`
   - Install: `python3 -m pip install --user deno`
   - Run the check again to confirm.

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
1. Work from the repo root, in the VM.
2. Run `PATH="$HOME/.local/bin:$PATH" python3 bids-yaml.py <yaml file>`. A bare filename is looked up in `dataset_yamls/`.
3. Add `--repo-url <url>` and `--branch <name>` only if the user gave them. Otherwise leave them off so the script's defaults apply.

## Working with the user
- Show the validator results to the user.
- Let them edit the YAML, then ask before rerunning.
