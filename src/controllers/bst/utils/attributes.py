from typing import TypeVar

from src.controllers.bst.operations import traverse
from src.models.nodes import BSTNode

T = TypeVar("T")


def update_attributes_recursive(node: BSTNode) -> None:
    for node in traverse(node, style="postorder", key=lambda _node: _node):
        node.update()
