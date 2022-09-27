from hello import add, multiply


def test_add():
    assert add(1, 2) == 3


def test_mutilply():
    assert multiply(1, 2) == 2
