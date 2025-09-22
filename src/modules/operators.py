"""
Модуль для работы с операторами и их приоритетами
"""

# Приоритеты операторов
OPERATOR_PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '//': 2,
    '%': 2,
    '**': 3,
    '~': 4,
    '$': 4,
}

def is_operator(token):
    """Проверяет, является ли токен оператором"""
    return token in ['+', '-', '*', '/', '//', '%', '**']

def is_unary_operator(token):
    """Проверяет, может ли токен быть унарным оператором"""
    return token in ['+', '-']

def is_unary_token(token):
    """Проверяет, является ли токен унарным оператором"""
    return token in ['$', '~']

def is_integer_division_operator(token):
    """Проверяет, является ли токен оператором целочисленного деления"""
    return token == '//'

def is_modul_operator(token):
    """Проверяет, является ли токен оператором остатка от деления"""
    return token == '%'

def get_operator_priority(operator: str) -> int:
    """Возвращает приоритет оператора"""
    return OPERATOR_PRIORITY.get(operator, 0)


def should_pop_operator(stack_operator, current_operator):
    """Определяет, нужно ли выталкивать оператор из стека"""
    if stack_operator == '(':
        return False

    stack_priority = get_operator_priority(stack_operator)
    current_priority = get_operator_priority(current_operator)

    # Для оператора ** особое условие
    if current_operator == '**':
        return stack_priority > current_priority
    else:
        return stack_priority >= current_priority

def convert_to_unary(token):
    """Преобразует бинарный оператор в унарный"""
    if token == '+':
        return '$'
    elif token == '-':
        return '~'
    else:
        return token
