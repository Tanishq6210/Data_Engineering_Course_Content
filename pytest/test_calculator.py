import pytest

from Day_70_DevOps.math_project.calculator import ( add, subtract, multiply, divide, power, modulus )


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_power():
    assert power(2, 3) == 8


def test_modulus():
    assert modulus(10, 3) == 1


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)