"""
Балансировка АВЛ-дерева.
"""

from src.models.attributes import Height
from src.models.nodes import AVLNode


def get_balance(node: AVLNode | None) -> int:
    """
    Коэффициент сбалансированности k:
    если k <= 1, то всё хорошо,
    если k = -2, значит, слева высота больше, поэтому балансируем дерево вправо,
    если k = 2, значит, больше высота справа, и нужно балансировать дерево влево.
    """
    if node is None:
        return 0

    return Height.value(node.right) - Height.value(node.left)


def right_rotate(node: AVLNode) -> AVLNode:
    # node = 4
    node_parent = node.parent  # ...
    a = node.left  # 2
    b = a.right  # 3
    a.right = node
    node.parent = a
    node.left = b

    if b is not None:
        b.parent = node

    a.parent = node_parent

    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a

    node.update()

    if a is not None:
        a.update()

    return a


def left_rotate(node: AVLNode) -> AVLNode:
    # node = 4
    node_parent = node.parent  # ...
    a = node.right  # 2
    b = a.left  # 3
    a.left = node
    node.parent = a
    node.right = b

    if b is not None:
        b.parent = node

    a.parent = node_parent

    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a

    node.update()

    if a is not None:
        a.update()

    return a


def balance(node: AVLNode | None) -> AVLNode | None:
    if node is None:
        return

    node.update()
    k = get_balance(node)
    possible_new_root = node

    if k == -2:
        if get_balance(node.left) == 1:
            left_rotate(node.left)
        possible_new_root = right_rotate(node)
    elif k == 2:
        if get_balance(node.right) == -1:
            right_rotate(node.right)
        possible_new_root = left_rotate(node)

    return possible_new_root
