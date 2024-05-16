from abc import ABC, abstractmethod

from pydantic import BaseModel

from custom_types import ID
from database.abc import CRUD, T
from datum.inventory import Inventory
from datum.items import Item
from generics.file_ops import return_json_data


class Read(CRUD[ID], ABC):
    @staticmethod
    def get_from_collection_using(id_: ID, collection: list[dict]):
        return [model for model in collection if model['id'] == id_][0]


class GetItem(Read):
    @classmethod
    def execute(cls, data: T):
        json_data = return_json_data('data/items.json')
        collection = json_data['items']
        if data not in (model['id'] for model in collection):
            raise ValueError(f'Item: id_{data} cannot be found!')
        return Item.model_validate(cls.get_from_collection_using(data, collection))


class GetInventory(Read):
    @classmethod
    def execute(cls, data: T):
        json_data = return_json_data('data/inventories.json')
        collection = json_data['inventories']
        if data not in (model['id'] for model in collection):
            raise ValueError(f'Inventory: id_{data} cannot be found!')
        return Inventory.model_validate(cls.get_from_collection_using(data, collection))
