from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.attributes import Attribute

if TYPE_CHECKING:
    from src.models.nodes import BSTNode


@dataclass
class Size(Attribute[int]):
    empty_value: int = 0

    @classmethod
    def value(cls, node: BSTNode | None) -> int:
        if node is None:
            return cls.empty_value

        return node.size

    @classmethod
    def updated(cls, node: BSTNode) -> int:
        return 1 + cls.value(node.left) + cls.value(node.right)

    @classmethod
    def update(cls, node: BSTNode | None) -> None:
        if node is None:
            return

        node.size = cls.updated(node)
