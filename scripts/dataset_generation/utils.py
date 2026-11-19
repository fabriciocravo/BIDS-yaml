from pathlib import Path
from ..path_names import DATASET_CACHE


def create_dataset_directory(directory_name):
    Path(DATASET_CACHE + directory_name).mkdir(parents=True, exist_ok=True)