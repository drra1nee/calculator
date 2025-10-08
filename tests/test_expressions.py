"""
Тесты выражений
"""

from src.modules.calculator import calculate

class TestExpressions:
    def test_expression_0(self):
        assert calculate("(-5) % 3 + (-5) // 3") == -1

    def test_expression_1(self):
        assert calculate("2 + 3 * 4 - 6 / 2") == 11

    def test_expression_2(self):
        assert calculate("(2 + 3) * (4 - 1)") == 15

    def test_expression_3(self):
        assert calculate("10 // 3 + 5 % 2") == 4

    def test_expression_4(self):
        assert calculate("(2 + 3) ** (4 - 1)") == 125

    def test_expression_5(self):
        assert calculate("3 + (-5) * 2") == -7

    def test_expression_6(self):
        assert calculate("(2 * (3 + (4 - 1)))") == 12
