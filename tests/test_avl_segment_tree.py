import pytest

from random_samples import get_random_avl_st_samples
from src.controllers.avl_segment_tree import AVLSegmentTree


@pytest.mark.run(order=5)
class TestAVLSegmentTree:
    @pytest.mark.parametrize("st", get_random_avl_st_samples())
    def test_sum_between(self, st: AVLSegmentTree):
        keys = sorted(st.dfs())

        for i in range(len(keys)):
            for j in range(i, len(keys)):
                left = keys[i]
                right = keys[j]
                assert st.sum_between(left, right) == sum(keys[i: j + 1])
