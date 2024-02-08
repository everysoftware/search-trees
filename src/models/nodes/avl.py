from __future__ import annotations

from dataclasses import dataclass

from src.models.nodes.base import NodeKey, NodeValue
from src.models.nodes.bst import BSTNode


@dataclass
class AVLNode(BSTNode[NodeKey, NodeValue]):
    left: AVLNode[NodeKey, NodeValue] | None = None
    right: AVLNode[NodeKey, NodeValue] | None = None
    parent: AVLNode[NodeKey, NodeValue] | None = None

    def __hash__(self):
        return hash((self.key, id(self)))
