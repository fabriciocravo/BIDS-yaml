from scripts.dataset_generation.yaml_converter import convert_yaml_to_dataset
from scripts.validator_code.validator_setup import setup_validator_from_git
from scripts.validator_code.schema import validate_dataset
import argparse
from pathlib import Path
from scripts import utils
from scripts.loger import Log
import sys



if __name__ == '__main__':
  
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml_file')
    parser.add_argument('--yaml_dir', default=None)
    parser.add_argument('--branch', default=None)
    parser.add_argument('--repo-url', default=None)
    parser.add_argument('--verbose', default=0)
    args = parser.parse_args()

    Log.set_verbose(args.verbose)
    yaml_dir, branch, repo_url = utils.parse_args_bids_yaml(args)

    yaml_full_file = Path(yaml_dir, args.yaml_file)
    dataset_path = convert_yaml_to_dataset(yaml_file=yaml_full_file, full_path=True)
    setup_validator_from_git(branch=branch, repo_url=repo_url)
    results = validate_dataset(dataset_path)
    
    print(results, file=sys.stderr)
