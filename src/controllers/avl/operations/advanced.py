"""
Продвинутые операции с АВЛ-деревом
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.controllers.avl.operations.basic import avl_delete, balance
from src.controllers.bst.operations import clear_parent, bst_max, bst_merge_with_root
from src.models.attributes import Height

if TYPE_CHECKING:
    from src.models.nodes import AVLNode, NodeKey


def avl_merge_with_root(
    left: AVLNode | None, right: AVLNode | None, root: AVLNode | None
) -> AVLNode | None:
    """Склейка при известной идеально подходящей вершине root: (node1 < root <= node2)."""
    if root is None:
        return None

    h1 = Height.value(left)
    h2 = Height.value(right)

    if abs(h1 - h2) <= 1:
        bst_merge_with_root(left, right, root)

        return balance(root)
    elif h1 > h2:
        new_root = avl_merge_with_root(left.right, right, root)
        left.right = new_root
        new_root.parent = left

        return balance(left)
    else:
        new_root = avl_merge_with_root(left, right.left, root)
        right.left = new_root
        new_root.parent = right

        return balance(right)


def avl_merge(left: AVLNode | None, right: AVLNode | None) -> AVLNode | None:
    """Слияние двух АВЛ-деревьев."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    left = avl_delete(left, new_root.key)
    clear_parent(new_root)

    return avl_merge_with_root(left, right, new_root)


def avl_split(
    node: AVLNode | None, key: NodeKey
) -> tuple[AVLNode | None, AVLNode | None]:
    """Разделение АВЛ-дерева по ключу."""
    if node is None:
        return None, None

    if node.key > key:
        left, temp = avl_split(node.left, key)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = avl_split(node.right, key)
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right
