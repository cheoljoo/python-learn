# content of test_expectation.py
import pytest

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3, 4])
def test_foo(x, y):
    #pass
    assert x*y == x*2

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected