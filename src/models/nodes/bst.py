from __future__ import annotations

from dataclasses import dataclass

from src.models.attributes import Size, Height, Attribute
from src.models.nodes.base import BinaryNode, NodeKey, NodeValue


@dataclass
class BSTNode(BinaryNode[NodeKey, NodeValue]):
    left: BSTNode[NodeKey, NodeValue] | None = None
    right: BSTNode[NodeKey, NodeValue] | None = None
    parent: BSTNode[NodeKey, NodeValue] | None = None
    size: int = 1
    height: int = 1

    @property
    def attributes(self) -> list[type[Attribute]]:
        return [Size, Height]

    def __hash__(self):
        return hash((self.key, id(self)))
