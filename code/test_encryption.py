import pytest
from functools import reduce

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 12),
    ([1, 3, 2, 1, 1, 3], 36),
    ([1000, 999, 998, 997, 996, 995], 986074810223904000)
])
def test_simple(nums, expected):
    assert solution(nums) == expected


def solution(numbers):
    ret = 1
    numbers.sort()
    numbers[0] += 1
    for i in numbers:
        ret *= i
    return ret


if __name__ == "__main__":
    solution(input)
