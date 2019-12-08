import pytest
from project_euler.fibonacci import fibonacci


@pytest.fixture
def known_fibonacci():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
            1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
            9227465, 14930352, 24157817, 39088169]


def test_fibonacci(known_fibonacci):
    assert list(fibonacci(len(known_fibonacci))) == known_fibonacci


def test_fibonacci_with_end(known_fibonacci):
    assert list(fibonacci(end=100)) == known_fibonacci[:12]
