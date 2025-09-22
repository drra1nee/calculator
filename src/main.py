"""
Главный модуль калькулятора - точка входа в приложение
"""

from calculator.src.modules.calculator import calculate



def main():
    print("Калькулятор готов к работе!")
    print("Поддерживаемые операции: +, -, *, /, //, %, **, скобки")
    print("Примеры: 2+3*4, 10//3, (2+3)**2, -5+3")
    print("Введите 'quit' для выхода")
    print("-" * 50)

    while True:
        try:
            expression = input("Введите выражение: ").strip()

            if expression.lower() in ('quit', 'exit', 'q'):
                print("Выход из программы. До свидания!")
                break

            if not expression:
                continue

            result = calculate(expression)
            print(f"Результат: {result}")

        except ValueError as e:
            print(f" Ошибка: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы. До свидания!")
            break
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
