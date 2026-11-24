import subprocess
import Path
from ..path_names import VALIDATOR_CACHE, SPEC_DIR


def run_subprocess(command):
    """
    Docstring for run_subprocess
    
    :param command: List with subprocess commandSubprocess com
    """
    returned_output = subprocess.run(
        command,
        cwd=VALIDATOR_CACHE,
        capture_output=True
    )

    if returned_output.returncode != 0:
        raise subprocess.CalledProcessError(
                returned_output.returncode,
                command
            )

    return (
        returned_output.stdout,
        returned_output.stderr
    )


def clone_spec(branch_name, repo_url):
    # Runs from VALIDATOR_CACHE (cwd), so the clone lands inside the cache
    command = ['git', 'clone', '--branch', branch_name, repo_url]
    returncode, _, _ = run_subprocess(command)
    return returncode


def fix_fork(repo_url):
    # Fixes the remote url to match the correct one requested
    spec = str(SPEC_DIR)
    commands = [
        ['git', '-C', spec, 'remote', 'set-url', 'origin', repo_url],
        ['git', '-C', spec, 'fetch', 'origin']
    ]
    for command in commands:
        run_subprocess(command)


def fix_branch(repo_url)


def process_git_errors(error_code, branch_name, repo_url):

    if error_code == 128:
        git_path = Path(VALIDATOR_CACHE, '.git')

        exists = git_path.exists()
        if exists:
            _, stdout, _ = run_subprocess(
                ['git', '-C', str(SPEC_DIR), 'remote', 'get-url', 'origin']
            )
            fork_url = stdout.decode().strip()
        
        if exists:
            _, stdout, _ = run_subprocess(
                ['git', '-C', str(SPEC_DIR), 'remote', 'get-url', 'origin']
            )
            fork_url = stdout.decode().strip()


        if exists and fork_url != repo_url:
            fix_fork(repo_url)

        pass
        command = ['git', '-C', SPEC_DIR, 'branch', '--show-current']
