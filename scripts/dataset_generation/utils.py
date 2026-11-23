from pathlib import Path
from ..path_names import DATASET_CACHE
import json
import pandas as pd


def create_dataset_directory(directory_name):
    Path(DATASET_CACHE, directory_name).mkdir(parents=True, exist_ok=True)


def save_json(path, data):
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def write_tsv(path, contents):
    
    # Write a simple tsv with the datframe stuff
    empty_df = pd.DataFrame()
    for key, value in contents.items():
        empty_df[key] = value

    empty_df.to_csv(path, sep='\t', index=False)
