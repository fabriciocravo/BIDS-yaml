import subprocess
from pathlib import Path
from ..path_names import VALIDATOR_CACHE


# The spec clone, its venv and the schema all live in validator_cache
SPEC_DIR = Path(VALIDATOR_CACHE, 'bids-specification')
VENV_BIN = SPEC_DIR / '.venv' / 'bin'
SCHEMA_OUTPUT = Path(VALIDATOR_CACHE, 'schema.json')


def clone_spec(branch_name, repo_url):
    # Runs from VALIDATOR_CACHE (cwd), so the clone lands inside the cache
    subprocess.run(
        ['git', 'clone', '--branch', branch_name, repo_url],
        cwd=VALIDATOR_CACHE, check=True,
    )


def build_schema():
    # Builds the venv, installs schemacode and exports schema.json.
    # Steps run in order from SPEC_DIR; check=True stops at the first failure.
    # The venv tools are called by path, so no `source activate` is needed.
    commands = [
        ['python3', '-m', 'venv', str(SPEC_DIR / '.venv')],
        [str(VENV_BIN / 'pip'), 'install', '-e', 'tools/schemacode'],
        [str(VENV_BIN / 'bst'), '-v', 'export', '--output', str(SCHEMA_OUTPUT)],
    ]
    for command in commands:
        subprocess.run(command, cwd=SPEC_DIR, check=True)


def validate_dataset(dataset_dir):
    # Runs the standard BIDS validator (Deno, from JSR) against one dataset,
    # checking it with the schema.json built above.
    # Schema is passed as a file:// URI, which handles spaces in the path.
    # check=False: the validator exits non-zero when it finds dataset errors,
    # so the result is returned for the caller to read, not raised.
    command = [
        'deno', 'run', '-ERWN', 'jsr:@bids/validator',
        '-v', '--ignoreNiftiHeaders',
        '-s', SCHEMA_OUTPUT.as_uri(),
        str(dataset_dir),
    ]
    return subprocess.run(command)
