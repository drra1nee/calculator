"""
Модуль для вычисления выражений в обратной польской нотации
"""

from calculator.src.modules.operators import is_operator, is_unary_token, is_integer_division_operator, is_modul_operator


def is_integer(number):
    """Проверяет, является ли число целым и возвращает его как int"""
    if (number is int(number)
            and number % 1 == 0
            and type(number) is int):
        return int(number)
    else:
        raise ValueError(f"{number} is not an integer")


def evaluate_rpn(rpn_tokens):
    """Вычисляет значение выражения в RPN нотации"""
    stack = []

    for token in rpn_tokens:
        # Обработка чисел
        if token.replace('.', '').isdigit():
            if '.' in token:
                number = float(token)
            else:
                number = int(token)
            stack.append(number)
            continue

        # Обработка унарных операторов
        if is_unary_token(token):
            if not stack:
                raise ValueError("There are not enough operands for the unary operator")

            operand = stack.pop()

            if token == '$':
                result = operand
            elif token == '~':
                result = -operand
            else:
                raise ValueError(f"Unknown unary operator: {token}")

            stack.append(result)
            continue

        # Обработка бинарных операторов
        if is_operator(token):
            if len(stack) < 2:
                raise ValueError("There are not enough operands for a binary operator")

            right_operand = stack.pop()
            left_operand = stack.pop()

            # Оператор целочисленного деления (только для целых чисел)
            if is_integer_division_operator(token):
                # Проверяем оба операнда
                left_int = is_integer(left_operand)
                right_int = is_integer(right_operand)

                if right_int == 0:
                    raise ValueError("Division by zero")

                result = left_int // right_int

            # Оператор остатка от деления (только для целых чисел)
            elif is_modul_operator(token):
                # Проверяем оба операнда
                left_int = is_integer(left_operand)
                right_int = is_integer(right_operand)

                if right_int == 0:
                    raise ValueError("Division by zero")

                result = left_int % right_int

            # Остальные операторы
            elif token == '+':
                result = left_operand + right_operand
            elif token == '-':
                result = left_operand - right_operand
            elif token == '*':
                result = left_operand * right_operand
            elif token == '/':
                if right_operand == 0:
                    raise ValueError("Division by zero")
                result = left_operand / right_operand
            elif token == '**':
                result = left_operand ** right_operand
            else:
                raise ValueError(f"Unknown operator: {token}")

            stack.append(result)
            continue

        raise ValueError(f"Unknown token: {token}")

    if len(stack) != 1:
        raise ValueError("Incorrect expression")

    return stack[0]
