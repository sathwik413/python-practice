import pytest
from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# dividing the code into different groups of tests. when run with + operator, test_positive and test_negative fails and test_zero passes. when run with * operator, all three tests passes.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


# after importing pytest for this part, test_str() expects a TypeError, if unvalid datatype is passed in square(). If a TypeError is raised, then test_str() passes.
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
