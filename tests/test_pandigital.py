import pytest
from project_euler.pandigital import pandigital, is_pandigital


@pytest.fixture
def known_pandigital():
    return [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413,
            2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231,
            4312, 4321]


@pytest.fixture
def known_not_pandigital(known_pandigital):
    r = range(known_pandigital[-1])
    return [x for x in r if x not in known_pandigital]


def test_pandigital(known_pandigital):
    assert list(pandigital(len(known_pandigital), chars='1234')) == [
        str(x) for x in known_pandigital]


def test_is_pandigital(known_pandigital, known_not_pandigital):
    assert all(is_pandigital(x, chars='1234') for x in known_pandigital)
    assert not any(is_pandigital(x, chars='1234')
                   for x in known_not_pandigital)
