"""
Различные продвинутые операции над BST.
"""

from src.controllers.bst.operations.basic import bst_max, bst_delete
from src.models.attributes import Size
from src.models.nodes import BSTNode, NodeKey


def bst_order_statistics(node: BSTNode | None, k: int) -> BSTNode | None:
    """Порядковая статистика в BST. Возвращает вершину с k-м по величине ключом."""
    if node is None:
        return

    left_size = Size.value(node.left)

    if k == left_size + 1:
        return node

    if k < left_size + 1:
        return bst_order_statistics(node.left, k)
    else:
        return bst_order_statistics(node.right, k - left_size - 1)


def bst_merge_with_root(
    left: BSTNode | None, right: BSTNode | None, root: BSTNode
) -> BSTNode:
    """Склейка при известной идеально подходящей вершине root: (node1 < root <= node2)."""
    root.left = left
    root.right = right

    if left is not None:
        left.parent = root

    if right is not None:
        right.parent = root

    root.update()

    return root


def bst_merge(left: BSTNode | None, right: BSTNode | None) -> BSTNode | None:
    """Слияние двух BST-деревьев."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    left = bst_delete(left, new_root.key)
    clear_parent(new_root)

    return bst_merge_with_root(left, right, new_root)


def clear_parent(*nodes: BSTNode) -> None:
    """Удаление родителя у вершин."""
    for node in nodes:
        if node is not None:
            node.parent = None


"""
Разбиение дерева на 2 дерева: (left <= key < right).

Принцип работы:
1. Если корень больше key, то он и всё его правое поддерево должно отправиться в дерево right.
   В левом же поддереве могут быть ключи как <= key, так и > key, поэтому мы продолжаем резать его рекурсивно.
   
   Левая часть разреза - это сразу первая часть нашего ответа (left), 
   а чтобы получить вторую часть (right) - мы сливаем правые части дерева и разреза.
2. Если корень меньше или равен key, то он и всё его левое поддерево должны отправиться в дерево left.
    В правом же поддереве могут быть как ключи <= key, так и > key, поэтому мы продолжаем резать его рекурсивно.
    
    Правая часть разреза - это сразу вторая часть нашего ответа (right),
    а чтобы получить первую часть (left) - мы сливаем левые части дерева и разреза.
"""


def bst_split(
    node: BSTNode | None, key: NodeKey
) -> tuple[BSTNode | None, BSTNode | None]:
    """
    Разбиение дерева на 2 дерева: (left <= key < right).

    Возвращает 2 дерева: (left, right), где left - это дерево,
    в котором все ключи меньше или равны key, а right - больше key.
    """
    if node is None:
        return None, None

    if node.key > key:
        left, temp = bst_split(node.left, key)
        clear_parent(temp, node.right)
        right = bst_merge_with_root(temp, node.right, node)
    else:
        temp, right = bst_split(node.right, key)
        clear_parent(node.left, temp)
        left = bst_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right
