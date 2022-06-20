import yaml


def load_yaml_file(yaml_file_path):
    """
    Load and read given YAML file

    Parameters
    ----------
    yaml_file_path: str
        Location (file path) of yaml file to read

    Returns
    --------
        dict

    """
    yaml_file = open(yaml_file_path, encoding="UTF-8").read()
    yaml_contents = yaml.full_load(yaml_file)

    return yaml_contents
