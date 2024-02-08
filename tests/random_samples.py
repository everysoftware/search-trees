import random
import string
from typing import TypeVar

from src.controllers.avl.tree import AVLTree
from src.controllers.avl_segment_tree import AVLSegmentTree
from src.controllers.bst import BST
from src.controllers.rope import Rope

T = TypeVar("T", bound=BST)


def generate_bst(size: int, tree_type: type[T] = BST) -> T:
    keys = [random.randint(1, 100) for _ in range(size)]

    return tree_type(keys=keys).check_correctness()


key_number = random.randint(10, 20)
tree_number = 5

keys_samples = [
    [random.randint(1, 100) for _ in range(key_number)] for _ in range(tree_number)
]


def get_random_bst_samples() -> list[BST]:
    return [generate_bst(key_number) for _ in range(tree_number)]


def get_random_avl_samples() -> list[AVLTree]:
    return [generate_bst(key_number, AVLTree) for _ in range(tree_number)]


def get_random_avl_st_samples() -> list[AVLSegmentTree]:
    return [generate_bst(key_number, AVLSegmentTree) for _ in range(tree_number)]


def get_random_rope_samples() -> list[Rope]:
    return [Rope("".join(random.choices(string.ascii_lowercase, k=key_number))) for _ in range(tree_number)]
