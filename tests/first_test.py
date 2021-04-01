from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_error(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_sum_calculate_correctly(self):
        assert self.calc.adding(self, 5, 6) == 11

    def test_divide_calculate_correctly(self):
        assert self.calc.division(10, 2) == 5

    def test_minus_calculate_correctly(self):
        assert self.calc.subtraction(8, 3) == 5