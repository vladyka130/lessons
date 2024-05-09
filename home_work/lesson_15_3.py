from math import sqrt

class Calc:
    @staticmethod
    def add(a, b):
        try:
            return a + b
        except TypeError:
            return 'Error! unsupported operand. int + str'

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'Error! division by zero!!!'

    @staticmethod
    def pow(a, b):
        try:
            if b < 0:
                raise My_except
            else:
                return a**b
        except My_except:
            return 'Error! second operand is negative'

    @staticmethod
    def sqrt(a):
        try:
            return sqrt(a)
        except ValueError:
            return 'Error!math domain error'

class My_except(Exception):
    def __init__(self):
        super().__init__('Pow Error')

a = Calc()

print(a.add(4, 'a'))
print(a.sub(4, 5))
print(a.mul(4, 4))
print(a.div(4, 0))
print(a.pow(4, -4))
print(a.sqrt(-4))