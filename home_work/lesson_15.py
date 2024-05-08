# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум додавання, віднімання,
# ділення, множення, зведення в ступінь та вилучення квадратного кореня.
# Обернути кожен метод у блок try/except і зробити обробку кількох винятків, як мінімум ділення на 0.
#
# Створити свій виняток, наприклад, зведення в негативний ступінь.

from math import sqrt

class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def pow(a, b):
        return a**b

    @staticmethod
    def sqrt(a):
        return sqrt(a)

a = Calc()

try:
    print(a.add(4, 'a'))
except TypeError:
    print('unsupported operand. int + str ')

print(a.sub(4, 5))
print(a.mul(4, 4))

try:
    print(a.div(4, 0))
except ZeroDivisionError:
    print('division by zero!!!')

print(a.pow(4, 4))

try:
    print(a.sqrt(-4))
except ValueError:
    print('math domain error')