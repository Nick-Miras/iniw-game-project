import json
from json import JSONDecodeError


def return_json_data(json_file_path: str) -> dict:
    with open(json_file_path) as f:
        try:
            data = json.load(f)
        except JSONDecodeError:
            return {}
        else:
            return data
