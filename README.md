# BIDS-yaml with LLM workflows

Write a BIDS dataset as a single YAML file, then compile it into a real dataset folder and run the official BIDS validator on it. You edit the YAML, not the dataset files.

## Repos functionalities

1. **Compiles** a YAML file from `dataset_yamls/` into a BIDS dataset in `dataset_cache/`.
2. **Clones** the BIDS specification repo into `validator_cache/` - with choice of branch and fork
3. **Builds** a `schema.json` from that specification.
4. **Validates** the generated dataset with the BIDS validator (Deno, from JSR) against that schema.

## Requirements

| Tool | Version | Used for |
|---|---|---|
| Python | 3.10 or newer, with `venv` and `pip` | Running `bids-yaml.py` and building the schema |
| git | any recent version | Cloning the BIDS specification |
| deno | any recent version | Running the validator |
| Python packages | `pandas`, `PyYAML` (see `requirements.txt`) | Reading YAML and writing TSV files |
| Network access | `github.com`, `pypi.org`, `jsr.io`, `deno.land` | Cloning, installing, and fetching the validator |

## Requirements

### 1. Python 3.10+ and pip

- **macOS:** `brew install python` (or use the python.org installer). Check with `python3 --version`.
- **Ubuntu/Debian:** `sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip`

### 2. git

- **macOS:** `xcode-select --install`, or `brew install git`.
- **Ubuntu/Debian:** `sudo apt-get install -y git`

### 3. Python packages

```bash
python3 -m pip install --user -r requirements.txt
```

Check with `python3 -c "import pandas, yaml"`. No output means it worked.

### 4. deno

- **macOS:** `brew install deno`
- **Any platform:** `python3 -m pip install --user deno`, which the workflow uses

Check with `deno --version`. If the command isn't found and you used pip, add `~/.local/bin` to your `PATH`. The workflow itself uses `PATH="$HOME/.local/bin:$PATH"` to handle this.

## Installation

### Clone this repo

```bash
git clone https://github.com/fabriciocravo/BIDS-yaml.git
```

Replace `<repo-url>` with the repository's GitHub URL

## Usage

### With Claude Desktop

1. Give Claude Desktop permission to access the following websites: jsr.io and deno.land 
2. Open a new chat in Claude Desktop and use the following prompt "[cloned repo path] - Read this directory and use the yaml-workflow skill inside it"
3. Claude will list the permissions it needs, for more details check the yaml-workflow SKILL.md. It contains the detailed necessary permissions.
4. Review the validator output with Claude. Edit the YAML if needed, then ask for a rerun.

The workflow is defined in `.claude/skills/yaml-workflow/SKILL.md`. It only runs when you ask for it by name.

### From the terminal

``` python3 bids-yaml.py <yaml file>```

- A bare filename is looked up in `dataset_yamls/`, for example `first_example.yaml`.
- A full path also works, but it needs to be specified in --yaml_dir

Optional flags:

| Flag | Default | Purpose |
|---|---|---|
| `--repo-url <url>` | `https://github.com/bids-standard/bids-specification.git` | Use a different specification repo or fork |
| `--branch <name>` | `master` | Specification branch to check out |
| `--yaml_dir <dir>` | `dataset_yamls/` | Folder to look for YAML files in |
| `--verbose <n>` | `0` | Higher values print more log messages to stderr |

Validator results are printed to stderr.

## Writing a dataset YAML

To write the BIDS dataset in yaml format follow the following rules

- `dataset`: the folder tree. Everything is a nested list. For example:
```yaml
dataset:
  - dataset_description.json
  - participants.tsv
  - sub-01:
      - anat:
        - sub-01_T1w.nii.gz
        - sub-01_T1w.json
      - func:
        - sub-01_task-rest_bold.nii.gz
```
The elements ending in : are considered directories, while the ones without it are considered files.
- `files`: the contents of files. JSON files take dictionaries, and TSV files take a dictionary of column names to lists of values. We will add support to more file types in time.
```yaml
  files:
  dataset_description.json:
    Name: test
    BIDSVersion: "1.10.0"
  participants.tsv:
    participant_id: [sub-01]
    age: [25]
    sex: [M]
  sub-01_T1w.json:
    TaskName: rest
    RepetitionTime: 2.0
```

`dataset_yamls/first_example.yaml` is a minimal example.

Supported file types are `.json`, `.tsv`, and `.nii.gz`. `.nii.gz`.
