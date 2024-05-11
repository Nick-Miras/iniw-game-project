from abc import ABC, abstractmethod

from typing import Any, TypeVar, Generic

T = TypeVar('T')


class CRUD(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def execute(cls, data: T):
        ...
