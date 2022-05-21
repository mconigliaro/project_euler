import pytest
from project_euler.fibonacci import fibonacci, fibonaccis


@pytest.fixture
def known_fibonaccis():
    return [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
        10946,
        17711,
        28657,
        46368,
        75025,
        121393,
        196418,
        317811,
        514229,
        832040,
        1346269,
        2178309,
        3524578,
        5702887,
        9227465,
        14930352,
        24157817,
        39088169,
    ]


def test_fibonacci(known_fibonaccis):
    for i, f in enumerate(known_fibonaccis):
        assert fibonacci(i)[0] == known_fibonaccis[i]


def test_fibonaccis(known_fibonaccis):
    assert list(fibonaccis(num=len(known_fibonaccis))) == known_fibonaccis


def test_fibonaccis_with_end(known_fibonaccis):
    assert list(fibonaccis(end=100)) == known_fibonaccis[:12]
