
# Створити батьківський клас auto, який має атрибути:
# brand, age, cоlor, mark і weight.
# А також методи: move, birthday і stop.
# Методи move і stop виводять повідомлення на екран «move» та «stop», а birthday збільшує атрибут age на 1.
# Атрибути brand, age та mark є обов'язковими під час оголошення об'єкта.

class Auto:

    weight = 1700
    color = 'red'

    def __init__(self, mark, brand, age):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("stop")

bmw = Auto('ANY', "BMW", 10)

print(f'age = {bmw.age} , bmw.birthday() = age + 1 ({bmw.birthday()})')
bmw.move()
bmw.stop()
print(bmw.color)
print(bmw.weight)

