from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controllers.avl_segment_tree import AVLSegmentTree
from src.models.attributes import Summa


def sum_between(tree: AVLSegmentTree, lo: int, hi: int) -> int:
    """Сумма на отрезке от lo до hi включительно."""
    left, temp = tree.split(lo - 1)
    middle, right = temp.split(hi)

    result = Summa.value(middle.root)

    temp = middle.merge(right)
    tree.root = left.merge(temp).root

    return result
