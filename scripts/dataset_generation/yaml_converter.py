import yaml


def convert_yaml_to_dataset(yaml_file):

    with open(yaml_file) as f:
        dataset_dict = yaml.safe_load(f)

    dataset_name = False

