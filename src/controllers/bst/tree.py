"""
Двоичное дерево поиска (BST)
"""

from __future__ import annotations

from typing import Sequence, Any, Callable, Literal

from src.controllers.base.tree import BinaryTree
from src.controllers.bst.operations import (
    bst_find,
    bst_insert,
    bst_delete,
    bst_max,
    bst_min,
    bst_next,
    bst_prev,
    bst_split,
    bst_merge,
    traverse,
    bst_present,
    KeyResult,
    check_for_cycles,
    check_parents,
    check_attributes,
    is_bst,
)
from src.controllers.bst.operations.advanced import bst_order_statistics
from src.controllers.bst.utils import update_attributes_recursive
from src.models.nodes import BSTNode, NodeKey, NodeValue, BinaryNode


class BST(BinaryTree[NodeKey, NodeValue]):
    node_type = BSTNode
    root: BSTNode | None = None

    def __init__(self, keys: Sequence[NodeKey] = (), root: BSTNode | None = None):
        super().__init__(root)

        for key in keys:
            self.insert(key)

    def empty(self) -> bool:
        """Проверка дерева на пустоту"""
        return self.root is None

    def insert(self, key: NodeKey, value: NodeValue = None) -> BSTNode:
        """Вставка узла в дерево по ключу и значению"""
        self.root = bst_insert(self.root, key, value, node_type=self.node_type)
        return self.root

    def find(self, key: NodeKey) -> BSTNode | None:
        """Поиск узла по ключу"""
        return bst_find(self.root, key)

    def contains(self, key: NodeKey) -> bool:
        """Проверка наличия узла в дереве по ключу"""
        return self.find(key) is not None

    def delete(self, key: NodeKey) -> BSTNode | None:
        """Удаление узла из дерева по ключу"""
        self.root = bst_delete(self.root, key)
        return self.root

    def max(self) -> BSTNode | None:
        """Поиск узла с максимальным ключом"""
        return bst_max(self.root)

    def min(self) -> BSTNode | None:
        """Поиск узла с минимальным ключом"""
        return bst_min(self.root)

    def next(self, key: NodeKey) -> BSTNode:
        """Поиск узла, следующего за данным"""
        return bst_next(self.find(key))

    def prev(self, key: NodeKey) -> BSTNode:
        """Поиск узла, предшествующего данному"""
        return bst_prev(self.find(key))

    def dfs(
        self,
        node: BSTNode | None = None,
        style: Literal["inorder", "preorder", "postorder"] = "inorder",
        key: Callable[[BinaryNode], KeyResult] = lambda _node: _node.key,
    ) -> list[KeyResult]:
        """Обход дерева в глубину (DFS)"""
        return traverse(self.root if node is None else node, style, key)

    def order_statistics(self, k: int) -> BSTNode | None:
        """Порядковая статистика"""
        return bst_order_statistics(self.root, k)

    def split(self, key: NodeKey) -> tuple[BST, BST]:
        """Разбиение дерева на 2 дерева: (left <= key < right). На месте."""
        left, right = bst_split(self.root, key)
        return self.__class__(root=left), self.__class__(root=right)

    def merge(self, rhs: BST) -> BST:
        """Слияние двух деревьев. На месте."""
        self.root = bst_merge(self.root, rhs.root)
        return self

    def check_correctness(self) -> BST:
        """Проверка корректности дерева"""
        check_for_cycles(self)
        check_parents(self)
        check_attributes(self)

        assert is_bst(self)

        return self

    def from_array(self, arr: Sequence[tuple[NodeKey, int, int]] | Any) -> BST:
        """Построение дерева из массива"""
        size = len(arr)
        tree = [self.node_type(0) for _ in range(size)]

        for i in range(size):
            key, left, right = arr[i]
            tree[i].key = key

            if left >= 0:
                tree[i].left = tree[left]
                tree[i].left.parent = tree[i]

            if right >= 0:
                tree[i].right = tree[right]
                tree[i].right.parent = tree[i]

        if tree:
            self.root = tree[0]
            update_attributes_recursive(self.root)

        return self

    def __str__(self) -> str:
        """Представление дерева в виде строки"""
        return bst_present(self)

    def __repr__(self) -> str:
        """Представление дерева"""
        return str(self)
