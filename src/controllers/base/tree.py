from __future__ import annotations

from typing import Generic

from src.models.nodes import BinaryNode, NodeKey, NodeValue


class BinaryTree(Generic[NodeKey, NodeValue]):
    node_type: type[BinaryNode[NodeKey, NodeValue]]
    root: BinaryNode[NodeKey, NodeValue] | None = None

    def __init__(self, root: BinaryNode[NodeKey, NodeValue] | None = None):
        self.root = root
