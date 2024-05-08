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
        if b < 0:
            raise My_except
        else:
            return a**b

    @staticmethod
    def sqrt(a):
        return sqrt(a)
class My_except(Exception):
    def __init__(self):
        super().__init__('Pow Error')

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

try:
    print(a.pow(4, -4))
except My_except:
    print('second operand is negative')

try:
    print(a.sqrt(-4))
except ValueError:
    print('math domain error')