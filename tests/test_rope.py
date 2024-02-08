import pytest

from random_samples import get_random_rope_samples
from src.controllers.rope import Rope
from src.controllers.rope.operations import naive_rope


@pytest.mark.run(order=6)
class TestRope:
    @pytest.mark.parametrize("rope", get_random_rope_samples())
    def test_move_substr(self, rope: Rope):
        s = rope.to_string()

        for i in range(len(s)):
            for j in range(i, len(s)):
                for k in range(j, len(s)):
                    result = rope.move_substr(i, j, k).to_string()
                    expected = naive_rope(s, i, j, k)

                    assert result == expected, (i, j, k)
                    s = result
