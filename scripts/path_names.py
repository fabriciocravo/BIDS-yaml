import os
import Path

# Get path names
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_CACHE = os.path.join(ROOT, "dataset_cache")
DATASET_YAMLS = os.path.join(ROOT, "dataset_yamls")
VALIDATOR_CACHE = os.path.join(ROOT, "validator_cache")

# Remote locations
BIDS_SPEC_URL = 'https://github.com/bids-standard/bids-specification.git'

# The spec clone, its venv and the schema all live in validator_cache
SPEC_DIR = Path(VALIDATOR_CACHE, 'bids-specification')
VENV_BIN = SPEC_DIR / '.venv' / 'bin'
SCHEMA_OUTPUT = Path(VALIDATOR_CACHE, 'schema.json')
