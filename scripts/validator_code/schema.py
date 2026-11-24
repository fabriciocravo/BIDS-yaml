import subprocess
from ..path_names import VALIDATOR_CACHE, SPEC_DIR, VENV_BIN, SCHEMA_OUTPUT


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
    # checking it with the schema.json
    # Captures output of subprocess and returns it
    command = [
        'deno', 'run', '-ERWN', 'jsr:@bids/validator',
        '-v', '--ignoreNiftiHeaders',
        '-s', SCHEMA_OUTPUT,
        str(dataset_dir),
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
