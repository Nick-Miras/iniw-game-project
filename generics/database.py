from custom_types import ID
from generics.file_ops import return_json_data


def check_if_exists(id_: ID, file_name: str) -> bool:
    json_data = return_json_data(f'data/{file_name}.json')
    collection = json_data[file_name]
    return id_ in (model['id'] for model in collection)
