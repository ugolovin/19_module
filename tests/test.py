import pytest

from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.Calculator = Calculator

    def test_1_add_sucsess(self):
        assert self.Calculator.adding(self, 1, 1) == 2

    def test_2_add_err(self):
        assert self.Calculator.adding(self, 1, 1) != 3

    def test_3_mult(self):
        assert self.Calculator.multiply(self, 2, 3) == 6

    def test_4_sub(self):
        assert self.Calculator.subtraction(self, 1, 1) == 0

    def test_5_zero_div(self):
        with pytest.raises(ZeroDivisionError):
            self.Calculator.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')

