from pydantic import BaseModel

from custom_types import ID
from generics.file_ops import return_json_data


def check_if_exists(id_: ID, file_name: str) -> bool:
    json_data = return_json_data(f'data/{file_name}.json')
    collection = json_data[file_name]
    return id_ in (model['id'] for model in collection)


def find_model_in_collection_with_id(model_id: ID, collection: list[dict]) -> dict:
    for model in collection:
        if model['id'] == model_id:
            return model
