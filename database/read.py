from abc import ABC

from custom_types import ID
from database.abc import CRUD, T
from datum import entity
from datum.inventory import Inventory
from datum.items import Item
from generics.database import find_model_in_collection_with_id
from generics.file_ops import return_json_data


class Read(CRUD[ID], ABC):
    @staticmethod
    def get_model_from_collection(model_id: ID, database_file: str) -> dict:
        database_data = return_json_data(f'data/{database_file}.json')
        collection = database_data[database_file]
        if model_id not in (model['id'] for model in collection):
            raise ValueError(f'Item: id_{model_id} cannot be found!')

        return find_model_in_collection_with_id(model_id, collection)


class GetItem(Read):
    @classmethod
    def execute(cls, data: T):
        return Item.model_validate(cls.get_model_from_collection(data, 'items'))


class GetInventory(Read):
    @classmethod
    def execute(cls, data: T):
        return Inventory.model_validate(cls.get_model_from_collection(data, 'inventories'))


class GetPlayer(Read):

    @classmethod
    def execute(cls, data: T):
        return entity.Player.model_validate(cls.get_model_from_collection(data, 'players'))
