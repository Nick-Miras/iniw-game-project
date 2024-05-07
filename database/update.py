import json
from abc import ABC
from json import JSONDecodeError

from pydantic import BaseModel

from database.abc import CRUD
from datum.inventory import Inventory
from generics.file_ops import return_json_data


class Create(CRUD, ABC):
    @staticmethod
    def update_json_file_with(model: BaseModel, json_file_path: str, add_only: bool):
        data = return_json_data(json_file_path)
        if add_only is True and str(model.id) in list(model.keys()) is True:
            raise ValueError('Inventory ID Already Exists. Cannot Add Existing Model.')
        data.update({model.id: model.model_dump()})

        with open(json_file_path, 'w') as f:
            json.dump(data, f)


class UpdateInventory(Create):
    @classmethod
    def execute(cls, data: BaseModel):
        """ Adds Inventory To Database. Can Update Existing Inventories And Add If It Doesn't Exist
        Args:
            data:`Inventory`
        """
        if isinstance(data, Inventory) is False:
            raise ValueError(f"Argument {type(data)} is not of type {type(BaseModel)}")
        cls.update_json_file_with(data, 'data/inventories.json', False)