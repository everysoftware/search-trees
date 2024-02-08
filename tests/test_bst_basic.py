import random

import pytest

from random_samples import keys_samples, get_random_bst_samples
from src.controllers.bst import BST
from src.models.nodes import NodeKey


@pytest.mark.run(order=2)
class TestBSTBasic:
    @pytest.mark.parametrize("keys", keys_samples)
    def test_insert(self, keys: list[NodeKey]):
        bst = BST()

        for key in keys:
            bst.insert(key)
            bst.check_correctness()

        assert bst.dfs() == sorted(set(keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_contains(self, bst: BST):
        for key in bst.dfs():
            assert bst.contains(key)

        assert not bst.contains(-1)

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_find(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            node = bst.find(key)
            assert node is not None
            assert node.key == key

        assert bst.find(-1) is None

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_min(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        min_key = min(keys)
        assert bst.min().key == min_key

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_max(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        max_key = max(keys)
        assert bst.max().key == max_key

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_next(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            if key == max(keys):
                assert bst.next(key) is None
            else:
                assert bst.next(key).key == min(filter(lambda x: x > key, keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_prev(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            if key == min(keys):
                assert bst.prev(key) is None
            else:
                assert bst.prev(key).key == max(filter(lambda x: x < key, keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_delete(self, bst: BST):
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            bst.delete(key)
            bst.check_correctness()

        assert bst.dfs() == []

    def test_empty(self):
        bst = BST()
        assert bst.empty()

        bst.insert(1)
        assert not bst.empty()

        bst.delete(1)
        assert bst.empty()
