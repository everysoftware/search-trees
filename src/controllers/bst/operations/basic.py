"""
Базовые функции для работы с BST.
"""

from typing import TypeVar

from src.models.nodes import BSTNode, NodeKey, NodeValue

T = TypeVar("T", bound=BSTNode)


def bst_insert(
    node: BSTNode | None,
    key: NodeKey,
    value: NodeValue = None,
    parent: BSTNode | None = None,
    node_type: type[T] = BSTNode,
) -> T:
    if node is None:
        return node_type(key, value, parent=parent)

    if node.key > key:
        node.left = bst_insert(node.left, key, value, node, node_type)
    elif node.key < key:
        node.right = bst_insert(node.right, key, value, node, node_type)

    if node is not None:
        node.update()

    return node


def bst_find(node: BSTNode | None, key: NodeKey) -> BSTNode | None:
    if node is None:
        return None

    if node.key == key:
        return node
    elif node.key > key:
        return bst_find(node.left, key)
    else:
        return bst_find(node.right, key)


def bst_max(node: BSTNode | None) -> BSTNode | None:
    if node is None:
        return None

    while node.right:
        node = node.right

    return node


def bst_min(node: BSTNode | None) -> BSTNode | None:
    if node is None:
        return None

    while node.left:
        node = node.left

    return node


def bst_next(node: BSTNode) -> BSTNode | None:
    if node.right is not None:
        return bst_min(node.right)

    # Идем наверх, пока идём направо.
    parent = node.parent
    while parent is not None and parent.right is node:
        node = parent
        parent = parent.parent

    return parent


def bst_prev(node: BSTNode) -> BSTNode | None:
    if node.left is not None:
        return bst_max(node.left)

    # Идем наверх, пока идём налево.
    parent = node.parent
    while parent is not None and parent.left is node:
        node = parent
        parent = parent.parent

    return parent


def bst_delete_child(node: BSTNode) -> BSTNode | None:
    child = node.right if node.left is None else node.left

    if child is not None:
        child.parent = node.parent

    if node.parent is not None:
        if node.parent.left is node:
            node.parent.left = child
        else:
            node.parent.right = child

    return child


def bst_delete(node: BSTNode | None, key: NodeKey) -> BSTNode | None:
    if node is None:
        return None

    if node.key == key:
        if node.left is None or node.right is None:
            node = bst_delete_child(node)
        else:
            swap_node = bst_prev(node)

            node.key = swap_node.key
            node.value = swap_node.value
            node.left = bst_delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = bst_delete(node.left, key)
    else:
        node.right = bst_delete(node.right, key)

    if node is not None:
        node.update()

    return node
