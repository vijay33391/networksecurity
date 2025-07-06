# write common file code here
import os
import yaml

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    
    :param file_path: Path to the YAML file.
    :return: Dictionary containing the YAML file content.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise Exception(f"Error reading YAML file {file_path}: {e}")
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise Exception(f"Error writing YAML file {file_path}: {e}")
    