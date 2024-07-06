import pytest
from mainfile import add,multiply,divide


@pytest.mark.parametrize("a, b", [(1, 2), (2, 3), (3, 4), (4, 5)])
def test_add(a, b):
    assert add(a, b) == a + b

@pytest.mark.parametrize("a, b", [(1, 2), (2, 3), (3, 4), (4, 5)])
def test_multiply(a, b):
    assert multiply(a, b) == a * b

@pytest.mark.parametrize("a, b", [(1, 2), (2, 3), (3, 4), (4, 5)])
def test_divide(a, b):
    assert divide(a, b) == a / b




