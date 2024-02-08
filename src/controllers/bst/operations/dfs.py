"""
Обход дерева в глубину (DFS).
"""

from typing import Callable, TypeVar, Literal

from src.controllers.bst.exceptions.dfs import TraverseStyleException
from src.models.nodes import BSTNode

KeyResult = TypeVar("KeyResult")


def dfs_preorder_iterative(
    node: BSTNode | None, key: Callable[[BSTNode], KeyResult] = lambda node: node.key
) -> list[KeyResult]:
    if node is None:
        return []

    st = [node]
    result = []

    while st:
        node = st.pop()

        result.append(key(node))

        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)

    return result


def dfs_inorder_iterative(
    node: BSTNode | None, key: Callable[[BSTNode], KeyResult] = lambda node: node.key
) -> list[KeyResult]:
    st = []
    result = []

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result.append(key(node))
            node = node.right

    return result


def dfs_postorder_iterative(
    node: BSTNode | None, key: Callable[[BSTNode], KeyResult] = lambda node: node.key
) -> list[KeyResult]:
    if node is None:
        return []

    st = [node]
    result = []

    while st:
        node = st.pop()
        result.append(key(node))
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)

    result.reverse()

    return result


def traverse(
    node: BSTNode | None,
    style: Literal["inorder", "preorder", "postorder"] = "inorder",
    key: Callable[[BSTNode], KeyResult] = lambda node: node.key,
) -> list[KeyResult]:
    match style:
        case "inorder":
            return dfs_inorder_iterative(node, key)
        case "preorder":
            return dfs_preorder_iterative(node, key)
        case "postorder":
            return dfs_postorder_iterative(node, key)
        case _:
            raise TraverseStyleException()
