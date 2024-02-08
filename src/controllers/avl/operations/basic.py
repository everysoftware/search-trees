"""
Базовые операции для AVL дерева
"""

from typing import TypeVar

from src.controllers.avl.operations.balancing import balance
from src.controllers.bst.operations.basic import bst_delete_child, bst_prev
from src.models.nodes import AVLNode, NodeKey, NodeValue

T = TypeVar("T", bound=AVLNode)


def avl_insert(
    node: AVLNode | None,
    key: NodeKey,
    value: NodeValue = None,
    parent: AVLNode | None = None,
    node_type: type[T] = AVLNode,
) -> T:
    if node is None:
        return node_type(key, value, parent=parent)

    if node.key > key:
        node.left = avl_insert(node.left, key, value, node, node_type)
    elif node.key < key:
        node.right = avl_insert(node.right, key, value, node, node_type)

    return balance(node)


def avl_delete(node: AVLNode | None, key: NodeKey) -> AVLNode | None:
    if node is None:
        return None

    if node.key == key:
        if node.left is None or node.right is None:
            node = bst_delete_child(node)
        else:
            swap_node = bst_prev(node)

            node.key = swap_node.key
            node.value = swap_node.value
            node.left = avl_delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = avl_delete(node.left, key)
    else:
        node.right = avl_delete(node.right, key)

    return balance(node)
