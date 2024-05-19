import json
from abc import ABC
from json import JSONDecodeError
from typing import Generic

from pydantic import BaseModel

from database.abc import CRUD, T
from datum.entity import Player
from datum.inventory import Inventory
from generics.database import find_model_in_collection_with_id
from generics.file_ops import return_json_data


class Update(CRUD, ABC, Generic[T]):
    @staticmethod
    def update_json_file_with(data: BaseModel, json_file_path: str):
        database_data = return_json_data(f'data/{json_file_path}.json')
        collection = database_data[json_file_path]

        if (old_model := find_model_in_collection_with_id(data.id, collection)) is None:
            raise ValueError(f'Model: id_{data.id} cannot be found!')
        collection.remove(old_model)
        collection.append(data.model_dump())
        database_data.update({json_file_path: collection})

        with open(f'data/{json_file_path}.json', 'w') as f:
            json.dump(database_data, f)


class UpdateInventory(Update[Inventory]):
    @classmethod
    def execute(cls, data: T):
        """ Update Existing Inventories
        Args:
            data:`Inventory`
        """
        if isinstance(data, Inventory) is False:
            raise ValueError(f"Argument {type(data)} is not of type {type(BaseModel)}")
        cls.update_json_file_with(data, 'inventories')


class UpdatePlayer(Update[Player]):

    @classmethod
    def execute(cls, data: T):
        """ Update Existing PLayers
        Args:
            data:`Player`
        """
        if isinstance(data, Player) is False:
            raise ValueError(f"Argument {type(data)} is not of type {type(BaseModel)}")
        cls.update_json_file_with(data, 'players')
