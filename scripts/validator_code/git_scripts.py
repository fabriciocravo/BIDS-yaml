import subprocess
from ..path_names import VALIDATOR_CACHE, SPEC_DIR, VENV_BIN, SCHEMA_OUTPUT


def clone_spec(branch_name, repo_url):
    # Runs from VALIDATOR_CACHE (cwd), so the clone lands inside the cache
    returned_output = subprocess.run(
        ['git', 'clone', '--branch', branch_name, repo_url],
        cwd=VALIDATOR_CACHE,
        capture_output=True
    )
    return returned_output.returncode