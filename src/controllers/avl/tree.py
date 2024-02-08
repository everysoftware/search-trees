"""
АВЛ-дерево
"""

from __future__ import annotations

from src.controllers.avl.operations import (
    avl_insert,
    avl_delete,
    avl_split,
    avl_merge,
    check_balance,
)
from src.controllers.bst.tree import BST
from src.models.nodes import AVLNode, NodeKey, NodeValue


class AVLTree(BST[NodeKey, NodeValue]):
    node_type = AVLNode
    root: AVLNode | None = None

    def insert(self, key: NodeKey, value: NodeValue = None) -> AVLNode:
        """Вставка элемента в дерево."""
        self.root = avl_insert(self.root, key, value, node_type=self.node_type)
        return self.root

    def delete(self, key: NodeKey) -> AVLNode | None:
        """Удаление элемента из дерева."""
        self.root = avl_delete(self.root, key)
        return self.root

    def split(self, key: NodeKey) -> tuple[AVLTree, AVLTree]:
        """Разделение дерева на два по ключу."""
        left, right = avl_split(self.root, key)
        return self.__class__(root=left), self.__class__(root=right)

    def merge(self, rhs: AVLTree) -> AVLTree:
        """Слияние двух деревьев."""
        self.root = avl_merge(self.root, rhs.root)
        return self

    def check_correctness(self) -> AVLTree:
        """Проверка корректности дерева."""
        super().check_correctness()
        check_balance(self)

        return self
