"""
Модуль для преобразования инфиксной записи в обратную польскую нотацию
"""

from .operators import (is_operator, is_unary_operator, convert_to_unary, should_pop_operator,
                                              is_unary_token)
from .tokenizer import get_next_token


def validate_operator_sequence(previous_token, current_token):
    """Проверяет допустимость последовательности операторов"""
    if previous_token is None:
        return True

    # Запрещаем последовательности бинарный оператор + бинарный оператор
    if (is_operator(current_token) and is_operator(previous_token) and
            not is_unary_token(previous_token) and not is_unary_token(current_token)):
        return False

    return True

def infix_to_rpn(expression):
    """Преобразует инфиксное выражение в RPN"""
    output = []
    operator_stack = []
    previous_token = None
    expression = expression.replace(' ', '')

    while expression:
        token, expression = get_next_token(expression)
        if not token:
            break

        # Определяем, является ли оператор унарным
        is_unary = (is_unary_operator(token) and
                    (previous_token is None or
                     previous_token == '('))

        # Проверка на недопустимые комбинации операторов
        if not validate_operator_sequence(previous_token, token):
            raise ValueError("Invalid operator sequence")

        # Если нет знака между скобкой и числом
        if (token == '(' and previous_token is not None and
                previous_token.replace('.', '').isdigit()):
                raise ValueError("Missing operator")
        if token.replace('.', '').isdigit() and previous_token == ')':
            raise ValueError("Missing operator")

        # Если нет знака между скобкой и скобкой
        if token == '(' and previous_token == ')':
            raise ValueError("Missing operator")

        # Обработка чисел
        if token.replace('.', '').isdigit():
            output.append(token)
            previous_token = token
            continue

        # Обработка унарных операторов
        if is_unary:
            unary_token = convert_to_unary(token)  # + -> $, - -> ~
            operator_stack.append(unary_token)
            previous_token = unary_token
            continue

        # Обработка бинарных операторов
        if is_operator(token):
            while (operator_stack and
                   should_pop_operator(operator_stack[-1], token)):
                output.append(operator_stack.pop())

            operator_stack.append(token)
            previous_token = token
            continue

        # Обработка скобок
        if token == '(':
            operator_stack.append(token)
            previous_token = token
            continue

        if token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())

            if not operator_stack or operator_stack[-1] != '(':
                raise ValueError("Mismatched brackets")

            operator_stack.pop()  # Удаляем '('
            previous_token = token
            continue

        raise ValueError(f"Unknown token: {token}")

    # Выталкиваем оставшиеся операторы
    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched brackets")
        output.append(operator_stack.pop())

    return output
