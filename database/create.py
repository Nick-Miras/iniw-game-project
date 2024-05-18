import json
from abc import ABC
from typing import Generic

from pydantic import BaseModel

from database.abc import CRUD, T
from datum.entity import Player
from datum.inventory import Inventory
from datum.items import Item
from generics.file_ops import return_json_data


class Create(CRUD, ABC, Generic[T]):

    @staticmethod
    def add_model_to_database_file(data: BaseModel, file_name: str):
        database_data = return_json_data(f'data/{file_name}.json')
        data_dumped = data.model_dump()

        if file_name not in list(database_data.keys()):
            database_data.update({file_name: [data_dumped]})
        else:
            collection = database_data[file_name]
            if (data.id in (model['id'] for model in collection)) is True:
                raise ValueError('ID Already Exists. Cannot Add Existing Model.')
            else:
                collection.append(data_dumped)
                database_data.update({file_name: collection})

        with open(f'data/{file_name}.json', 'w') as f:
            json.dump(database_data, f)


class AddInventory(Create[Inventory]):
    @classmethod
    def execute(cls, data: T):
        """ Adds Inventory To Database. Only Adds. Raises Error If Inventory Already Exists
        Args:
            data:`Inventory`
        """
        if isinstance(data, Inventory) is False:
            raise ValueError(f"Argument {type(data)} is not an instance of {type(BaseModel)}.")
        cls.add_model_to_database_file(data, 'inventories')


class AddItem(Create[Item]):
    @classmethod
    def execute(cls, data: T):
        """ Adds Inventory To Database. Only Adds. Raises Error If Inventory Already Exists
        Args:
            data:`Item`
        """
        if isinstance(data, Item) is False:
            raise ValueError(f"Argument {type(data)} is not an instance of {type(BaseModel)}.")
        cls.add_model_to_database_file(data, 'items')


class AddPlayer(Create[Player]):
    @classmethod
    def execute(cls, data: T):
        if isinstance(data, Player) is False:
            raise ValueError(f"Argument {type(data)} is not an instance of {type(BaseModel)}.")
        cls.add_model_to_database_file(data, 'players')
