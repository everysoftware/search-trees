from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.models.attributes import Attribute

if TYPE_CHECKING:
    from src.models.nodes import SummingNode


@dataclass
class Summa(Attribute[int]):
    empty_value: int = 0

    @classmethod
    def value(cls, node: SummingNode | None) -> int:
        if node is None:
            return cls.empty_value

        return node.summa

    @classmethod
    def updated(cls, node: SummingNode) -> int:
        return node.key + cls.value(node.left) + cls.value(node.right)

    @classmethod
    def update(cls, node: SummingNode | None) -> None:
        if node is None:
            return

        node.summa = cls.updated(node)
