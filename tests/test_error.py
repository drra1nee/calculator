"""
Тесты ошибочных случаев
"""

import pytest # type: ignore

from src.modules.calculator import calculate

class TestErrorCases:
    def test_empty_expression(self):
        """Тест пустого выражения"""
        with pytest.raises(ValueError, match="Empty expression"):
            calculate("")
        with pytest.raises(ValueError, match="Empty expression"):
            calculate("   ")

    def test_mismatched_parentheses(self):
        """Тест несогласованных скобок"""
        with pytest.raises(ValueError, match="Mismatched brackets"):
            calculate("(2 + 3")
        with pytest.raises(ValueError, match="Mismatched brackets"):
            calculate("2 + 3)")

    def test_invalid_tokens(self):
        """Тест неверных токенов"""
        with pytest.raises(ValueError, match="Unknown token: &"):
            calculate("2 & 3")
        with pytest.raises(ValueError, match="Unknown token: a"):
            calculate("2 abc 3")

    def test_invalid_number_format(self):
        """Тест неверного формата чисел"""
        with pytest.raises(ValueError, match="could not convert string to float: '2.3.4'"):
            calculate("2.3.4 + 5")

    def test_not_enough_operands(self):
        """Тест недостатка операндов"""
        with pytest.raises(ValueError, match="There are not enough operands for a binary operator"):
            calculate("2 +")
        with pytest.raises(ValueError, match="There are not enough operands for a unary operator"):
            calculate("-")

    def test_not_integer_number(self):
        """Тест операций // и % на нецелых числах"""
        with pytest.raises(ValueError, match="5.0 is not an integer"):
            calculate("5.0 % 2")

    def test_invalid_operator_sequence(self):
        """Тест двух и более подряд операторов"""
        with pytest.raises(ValueError, match="Invalid operator sequence"):
            calculate("5 -+- 2")

    def test_missing_operation(self):
        """Тест пропуска оператора между скобкой и числом/другой скобкой"""
        with pytest.raises(ValueError, match="Missing operator"):
            calculate("(4-2)3")
        with pytest.raises(ValueError, match="Missing operator"):
            calculate("(4-2)(3+1)")

    def test_division_by_zero(self):
        """Тест деления на ноль"""
        with pytest.raises(ValueError, match="Division by zero"):
            calculate("5 / 0")
        with pytest.raises(ValueError, match="Division by zero"):
            calculate("10 // 0")
        with pytest.raises(ValueError, match="Division by zero"):
            calculate("10 % 0")
