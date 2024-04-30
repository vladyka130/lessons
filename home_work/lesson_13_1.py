# Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл.
# У результаті віднімання двох кіл буде об'єкт класу Circle у которого будуть нові значення х, у та радіуса.
# Віднімання радіусов зробити по модулю. Якщо два кола з однаковим значенням радіуса віднімаються,
# то результатом віднімання буде об'єкт классу Point.

import math
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __sub__(self, other):
        if self.radius - other.radius == 0:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Circle(self.x - other.x, self.y - other.y, abs(self.radius - other.radius))

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'

c_1 = Circle(10, 10, 10)
c_2 = Circle(10, 8, 12)
c_3 = c_1 - c_2
print(c_3)