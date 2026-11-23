import os
from . import utils


def checks_dataset_file(dataset_dict, dir_name, file_name):

    # Function that checks dataset_dict['files']
    files = dataset_dict.get('files', {})
    full_name = os.path.join(dir_name, file_name)

    # First checks the file with full path name
    # if it finds - returns dictionary with contents
    if full_name in files:
        return files[full_name]
    
    # Then checks with only the file name alone
    if file_name in files:
        return files[file_name]
    return None


def dfs_yaml(node, dir_name, dataset_dict):
    
    # Loop over each element
    for e in node:
        # If the element is a dictionary - explore deeper with the new name
        if isinstance(e, dict):
            (node_name, new_node), = e.items()

            dfs_yaml(
                new_node,
                os.path.join(dir_name, node_name),
                dataset_dict,
            )

        else:
            # If it's a string - assume file - for files
            # Call checks_dataset_file for contents
            contents = checks_dataset_file(dataset_dict, dir_name, e)
            os.makedirs(dir_name, exist_ok=True)
            file_path = os.path.join(dir_name, e)

            # Create file - if json, use contents as specified
            if e.endswith('.json'):
                utils.save_json(file_path, contents)
            # tsv assume dictionary names keys - items list values
            elif e.endswith('.tsv'):
                utils.write_tsv(file_path, contents)
            # If nii.gv just create
            elif e.endswith('.nii.gz'):
                open(file_path, 'wb').close()
            else:
                raise ValueError('Error file type not supported')