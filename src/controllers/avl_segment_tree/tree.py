from src.controllers.avl import AVLTree
from src.controllers.avl_segment_tree.operations import sum_between
from src.models.nodes import SummingNode


class AVLSegmentTree(AVLTree[int, None]):
    node_type = SummingNode
    root: SummingNode | None = None

    def sum_between(self, lo: int, hi: int) -> int:
        """Сумма на отрезке от lo до hi включительно."""
        return sum_between(self, lo, hi)
