from __future__ import annotations

from dataclasses import dataclass

from src.models.attributes import Attribute, Summa
from src.models.nodes.avl import AVLNode
from src.models.nodes.base import NodeValue


@dataclass
class SummingNode(AVLNode[int, None]):
    left: SummingNode | None = None
    right: SummingNode | None = None
    parent: SummingNode | None = None
    summa: NodeValue = 0

    @property
    def attributes(self) -> list[type[Attribute]]:
        return super().attributes + [Summa]

    def __hash__(self):
        return hash((self.key, id(self)))

    def __post_init__(self):
        self.summa = self.key
