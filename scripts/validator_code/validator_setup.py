import subprocess
from path_names import VALIDATOR_CACHE


def setup_validator_from_git(branch_name, git=True):
    
    cd_comand    = 'cd ' + VALIDATOR_CACHE
    clone_comand = f'git clone --branch {branch_name} ' +\
        'git@github.com:bids-standard/bids-specification.git'
    
