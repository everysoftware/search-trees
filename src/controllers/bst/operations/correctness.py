from __future__ import annotations

from typing import TYPE_CHECKING

from src.controllers.bst.exceptions import (
    CycleException,
    ParentException,
    AttributeException,
)

if TYPE_CHECKING:
    from src.controllers.bst.tree import BST
    from src.models.nodes import BSTNode


def check_for_cycles_helper(node: BSTNode | None, visited: set[BSTNode]) -> None:
    if node is None:
        return

    if node in visited or node.parent is node:
        raise CycleException(node)

    visited.add(node)

    check_for_cycles_helper(node.left, visited)
    check_for_cycles_helper(node.right, visited)


def check_for_cycles(tree: BST) -> None:
    """Проверка наличия циклов в дереве."""
    check_for_cycles_helper(tree.root, set())


def check_parents(tree: BST) -> None:
    """Проверка родителей узлов."""
    for node in tree.dfs(key=lambda _node: _node):
        if node.left and node.left.parent is not node:
            raise ParentException("left", node)
        if node.right and node.right.parent is not node:
            raise ParentException("right", node)


def check_attributes(tree: BST) -> None:
    """Проверка атрибутов узлов."""
    if tree.empty():
        return

    for attribute in tree.root.attributes:
        for node in tree.dfs(key=lambda _node: _node):
            if not attribute.check(node):
                raise AttributeException(attribute, node)


def is_bst(tree: BST) -> bool:
    """
    Проверка, является ли дерево строгим BST. В строгом BST каждый узел должен быть больше всех узлов
    в его левом поддереве и меньше всех узлов в его правом поддереве.

    Основано на DFS In-Order обходе.
    """
    st = []
    prev_key = None

    node = tree.root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()

            if prev_key and node.key < prev_key:
                return False

            prev_key = node.key
            node = node.right

    return True


def is_general_bst(tree: BST) -> bool:
    """
    Проверка, является ли дерево общим BST. В общем BST каждый узел должен быть больше
    всех узлов его левого поддерева и меньше или равен всем узлам в его правом поддереве.

    Основано на DFS In-Order обходе.
    """
    st = []
    prev = None

    node = tree.root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()

            # В общем дереве поиска ключи узлов могут быть равны, но тогда равный узел должен быть справа.
            if prev and (
                node.key < prev.key or node.key == prev.key and node.left is prev
            ):
                return False

            prev = node
            node = node.right

    return True
