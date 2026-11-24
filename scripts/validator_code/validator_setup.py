from ..path_names import BIDS_SPEC_URL
from .git_scripts import clone_spec
import subprocess

def setup_validator_from_git(branch_name=None, repo_url=None, git=True):

    # Fall back to the BIDS spec repo and its main branch when not given
    if repo_url is None:
        repo_url = BIDS_SPEC_URL
    if branch_name is None:
        branch_name = 'main'

    try:
        clone_spec(branch_name, repo_url)
    except subprocess.CalledProcessError as e:
        print(e.returncode)   # git's exit code, e.g. 128
        print(e.cmd)          # the command list that failed



    
