from __future__ import annotations

from src.controllers.avl import AVLTree
from src.controllers.rope.operations import rope_build, rope_move_substr, rope_to_string
from src.models.nodes import RopeNode


class Rope(AVLTree[int, str]):
    node_type = RopeNode
    root: RopeNode | None = None

    def __init__(self, s: str):
        super().__init__((), rope_build(s))

    def move_substr(self, i: int, j: int, k: int) -> Rope:
        """
        Вырезает подстроку s[i:j + 1] и вставляет её после k-го символа оставшейся строки.
        """
        self.root = rope_move_substr(self.root, i, j, k)
        return self

    def to_string(self):
        """
        Возвращает строку.
        """
        return rope_to_string(self.root)
