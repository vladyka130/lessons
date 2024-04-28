# Створити батьківський клас auto, який має атрибути:
# brand, age, cоlor, mark і weight.
# А також методи: move, birthday і stop.
# Методи move і stop виводять повідомлення на екран «move» та «stop», а birthday збільшує атрибут age на 1.
# Атрибути brand, age та mark є обов'язковими під час оголошення об'єкта.

class Auto:
    def __init__(self, mark, brand, age, weight='', color=''):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color

    def move(self):
        print('move')

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("stop")

bmw = Auto('ANY', "BMW", 10)


bmw.move()
bmw.stop()
print(f'age = {bmw.age} , bmw.birthday = {bmw.birthday()} (age + 1)')

bmw.color = 'Red'
bmw.weight = 1700

print(bmw.__dict__)

