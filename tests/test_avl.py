import random

import pytest

from random_samples import keys_samples, get_random_avl_samples
from src.controllers.avl import AVLTree
from src.models.nodes import NodeKey


@pytest.mark.run(order=4)
class TestAVL:
    @pytest.mark.parametrize("keys", keys_samples)
    def test_insert(self, keys: list[NodeKey]):
        avl = AVLTree()

        for key in keys:
            avl.insert(key)
            avl.check_correctness()

        assert avl.dfs() == sorted(set(keys))

    @pytest.mark.parametrize("avl", get_random_avl_samples())
    def test_delete(self, avl: AVLTree):
        keys = avl.dfs()
        random.shuffle(keys)

        for key in keys:
            avl.delete(key)
            avl.check_correctness()

        assert avl.dfs() == []

    def test_empty(self):
        avl = AVLTree()
        assert avl.empty()

        avl.insert(1)
        assert not avl.empty()

        avl.delete(1)
        assert avl.empty()

    @pytest.mark.parametrize("avl", get_random_avl_samples())
    def test_split(self, avl: AVLTree):
        keys = avl.dfs()
        key = random.choice(keys)

        left, right = avl.split(key)

        left.check_correctness()
        right.check_correctness()

        assert left.dfs() == sorted([k for k in keys if k <= key])
        assert right.dfs() == sorted([k for k in keys if k > key])

    @pytest.mark.parametrize("avl", get_random_avl_samples())
    def test_merge(self, avl: AVLTree):
        keys = avl.dfs()
        key = random.choice(keys)
        left, right = avl.split(key)

        merged = AVLTree.merge(left, right)

        merged.check_correctness()
        assert merged.dfs() == keys
