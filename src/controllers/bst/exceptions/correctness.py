from typing import Literal

from src.models.attributes import Attribute
from src.models.nodes import BSTNode


class CycleException(ValueError):

    def __init__(self, node: BSTNode | None = None):
        super().__init__(f"Cycle detected at node: {node}")


class ParentException(ValueError):

    def __init__(self, child: Literal["left", "right"], node: BSTNode | None = None):
        super().__init__(
            f"Parent of {child} child is not equal to node at node: {node}"
        )


class AttributeException(ValueError):

    def __init__(self, attribute: type[Attribute], node: BSTNode | None = None):
        super().__init__(
            f"Invalid attribute: {attribute.__name__} = {attribute.value(node)} "
            f"(expected: {attribute.updated(node)}) at node: {node}"
        )
