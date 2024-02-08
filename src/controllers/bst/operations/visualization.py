"""
Визуализация дерева.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controllers.bst import BST

from src.controllers.bst.operations.dfs import traverse
from src.models.nodes import BSTNode


def bst_visualize(node: BSTNode, level: int = 0) -> str:
    if node is None:
        return ""

    left = bst_visualize(node.left, level + 1)
    node_str = " " * 4 * level + "-> " + str(node.key) + "\n"
    right = bst_visualize(node.right, level + 1)

    return left + node_str + right


def bst_present(tree: BST) -> str:
    result = f"{type(tree).__name__} ({tree.root})\n"
    result += "Rope nodes: "
    result += str(traverse(tree.root)) + "\n"
    result += bst_visualize(tree.root)

    return result
