"""
Модуль для токенизации математических выражений
"""

import string

def is_digit(token):
    """Проверяет, является ли символ цифрой или точкой"""
    return token in string.digits + '.'

def get_next_token(expression):
    """Извлекает следующий токен из выражения"""
    expression=expression.lstrip()

    # Пустая строка
    if not expression:
        return ", "

    # Обработка оператора **
    if expression.startswith('**'):
        return '**', expression[2:]

    # Обработка оператора //
    if expression.startswith('//'):
        return '//', expression[2:]

    # Обработка чисел (многозначных и десятичных)
    if is_digit(expression[:1]):
        end_index = 0
        while end_index < len(expression) and is_digit(expression[end_index]):
            end_index += 1
        return expression[:end_index], expression[end_index:]

    # Обработка остальных операторов и скобок
    return expression[:1], expression[1:]
