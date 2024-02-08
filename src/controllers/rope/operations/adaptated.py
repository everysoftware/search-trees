from src.controllers.avl.operations import avl_merge_with_root, balance
from src.controllers.bst.operations import (
    bst_prev,
    bst_delete_child,
    clear_parent,
    bst_max,
)
from src.models.attributes import Size
from src.models.nodes import RopeNode

"""
Во всех функциях ниже используется неявный ключ.

Неявный ключ - это размер поддерева, корнем которого является узел. То есть, если узел имеет неявный ключ x, то
все символы, которые находятся в левом поддереве этого узла, имеют неявные ключи от 1 до x - 1, а все символы,
которые находятся в правом поддереве этого узла, имеют неявные ключи от x + 1 до x + размер_правого_поддерева.
"""


def rope_delete(node: RopeNode | None, i: int) -> RopeNode | None:
    """Удалить s[i]."""
    stack = []
    current = node

    while current is not None:
        left_size = Size.value(current.left)

        # left_size + 1 - неявный ключ текущего узла (индекс символа в строке).
        if left_size + 1 == i:
            if current.left is None or current.right is None:
                current = bst_delete_child(current)
            else:
                swap_node = bst_prev(current)
                current.key = swap_node.key
                current.value = swap_node.value
                current.left = None
                current = swap_node
        elif left_size + 1 > i:
            stack.append(current)
            current = current.left
        else:
            stack.append(current)
            current = current.right
            i -= left_size + 1

    # Балансируем все узлы, которые были изменены.
    while stack:
        current = stack.pop()
        current = balance(current)

    return current


def rope_merge(left: RopeNode | None, right: RopeNode | None) -> RopeNode | None:
    """Склеить две строки."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    left = rope_delete(left, Size.value(left))
    clear_parent(new_root)

    return avl_merge_with_root(left, right, new_root)


def rope_split(
    node: RopeNode | None, i: int
) -> tuple[RopeNode | None, RopeNode | None]:
    """Разделить строку на две подстроки: s[:i], s[i:]."""
    if node is None:
        return None, None

    left_size = Size.value(node.left)

    if left_size + 1 > i:
        left, temp = rope_split(node.left, i)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = rope_split(node.right, i - (left_size + 1))
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right
