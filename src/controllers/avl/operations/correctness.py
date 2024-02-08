from __future__ import annotations

from typing import TYPE_CHECKING

from src.controllers.avl.exceptions import ImbalancedException
from src.controllers.avl.operations import get_balance

if TYPE_CHECKING:
    from src.controllers.avl.tree import AVLTree


def check_balance(tree: AVLTree) -> None:
    """Проверка сбалансированности дерева. Бросает исключение, если дерево не сбалансировано."""
    for node in tree.dfs(key=lambda _node: _node):
        balance = get_balance(node)
        if abs(balance) > 1:
            raise ImbalancedException(node, balance)
