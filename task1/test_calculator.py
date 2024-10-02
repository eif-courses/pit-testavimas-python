import pytest

from calculator import Calculator

def test_add(calculator):
    assert calculator.add(3, 2) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3

def test_multiply(calculator):
    if calculator.subtract(2,1):
        assert calculator.multiply(3, 2) == 6

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)

@pytest.fixture
def calculator():
    return Calculator()