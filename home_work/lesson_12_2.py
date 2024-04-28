# Створити 2 класу truck та car, які є спадкоємцями класу auto з попереднього домашнього завдання.
# б'єкти класу truck мають додатковий обов'язковий атрибут max_load.

# Перевизначений метод move перед появою напису «move» виводить напис «attention»,
# його реалізацію зробити з допомогою оператора super.

# А також додатковий метод load. При його виклику відбувається пауза 1 сек.
# потім видається повідомлення «load» і знову пауза 1 сек.

# Об'єкти класу car мають додатковий обов'язковий атрибут max_speed та при виклик методу move,
# після появи напису «move» має з'явитися напис "max speed is <max_speed>".
# Замість <max_speed> має виводиться значення обов'язкового атрибуму max_speed.

# Створити по 2 об'єкти для кожного з класів truck та car,
# перевірити всі їх методи та атрибути.
# При цьому об'єкти Truck і Car при створенні можуть приймати такі самі аргументи,
# що об'єкти класу Auto (brand, mark, age - обов'язкові, а color і weight - не обов'язкові).

import time
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

class Truck(Auto):                                      # добавляємо атрибут до батьківського класу
    def __init__(self, mark, brand, age, max_load):
        super().__init__(mark, brand, age)
        self.max_load = max_load

    def move(self):                                    #  переоприділяємо метод з батькіського класу
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    def __init__(self, mark, brand, age, max_speed):
        super().__init__(mark, brand, age)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {vlv.max_speed}')


man, man.color, man.weight = Truck("Man", 'Any', 15, 30), 'White', 8000
sc, sc.color, sc.weight = Truck('Scania', 'any', 4, 25), 'Blue', 7800
vlv = Car('VOLVO', 'Any', 12, 240)
tvr = Car('Tavria', 'Any', 22, 110)
auto = Auto('Mers', 'Any', 2)

print(man.__dict__)
print(sc.__dict__)
print(vlv.__dict__)
print(tvr.__dict__)
print(auto.__dict__, auto.color)


