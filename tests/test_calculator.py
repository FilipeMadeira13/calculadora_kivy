import pytest

from src.main import CalculatorLayout


class FakeDisplay:
    def __init__(self):
        self.text = "0"


@pytest.fixture
def calc():
    c = CalculatorLayout()
    c.calc_display = FakeDisplay()
    return c


def press(calc, seq):
    """Simula pressionar teclas na calculadora"""
    for char in seq:
        if char.isdigit():
            calc.process_input(char)
        elif char in "+-*/":
            calc.process_operator(char)
        elif char == ".":
            calc.process_dot()
        elif char == "%":
            calc.process_percent()
        elif char in "()":
            calc.process_parenthesis(char)
        elif char == "C":
            calc.clear_display()
        elif char == "=":
            calc.calculate()
    return calc.calc_display.text


def test_basics(calc):
    assert press(calc, "2+3=") == "5"
    assert press(calc, "9-4=") == "5"
    assert press(calc, "7*8=") == "56"
    assert press(calc, "8/2=") == "4"
    assert press(calc, "8/3=") == "2.6666666666666665"


def test_decimals(calc):
    assert press(calc, "0.5+0.5=") == "1"
    assert press(calc, "3.5+2.5=") == "6"
    assert press(calc, "6.=") == "6"  # comportamento de calculadora real


def test_parentheses(calc):
    assert press(calc, "(2+3)*4=") == "20"
    assert press(calc, "2*(3+4)=") == "14"
    assert press(calc, "(5+5)/(2+3)=") == "2"


def test_percent(calc):
    assert press(calc, "50%=") == "0.5"
    assert press(calc, "200+10%=") == "200.1"
    assert press(calc, "200*10%=") == "20"


def test_clear(calc):
    assert press(calc, "6+6=") == "12"
    assert press(calc, "C") == "0"
    assert press(calc, "+6=") == "6"


def test_invalid(calc):
    assert press(calc, "(2+3=") == "ERROR"
