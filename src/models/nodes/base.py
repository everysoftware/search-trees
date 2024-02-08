from __future__ import annotations

from dataclasses import dataclass
from types import NoneType
from typing import TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.attributes import Attribute

NodeKey = TypeVar("NodeKey", int, float, str, NoneType)
NodeValue = TypeVar("NodeValue", int, float, str, NoneType)


@dataclass
class BinaryNode(Generic[NodeKey, NodeValue]):
    key: NodeKey = None
    value: NodeValue = None
    left: BinaryNode[NodeKey, NodeValue] | None = None
    right: BinaryNode[NodeKey, NodeValue] | None = None
    parent: BinaryNode[NodeKey, NodeValue] | None = None

    @property
    def attributes(self) -> list[type[Attribute]]:
        return []

    def update(self):
        for attr in self.attributes:
            attr.update(self)

    def __str__(self):
        return f"{type(self).__name__}({self.key}, {self.value})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self):
        return hash((self.key, id(self)))
