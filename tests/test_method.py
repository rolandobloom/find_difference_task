import methods
import pytest

approaches = methods.Approach.get_subclasses_names()
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
    [
        [4087, 3984, 3936, 3277, 2887, 2841, 2698, 2519, 2037, 2030],
        [2127, 2167, 2212, 2237, 2288, 2379, 2599, 2649, 2896, 2967],
        9,
    ],
)


class TestApproaches:
    @pytest.mark.parametrize(
        "approach, array_a, array_b, expected_result",
        list(([approach] + test_case) for test_case in test_cases for approach in approaches),
    )
    def test_approach(
        self, approach: str, array_a: list, array_b: list, expected_result: int
    ) -> None:
        approach_class = getattr(methods, approach)
        result = approach_class.find_difference(array_a, array_b)
        assert result == expected_result
