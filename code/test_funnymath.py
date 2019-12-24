import pytest
from functools import reduce


@pytest.mark.parametrize("base, expected", [
    (10, [3, 9]),
    (3, [2]),
    (9, [2, 4, 8]),
    (26, [5, 25]),
    (30, [29])
])
def test_simple(base, expected):
    assert solution(base) == expected


def solution(base):
    arr = []
    for i in range(2, base):
        if (base - 1) % i == 0:
            arr.append(i)
    return arr


def change_base_10_to_number(number, base):
    """
    10진법의 숫자를 n 진법으로 바꾼후 각각의 값을 더한다.
    """
    result = 0
    while number > 0:
        result += (number % base)
        number //= base

    return result


if __name__ == "__main__":
    solution(input)
