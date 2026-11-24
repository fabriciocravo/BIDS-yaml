import subprocess
from ..path_names import VALIDATOR_CACHE, BIDS_SPEC_URL


def setup_validator_from_git(branch_name=None, repo_url=None, git=True):

    # Fall back to the BIDS spec repo and its main branch when not given
    if repo_url is None:
        repo_url = BIDS_SPEC_URL
    if branch_name is None:
        branch_name = 'main'

    cd_comand    = 'cd ' + VALIDATOR_CACHE
    git_command  = f'git clone --branch {branch_name} {repo_url}'

    # PREPARED SPOT (you): run the clone and decide what git=False does.
    # See the chat for the options and trade-offs.

