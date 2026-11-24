import yaml
import json
import sys
from . import utils
from scripts.path_names import DATASET_YAMLS, DATASET_CACHE
import os
from pathlib import Path
from .dfs_yaml import dfs_yaml


def convert_yaml_to_dataset(yaml_file, full_path=False):

    if not full_path:
        yaml_path = os.path.join(DATASET_YAMLS, yaml_file)
    else:
        yaml_path = yaml_file

    with open(yaml_path) as f:
        dataset_dict = yaml.safe_load(f)

    try:
        dataset_name =\
            dataset_dict['files']['dataset_description.json']['Name']
    except KeyError as e:
        print(
            f'{e}\n' +
            'Dataset name not found in yaml file',
            file=sys.stderr
        )

    utils.create_dataset_directory(dataset_name)
    dataset_path = os.path.join(DATASET_CACHE, dataset_name)

    # DFS start of the exploration
    dfs_yaml(dataset_dict['dataset'], dataset_path, dataset_dict)

    return dataset_path




