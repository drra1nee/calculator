"""
Основной модуль калькулятора
"""

from .shunting_yard import infix_to_rpn
from .rpn_evaluator import evaluate_rpn


def calculate(expression: str):
    """Основная функция вычисления выражения"""
    if not expression.strip():
        raise ValueError("Empty expression")

    # Преобразуем в RPN
    rpn_tokens = infix_to_rpn(expression)

    # Вычисляем результат
    result = evaluate_rpn(rpn_tokens)

    return result
