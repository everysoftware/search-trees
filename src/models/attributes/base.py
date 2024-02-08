from __future__ import annotations

from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.nodes import BinaryNode

T = TypeVar("T")


@dataclass
class Attribute(ABC, Generic[T]):
    empty_value: T = None

    @classmethod
    @abstractmethod
    def value(cls, node: BinaryNode | None) -> T:
        pass

    @classmethod
    @abstractmethod
    def updated(cls, node: BinaryNode) -> T:
        pass

    @classmethod
    @abstractmethod
    def update(cls, node: BinaryNode | None) -> None:
        pass

    @classmethod
    def check(cls, node: BinaryNode | None) -> bool:
        return node is None or cls.value(node) == cls.updated(node)

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        return str(self)
