from __future__ import annotations

from dataclasses import dataclass

from src.models.nodes.avl import AVLNode


@dataclass
class RopeNode(AVLNode[int, str]):
    left: RopeNode | None = None
    right: RopeNode | None = None
    parent: RopeNode | None = None

    def __hash__(self):
        return hash((self.key, id(self)))
