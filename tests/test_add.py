from src.main import add


def test_add1():
    assert add(10, 10) == 20
    assert add(-1, -3) == -4
