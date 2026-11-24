from scripts.dataset_generation.yaml_converter import convert_yaml_to_dataset
import argparse
from .scripts import path_names
import Path 

if __name__ == '__main__':
  
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml_file')
    parser.add_argument('--yaml_dir', default=None)
    parser.add_argument('--branch', default=None)
    parser.add_argument('--repo-url', default=None)
    args = parser.parse_args()

    if args.yaml_dir is None:
        pass

    yaml_path = Path(path_names.DATASET_YAMLS)
    convert_yaml_to_dataset()