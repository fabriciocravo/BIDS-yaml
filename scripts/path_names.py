import os

# Get path names
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_CACHE = os.path.join(ROOT, "dataset_cache")
DATASET_YAMLS = os.path.join(ROOT, "dataset_yamls")