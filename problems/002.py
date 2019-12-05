from project_euler.fibonacci import fibonacci


def test_002():
    answer = sum([x for x in fibonacci(up_to=4000000) if x % 2 == 0])
    assert answer == 4613732
