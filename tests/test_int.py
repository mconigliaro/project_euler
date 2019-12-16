from project_euler.int import int_digits


def test_int_digits():
    assert list(int_digits(0)) == [0]
    assert list(int_digits(12345678900)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
    assert list(int_digits(-123)) == [1, 2, 3]
    assert list(int_digits(1234567890, num=-3)) == [0, 9, 8]
