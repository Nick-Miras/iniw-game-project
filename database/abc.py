from abc import ABC, abstractmethod

from pydantic import BaseModel


class CRUD(ABC):
    @classmethod
    @abstractmethod
    def execute(cls, data: BaseModel):
        ...
