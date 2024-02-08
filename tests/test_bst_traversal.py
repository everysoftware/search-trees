import pytest

from prepared_samples import (
    expected_dfs_inorder,
    expected_dfs_postorder,
    expected_dfs_preorder,
)
from src.controllers.bst import BST
from src.models.nodes import NodeKey


@pytest.mark.run(order=1)
class TestTraversal:
    @pytest.mark.parametrize("bst, expected", expected_dfs_inorder)
    def test_dfs_inorder(self, bst: BST, expected: list[NodeKey]):
        assert bst.dfs() == expected

    @pytest.mark.parametrize("bst, expected", expected_dfs_preorder)
    def test_dfs_preorder(self, bst: BST, expected: list[NodeKey]):
        assert bst.dfs(style="preorder") == expected

    @pytest.mark.parametrize("bst, expected", expected_dfs_postorder)
    def test_dfs_postorder(self, bst: BST, expected: list[NodeKey]):
        assert bst.dfs(style="postorder") == expected
