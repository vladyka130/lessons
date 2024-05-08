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
