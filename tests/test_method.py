import pytest
from methods import ReverseWithReversed

# array A, array B, expected result
test_cases = (
    [[2, 1, -1, -2, -3], [-10, 10], 7],
    [[3, 2, 1, -1, -2], [-10, 10], 7],
    [[3, 2, 1, -1, -2], [0, 10], 1],
    [[-2, -3, -10], [-10, -3, -2], 0],
    [[0], [0], 0],
    [[10], [10], 0],
    [[10], [-10], 20],
    [[10, 5, 0], [15, 20, 25], 5],
    [[5, 4, 3], [6, 7, 8], 1],
    [[-6, -7, -8], [-5, -4, -3], 1],
)


class TestApproaches:
    @pytest.mark.parametrize(
        "array_a, array_b, expected_result", test_cases,
    )
    def test_reversed(self, array_a: list, array_b: list, expected_result: int) -> None:
        result = ReverseWithReversed.find_difference(array_a, array_b)
        assert result == expected_result
