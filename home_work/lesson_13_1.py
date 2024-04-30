# Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл.
# У результаті віднімання двох кіл буде об'єкт класу Circle у которого будуть нові значення х, у та радіуса.
# Віднімання радіусов зробити по модулю. Якщо два кола з однаковим значенням радіуса віднімаються,
# то результатом віднімання буде об'єкт классу Point.

import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        return self.radius - other.radius

    def new(self):
        self.x += 1
        self.y += 1
        return Point(self.x, self.y)

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

c = Point(0, 0)
c_1 = c.new()
