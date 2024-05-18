import json
from abc import ABC
from typing import Generic

from pydantic import BaseModel

from custom_types import ID
from database.abc import CRUD, T
from datum.entity import Player
from datum.inventory import Inventory
from generics.database import find_model_in_collection_with_id
from generics.file_ops import return_json_data


class Delete(CRUD[ID], ABC):
    @staticmethod
    def remove_model_from_database_file(model_id: ID, file_name: str):
        database_data = return_json_data(f'data/{file_name}.json')
        collection: list[dict] = database_data[file_name]
        if (model_id not in (model['id'] for model in collection)) is True:
            raise ValueError(f'cannot find id of model type:{file_name}')
        else:
            model = find_model_in_collection_with_id(model_id, collection)
            collection.remove(model)

        database_data[file_name] = collection
        with open(f'data/{file_name}.json', 'w') as f:
            json.dump(database_data, f)


class DeletePlayer(Delete):
    @classmethod
    def execute(cls, data: T):
        cls.remove_model_from_database_file(data, 'players')


class DeleteInventory(Delete):
    @classmethod
    def execute(cls, data: T):
        cls.remove_model_from_database_file(data, 'inventories')
