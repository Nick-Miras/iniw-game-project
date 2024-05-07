import json
from abc import ABC
from json import JSONDecodeError

from pydantic import BaseModel

from database.abc import CRUD
from datum.inventory import Inventory
from generics.file_ops import return_json_data


class Create(CRUD, ABC):
    pass


class AddInventory(Create):

    @classmethod
    def execute(cls, data: BaseModel):
        """ Adds Inventory To Database. Only Adds. Raises Error If Inventory Already Exists
        Args:
            data:`Inventory`
        """
        if isinstance(data, Inventory) is False:
            raise ValueError(f"Argument {type(data)} is not of type {type(BaseModel)}")

        file_path = 'data/inventories.json'
        database_data = return_json_data(file_path)

        if str(data.id) in list(database_data.keys()) is True:
            raise ValueError('Inventory ID Already Exists. Cannot Add Existing Model.')
        database_data.update({data.id: data.model_dump()})

        with open(file_path, 'w') as f:
            json.dump(database_data, f)
