import pytest
from project_euler.fibonacci import fibonacci


@pytest.fixture
def expected():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
            1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
            9227465, 14930352, 24157817, 39088169]


def test_fibonacci(expected):
    assert list(fibonacci(len(expected))) == expected


def test_fibonacci_up_to(expected):
    assert list(fibonacci(up_to=100)) == expected[:12]
